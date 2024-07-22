#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#For more information, please refer to <https://unlicense.org>
# Gemini API-key  AIzaSyC-uIF-9r_7h0qf7IzED38DCDuguoK2AHQ
from __future__ import annotations

import os
import google.generativeai as genai

from base import YalfModel


class GeminiClient(YalfModel):
	"""Gemini model clients."""

	def __init__(self, model_name, prompt, task):
		super().__init__()
		self.model_name = model_name
		self.prompt = prompt
		self.task = task ## review if replacable by abstractmethods

#genai.configure(api_key=os.environ['API_KEY'])

#model = genai.GenerativeModel(model_name='gemini-1.5-flash')
#response = model.generate_content('Teach me about how an LLM works')
	def __call__(self, api_key):
		genai.configure(api_key=os.environ["GEMINI_API_KEY"])
	def chat(self):
		"""Question and Answer generation."""
		pass
