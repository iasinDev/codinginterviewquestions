from collections import defaultdict
from collections import Counter
# Complete the electionWinner function below.

def electionWinner(votes):
    number_of_voltes_per_candidate = Counter(votes)
    max_votes = max(number_of_voltes_per_candidate.items(),key = lambda item: item[1])[1]
    max_votes_name_list = list(map(lambda item: item[0], filter(lambda item: item[1] == max_votes, number_of_voltes_per_candidate.items())))
    return sorted(max_votes_name_list,reverse=True)[0]

# print(electionWinner(['Alex','Michael','Harry', 'Harry'])=='Harry')
# print(electionWinner(['Alex','Michael','Alex', 'Michael', 'Harry', 'Harry'])=='Alex')
print(electionWinner(['Michael','Alex', 'Michael', 'Alex','Harry', 'Harry']) == 'Michael')
# print(electionWinner(['Alex'
# Michael
# Harry
# Dave
# Michael
# Victor
# Harry
# Alex
# Mary
# Mary]))