import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A' , level=logging.DEBUG ,filename="test2.log",filemode="a")
logging.critical("critical")
logging.error("error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")
