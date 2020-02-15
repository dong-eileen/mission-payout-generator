import sys
import constants
import csv
from member import Member

def addMissionToParticipants(missionSize, participants, payoutInfo):
    isSolo = True if len(participants) == 1 else False
    for participantName in participants:
        participantName = participantName
        payoutInfo.setdefault(participantName, Member(participantName))
        payoutInfo[participantName].addMission(missionSize, isSolo)

def printPayoutInfo(payoutInfo):
    for participant in payoutInfo:
        numMissions = payoutInfo[participant].getNumMissions()
        points = payoutInfo[participant].getMissionPoints()
        print(f'{participant}: {numMissions}, {points}')

# when there are more columns in the entire data range than in the row, there can be empty columns. Get rid of those empty columns
def getCleanParticipants(participants):
    return [participant for participant in participants if participant != '']

# input: comma-separated CSV
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Defaulting input file -> input.csv, output file -> output.csv")
        sys.argv.append("input.csv")
        sys.argv.append("output.csv")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Input and output files should be CSV")
        sys.exit(1)

    inputFile = open(sys.argv[1], 'r', newline='')
    outputFile = open(sys.argv[2], 'w', newline='')

    # calculate mission points
    payoutInfo = {}
    for line in inputFile:
        data = line.strip().split(',')
        missionType = data[0];
        missionSize = constants.FISHING if missionType == "Fishing" else data[1]
        addMissionToParticipants(missionSize, getCleanParticipants(data[2:]), payoutInfo)

    # sort by mission points, descending
    sortedPayoutInfo = sorted(payoutInfo.items(), key=lambda payoutEntry:payoutEntry[1].getMissionPoints(), reverse=True)
    sortedPayoutInfo = {key: value for (key, value) in sortedPayoutInfo};
    printPayoutInfo(sortedPayoutInfo)

    outputWriter = csv.writer(outputFile, delimiter=',')
    # write payout info
    for memberName in sortedPayoutInfo:
        memberObj = sortedPayoutInfo[memberName]
        outputWriter.writerow([memberName,
            memberObj.getNumSoloMissions(constants.SMALL),
            memberObj.getNumSoloMissions(constants.MEDIUM),
            memberObj.getNumSoloMissions(constants.LARGE),
            memberObj.getNumSoloMissions(constants.EXTRALARGE),
            memberObj.getNumPartyMissions(constants.SMALL),
            memberObj.getNumPartyMissions(constants.MEDIUM),
            memberObj.getNumPartyMissions(constants.LARGE),
            memberObj.getNumPartyMissions(constants.EXTRALARGE),
            memberObj.getNumSoloMissions(constants.FISHING),
            memberObj.getNumPartyMissions(constants.FISHING),
            memberObj.getNumMissions(),
            memberObj.getMissionPoints()
        ])

    inputFile.close()
    outputFile.close()