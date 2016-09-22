#importing datetime modules
import time
from datetime import date

#converting time into subtitle time range format
class timeFunctions:
    @staticmethod
    def outputTimeRange(startMin, startSec, startMillisec, endMin, endSec, endMillisec):            
        timeRange = "00:" + str(startMin).zfill(2) + ":" + str(startSec).zfill(2) + startMillisec + " --> 00:" + str(endMin).zfill(2) + ":" + str(endSec).zfill(2) + endMillisec
        return timeRange
    
#init variables
subCount = 0
startTime = time.time()
videoFileName = "subtitles" + str(time.time())[5:10] + ".srt"

#open subtitle input file and output file
with open("rawSubtitles.txt") as f:
    rawSubtitleList = f.readlines()
writeFile = open(videoFileName, 'w+')

#first user input
userIn = raw_input('Press Enter when dialogue starts.  Input any letter when subtitle line terminates.  Type "done" when you\'re done : ')

while userIn != 'done':
    if userIn == "":
        subStart = time.time() - startTime
        print "Reinstantiate subtitle start time."
        userIn = raw_input('> ')
        pass
    else:
        subCount += 1
        dotPos = str(subStart).find('.')
        startMin, startSec = divmod(int(str(subStart)[:dotPos]), 60)
        startMillisec = str(subStart)[dotPos:dotPos + 4]
        subStart = time.time() - startTime
        dotPos = str(subStart).find('.')
        endMin, endSec = divmod(int(str(subStart)[:dotPos]), 60)
        endMillisec = str(subStart)[dotPos:dotPos + 4]
        timeRange = timeFunctions.outputTimeRange(startMin, startSec, startMillisec, endMin, endSec, endMillisec)
        writeFile.write(str(subCount) + '\n' + timeRange + '\n' + rawSubtitleList[subCount - 1] + '\n')
        print timeRange
        print rawSubtitleList[subCount - 1]
        userIn = raw_input('> ')
        pass
        
    try:
        var = rawSubtitleList[subCount + 1]
    except IndexError:
        break