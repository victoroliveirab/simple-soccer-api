from base import BaseService
from utils import id_as_object_id


class CountryService(BaseService):
    TOURNAMENT_FIELD = 'tournaments'

    def __init__(self):
        super().__init__('country', 'countries')

    def create(self, info):
        name = info[self.NAME_FIELD]
        tournaments = []
        return super().create({
            self.NAME_FIELD: name,
            self.TOURNAMENT_FIELD: tournaments
        })

    def add_tournament(self, country_id, tournament_id):
        return super().update_by_id(country_id, {
            '$push': {
                self.TOURNAMENT_FIELD: id_as_object_id(tournament_id)
            }
        })

    def remove_tournament(self, country_id, tournament_id):
        return super().update_by_id(country_id, {
            '$pull': {
                self.TOURNAMENT_FIELD: id_as_object_id(tournament_id)
            }
        })


