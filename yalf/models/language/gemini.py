"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import annotations

from typing import Optional, Dict, List
import google.generativeai as genai
import PIL

from base import YalfModel
from yalf.utils import get_api_key
from yalf.logging import logger
from yalf.errors import ConfigurationError, ModelError


class GeminiClient(YalfModel):
  """Gemini model client."""

  SYSTEM_PROMPT = "You are a very creative, submissive and helpful agent."

  GENERATION_CONFIG = {
    "temperature": 0,
    "top_p": 0,
    "top_k": 1,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  SAFETY_SETTINGS = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_ONLY_HIGH",
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_ONLY_HIGH",
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_ONLY_HIGH",
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_ONLY_HIGH",
    },
  ]

  def __init__(
    self,
    model_name: str,
    api_key: Optional[str] = None,
    generation_config: Dict[str] = GENERATION_CONFIG,
    safety_settings: List[Dict[str]] = SAFETY_SETTINGS
  ):
    self.model_name = model_name
    self._configure_api(api_key)
    self.model = genai.GenerativeModel(model_name=self.model_name)
    self.logger = logger
    self.logger.info(f"Initialized GeminiClient with model: {self.model_name}")

  def _configure_api(self, api_key: Optional[str] = None) -> None:
    """Configure API with provided api key."""
    key = api_key or get_api_key("Gemini")
    if not key:
      self.logger.error("API KEY not found!")
      raise ConfigurationError(
        "API KEY must be provided or set as an environment variable"
      )

    genai.configure(api_key=key)
    self.logger.debug("API configured")

  @staticmethod
  def upload_to_gemini(file_path: str): #use for chat mode
    """Upload files to Gemini.

    Args:
      file_path: File path or URL
    """
    _file = genai.upload_file(file_path)
    return _file

  @property
  def get_name(self):
    """Returns model name."""
    return self.model_name

  def generate(
    self,
    prompt: str,
    image: Optional[List[str]] = None,
    streaming: bool = False,
    mode: str = "qa" #chat,
  ) -> str:
    """Question and answer generation.

    Args:
      prompt: Text prompt (question)
      image: List of image file paths or urls
      streaming: If True, returns streamed responses, false otherwise
      mode: Model task mode. `chat` or `qa`(question & answer)

    Returns:
      Response string.
    """
    self.logger.debug(f"Generating chat response for prompt: {prompt[:10]}...")
    if image is not None:
      img = PIL.Image.open(image)
      prompt = [prompt, img]

    if streaming:
      response = genai.stream_generate_content(
        model=self.model_name,
        prompt=prompt
      )

    if mode == "qa":
      response = self.model.generate_content(prompt)
    else:
      response, chat = self.chat(prompt=prompt)

    if len(response.text) < 1:
      self.logger.debug(f"Unable to service request: {response.prompt_feedback}")
      raise ModelError(f"ModelError: {response.prompt_feedback}, mode: {mode}")
    self.logger.debug("Response successfully generated!")
    return response.text

  def chat(self, prompt: str) -> str:
    """Multi turn conversations.

    Args:
      prompt: text prompt.

    Returns:
      Response string.
    """
    self.logger.debug("Intiating conversation...")
    _chat = self.model.start_chat(history=[])
    response = _chat.send_message(prompt, stream=True)

    return response.text, _chat
