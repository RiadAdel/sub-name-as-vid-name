# videos should be in alphabetical order
import os

if __name__ == "__main__":
    vidExt = "mkv"
    subExt = "srt"

    vid = sorted(name for name in os.listdir() if name.split(".")[-1] == vidExt)
    sub = sorted(name for name in os.listdir() if name.split(".")[-1] == subExt)

    if len(vid) != len(sub):
        print("warning!!! no. of subtitles not equal to no. of videos")

    for indx in range(min(len(vid), len(sub))):
        os.rename(sub[indx], vid[indx][: -len(vidExt)] + subExt)
