import tgt
from os import walk, listdir
from os.path import isfile, join
import re

toAnnotateDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/"
outDir = "/Users/balamkej/Dropbox/Uspanteko_NSF_project/Recordings/2017/For_analysis/Forced_aligned/resample/out/"

allToAnnotate = [f for f in listdir(toAnnotateDir) if re.search(r'TextGrid', f)]
textGrids = [[tgt.read_textgrid(toAnnotateDir + f), f] for f in allToAnnotate]

# items = [
# "jtéleb7",
# "xajab7",
# "suq7uk7",
# "cháaj",
# "jch7úuk7",
# "qálaq",
# "qapoop",
# "kaach7",
# "qajóoq7",
# "jkinaq7",
# "rixóqil",
# "qaxoot",
# "jcháaj",
# "rixóql",
# "kinaq7",
# "jkaach7",
# "jxajab7",
# "sib7ooy",
# "xájbla"
# ]

items = [
'JTLB', 
'XJB', 
'SQK', 
'CHJ', 
'JCHK', 
'QLQ', 
'QPP', 
'KCH', 
'QJQ', 
'JKNQ', 
'RXQL', 
'QXT', 
'JCHJ', 
'RXQL', 
'KNQ', 
'JKCH', 
'JXJB',
'SBY',
'XJBL']

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
        annInterval = tgt.Interval(start_time=st, end_time=et, text="NEN-f")
        annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Question Type")
        annTier.add_interval(annInterval)
        i[0].add_tier(annTier)
        narrow.append(i)
    if "NEEN" in words:
        annInterval = tgt.Interval(start_time=st, end_time=et, text="NEEN-f")
        annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Question Type")
        annTier.add_interval(annInterval)
        i[0].add_tier(annTier)
        narrow.append(i)
    elif "LAMAS" in words:
        annInterval = tgt.Interval(start_time=st, end_time=et, text="LAMAS-n")
        annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Question Type")
        annTier.add_interval(annInterval)
        i[0].add_tier(annTier)
        narrow.append(i)
    else:
        broad.append(i)

for i in narrow:
    tgt.write_to_file(i[0], outDir + i[1] + '_annotated_focus' + '.TextGrid', format='short')

def isFinal(tiers,tier):
    for i in range(len(tiers)):
        if tiers[i] == tier:
            if tiers[i+1].text == "sp":
                return True
            else:
                return False

annBroad = []
for i in broad:
    tiers = i[0].tiers[1]
    for j in tiers:
        if strip(j.text) in items:
            st = j.start_time
            et = j.end_time
            if isFinal(tiers,j) == True:
                ann =  j.text + "-g-l"
            else:
                ann = j.text + "-g-m"
            annInterval = tgt.Interval(start_time=st, end_time=et, text=ann)
            annTier = tgt.IntervalTier(start_time=st, end_time=et, name="Question Type")
            annTier.add_interval(annInterval)
            i[0].add_tier(annTier)
            annBroad.append(i)
            break # only grab the first match

for i in annBroad:
    tgt.write_to_file(i[0], outDir + i[1] + '_annotated_given' + '.TextGrid', format='short')

narrowFiles = [f[1] for f in narrow]
broadFiles = [f[1] for f in annBroad]
allFiles = narrowFiles + broadFiles

bad = []
for i in allToAnnotate:
    if i in allFiles:
        pass
    else:
        bad.append(i)

for i in bad:
    print(i)    

# print(bad)

# tg = tgt.read_textgrid(toAnnotateDir + allToAnnotate[0])