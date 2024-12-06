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
