"""Make website to visualize data.

-- genre
-- name of song
-- length
-- image

python3.7 make_website
"""
import numpy as np
import librosa
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
music_matrix_upsize, music_matrix_downsize = [], []
dance_matrix1, dance_matrix2, dance_matrix3, dance_matrix4 = [], [], [], []
dance_video10, dance_video11, dance_video12, dance_video13, dance_video2, dance_video3, dance_video40, dance_video41, dance_video42, dance_video43 = [], [], [], [], [], [], [], [], [], []
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
        dance_video10.append(genre + "/" + currsong + "/output10.mp4")
        dance_video11.append(genre + "/" + currsong + "/output11.mp4")
        dance_video12.append(genre + "/" + currsong + "/output12.mp4")
        dance_video13.append(genre + "/" + currsong + "/output13.mp4")
        dance_video2.append(genre + "/" + currsong + "/output2.mp4")
        dance_video3.append(genre + "/" + currsong + "/output3.mp4")
        dance_video40.append(genre + "/" + currsong + "/output40.mp4")
        dance_video41.append(genre + "/" + currsong + "/output41.mp4")
        dance_video42.append(genre + "/" + currsong + "/output42.mp4")
        dance_video43.append(genre + "/" + currsong + "/output43.mp4")

        # read the correlation information and number of beats in song
        numbeats.append(np.loadtxt(genre + "/" + currsong + "/num_beats.txt", dtype=float))

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
dance_video10 = [dance_video10[i] for i in sorted_idx]
dance_video11 = [dance_video11[i] for i in sorted_idx]
dance_video12 = [dance_video12[i] for i in sorted_idx]
dance_video13 = [dance_video13[i] for i in sorted_idx]
dance_video2 = [dance_video2[i] for i in sorted_idx]
dance_video3 = [dance_video3[i] for i in sorted_idx]
dance_video40 = [dance_video40[i] for i in sorted_idx]
dance_video41 = [dance_video41[i] for i in sorted_idx]
dance_video42 = [dance_video42[i] for i in sorted_idx]
dance_video43 = [dance_video43[i] for i in sorted_idx]
numbeats = [numbeats[i] for i in sorted_idx]

css = "<head><link rel='stylesheet' href='mycss.css'></head>"
html_code = css + "<center><table border=1><thead><tr><b><th>Sr. No.</th><th>Genre</th><th>Song Name</th><th>Audio</th><th>Duration (secs)</th><th>Number of beats</th><th>Music Matrix Downsize</th><th>Music Matrix Upsize</th><th>Dance Matrix Baseline 1 (un-synced, random actions from LRS)</th><th>Dance Video Baseline 1 (un-synced, random actions from LRS)</th><th>Dance Matrix Baseline 2 (un-synced, left to right)</th><th>Dance Video Baseline 2 (un-synced, left to right)</th><th>Dance Matrix Baseline 3 (synced, left to right)</th><th>Dance Video Baseline 3 (synced, left to right)</th><th>Dance Matrix Baseline 4 (synced, random actions from LRS)</th><th>Dance Video Baseline 4 (synced, random actions from LRS)</th></b></tr></thead><tbody>"

for i in range(len(songs)):
    row_data = "<td>%d.</td><td>%s</td><td>%s</td><td><audio controls><source src=%s type='audio/mpeg'></audio></td><td>%s</td><td>%d</td><td><img src=%s></td><td><img src=%s></td><td><figure><img src=%s></figure></td><td><video controls><source src=%s></video><video controls><source src='%s'></video><br><video controls><source src='%s'></video><video controls><source src='%s'></video></td><td><figure><img src=%s></figure></td><td><video controls><source src=%s></video></td><td><figure><img src=%s></figure></td><td><video controls><source src=%s></video></td><td><figure><img src=%s></figure></td><td><video controls><source src=%s></video><video controls><source src=%s></video><br><video controls><source src=%s></video><video controls><source src=%s></video></td>" % (srno[i], genres[i], songnames[i], songs[i], durations[i], numbeats[i], music_matrix_downsize[i], music_matrix_upsize[i], dance_matrix1[i], dance_video10[i], dance_video11[i], dance_video12[i], dance_video13[i], dance_matrix2[i], dance_video2[i], dance_matrix3[i], dance_video3[i], dance_matrix4[i], dance_video40[i], dance_video41[i], dance_video42[i], dance_video43[i])
    html_code += "<tr>%s</tr>" % row_data

html_code += "</tbody></table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
