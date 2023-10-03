class SpadesScoreKeeper:
    round = 1

    team1_total = 0
    team1_bags = 0
    team1_bid_and_tricks_dict = {}
    team1_round_and_points_dict = {}

    team2_total = 0
    team2_bags = 0
    team2_bid_and_tricks_dict = {}
    team2_round_and_points_dict = {}

    def getUsersBid(self, team: str):
        return int(input("team " + team + " enter your bid: "))

    def getTricksWon(self, team: str):
        return int(input("team " + team + " enter how many tricks you won: "))

    def calculateScore(self, bid: int, tricks_won: int) -> int:
        score = 0
        if bid == 0:
            if tricks_won == 0:
                score = 200
            else:
                score = -200

        if tricks_won < bid:
            score = -10 * bid
        else:
            score = (bid * 10) + (tricks_won - bid)


        return score

    def nextRound(self):
        self.round += 1

    def printBoard(self, name1: str, name2: str):
        print("___________________________")
        print("round", self.round)
        print("---------------------------")
        print("team", name1)
        print("---------------------------")
        print(self.team1_total)

        print("bid: ", end="")
        for bid in self.team1_bid_and_tricks_dict:
            print(bid, end=" ")

        print("\ntricks: ", end="")
        for bid in self.team1_bid_and_tricks_dict:
            print(self.team1_bid_and_tricks_dict[bid], end=" ")

        print("\npts: ", end="")
        for rnd in self.team1_round_and_points_dict:
            print(self.team1_round_and_points_dict[rnd], end=" ")

        print("\n---------------------------")

        print("team", name2)
        print("---------------------------")
        print(self.team2_total)

        print("bid: ", end="")
        for bid in self.team2_bid_and_tricks_dict:
            print(bid, end=" ")

        print("\ntricks: ", end="")
        for bid in self.team2_bid_and_tricks_dict:
            print(self.team2_bid_and_tricks_dict[bid], end=" ")

        print("\npts: ", end="")
        for rnd in self.team2_round_and_points_dict:
            print(self.team2_round_and_points_dict[rnd], end=" ")

        print("\n---------------------------\n")

    def game(self, team1_name, team2_name):
        team1_bid = self.getUsersBid(team1_name)
        team2_bid = self.getUsersBid(team2_name)

        team1_tricks_won = self.getTricksWon(team1_name)
        team2_tricks_won = self.getTricksWon(team2_name)

        team1_score = self.calculateScore(team1_bid, team1_tricks_won)
        team2_score = self.calculateScore(team2_bid, team2_tricks_won)

        bag1, bag2 = self.calculate_bags(team1_score, team2_score)

        self.team1_total += team1_score - bag1
        self.team2_total += team2_score - bag2

        self.team1_round_and_points_dict[self.round] = team1_score
        self.team2_round_and_points_dict[self.round] = team2_score

        self.team1_bid_and_tricks_dict[team1_bid] = team1_tricks_won
        self.team2_bid_and_tricks_dict[team2_bid] = team2_tricks_won

        self.printBoard(team1_name, team2_name)
        self.nextRound()

    def done(self):
        return input('done? (y/n) ') == "y"

    def finish(self, team1_name, team2_name):
        if self.team1_total > self.team2_total:
            print("\nTEAM " + team1_name + " WON!")
        elif self.team1_total < self.team2_total:
            print("\nTEAM " + team2_name + " WON!")
        else:
            print("\nIt's a TIE!")

    def calculate_bags(self, score1, score2):
        pts1_minus = 0
        pts2_minus = 0

        self.team1_bags += score1 % 10
        self.team2_bags += score2 % 10

        if self.team1_bags >= 10:
            pts1_minus = 100
            self.team1_bags -= 10
        else:
            pts1_minus = 0

        if self.team2_bags >= 10:
            pts2_minus = 100
            self.team2_bags -= 10
        else:
            pts2_minus = 0

        return pts1_minus, pts2_minus