from enum import StrEnum


class MenuKeys(StrEnum):
    up = "w"
    down = "s"
    choose = ""
    escape = "e"
    enter = "enter"


class RoadQualityStatus(StrEnum):
    normal = "normal"
    bad = "bad"
    good = "good"
    start = "start"
    finish = "finish"


class CellName(StrEnum):
    wall = "wall"
    road = "road"


class ExternalSides(StrEnum):
    down = "down"
    up = "up"
    left = "left"
    right = "right"


class CellSymbols(StrEnum):
    wall = "#"
    start = "S"
    finish = "F"
    good_road = "$"
    normal_road = "*"
    bad_road = "^"
