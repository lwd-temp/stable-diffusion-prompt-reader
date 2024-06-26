__author__ = "receyuki"
__filename__ = "base_format.py"
__copyright__ = "Copyright 2023"
__email__ = "receyuki@gmail.com"

import json
from enum import Enum
from ..logger import Logger


class BaseFormat:
    PARAMETER_KEY = ["model", "sampler", "seed", "cfg", "steps", "size"]

    def __init__(
        self, info: dict = None, raw: str = "", width: int = 0, height: int = 0
    ):
        self._height = str(height)
        self._width = str(width)
        self._info = info
        self._positive = ""
        self._negative = ""
        self._positive_sdxl = {}
        self._negative_sdxl = {}
        self._setting = ""
        self._raw = raw
        self._parameter = dict.fromkeys(BaseFormat.PARAMETER_KEY, "")
        self._is_sdxl = False
        self._status = self.Status.UNREAD
        self._logger = Logger("SD_Prompt_Reader.Parser")

    def parse(self):
        try:
            self._process()
        except Exception as e:
            self._logger.error(e)
            self._status = self.Status.FORMAT_ERROR
            return self._status
        else:
            self._status = self.Status.READ_SUCCESS
            return self._status

    def _process(self):
        pass

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def info(self):
        return self._info

    @property
    def positive(self):
        return self._positive

    @property
    def negative(self):
        return self._negative

    @property
    def positive_sdxl(self):
        return self._positive_sdxl

    @property
    def negative_sdxl(self):
        return self._negative_sdxl

    @property
    def setting(self):
        return self._setting

    @property
    def raw(self):
        return self._raw

    @property
    def parameter(self):
        return self._parameter

    @property
    def is_sdxl(self):
        return self._is_sdxl

    @property
    def status(self):
        return self._status

    @property
    def props(self):
        properties = {
            "positive": self._positive,
            "negative": self._negative,
            "positive_sdxl": self._positive_sdxl,
            "negative_sdxl": self._negative_sdxl,
            "is_sdxl": self._is_sdxl,
            **self._parameter,
            "height": self._height,
            "width": self._width,
            "setting": self._setting,
        }
        return str(json.dumps(properties))

    class Status(Enum):
        UNREAD = 1
        READ_SUCCESS = 2
        FORMAT_ERROR = 3
        COMFYUI_ERROR = 4
