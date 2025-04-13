import logging

def setup_logger(name,level=logging.DEBUG,file="server.log"):
    logger=logging.getLogger(name)

    logger.setLevel(level)
    file_handler=logging.FileHandler(file)
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger.addHandler(file_handler)
    file_handler.setFormatter(formatter)

    return logger