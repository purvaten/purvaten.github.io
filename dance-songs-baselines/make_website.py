"""Make website to visualize data.

-- genre
-- name of song
-- length
-- image

python3.7 make_website
"""
import matplotlib.pyplot as plt
import numpy as np
import librosa
import sys
import os
import pdb


folders = ["acapella", "african", "american-pop", "bollywood", "chinese", "indian-classical", "latin", "no-lyrics", "offbeat", "rap", "rocknroll", "jazz", "instrumental"]

# get folder and filenames
srno = []
genres = []
songnames = []
songs = []
durations = []
music_matrix_upsize, music_matrix_downsize = [], []
dance_matrix1, dance_matrix2, dance_matrix3, dance_matrix4 = [], [], [], []
dance_video1, dance_video2, dance_video3, dance_video4 = [], [], [], []
idx = 0

for genre in folders:
    for currsong in os.listdir(genre):
        # append srno
        idx += 1
        srno.append(idx)

        # append genre and songname
        genres.append(genre)
        songnames.append(currsong)

        # append actual song location
        songs.append(genre + "/" + currsong + "/song.mp3")

        # append durations
        y, sr = librosa.load(genre + "/" + currsong + "/song.mp3")
        duration = librosa.get_duration(y=y, sr=sr)
        durations.append(str(duration))

        # append music matrices location
        music_matrix_downsize.append(genre + "/" + currsong + "/music_matrix_downsize.png")
        music_matrix_upsize.append(genre + "/" + currsong + "/music_matrix_upsize.png")

        # append dance matrices location
        dance_matrix1.append(genre + "/" + currsong + "/dance_matrix1.png")
        dance_matrix2.append(genre + "/" + currsong + "/dance_matrix2.png")
        dance_matrix3.append(genre + "/" + currsong + "/dance_matrix3.png")
        dance_matrix4.append(genre + "/" + currsong + "/dance_matrix4.png")

        # append dance videos location
        dance_video1.append(genre + "/" + currsong + "/output1.mp4")
        dance_video2.append(genre + "/" + currsong + "/output2.mp4")
        dance_video3.append(genre + "/" + currsong + "/output3.mp4")
        dance_video4.append(genre + "/" + currsong + "/output4.mp4")

html_code = "<center><table border=1><tr><b><td>Sr. No.</td><td>Genre</td><td>Song Name</td><td>Audio</td><td>Duration (secs)</td><td>Music Matrix Downsize</td><td>Music Matrix Upsize</td><td>Dance Matrix Baseline 1</td><td>Dance Video Baseline 1</td><td>Dance Baseline 2</td><td>Dance Video Baseline 2</td><td>Dance Baseline 3</td><td>Dance Video Baseline 3</td><td>Dance Baseline 4</td><td>Dance Video Baseline 4</td></b></tr>"

for i in range(len(songs)):
    row_data = "<td>%d.</td><td>%s</td><td>%s</td><td><audio controls><source src=%s type='audio/mpeg'></audio></td><td>%s</td><td><img src=%s></td><td><img src=%s></td><td><img src=%s></td><td><video controls><source src=%s></video></td><td><img src=%s></td><td><video controls><source src=%s></video></td><td><img src=%s></td><td><video controls><source src=%s></video></td><td><img src=%s></td><td><video controls><source src=%s></video></td>" % (srno[i], genres[i], songnames[i], songs[i], durations[i], music_matrix_downsize[i], music_matrix_upsize[i], dance_matrix1[i], dance_video1[i], dance_matrix2[i], dance_video2[i], dance_matrix3[i], dance_video3[i], dance_matrix4[i], dance_video4[i])
    html_code += "<tr>%s</tr>" % row_data

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
