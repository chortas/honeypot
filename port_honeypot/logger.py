import sys
import logging

def create_logger(filename):
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)

  formatter = logging.Formatter('(%(levelname)s) %(asctime)s - %(message)s', '%m-%d-%Y %H:%M:%S')

  # set up stdout handler with DEBUG logging
  stdout_handler = logging.StreamHandler(sys.stdout)
  stdout_handler.setLevel(logging.DEBUG)
  stdout_handler.setFormatter(formatter)

  # set up custom file handler with INFO logging
  file_handler = logging.FileHandler(filename)
  file_handler.setLevel(logging.INFO)
  file_handler.setFormatter(formatter)

  logger.addHandler(file_handler)
  logger.addHandler(stdout_handler)

  return logger
