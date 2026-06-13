from logger import logging

def add(a,b):
    logging.debug("THe addition Operation is taking Palace")
    return a+b

logging.debug("The addition function is called")
add(10,18)