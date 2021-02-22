import logging


class LogGen:
    # Static methods should not have self as argument
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="C:\\Users\\VARSHANAYAK\\PycharmProjects\\nopcommerceApp\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger




