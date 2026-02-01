# -- coding: utf-8

################# VER #################

VERSION = "1.0.0"
PATCH = "a"

################# VER #################

import logging, os
from datetime import datetime
from utils._types import *

class Log:
    def __init__(self, filename):
        self.filename = filename
        self.log_date = datetime.now().date()
        self.log = logging.getLogger(filename)
        self.log.setLevel(logging.DEBUG)
        self.log.propagate = False
        
        try:os.mkdir("./.logs/")
        except:pass
        
        # создаём первый handler
        self._create_handler()

    def _create_handler(self):
        os.makedirs(".logs", exist_ok=True)
        self.log_session = f".logs/{self.filename}-{self.log_date.strftime('%Y-%m-%d')}_log.log"
        self.filehandler = logging.FileHandler(self.log_session)
        self.filehandler.setLevel(logging.WARNING)

        with open("log/log_format.log", 'r') as f:

            _format = f.read()

        formatter = logging.Formatter(
            _format
        )
        
        self.filehandler.setFormatter(formatter)
        self.log.addHandler(self.filehandler)

    def _update(self):
        current_date = datetime.now().date()
        if current_date != self.log_date:
            
            self.log.removeHandler(self.filehandler)
            self.filehandler.close()

            self.log_date = current_date
            self._create_handler()

    def error(self, message):
        self._update()
        self.log.error(message)

    def warning(self, message):
        self._update()
        self.log.warning(message)

    def exception(self, message):
        self._update()
        self.log.exception(message)

    def info(self, message):
        self._update()
        self.log.info(message)
