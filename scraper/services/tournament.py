from services.base import BaseService
from services import CountryService


class TournamentService(BaseService):
    COUNTRY_FIELD = 'country'

    def __init__(self):
        super().__init__('tournament')

    def _add_tournament_to_country(self, tournament):
        return CountryService.add_tournament(
            tournament[self.COUNTRY_FIELD],
            tournament[self.ID_FIELD]
        )

    def _delete_tournament_of_country(self, tournament):
        return CountryService.remove_tournament(
            tournament[self.COUNTRY_FIELD],
            tournament[self.ID_FIELD]
        )

    def create(self, info):
        name = info[self.NAME_FIELD]
        country_id = info[self.COUNTRY_FIELD]
        tournament = super().create({
            self.NAME_FIELD: name,
            self.COUNTRY_FIELD: country_id
        })

        self._add_tournament_to_country(tournament)

        return tournament

    def delete_by_id(self, _id, return_obj=True):
        tournament = super().delete_by_id(_id, return_obj=return_obj)

        self._delete_tournament_of_country(tournament)

        return tournament

    def delete_by_name(self, name, return_obj=True):
        tournament = super().delete_by_name(name, return_obj=return_obj)

        self._delete_tournament_of_country(tournament)

        return tournament


TournamentServiceSingleton = TournamentService()