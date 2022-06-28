import csv
import sys

from metricer import calculate_metrics

def load_csv(filename, colnum, infval):
    y_score = []
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')
        for row in spamreader:
            if row[colnum]=="-inf":
                score = float(infval)
            else:
                score = float(row[colnum])
            y_score.append(score)
    return y_score

positive = sys.argv[1]
negative = sys.argv[2]
colnum = int(sys.argv[3])

y_score = load_csv(positive, colnum, -2000)
y_true = [True] * len(y_score)

y_score += load_csv(negative, colnum, -1000)
y_true += [False] * (len(y_score) - len(y_true))

print(calculate_metrics(y_true, y_score))
