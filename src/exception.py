import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    # Extract the exception type, value, and traceback using sys.exc_info()
    _, _, exc_tb = error_detail.exc_info()

    # Get the filename and line number where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    # Return the formatted error message
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class constructor with the error message
        super().__init__(error_message)
        
        # Generate the detailed error message
        self.error_message = error_message_detail(error_message, error_detail)
        
    def __str__(self):
        # Return the detailed error message as a string
        return self.error_message

# # # Practice block
# if __name__ == "__main__":
#     # Set up logging configuration
#     logging.basicConfig(level=logging.INFO)  # Configure logging to show INFO level messages

#     try:
#         # Simulating a division by zero error
#         a = 1 / 0  # Division by zero
#     except Exception as e:
#         # Log the exception message
#         logging.info("Divide by Zero error occurred")
        
#         # Raise the custom exception with the original exception and sys for traceback details
#         raise CustomException(e, sys)


    