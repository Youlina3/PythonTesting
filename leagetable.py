# The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 

# The player's rank in the league is calculated using the following logic:

# The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
# If two players are tied on score, then the player who has played the fewest games is ranked higher.
# If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.
# Implement the player_rank function that returns the player at the given rank.

# For example:

# table = LeagueTable(['Mike', 'Chris', 'Arnold'])
# table.record_result('Mike', 2)
# table.record_result('Mike', 3)
# table.record_result('Arnold', 5)
# table.record_result('Chris', 5)
# print(table.player_rank(1))
# All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".

from collections import Counter
from collections import OrderedDict

#counter class：计数器
#orderdDict class: 保持key-value前后插入的顺序
class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1 #self.standings[player] is counter() which is value of self.standings and 本身counter也是一个dict
        self.standings[player]['score'] += score #here:count+1 for games_played score+score for score
      
    def player_rank(self, rank):
        print(self.standings) #OrderedDict([('Mike', Counter({'score': 5, 'games_played': 2})), ('Chris', Counter({'score': 5, 'games_played': 1})), ('Arnold', Counter({'score': 5, 'games_played': 1}))])
        ranking = sorted(self.standings.keys(), key=lambda p: (
        -self.standings[p]['score'],self.standings[p]['games_played'], 
        self.standings[p]['pos']))
        return ranking[rank - 1]
#key: to specify a function to be called on each list element prior to making comparisons.
#sorted(self.standings,key) = sorted(self.standings.keys(),key)
#so, the lambda p means a element of self.standings.keys() which is a list of player      
            
      
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))


