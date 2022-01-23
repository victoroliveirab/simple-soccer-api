from services.base import BaseService


class TeamService(BaseService):
    def __init__(self):
        super().__init__('team')


TeamServiceSingleton = TeamService()
