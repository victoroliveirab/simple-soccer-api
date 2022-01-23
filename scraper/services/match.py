from base import BaseService
from lib.enums import MatchStatus
# TODO: create index by teams and tournament


class MatchService(BaseService):
    def __init__(self):
        super().__init__('match', 'matches')

    def create(self, info):
        home_team = info['home_team']
        away_team = info['away_team']
        tournament = info['tournament']
        match_time = info['time']
        status = MatchStatus.NOT_STARTED

        super().create({
            'home': home_team,
            'away': away_team,
            'home_goals': 0,
            'away_goals': 0,
            'tournament': tournament,
            'time': match_time,
            'status': status,
            'elapsed': 0
        })

    def update_status_by_id(self, _id, status, return_orig=True):
        return super().update_by_id(_id, {
            'status': status
        }, return_orig=return_orig)

    def update_score_by_id(self, _id, score, return_orig=True):
        home_goals = score['home']
        away_goals = score['away']

        return super().update_by_id(_id, {
            'home_goals': home_goals,
            'away_goals': away_goals
        }, return_orig=return_orig)
