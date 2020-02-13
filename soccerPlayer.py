import personInterface


class SoccerPlayer(personInterface):

    type: str
    salary: float
    canPlay: bool

    def isHapit(self, parameter: bool):
        self.canPlay = parameter
