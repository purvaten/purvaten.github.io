import numpy as np
import pickle

with open('hp.pickle', 'rb') as f:
    data = pickle.load(f)

output = "<html><body><center><table border=1>"

classes = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

for type in ['lower', 'upper']:
    for letter in range(97, 123):
        if type == 'lower':
            row = "<td><b>%s</b></td>" % chr(letter)
        else:
            row = "<td><b>%s</b></td>" % chr(letter - 32)
        for gif_num in range(0, 8):
	    row += "<td><img src='lossy_%s_%s_%s.gif'></td>" % (type, chr(letter), str(gif_num))
	output += "<tr>%s</tr>" % row

output += "</table></body></center></html>"

with open('index.html', 'w') as f:
    f.write(output)

