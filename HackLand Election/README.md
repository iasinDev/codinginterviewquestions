# Hackland Election

Company| iPsY
---|---
Date|11/8/2018
Platform|HackerRank

In elections that use the ballot box system for voting, each voter writes the name of a candidate on a ballot and places it in the ballot box. The candidate with the highest number of votes wins the election. If two or more candidates have the same number of votes, then the tied candidates' names are ordered alphabetically and the last name in the alphabetical order wins.

For example, votes are in the names _['Joe', 'Mary', 'Mary', 'Joe']_. Each candidate received two votes, but _Mary_ is alphabetically later than _Joe_, so she wins.

#### Function Description

Complete the function electionWinner in the editor below. The function must return a string denoting the name of the winning candidate.

_electionWinner_ has the following parameter(s):
    _votes[votes[0],... votest[n-1]]:_ an array of strings representing the names of the candidates as voted by the _ith_ voter.

####Constraints
* _1 <=n <= 10^4_

#### Sample Case 0
###### Sample Input
```
10
Alex
Michael
Harry
Dave
Michael
Victor
Harry
Alex
Marry
Marry
```
###### Sample Output
```
Michael
```
###### Explanation 0
The _votes_ tally is:
* 2 votes: Alex, Harry, Micheal, Mary
* 1 vote: Dave, Victor
The hightest vote count is 2, and among those receiving 2 votes, the last name alphabetically is _Michael_