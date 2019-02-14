import os
import sys

base = "https://purvaten.github.io/crowd-results/"
folders = ["crowd-results-original-education", "crowd-results-original-education1", "crowd-results-original-education2", "crowd-results-original-education3", "crowd-results-original-education4", "crowd-results-original-education5", "crowd-results-original-education6"]
# folders = ["crowd-results-original", "crowd-results-original-replace1", "crowd-results-original-replace2", "crowd-results-original-replace3", "crowd-results-original-replace4"]


# get folder and filenames
themes = []
words = []
urls = [[], [], [], [], [], [], []]

for f, folder in enumerate(folders):
    for theme in os.listdir(folder):
        os.rename(folder + '/' + theme, folder + '/' + theme)
        theme_modified = theme.replace(' ', '%20')
        for img in os.listdir(folder + '/' + theme):
            url = base + folder + "/" + theme_modified + '/' + img
            urls[f].append(url)
            semicolon = theme.replace('_', '-')
            themes.append(semicolon)
            words.append(img.split('.')[0])

html_code = "<center><table border=1><tr><b><td>Word</td><td>Theme</td><td>Doodle0</td><td>Doodle1</td><td>Doodle2</td><td>Doodle3</td><td>Doodle4</td><td>Doodle5</td><td>Doodle6</td></b></tr>"

for i in range(14):
    row_data = "<td>%s</td><td>%s</td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td><td><img src='%s'></td>" % (words[i], themes[i], urls[0][i], urls[1][i], urls[2][i], urls[3][i], urls[4][i], urls[5][i], urls[6][i])
    html_code += "<tr>%s</tr>" % row_data

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
