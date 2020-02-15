import constants

class Member:
    # missions = {SMALL: [isSolo, isSolo], FISHING: [isSolo]}
    def __init__(self, name):
        self.name = name
        self.missions = {}
        self.missionPoints = 0

    def addMission(self, missionSize, isSolo):
        self.missions.setdefault(missionSize, [])
        self.missions[missionSize].append([isSolo])
        self.missionPoints += self._calculateMissionPoints(missionSize, isSolo)

    def _calculateMissionPoints(self, missionSize, isSolo):
        return (constants.SOLO_MISSION_POINTS if isSolo else constants.PARTY_MISSION_POINTS)[missionSize]

    def getMissionPoints(self):
        return self.missionPoints

    def getNumSoloMissions(self, missionSize):
        return self._getNumMission(missionSize, True)

    def getNumPartyMissions(self, missionSize):
        return self._getNumMission(missionSize, False)

    def _getNumMission(self, missionSize, isSolo):
        missions = self.missions.get(missionSize, [])
        filteredMissions = [mission for mission in missions if mission[0] == isSolo]
        return len(filteredMissions)

    def getNumMissions(self):
        numMissions = 0
        for missions in self.missions.values():
            numMissions += len(missions)
        return numMissions