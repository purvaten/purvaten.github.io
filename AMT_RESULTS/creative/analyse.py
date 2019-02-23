"""Analyse creativity results."""
import pickle
import sys

# write to pickle file
with open('creativity.pickle', 'rb') as f:
    x = pickle.load(f)

# open txt file
with open('creativity_images.txt') as f:
    imgs = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
imgs = [i.strip() for i in imgs]

scores = [[], [], [], [], []]
for img in imgs:
    dtype = int(x[img][0][1][1])
    dscore = 0
    for i in range(len(x[img])):
        dscore += x[img][i][3]
    avg = dscore / len(x[img])
    scores[dtype - 1].append(avg)

print(sum(scores[0]) / len(scores[0]))
print(sum(scores[1]) / len(scores[1]))
print(sum(scores[2]) / len(scores[2]))
print(sum(scores[3]) / len(scores[3]))
print(sum(scores[4]) / len(scores[4]))
