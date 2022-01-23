from enum import Enum


class MatchStatus(Enum):
    CANCELED = 'canceled'
    LIVE = 'live'
    FINISHED = 'finished'
    NOT_STARTED = 'not-started'
