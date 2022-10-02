# replace ▁ < m as k > with one token <maske>
# this code snippet is from https://github.com/wjko2/NMT-Adapt/blob/main/replace.py

f = open('/your_path/denoise/train.spm.no_hi1', 'r')
fw = open('/your_path/denoise/train.spm.no_HI', 'w')
for line in f:
    line = line.replace("▁ < m as k >", "<mask>")
    fw.write(line)

f.close()
fw.close()

f = open('/your_path/denoise/train.spm.no_ml1', 'r')
fw = open('/your_path/denoise/train.spm.no_ML', 'w')
for line in f:
    line = line.replace("▁ < m as k >", "<mask>")
    fw.write(line)

f.close()
fw.close()
