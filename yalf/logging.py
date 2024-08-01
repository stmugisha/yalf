#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

#For more information, please refer to <https://unlicense.org>

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
