from insurance.logger import logging
from insurance.exception import InsuranceException
import os, sys

def test_logger_and_exception():
    try:
        logging .info("starting the test_logger_and_exception")
        result=3/10
        print(result)
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e,sys)
    

if __name__ =="__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)        