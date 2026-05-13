import sys
from typing import Any
import logging
from src.logger import logging


def error_message_details(error, error_detail: Any):

    _, _, exc_traceback = error_detail.exc_info()
    if exc_traceback is None:
        return "Error occured in py script: [unknown] at line number: [unknown] error message: [{0}]".format(str(error))

    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno

    error_message = "Error occured in py script: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: Any):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
    def __str__(self):
        return self.error_message



    
