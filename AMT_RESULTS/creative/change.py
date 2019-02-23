"""Change creativity results pickle file to new desirable format."""
import csv
import pickle
import sys

# Open creativity CSV
f = open('creativity.csv')
csv_f = csv.reader(f)

# Initialize mydict
all_images = []
mydict = {}
for h, hit in enumerate(csv_f):
    if h == 0:
        continue
    # create new entry in CSV file for that image
    for i in range(5):
        mydict[hit[27 + i]] = []

# Open creativity CSV
f = open('creativity.csv')
csv_f = csv.reader(f)

# Read CSV and store in mydict
for h, hit in enumerate(csv_f):
    if h == 0:
        continue

    # add details
    details = [[], [], [], [], []]

    # add (theme, word)
    for i in range(5):
        details[i].append((hit[32 + i], hit[37 + i]))

    # add type
    for i in range(5):
        details[i].append(hit[42 + i])

    # add comment
    for i in range(5):
        details[i].append(hit[48 + i])

    # add score
    for i in range(5):
        # check which index is true in 53-57
        scores = [hit[53 + 5 * i + j] for j in range(5)]
        ans = [k for k, s in enumerate(scores) if s == "true"][0] + 1
        details[i].append(ans)

    # add all details to mydict with key as image
    for i in range(5):
        mydict[hit[27 + i]].append(details[i])

        if mydict[hit[27 + i]] not in all_images:
            all_images.append(hit[27 + i])

# write to pickle file
with open('creativity.pickle', 'wb') as handle:
    pickle.dump(mydict, handle, protocol=pickle.HIGHEST_PROTOCOL)

# write to text file
with open('creativity_images.txt', 'w') as handle:
    for img in all_images:
        handle.write(img)
        handle.write("\n")
