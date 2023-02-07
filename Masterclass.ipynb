import uproot  # import uproot which is used for reading ROOT files
import math


##################
file = uproot.open("data_pp.root")

dataTree = file["mytree"]

print(dataTree.typenames())

data = dataTree.arrays(["tracks", "centrality"], library="np")
###################

trackCounter=0
eventCounter=0
for i in range(len(data["tracks"])):
    cent= data["centrality"][i]
    tracks= data["tracks"][i]
    
    if cent > 50:    
        eventCounter+=1

        for tr in range(len(tracks)):
            # print(tracks[tr])
            if tracks[tr] > 1 and tracks[tr] < 2:
                trackCounter+=1

trackCounterStat=math.sqrt(trackCounter)
TracksPerEvent=trackCounter / eventCounter
TracksPerEventStat=trackCounterStat / eventCounter
print(TracksPerEvent)
print(TracksPerEventStat)
