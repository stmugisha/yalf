"""
Yalf client.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

# Claude-API-key  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
# cohere API-key 
from __future__ import annotations

import cohere
import anthropic

# implement as llm factory with class methods. class Client.<provider>()

class Client:
	"""Yalf LLM provider client factory."""

	def __init__(self):
		pass

	def __call__(self, model, prompt):
		pass

# setup language and audio agents that invoke models to do stuff