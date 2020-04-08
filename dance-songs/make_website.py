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
music_matrices = []
idx = 0

for genre in folders:
    for songname in os.listdir(genre):

        # check that songname ends in .mp3
        if songname[-4:] != '.mp3':
            continue

        # append srno
        idx += 1
        srno.append(idx)

        # append genre
        genres.append(genre)

        # append durations
        y, sr = librosa.load(genre + "/" + songname)
        duration = librosa.get_duration(y=y, sr=sr)
        durations.append(str(duration))

        # append songname
        songnames.append(songname)

        # append actual song location
        songs.append(genre + "/" + songname)

        # compute music matrix
        # if genre in ["rocknroll", "jazz", "instrumental"]:
        #     hop_length = 128
        #     lifter = 0
        #     n_mfcc = 20
        #     mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, lifter=lifter, hop_length=hop_length)
        #     R = np.transpose(librosa.segment.recurrence_matrix(mfcc, sym=True))    # already normalized in 0-1
        #     R = R + np.zeros(R.shape)    # change (True, False) to (1, 0)
        #     np.fill_diagonal(R, 1)
        #     if int(duration) != round(duration):
        #         d = round(duration)
        #     else:
        #         d = int(duration)
        #     plt.xticks(np.arange(0, R.shape[0], R.shape[0] / duration), np.arange(0, d, 1.0))
        #     plt.yticks(np.arange(0, R.shape[0], R.shape[0] / duration), np.arange(0, d, 1.0))
        #     plt.imshow(R)
        #     plt.savefig(genre + "/" + songname + '.png')

        # append music matrix
        music_matrices.append(genre + "/" + songname + '.png')

html_code = "<center><table border=1><tr><b><td>Sr. No.</td><td>Genre</td><td>Song Name</td><td>Audio</td><td>Duration (secs)</td><td>Music Matrix</td></b></tr>"

for i in range(len(songs)):
    row_data = "<td>%d.</td><td>%s</td><td>%s</td><td><audio controls><source src=%s type='audio/mpeg'></audio></td><td>%s</td><td><img src=%s></td>" % (srno[i], genres[i], songnames[i], songs[i], durations[i], music_matrices[i])
    html_code += "<tr>%s</tr>" % row_data

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
