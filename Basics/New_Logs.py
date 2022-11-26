import logging

#create custom logger
logger = logging.getLogger("__name__")

#create handlers and set level
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.DEBUG)

#create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode='w',
#                     format="%(asctime)s - %(levelname)s - %(message)s")
logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
