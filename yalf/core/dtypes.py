"""
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

from __future__ import annotations

from typing import List, Type
from dataclasses import dataclass

# image/video, audio, text(chat) i/o types

@dataclass
class Prompt:
	"""Workflow prompt type."""
	problem: List[str]
	constraints: List[str]
	#best_practices
	solution: List[str]


@dataclass
class TextResponse:
	prompt: Type[Prompt]
	response: str
