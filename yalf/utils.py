#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#For more information, please refer to <https://unlicense.org>
# Yalf helper functions
from __future__ import annotations

import os


def get_api_key(provider: str) -> str:
	"""Load model provider api keys.

	API keys are read from either user passed api key string or
	from set environment variables. API key environment variables must be named as
	<PROVIDER>_API_KEY where <PROVIDER> is the uppercase name of the model provider.e.g.

	Args:
		model: name of the model e.g. GEMINI, CLAUDE, etc.

	Returns:
		api key string
	"""
	key = os.getenv(f"{provider.upper()}_API_KEY")
	return key
