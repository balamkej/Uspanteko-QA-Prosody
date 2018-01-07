import tgt
from os import walk, listdir
from os.path import isfile, join
import re

annotatedDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/"
alignedDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Force_aligned/resample/"
outDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Merged/"

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

allAnnotatedGrid = [f for f in listdir(annotatedDir) if re.search(r'TextGrid', f)]
allAlignedGrid = [f for f in listdir(alignedDir) if re.search(r'TextGrid', f)]

len(allAnnotatedGrid)
len(allAlignedGrid)

list.sort(allAnnotatedGrid)
list.sort(allAlignedGrid)

for i in range(allAnnotatedGrid):
	annotatedTextGrid = tgt.read_textgrid(annotatedDir + allAnnotatedGrid[i])
	alignedTextGrid = tgt,read_textgrid(alignedDir + allAlignedGrid[i])
	outGrid = annotate(alignedTextGrid,annotatedTextGrid)
	tgt.write_to_file(outGrid, outDir + allAlignedGrid[i] + '_annotated' + '.TextGrid', format='short')