#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#For more information, please refer to <https://unlicense.org>
# Gemini API-key  AIzaSyC-uIF-9r_7h0qf7IzED38DCDuguoK2AHQ  #'gemini-1.5-flash'
from __future__ import annotations

from typing import Optional
import google.generativeai as genai
import PIL

from base import YalfModel
from yalf.utils import get_api_key
from yalf.logging import logger
from yalf.errors import ConfigurationError, ModelError


class GeminiClient(YalfModel):
	"""Gemini model clients."""

	SYSTEM_PROMPT = "You are a very creative and helpful agent"

	def __init__(self, model_name: str, api_key: Optional[str] = None):
		self.model_name = model_name
		self._configure_api(api_key)
		self.model = genai.GenerativeModel(model_name=self.model_name)
		#self.embedding_model = None
		self.logger = logger
		self.logger.info(f"Initialized GeminiClient with model: {self.model_name}")

		#response = model.generate_content('Teach me about how an LLM works')
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

	def generate(
		self,
		prompt: str,
		image: Optional[str] = None,
		streaming: bool = False
	) -> str:
		"""Question and answer generation.

		Args:
			prompt: text prompt (question)
			media: image file path or url
			streaming: If True, returns streamed responses, false otherwise

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

		response = self.model.generate_content(prompt)
		if len(response.text) < 1:
			self.logger.debug(f"Unable to service request: {response.prompt_feedback}")
			raise ModelError(f"ModelError: {response.prompt_feedback}")
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

		return response.text
