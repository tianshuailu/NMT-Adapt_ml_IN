# this code snippet is adapted from https://github.com/wjko2/NMT-Adapt/blob/main/noise.py

import random

#############SET THESE PARAMETERS BEFORE RUNNING########
"""
INPUT_FILEPATH = "/your_path/nmt_train.hi_IN"
OUTPUT_NOISED_FILEPATH = "/your_path/train.no_IN1"
OUTPUT_ORIGINAL_FILEPATH = "/your_path/train.hi_IN"
CHAR_RANGE = [2304, 2431]  # unicode range of hindi character
"""
INPUT_FILEPATH = "/your_path/train.ml_XX"
OUTPUT_NOISED_FILEPATH = "/your_path/train.no_ML1"
OUTPUT_ORIGINAL_FILEPATH = "/your_path/train.ml_XX"
CHAR_RANGE = [3328, 3455]  # unicode range of ml character

CHAR_THRESHOLD = 0.4
REPEAT = 10


#########################
def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


f = []
with open(INPUT_FILEPATH, 'rt', encoding='utf-8') as file:
    for line in file:
        f.append(line)

fw = open(OUTPUT_NOISED_FILEPATH, 'w', encoding='utf-8')
fw2 = open(OUTPUT_ORIGINAL_FILEPATH, 'w', encoding='utf-8')
z = 0
k = 0
for line in f:
    line = line.strip().split()
    c = []
    sa = ''.join(line)
    b = 0
    for ca in sa:
        if ord(ca) < CHAR_RANGE[0] or ord(ca) > CHAR_RANGE[1]:
            b = b + 1
    if b / len(sa) < CHAR_THRESHOLD:
        k = k + 1
        for iag in range(REPEAT):
            c = []
            for a in line:
                if random.random() < 0.9:
                    c.append(a)
                else:
                    c.append('<mask>')
            p = []
            for v in range(len(c)):
                p.append(v + random.random() * 4)
            p = argsort(p)

            e = []
            for v in p:
                e.append(c[v])

            fw.write("%s" % ' '.join(e) + '\n')
            fw2.write("%s" % ' '.join(line) + '\n')
            z = z + 1
#            if z%100000==0:
#                print(z)

fw.close()
fw2.close()
