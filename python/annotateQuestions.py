import tgt
from os import walk, listdir
from os.path import isfile, join
import re

toAnnotateDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/"
outDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/out/"

allToAnnotate = [f for f in listdir(toAnnotateDir) if re.search(r'TextGrid', f)]
textGrids = [[tgt.read_textgrid(toAnnotateDir + f), f] for f in allToAnnotate]


# Sort textgrids into those that elicit broad and narrow answers.
broad = []
narrow = []
for i in textGrids:
    st = i[0].start_time
    et = i[0].end_time
    words = [f.text for f in i[0].tiers[1]] # Get words in the words tier
    if "NEN" in words:
        annInterval = tgt.Interval(start_time=st, end_time=et, text="n-nen")
        annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Question Type")
        annTier.add_interval(annInterval)
        i[0].add_tier(annTier)
        narrow.append(i)
    elif "LAMAS" in words:
        annInterval = tgt.Interval(start_time=st, end_time=et, text="n-lamas")
        annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Question Type")
        annTier.add_interval(annInterval)
        i[0].add_tier(annTier)
        narrow.append(i)
    else:
        broad.append(i)



for i in narrow:
    tgt.write_to_file(i[0], outDir + i[1] + '_annotated' + '.TextGrid', format='short')







# tg = tgt.read_textgrid(toAnnotateDir + allToAnnotate[0])