import tgt
from os import walk, listdir
from os.path import isfile, join
import re

annotatedDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/"
alignedDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/"
outDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Merged/"
# consonants = "BCDFGHJKLMNPQRSTVWXYZ"

# A function that takes a textgrid and adds an annotation tier that matches
# the annotation tier of an annotated textgrid. Note, the function assumes
# the textgrid to be annotate already has a first tier bearing the start
# and end times.

def annotate(textGrid,annotatedTextGrid):
    utterance = annotatedTextGrid.tiers[0][0].text
    annotation = annotatedTextGrid.tiers[2][0].text
    st = textGrid.tiers[0].start_time
    et = textGrid.tiers[0].end_time
    uttInterval = tgt.Interval(start_time=st, end_time=et, text=utterance)
    annInterval = tgt.Interval(start_time=st, end_time=et, text=annotation)
    uttTier = tgt.IntervalTier(start_time=st, end_time=et, name="Utterance")
    annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Annotation")
    uttTier.add_interval(uttInterval)
    annTier.add_interval(annInterval)
    textGrid.add_tier(uttTier)
    textGrid.add_tier(annTier)
    return textGrid

def strip(string):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    string = string.upper()
    string = ''.join([c for c in string if c in consonants])
    return string

def findTarget(textGrid):
    target = textGrid.tiers[3][0].text
    target = target.split("-")
    target = strip(target[1])
    return target

def findMatchInterval(textGrid, target):
    for interval in textGrid.tiers[1]:
        if strip(interval.text) == target:
            return interval

def createTargetGrid(textGrid):
    targetInterval = findMatchInterval(textGrid, findTarget(textGrid))
    st = targetInterval.start_time
    et = targetInterval.end_time
    targetTier = tgt.IntervalTier(start_time=st, end_time=et, name="Target Word")
    targetTier.add_interval(targetInterval)
    textGrid.add_tier(targetTier)
    return textGrid

allAnnotatedGrid = [f for f in listdir(annotatedDir) if re.search(r'TextGrid', f)]
allAlignedGrid = [f for f in listdir(alignedDir) if re.search(r'TextGrid', f)]

list.sort(allAnnotatedGrid)
list.sort(allAlignedGrid)

for i in range(len(allAnnotatedGrid)):
    annotatedTextGrid = tgt.read_textgrid(annotatedDir + allAnnotatedGrid[i])
    alignedTextGrid = tgt.read_textgrid(alignedDir + allAlignedGrid[i])
    outGrid = annotate(alignedTextGrid,annotatedTextGrid)
    outGrid = createTargetGrid(outGrid)
    print(allAlignedGrid[i])
    tgt.write_to_file(outGrid, outDir + allAlignedGrid[i] + '_merged' + '.TextGrid', format='short')