import glob
import os
import pickle

models = glob.glob('model_*')
themes = [
    'celebration', 'cooking', 'cowboy', 'education', 'environment',
    'halloween', 'harry_potter', 'indian', 'magic'
]

letters = [
    'uppera', 'upperb', 'upperc', 'upperd', 'uppere', 'upperf', 'upperg', 'upperh', 'upperi', 'upperj',
    'upperk', 'upperl', 'upperm', 'uppern', 'uppero', 'upperp', 'upperq', 'upperr', 'uppers', 'uppert',
    'upperu', 'upperv', 'upperw', 'upperx', 'uppery', 'upperz', 'lowera', 'lowerb', 'lowerc', 'lowerd',
    'lowere', 'lowerf', 'lowerg', 'lowerh', 'loweri', 'lowerj', 'lowerk', 'lowerl', 'lowerm', 'lowern',
    'lowero', 'lowerp', 'lowerq', 'lowerr', 'lowers', 'lowert', 'loweru', 'lowerv', 'lowerw', 'lowerx',
    'lowery', 'lowerz'
]

for model in models:
    for theme in themes:
        output = "<html><body><center><table border=1>"
        if not os.path.exists('%s/%s' % (model, theme)):
            os.makedirs('%s/%s' % (model, theme))
        with open('%s/%s.pickle' % (model, theme), 'rb') as f:
            data = pickle.load(f)
        for letter in letters:
            output += "<tr><td><img src='../../letters/%s58.png'></td>" % letter
            for i in range(5):
                filename = data[letter][0][i][data[letter][0][i].rindex('/') + 1:]
                output += "<td><img src='../../themes/%s/%s'><br>distance = <b>%.4f</b></td>" % (theme, filename, data[letter][1][i])
            output += "</tr>"
        output += "</table></center></body></html>"
        with open('%s/%s/index.html' % (model, theme), 'w') as f:
            f.write(output)
        pass
