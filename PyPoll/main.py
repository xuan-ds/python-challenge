import os
import csv
csvpath = os.path.join('/Users/xuandi/Desktop/python-challenge/PyPoll/Resources/election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    next(csvreader)
    vote_list = []
    candidate_list = []
    cand_list =[]

    vote_1 = 0
    vote_2 = 0
    vote_3 = 0

    pct_1 = 0
    pct_2 = 0
    pct_3 = 0

    for row in csvreader:
        vote_list.append(int(row[0]))
        candidate_list.append(str(row[2]))
        
    candidates = list(dict.fromkeys(candidate_list))
    total_vote = len (vote_list)
    total_candidates = len (candidates)

for i in range(1,len(vote_list)):
    if candidate_list[i] == candidates[0] :
        vote_1 = vote_1 + 1
    if candidate_list[i] == candidates[1]:
        vote_2 = vote_2 + 1
    if candidate_list[i] == candidates[2]:
        vote_3 = vote_3 + 1

pct_1 = "{:.0%}".format(vote_1 / total_vote)
pct_2 = "{:.0%}".format(vote_2 / total_vote)
pct_3 = "{:.0%}".format(vote_3 / total_vote)


print("ELection Resolts")
print("-------------------------------")
print(f"{candidates[0]}:{pct_1}({vote_1})")
print(f"{candidates[1]}:{pct_2}({vote_2})")
print(f"{candidates[2]}:{pct_3}({vote_3})")
print("-------------------------------")
