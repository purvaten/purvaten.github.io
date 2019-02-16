import os
import sys

base = "https://purvaten.github.io/model_eval/"
folder = "all_cliparts"


# get folder and filenames
themes = []
urls = [[], [], [], [], []]
dists = [[], [], [], [], []]

for theme in os.listdir(folder):
    themes.append(theme)
    for img in os.listdir(folder + '/' + theme):
        url = base + folder + "/" + theme + '/' + img
        match_no = int(img[1])
        d = "0."+img.split('.')[1]
        urls[match_no].append(url)
        dists[match_no].append(d)

html_code = "<center><table border=1><tr><b><td>Word</td><td>Match1</td><td>Match2</td><td>Match3</td><td>Match4</td><td>Match5</td></b></tr>"

for i in range(26):
    row_data = "<td>%s</td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td>" % (themes[i], urls[0][i], urls[1][i], urls[2][i], urls[3][i], urls[4][i])
    distances = "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % ("", dists[0][i], dists[1][i], dists[2][i], dists[3][i], dists[4][i])
    html_code += "<tr>%s</tr><tr>%s</tr>" % (row_data, distances)

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
