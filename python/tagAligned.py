import tgt
from os import walk, listdir
from os.path import isfile, join
import re

alignedDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/"
expDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/"

allAlignedFiles = [f for f in listdir(alignedDir) if re.search(r'TextGrid', f)]
allExpFolders = [f for f in listdir(expDir) if re.search(r'S0', f)]

numberOfSpk = 5

alignedFilesBySpeaker = []
for i in range(1,numberOfSpk+1):
    speaker = 'S' + str(i).zfill(2)
    speakerFiles = [f for f in allAlignedFiles if re.search(speaker, f)]
    alignedFilesBySpeaker.append(speakerFiles)

rawFilesBySpeakers = []
for i in allExpFolders:
    directory = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/" + i
    rawFilesBySpeakers = rawFilesBySpeakers + [f for f in listdir(directory) if re.search(r'TextGrid', f)]

list.sort(allExpFolders)
list.sort(alignedFilesBySpeaker)

for i in alignedFilesBySpeaker:
    sort(i)

for i in range(numberOfSpk):
    expFile = expDir + allExpFolders[i] + rawFilesBySpeakers[i]
    alignedList = alignedFilesBySpeaker[i]
    tg = tgt.read_textgrid(expFile)
    annotations_tier = tg.get_tier_by_name('Annotations')
    for j in range(annotations_tier):
        alignedTextGrid = tgt.read_textgrid(alignedDir + alignedList[j])
        annotation = annotations_tier[j].text

# A function that takes a textgrid and adds an annotation tier that matches
# the annotation tier of an annotated textgrid. Note, the function assumes
# the textgrid to be annotate already has a first tier bearing the start
# and end times.

def annotate(textGrid,annotatedTextGrid):
    annotation = annotations_tier[annotatedTextGrid].text
    st = textGrid.tiers[0].start_time
    et = textGrid.tiers[0].end_time
    interval = tgt.Interval(start_time=st, end_time=et, text=annotation)
    tier = tgt.IntervalTier(start_time=st, end_time=et, name="Annotation")
    tier.add_interval(interval)
    textGrid.add_tier(tier)
    return textGrid




expFile = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/" + "S01_Rosa_Petranilla" + "/" + "S01_Rosa_Petranilla_Mic1_OMNIDIR_Mic2_UNIDER.TextGrid"
tg = tgt.read_textgrid(expFile)
annotations_tier = tg.get_tier_by_name('Annotations')
