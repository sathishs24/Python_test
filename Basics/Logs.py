from lxml import etree
import logging

if __name__=='__main__':
    print("This is a print statement")

    # try:
    #     x=etree.fromstring('<This is not XML>')
    # except Exception as e:
    #     print(str(e))
    logging.debug("This is debug message")
    logging.info("This is infor message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")

class main():
    pass