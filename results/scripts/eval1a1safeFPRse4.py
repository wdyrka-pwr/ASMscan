import numpy as np
import math
from sklearn.metrics import average_precision_score, roc_auc_score, roc_curve

import csv
import sys

y_score=[]
y_true=[]
all_positive=0
all_negative=0
with open(sys.argv[1]) as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        all_positive += 1
        if row[int(sys.argv[3])]=="-inf":
            score = float(-2000)
        else:
            score = float(row[int(sys.argv[3])])
        if score>float(sys.argv[4]):
            y_true.append(True)
            y_score.append(score)

with open(sys.argv[2]) as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        all_negative += 1
        if row[int(sys.argv[3])]=="-inf":
            score = float(-1000)
        else:
            score = float(row[int(sys.argv[3])])

        if score>float(sys.argv[4]):
            y_true.append(False)
            y_score.append(score)

sefpr = {}
for j in range(5,len(sys.argv)):
    sefpr[float(sys.argv[j])] = None

sefprlin = {}
for j in range(5,len(sys.argv)):
    sefprlin[float(sys.argv[j])] = None

yimax = -1.0
scmax = None

if sum(y_true)!=len(y_true) and sum(y_true)>0:
    fprates, tprates, thresholds = roc_curve(y_true, y_score)

    for i in range(len(fprates)):
        if fprates[i] == 0.0:
            fprates[i] = 1.0/all_negative
        else:
            break

    for i in range(len(fprates)):
        yi = tprates[i] - fprates[i]
        if yi > yimax:
            yimax = yi
            scmax = thresholds[i]

    for th in sefpr.keys():
        if fprates[0] <= th:
            for i in range(len(fprates)):
                if fprates[i] > th:
                    sefprlin[th] = (tprates[i] - tprates[i-1]) * (th-fprates[i-1])/(fprates[i]-fprates[i-1]) + tprates[i-1]
                    sefpr[th] = (tprates[i] - tprates[i-1]) * math.log(th/fprates[i-1], fprates[i]/fprates[i-1]) + tprates[i-1]
                    break

auc = roc_auc_score(y_true, y_score) if sum(y_true)!=len(y_true) and sum(y_true)>0 else sum(y_true)>0
ap = average_precision_score(y_true, y_score) if sum(y_true)!=len(y_true) and sum(y_true)>0 else sum(y_true)>0

se = 1.0*sum(y_true)/all_positive if all_positive else 0.0
pr = 1.0*sum(y_true)/len(y_true) if len(y_true) else 0.0
sp = 1.0 if all_negative == 0 else 1.0/all_negative if len(y_true)-sum(y_true) == 0.0 else 1.0 * (len(y_true)-sum(y_true)) / all_negative

print sum(y_true), \
      len(y_true) - sum(y_true), \
      ap, auc, se, pr, sp, yimax, scmax,

for key in sorted(sefpr):
    print sefpr[key],

for key in sorted(sefprlin):
    print sefprlin[key],

print ""
