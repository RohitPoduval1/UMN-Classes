# Rohit Poduval, poduv006
# hw6.py
# HW6


class SoccerPlayer:
    #==========================================
    # Purpose: Constructs each SoccerPlayer object
    # Input Parameters:
        # player_id: int
        # active: boolean, represents whether the player is on the current roster;
            # True means currently on the team
            # False means not currently on the team
        # stats: a list of lists, each internal list represents the stats for a player
            # each list will be formatted as: [year, position, number of goals, number of assists]
            # e.g. [[2019, striker, 4, 10], [2019, midfielder, 2, 5], [2020, striker, 10, 20]]
    # Return Value(s): None (a SoccerPlayer object is created)
    #==========================================
    def __init__(self, player_id, active=True,):
        self.__player_id = player_id
        self.__active = active
        self.__stats = []                               


    #==========================================
    # Purpose: getter method for the private player_id variable, allows access to the value of player_id
    # Input Parameter(s): None
    # Return Value(s): the value of the player_id variable
    #==========================================
    def get_player_id(self):
        return self.__player_id
    
    #==========================================
    # Purpose: getter method for the private active variable, allows access to the value of active
    # Input Parameter(s): None
    # Return Value(s): the value of the active variable
    #==========================================
    def get_active(self):
        return self.__active
    
    #==========================================
    # Purpose: getter method for the private stats variable, allows access to the value of stats
    # Input Parameter(s): None
    # Return Value(s): the value of the stats variable
    #==========================================
    def get_stats(self):
        return self.__stats
    
    #==========================================
    # Purpose: setter method for the private player_id variable, allows the user to change whether or not the player is active
    # Input Parameter(s): a boolean value indicating whether or not the player is active
    # Return Value(s): None (The value of the variable "is_active"is change)
    #==========================================
    def set_active(self, is_active):
        self.__active = is_active
    
    #==========================================
    # Purpose: updates a player's stats with given information
    # Input Parameter(s):
        # year: 4-digit integer representing a year
        # position: string representing position of player
        # goals: integer representing the number of goals
        # assists: integer representing the number of assists
    # Return Value(s): None (a collection of information is added to a player's statistics list)
    #==========================================
    def stat_add(self, year, position, goals, assists):
        self.__stats.append([year, position, goals, assists])
    
    #==========================================
    # Purpose: find the average number of goals for a SoccerPlayer (only accounts for a year once)
    # Input Parameter(s): None
    # Return Value(s): average number of goals across all years 
    #==========================================
    def average_goals(self):
        total_goals = 0
        tracked_years = []
        total_years = 0
        for stat in self.__stats:  # TODO: Use getters within class itself?
            total_goals += stat[2]
            if stat[0] not in tracked_years:
                tracked_years.append(stat[0])
                total_years += 1
        return total_goals // total_years
    
    #==========================================
    # Purpose: find the average number of assists for a SoccerPlayer (only accounts for a year once)
    # Input Parameter(s): None
    # Return Value(s): average number of assists across all years 
    #==========================================
    def average_assists(self):
        total_assists = 0
        tracked_years = []
        total_years = 0
        for stat in self.__stats:  # TODO: Use getters within class itself?
            total_assists += stat[3]
            if stat[0] not in tracked_years:
                tracked_years.append(stat[0])
                total_years += 1
        return total_assists // total_years
    
    #==========================================
    # Purpose: count the total number of goals of a player for a given year
    # Input Parameters: year to look at (int) 
    # Return Value: the total number of goals of a player for a given year (int)
    #==========================================
    def number_of_goals(self, year):
        total_goals = 0
        for stat in self.__stats:
            if stat[0] == year:
                total_goals += stat[2]
        return total_goals
    
    #==========================================
    # Purpose: Overload the default __str__ method to suit the SoccerPlayer class
    # Input Parameter: None
    # Return Value: string representation of the SoccerPlayer object with their relevant information
    #==========================================
    def __str__(self):
        return f"Player ID: {self.__player_id}\nActive: {self.__active}\nStats: {self.__stats}\nAvg Goals Over All Years: {self.average_goals()}\nAvg Assists Over All Years: {self.average_assists()}"
    

class SoccerTeam:
    #==========================================
    # Purpose: Constructs each SoccerTeam object
    # Input Parameters:
        # league: the name of the league the team belongs to (string)
        # soccer_team: the name of the soccer team (string)
    # Return Value(s): None (a SoccerTeam object is created)
    #==========================================
    def __init__(self, league, soccer_team = []):
        self.__league = league
        self.__soccer_team = soccer_team
        self.__players = []
    
    #==========================================
    # Purpose: getter method for the private players variable, allows access to the value of players
    # Input Parameter(s): None
    # Return Value(s): the value of the players variable
    #==========================================
    def get_players(self):
        return self.__players
    
    #==========================================
    # Purpose: print each of the players on the team 
    # Input Parameters: None
    # Return Values: None (each player is printed)
    #==========================================
    def print_roster(self):
        for player in self.__players:
            print(player)
    
    #==========================================
    # Purpose: count the number of players on the team in a given year
    # Input Parameter: year (int) to look at
    # Return Value: the number players on the team for a given year (int)
    #==========================================
    def count(self, year):
        count = 0
        for player in self.__players:
            for stat in player.get_stats():
                if stat[0] == year:
                    count += 1
        return count
    
    #==========================================
    # Purpose: count the number of active players on the team
    # Input Parameter: None
    # Return Value: the number of active players on the team (int)
    #==========================================
    def count_players(self):
        count = 0
        for player in self.__players:
            if (player.get_stats())[1]:
                count += 1
        return count
    
    #==========================================
    # Purpose: add a new soccer player (SoccerPlayer object) to the team (SoccerTeam)
    # Input Parameter: a SoccerPlayer object to add to the SoccerTeam
    # Return Value: None (a player is added to the list of players)
    #==========================================
    def add_player(self, player):
        self.__players.append(player)

    #==========================================
    # Purpose: add the inputted information to the player_id’s list of stats
    # Input Parameter(s):
        # player_id: a player's id number (int)
        # year: 4 digit integer
        # position: the player's position (string)
        # goals: the number of goals the player scored (int)
        # assists: the number of helpers the player has (int) 
    # Return Value(s): None (a statistic is added to a player's list of statistics)
    #==========================================
    def stat_add(self, player_id, year, position, goals, assists):
        for player in self.__players:
            if player.get_player_id() == player_id:
                player.stat_add(year, position, goals, assists)
    
    #==========================================
    # Purpose: Calculate the total number of goals from all players on the team
    # Input Parameter: None
    # Return Value: total number of goals from all players on the team (int)
    #==========================================
    def __total_goals(self):
        total = 0
        for player in self.__players:
            for stat in player.get_stats():
                total += stat[2]
        return total

    #==========================================
    # Purpose: Overload the default __str__ method to suit the SoccerTeam class
    # Input Parameter: None
    # Return Value: string representation of the SoccerTeam object
    #==========================================
    def __str__(self):
        return f"{self.__soccer_team}: {self.__total_goals()}"


def main():
    # Test Cases for SoccerTeam class
    Gophers = SoccerTeam(
        league="Big 10",
        soccer_team="Golden Gophers"
    )

    John = SoccerPlayer(
        player_id=123456,
        active=True
    )
    Jimmy = SoccerPlayer(
        player_id=136246,
        active=False
    )
    Jeremy = SoccerPlayer(
        player_id=654321,
        active=True
    )

    # test cases for add_player()
    Gophers.add_player(John)
    Gophers.add_player(Jimmy)
    Gophers.add_player(Jeremy)

    # [year, position, number of goals, number of assists]
    # testing adding stats through team and player class
    Gophers.get_players()[1].stat_add(2020, "goalie", 0, 0)
    Gophers.get_players()[1].stat_add(2021, "midfielder", 5, 5)
    Gophers.get_players()[0].stat_add(2019, "striker", 4, 10)
    Gophers.get_players()[0].stat_add(2020, "striker", 10, 20)
    Gophers.get_players()[2].stat_add(2023, "striker", 4, 20)

    for player in Gophers.get_players():
        print(player)

    # Test Cases for SoccerPlayer class
    # test getter methods
    print()
    print(f"TESTING get_active():      {Gophers.get_players()[1].get_active() == False}")   
    print(f"TESTING get_player_id():   {Gophers.get_players()[0].get_player_id() == 123456}") 
    print(f"TESTING get_stats():       {Gophers.get_players()[2].get_stats() == [[2023, 'striker', 4, 20]]}")
    print(f"TESTING get_stats():       {Gophers.get_players()[0].get_stats() == [[2019, 'striker', 4, 10], [2020, 'striker', 10, 20]]}")
    
    # test setter method
    Gophers.get_players()[1].set_active(True)  
    print(f"TESTING set_active():      {Gophers.get_players()[1].get_active() == True}")

    # test stat_add() method
    Gophers.get_players()[2].stat_add(year=2022, position="striker", goals=0, assists=1)
    print(f"TESTING stat_add():        {Gophers.get_players()[2].get_stats() == [[2023, 'striker', 4, 20], [2022, 'striker', 0, 1]]}")
    print(f"TESTING number_of_goals(): {Gophers.get_players()[2].number_of_goals(2023) == 4}")
    print()


    print(Gophers)  # total number of goals = 0+5+4+10+4 = 23
    
    # test case for print_roster()
    Gophers.print_roster()

    # test case for count()
    print()
    print(f"TESTING count():         {Gophers.count(2020) == 2}")
    print(f"TESTING count():         {Gophers.count(2019) == 1}")
    print(f"TESTING count():         {Gophers.count(2020) == 2}")
    print(f"TESTING count():         {Gophers.count(2023) == 1}")

    # test case for count_players()
    print(f"TESTING count_players(): {Gophers.count_players() == 3}")


if __name__ == '__main__':
    main()