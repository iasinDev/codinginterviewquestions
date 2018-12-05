from collections import defaultdict
from collections import Counter
# Complete the electionWinner function below.

def electionWinner(votes):
    number_of_voltes_per_candidate = Counter(votes)
    
    maximum_votes = 0
    name_list = []
    for k, v in number_of_voltes_per_candidate.items():
        if v > maximum_votes:
            maximum_votes = v
            name_list.clear()
        if v == maximum_votes:
            name_list.append(k)
    
    return sorted(name_list,reverse=True)[0]

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