import logging




class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)

        filehandler=logging.FileHandler(filename="E:\\pythonProject2\\logs\\autolog.log",mode='w')
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug log")
        logger.info("Information log ")
        logger.warning("Warning log")
        logger.error("Error log")
        logger.critical("Critical log")
        print()

        return logger
