#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#For more information, please refer to <https://unlicense.org>

from __future__ import annotations

from abc import ABC, abstractmethod


class YalfModel(ABC):
	"""Yalf LLM model base class."""

	@abstractmethod
	def _generate(self, prompt):
		"""Q&A text generation method."""
		pass

	@abstractmethod
	def embed(self, documents):
		"""Embed a given set of documents."""
		pass

	@abstractmethod
	def retrieve(self, documents):
		"""Retreival augmented generation function."""
		pass

	@abstractmethod
	def finetune(self):
		"""Finetune model on a set of input documents."""
		pass

	@abstractmethod
	def serialize(self):
		"""I/O serialization."""
		pass

	@abstractmethod
	def deserialize(self):
		"""I/O deserialization."""
		pass
