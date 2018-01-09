import tgt
from os import walk, listdir
from os.path import isfile, join
import re

toAnnotateDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/"
outDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/out/"

allToAnnotate = [f for f in listdir(toAnnotateDir) if re.search(r'TextGrid', f)]
textGrids = [[tgt.read_textgrid(toAnnotateDir + f), f] for f in allToAnnotate]

items = [
"jtéleb7",
"xajab7",
"suq7uk7",
"cháaj",
"jch7úuk7",
"qálaq",
"qapoop",
"kaach7",
"qajóoq7",
"jkinaq7",
"rixóqil",
"qaxoot",
"jcháaj",
"rixóql",
"kinaq7",
"jkaach7",
"jxajab7"
]

# items = [
# 'JTLB', 
# 'XJB', 
# 'SQK', 
# 'CHJ', 
# 'JCHK', 
# 'QLQ', 
# 'QPP', 
# 'KCH', 
# 'QJQ', 
# 'JKNQ', 
# 'RXQL', 
# 'QXT', 
# 'JCHJ', 
# 'RXQL', 
# 'KNQ', 
# 'JKCH', 
# 'JXJB']

def strip(string):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    string = string.upper()
    string = ''.join([c for c in string if c in consonants])
    return string

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

for i in broad:
    st = i[0].start_time
    et = i[0].end_time
    words = [f.text for f in i[0].tiers[1]] # Get words in the words tier


for i in narrow:
    tgt.write_to_file(i[0], outDir + i[1] + '_annotated' + '.TextGrid', format='short')







# tg = tgt.read_textgrid(toAnnotateDir + allToAnnotate[0])