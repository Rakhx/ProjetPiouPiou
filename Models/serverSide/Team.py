
class Team():

    def __init__(self,name,  flagPosition):
        self._name = name
        self._units = {}
        self.flag = flagPosition

    def registerUnit(self, name, type, position):
        self._units[name]=(type, position)



