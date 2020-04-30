"""Make website to visualize data.

-- genre
-- name of song
-- length
-- image

python3.7 make_website
"""
import numpy as np
import librosa
import madmom
import pdb
import os


folders = ["acapella", "african", "american-pop", "bollywood", "chinese", "indian-classical", "latin", "no-lyrics", "offbeat", "rap", "rocknroll", "jazz", "instrumental"]

# get folder and filenames
srno = []
genres = []
songnames = []
songs = []
durations = []
numbeats = []
correlations = []
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

        # read the correlation information
        correlations.append(np.loadtxt(genre + "/" + currsong + "/correlations.txt", dtype=float))

        # get number of beats in song
        proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
        act = madmom.features.beats.RNNBeatProcessor()(genre + "/" + currsong + "/song.mp3")
        beat_times = proc(act)
        numbeats.append(len(beat_times))

# sort all lists in decending order of numbeats
sorted_idx = np.argsort(numbeats)[::-1]
genres = [genres[i] for i in sorted_idx]
songnames = [songnames[i] for i in sorted_idx]
songs = [songs[i] for i in sorted_idx]
durations = [durations[i] for i in sorted_idx]
music_matrix_downsize = [music_matrix_downsize[i] for i in sorted_idx]
music_matrix_upsize = [music_matrix_upsize[i] for i in sorted_idx]
dance_matrix1 = [dance_matrix1[i] for i in sorted_idx]
dance_matrix2 = [dance_matrix2[i] for i in sorted_idx]
dance_matrix3 = [dance_matrix3[i] for i in sorted_idx]
dance_matrix4 = [dance_matrix4[i] for i in sorted_idx]
dance_video1 = [dance_video1[i] for i in sorted_idx]
dance_video2 = [dance_video2[i] for i in sorted_idx]
dance_video3 = [dance_video3[i] for i in sorted_idx]
dance_video4 = [dance_video4[i] for i in sorted_idx]
correlations = [correlations[i] for i in sorted_idx]
numbeats = [numbeats[i] for i in sorted_idx]

css = "<head><link rel='stylesheet' href='mycss.css'></head>"
html_code = css + "<center><table border=1><thead><tr><b><th>Sr. No.</th><th>Genre</th><th>Song Name</th><th>Audio</th><th>Duration (secs)</th><th>Number of beats</th><th>Music Matrix Downsize</th><th>Music Matrix Upsize</th><th>Dance Matrix Baseline 1 (un-synced, random actions from LRS)</th><th>Dance Video Baseline 1 (un-synced, random actions from LRS)</th><th>Dance Matrix Baseline 2 (un-synced, left to right)</th><th>Dance Video Baseline 2 (un-synced, left to right)</th><th>Dance Matrix Baseline 3 (synced, left to right)</th><th>Dance Video Baseline 3 (synced, left to right)</th><th>Dance Matrix Baseline 4 (synced, random actions from LRS)</th><th>Dance Video Baseline 4 (synced, random actions from LRS)</th></b></tr></thead><tbody>"

for i in range(len(songs)):
    row_data = "<td>%d.</td><td>%s</td><td>%s</td><td><audio controls><source src=%s type='audio/mpeg'></audio></td><td>%s</td><td>%d</td><td><img src=%s></td><td><img src=%s></td><td><figure><img src=%s><figcaption>Correlation-downsize = %f<br>Correlation-upsize = %f</figcaption></figure></td><td><video controls><source src=%s></video></td><td><figure><img src=%s><figcaption>Correlation-downsize = %f<br>Correlation-upsize = %f</figcaption></figure></td><td><video controls><source src=%s></video></td><td><figure><img src=%s><figcaption>Correlation-downsize = %f<br>Correlation-upsize = %f</figcaption></figure></td><td><video controls><source src=%s></video></td><td><figure><img src=%s><figcaption>Correlation-downsize = %f<br>Correlation-upsize = %f</figcaption></figure></td><td><video controls><source src=%s></video></td>" % (srno[i], genres[i], songnames[i], songs[i], durations[i], numbeats[i], music_matrix_downsize[i], music_matrix_upsize[i], dance_matrix1[i], correlations[i][0], correlations[i][4], dance_video1[i], dance_matrix2[i], correlations[i][1], correlations[i][5], dance_video2[i], dance_matrix3[i], correlations[i][2], correlations[i][6], dance_video3[i], dance_matrix4[i], correlations[i][3], correlations[i][7], dance_video4[i])
    html_code += "<tr>%s</tr>" % row_data

html_code += "</tbody></table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
