'''

import logging

logging.error("Error")              # This is the order of level of 'logging'
logging.critical("Critical")
logging.warn("Warning")
logging.debug("Debug")
logging.info("Info")

Output:

ERROR:root:Error
CRITICAL:root:Critical
D:/My_Programs/Python/Learn-Python/16 Exception Handling/loggingdemo.py:5: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("Warning")
WARNING:root:Warning

'''


'''Configure the logging level'''
#
# import logging
#
# logging.basicConfig(filename="mylog.log", level = logging.ERROR)                # Only Critical and Error will go in mylog.log file, since level is ERROR. And, filename can be anything, but file extension will always be ".log"
# logging.critical("Critical")            # Changing the level of logging
# logging.error("Error")
# logging.warn("Warning")
# logging.info("Info")
# logging.debug("Debug")



import logging

logging.basicConfig(filename="mylog.log", level = logging.DEBUG)                # Now, everything will go in mylog.log file, since level is DEBUG. And, filename can be anything, but file extension will always be ".log"
logging.critical("Critical")            # Changing the level of logging
logging.error("Error")
logging.warn("Warning")
logging.info("Info")
logging.debug("Debug")


# If we use "level = logging.CRITICAL", we will only see Critical in mylog file