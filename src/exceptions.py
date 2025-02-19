import sys
def error_message_details(error,error_detail:sys):
    _,_,tb = error_detail.exc_info()
    filename=tb.tb_frame.f_code.co_filename
    line_number=tb.tb_lineno
    return f"Error: {error} in {filename} at line {line_number}"


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_detail)
        self.error_message=error_message_details(error_message,error_detail)
    
    def __str__(self):
        return self.error_message