class MatchDetails:
    def __init__(self,MatchID,Map,Win,RoundsWon,RoundsLost,Date):
        self.MatchID = MatchID
        self.Map = Map
        self.Win = Win
        self.RoundsWon = RoundsWon
        self.RoundsLost = RoundsLost
        self.Date = Date

    def __str__(self):
        return "MatchID: " + str(self.MatchID) + "\nMap: " + self.Map + "\nWin: " + str(self.Win) + "\nRoundsWon: " + str(self.RoundsWon) + "\nRoundsLost: " + str(self.RoundsLost) + "\nDate: " + str(self.Date)