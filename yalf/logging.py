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

import sys
import logging
from typing import Optional


def get_logger(
	name: str = "Yalf",
	log_level: str = "INFO",
	log_file: Optional[str] = None
) -> logging.Logger:
	"""Set up logger with name `name` and logging level `log_level`.

	Args:
		name: logger name
		level: Log level
		file: File to write logging info.

	Returns:
		Loggger object
	"""
	logger = logging.getLogger(name)
	logger.setLevel(log_level)

	formatter = logging.Formatter(
		"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	)
	# Handlers
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.setFormatter(formatter)
	logger.addHandler(console_handler)

	if log_file:
		file_handler = logging.FileHandler(log_file)
		file_handler.setFormatter(formatter)
		logger.addHandler(file_handler)

	return logger


logger = get_logger()
