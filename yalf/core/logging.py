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

	logging.Formatter(
		"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	)
