import tgt
from os import walk, listdir
from os.path import isfile, join
import re

alignedDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/"

allAlignedFiles = [f for f in listdir(alignedDir) if re.search(r'TextGrid', f)]

numberOfSpk = 5

filesBySpeaker = []
for i in range(1,numberOfSpk+1):
	speaker = 'S' + str(i).zfill(2)
	speakerFiles = [f for f in allAlignedFiles if re.search(speaker, f)]
	filesBySpeaker.append(speakerFiles)

print(filesBySpeaker[0])