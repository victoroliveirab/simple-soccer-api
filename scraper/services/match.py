from services.base import BaseService
from lib.enums import MatchStatus
# TODO: create index by teams and tournament


class MatchService(BaseService):
    def __init__(self):
        super().__init__('match', 'matches')

    def create(self, info):
        home_team = info['home_team']
        away_team = info['away_team']
        tournament = info['tournament']
        match_datetime = info['datetime']
        status = str(MatchStatus.NOT_STARTED)

        super().create({
            'home': home_team,
            'away': away_team,
            'home_goals': 0,
            'away_goals': 0,
            'tournament': tournament,
            'datetime': match_datetime,
            'status': status,
            'elapsed': 0
        })

    def update_status_by_id(self, _id, status, return_obj=True):
        return super().update_by_id(_id, {
            'status': status
        }, return_obj=return_obj)

    def update_score_by_id(self, _id, score, return_obj=True):
        home_goals = score['home']
        away_goals = score['away']

        return super().update_by_id(_id, {
            'home_goals': home_goals,
            'away_goals': away_goals
        }, return_obj=return_obj)


MatchServiceSingleton = MatchService()