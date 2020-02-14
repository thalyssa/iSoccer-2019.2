from employeeConcrete import EmployeeConcrete


class PlayerConcrete(EmployeeConcrete):
    position: str
    canPlay: bool

    def isHapit(self, parameter: bool):
        self.canPlay = parameter
