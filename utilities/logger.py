import logging
import inspect



class LoggenClass:

    @staticmethod
    def logen():
        logname=inspect.stack()[1][3]
        logger=logging.getLogger(logname)
        log_file=logging.FileHandler("D:\\pytest\\orange_hrm_copy\\Logs\\copyorangehrm.log")
        format=logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s")
        log_file.setFormatter(format)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger