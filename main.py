import os
import csv
csvfile = os.path.join("Resources","election_data.csv")
candidates = []
with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    for row in csv_reader:
        candidates.append(row[2])
votecount = len(candidates)
Khan = int(candidates.count("Khan"))
Correy = int(candidates.count("Correy"))
Li = int(candidates.count("Li"))
OTooley = int(candidates.count("O'Tooley"))
Khan_pct = (Khan/votecount) * 100
Correy_pct = (Correy/votecount) * 100
Li_pct = (Li/votecount) * 100
OTooley_pct = (OTooley/votecount) * 100
if Khan > Correy and Khan > Li and Khan > OTooley:
    winner = "Kahn"
elif Correy > Kahn and Correy > Li and Correy > OTooley:
    winner = "Correy"
elif Li > Kahn and Li > Correy and Li > OTooley:
    winner = "Li"
elif OTooley > Kahn and OTooley > Li and OTooley > Correy:
    winner = "OTooley"
print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(votecount))
print("-------------------------------")
print("Khan: " + str(round(Khan_pct,3)) + "% (" + str(Khan) + ")")
print("Correy: " + str(round(Correy_pct, 3)) + "% (" + str(Correy) + ")")
print("Li: " + str(round(Li_pct, 3)) + "% (" + str(Li) + ")")
print("O'Tooley: " + str(round(OTooley_pct, 3)) + "% (" + str(OTooley) + ")")
print("-------------------------------")
print("Winner: " + winner)
            