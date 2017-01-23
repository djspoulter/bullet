# coding=utf-8
from enum import Enum


class Choice(Enum):
    @classmethod
    def choices(cls):
        return tuple((_[0], _[1].value) for _ in cls.__members__.items())
