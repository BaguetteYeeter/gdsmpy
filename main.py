from time import sleep
import sys
import vlc
from mutagen.mp3 import MP3

#You can change the values below
song = "songs/antihero.mp3"
title_length = 20
name = "Taylor Swift - Anti Hero" + " "*5
width = 60
#Stop changing here

p = vlc.MediaPlayer(song)
p.play()

song_length = int(MP3(song).info.length)
song_minutes = str(int(song_length/60))
song_seconds = str(int(song_length%60)).rjust(2, "0")
buffer = ""
buffer_index = 0

for i in range(0, title_length):
    buffer += name[i]
for i in buffer:
    sys.stdout.write(i)
sys.stdout.flush()

sys.stdout.write(" [%s]" % (" "*width))
sys.stdout.flush()

sys.stdout.write(" (0:00 / %s:%s)" % (song_minutes, song_seconds))
sys.stdout.flush()

sys.stdout.write("\b" * (title_length + 3 + width + 13 + len(song_minutes)))

buffer_index = title_length
second_buffer = 0
bar_length = 0

for i in range(1, song_length*2+1):
    sleep(0.5)
    second_buffer += 1
    for j in buffer:
        sys.stdout.write(j)
    buffer = buffer[1:]
    if buffer_index >= len(name):
        buffer_index = 0
    buffer += name[buffer_index]

    sys.stdout.write(" [%s]" % ("█"*int(bar_length)).ljust(width))
    if second_buffer == 2:
        bar_length += width / song_length
        second_buffer = 0

    sys.stdout.write(" (%d:%s / %s:%s)" % (int(int(i/2)/60), str(int(int(i/2)%60)).rjust(2, "0"), song_minutes, song_seconds))
    sys.stdout.flush()

    sys.stdout.write("\b" * (title_length + 3 + width + 13 + len(song_minutes)))
    buffer_index += 1

print("")