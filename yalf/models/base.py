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

from abc import ABC, abstractmethod
from typing import List


class YalfModel(ABC):
  """Yalf LLM model base class."""

  @abstractmethod
  def chat(self, prompt: str) -> str:
    """Question and Answer generation."""
    pass

  @abstractmethod
  def embed(self, documents: List[str]) -> List[List[float]]:
    """Embed a given set of documents."""
    pass

  @abstractmethod
  def retrieve(self, documents: List[str]) -> List[str]:
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
