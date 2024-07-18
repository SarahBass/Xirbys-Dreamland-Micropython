############################################################################
#                      __  ___      _           
#                      \ \/ (_)_ __| |__  _   _ 
#                       \  /| | '__| '_ \| | | |
#                       /  \| | |  | |_) | |_| |
#                      /_/\_\_|_|  |_.__/ \__, |
#                                         |___/ 
#
#              / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
#             (  C  o  c  o   ) ( C   l   o  u   d   s  )
#              \ / \ / \ / \ /   \ / \ / \ / \ / \ / \_/ 
#   ˚☽                                     
#            ☆                          ☆                 ☆            ☆
#               Volume 1. Coco Clouds - Xirby's Dreamland                  
############################################################################

#                              Written by Sarah Bass
#                Check out my other games for Android, Fitbit, and more
#                           https://github.com/SarahBass
################
#####IMPORTS####
################
import thumby
import gc
import time
gc.enable() #Garbage Collection
#With Garbage Collection the memoryallocated is 60,096 bytes

#Global Variables-------------------------# 
abutton = 0
#Average Xirby or Enemy is 16 x 16
width=16
height=16
xPosition = int((thumby.display.width/2) - (width/2))
yPosition = int((thumby.display.height/2) - (height/2))

#####################
#    Music          #
#####################

#Music Notes within Human Comfort 0 to 1046
#Music Re-Designed to not hurt ears. Sounds above 2000Hz can cause hearing damage
#Xirby Song is a remix to avoid copyright and was composed by myself
MusicNoteDict = {
    0: 1046,
    "C3": 130,
    "D3": 147,
    "E3": 165,
    "F3": 175,
    "G3": 196,
    "AS3": 233,
    "Bf3": 233,
    "A3": 220,
    "B3": 247,
    "C4": 261,
    "CS4": 277,
    "D4": 294,
    "DS4": 311,
    "E4": 330,
    "F4": 349,
    "FS4": 370,
    "G4": 392,
    "GS4": 415,
    "Bf4": 466,
    "An4": 440,
    "B4": 494,
    "C5": 523,
    "CS5": 554,
    "D5": 587,
    "DS5": 622,
    "E5": 659,
    "F5": 698,
    "FS5": 740,
    "G5": 784,
    "GS5": 831,
    "An5": 880,
    "B5": 988,
    "C6": 1046
}
#Introduction Theme
SongList1 = [
    # Original Opening Music Designed by Myself
    "B3", "E4", "FS4", "GS4", "B3", "E4", "FS4", "GS4",
    "B4", "E5", "FS5", "GS5", "B4", "E5", "FS5", "GS5",
    # Original Boss Music Designed by Myself
    "C4", "G3", "AS3", "A3",
    "G3", "C3", "C3", "G3", "G3", "G3",
    "C4", "G3", "AS3", "A3",
    "G3",
    "C4", "G3", "AS3", "A3",
    "G3", "C3", "C3", "G3", "G3", "G3",
    "F3", "E3", "D3", "C3",
    # Xirby Remix Main Game - Composed by taking Sheet Music notes, remixing lines, and lowering an octave
    "DS5", "D5", "C5", "Bf4", "F4", "D4", "GS4", "Bf4", "C5", "D5", "B4", 0,
    "C5", 0, "G4", 0, "DS4", "D4", "C4", 0, "C4", "D4", "DS4", "C4", "Bf3", "C4", "G3", 0,
    "C5", 0, "G4", 0, "DS4", "D4", "C4", "C4", "D4", "DS4", "F4", "D4", "Bf3", "C4", "G3", "C4", 0,
    "C5", 0, "G4", 0, "D4", "F4", "G4", "C4", "D4", "F4", "D4", "Bf3", "C4", 0,
    # Xirby Remix Part 2  Composed by taking Sheet Music notes, remixing lines, and lowering an octave
    "DS4", "DS4", "DS4", "DS4", "F4", "G4", "G4", "G4", "F4", "DS4", "D4", "D4", "D4", "D4", "DS4", "D4",
    "DS4", "D4", "C4", "C4", "C4", "C4", "D4", "DS4", "DS4", "DS4", "D4", "C4", "Bf3", "Bf3", "Bf3", "Bf3", "C4", "D4",
    "D5", "F5", "G5", "D5", "F5", "G5", "D5", "F5", "D5", "F5", "G5", "C6", "B5", 0
]
#Waiting and Boss Music
SongList2 = ["C4", "G3", "AS3", "A3",
    "G3", "C3", "C3", "G3", "G3", "G3",
    "C4", "G3", "AS3", "A3",
    "G3",
    "C4", "G3", "AS3", "A3",
    "G3", "C3", "C3", "G3", "G3", "G3",
    "F3", "E3", "D3", "C3"]
#Game Music Main    
SongList3 = [ "DS5", "D5", "C5", "Bf4", "F4", "D4", "GS4", "Bf4", "C5", "D5", "B4", 0,
    "C5", 0, "G4", 0, "DS4", "D4", "C4", 0, "C4", "D4", "DS4", "C4", "Bf3", "C4", "G3", 0,
    "C5", 0, "G4", 0, "DS4", "D4", "C4", "C4", "D4", "DS4", "F4", "D4", "Bf3", "C4", "G3", "C4", 0,
    "C5", 0, "G4", 0, "D4", "F4", "G4", "C4", "D4", "F4", "D4", "Bf3", "C4", 0]    
#End Game
SongList4 = ["DS4", "DS4", "DS4", "DS4", "F4", "G4", "G4", "G4", "F4", "DS4", "D4", "D4", "D4", "D4", "DS4", "D4",
    "DS4", "D4", "C4", "C4", "C4", "C4", "D4", "DS4", "DS4", "DS4", "D4", "C4", "Bf3", "Bf3", "Bf3", "Bf3", "C4", "D4",
    "D5", "F5", "G5", "D5", "F5", "G5", "D5", "F5", "D5", "F5", "G5", "C6", "B5", 0]

#Continue Screen
SongList5 =["B3", "E4", "FS4", "GS4", "B3", "E4", "FS4", "GS4",
    "B4", "E5", "FS5", "GS5", "B4", "E5", "FS5", "GS5"]
    
SongList=SongList1

# Note durations (using a standard quarter note duration of 200ms for simplicity)
NoteLengthMS = 200
NoteLengthUS = NoteLengthMS * 1000 
SongLength = len(SongList) * NoteLengthUS
#Function to play music
def PlayMusic(utimeTicksUS):
    CurSongBeat = int((utimeTicksUS % SongLength)/NoteLengthUS)
    CurNote = SongList[CurSongBeat] 
    CurFreq = MusicNoteDict[CurNote]
    #print(CurFreq)
    thumby.audio.play(CurFreq, NoteLengthMS)
    return
#####################################
########### SPRITE ARRAYS ###########
#####################################
# 5x9 for 1 frames
FreakLogo = bytearray([131,125,78,117,131,0,1,1,1,0])
# 69x36 for 1 frames
GameTitle = bytearray([255,255,255,255,255,31,207,207,159,63,127,15,199,247,247,39,15,231,231,231,7,3,51,59,249,249,29,29,189,249,123,33,9,29,253,253,253,157,157,253,249,123,3,1,29,125,249,227,231,251,61,29,0,14,224,243,247,55,55,247,239,31,255,255,255,255,255,255,255,255,255,255,255,255,252,121,3,199,224,248,62,31,7,224,224,192,1,15,127,254,240,0,0,63,127,127,3,7,15,30,60,16,0,31,63,63,49,49,63,63,62,12,0,0,0,63,63,1,0,0,60,124,112,224,255,127,120,0,248,254,255,255,255,255,255,255,255,255,255,255,255,255,255,127,56,51,23,3,128,192,192,192,192,129,1,1,192,240,48,16,0,0,0,248,28,60,240,192,0,248,60,248,240,56,60,248,0,0,0,192,254,127,15,3,0,192,240,188,134,254,0,0,0,224,192,1,3,227,7,7,15,207,207,223,191,63,127,243,225,204,30,126,198,134,12,188,248,243,7,12,249,255,63,57,112,7,223,223,211,219,192,231,231,241,249,249,243,246,240,248,248,251,248,248,251,248,240,192,223,223,216,208,208,195,249,248,248,240,247,243,248,128,191,129,227,207,191,128,152,63,111,32,48,153,207,224,15,15,15,15,12,9,3,6,3,11,9,12,14,14,14,14,15,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15])

###Xirby###
#16X16 for 1 frames
Xirbystarsmall = bytearray([255,31,231,217,190,158,166,190,166,193,251,253,253,131,127,127,255,255,142,181,187,223,223,239,223,191,191,127,15,243,251,252])
#25X30 for 1 frames
Xirbyumbrella = bytearray([255,255,255,255,255,255,255,255,255,255,143,183,59,13,5,198,226,242,122,26,130,225,241,135,31,255,255,63,223,223,223,191,223,223,223,223,191,223,223,198,128,56,253,248,249,243,243,231,243,240,255,255,4,123,255,227,191,255,227,63,191,63,127,127,159,227,252,255,255,255,255,255,255,255,255,63,63,56,59,56,57,59,59,59,56,57,57,59,56,63,63,63,63,63,63,63,63,63,63,63])
# 72x30 for 2 frames
Xirbyheadphones = bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,223,255,119,255,223,255,255,255,255,255,255,255,255,255,255,207,31,191,127,255,255,255,255,255,255,255,255,255,127,127,127,127,127,127,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,191,255,239,255,191,255,255,255,191,95,30,153,199,255,63,207,199,11,229,242,250,120,184,253,125,189,253,253,248,224,205,29,57,147,199,143,127,255,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,86,87,87,87,87,87,87,87,87,87,87,87,64,27,251,243,207,191,127,254,247,255,254,255,255,63,207,231,243,251,243,231,15,3,80,87,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,55,35,2,1,3,15,15,7,0,3,3,3,3,1,6,15,15,15,7,1,1,0,32,32,50,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,87,255,119,255,87,255,255,255,255,255,255,255,255,255,255,255,249,195,55,239,255,255,255,255,255,255,255,255,255,127,127,127,127,127,127,127,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,175,255,239,255,175,255,255,247,235,227,243,248,255,63,207,199,11,229,242,250,56,216,253,61,221,253,253,248,224,205,29,57,147,199,143,127,255,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,87,86,87,86,87,86,87,87,87,87,87,87,87,87,64,27,251,243,207,191,127,255,251,255,255,255,255,63,207,231,243,251,243,231,15,3,80,87,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,59,51,48,33,35,15,15,7,0,3,3,3,3,1,6,15,15,15,7,1,1,0,32,32,50])
Spr = thumby.Sprite(72, 30, Xirbyheadphones)

###Foreground Objects####
# 12x10 for 1 frames
starblack = bytearray([255,239,207,15,7,129,129,7,15,207,239,255,3,3,3,2,3,3,3,3,2,3,3,3])
# 12x10 for 1 frames
starstaticblit = bytearray([16,40,200,8,6,1,129,6,8,200,40,16,0,0,1,2,2,3,1,2,2,1,0,0])
# 12x10 for 1 frames
starwhite = bytearray([239,215,55,247,249,254,126,249,247,55,215,239,3,3,2,1,1,0,2,1,1,2,3,3])
# 12x10 for 1 frames
starmask = bytearray([0,16,48,240,248,126,126,248,240,48,16,0,0,0,0,1,0,0,0,0,1,0,0,0])


###Background Objects###
# 16x16 for 1 frames
enemy = bytearray([255,113,109,29,139,199,71,129,134,65,199,151,19,75,113,254,190,157,205,192,217,227,242,193,49,194,243,225,212,173,157,254])
#20x23 for 1 frames
moon= bytearray([255,63,223,239,247,251,253,253,253,254,254,62,206,246,250,253,255,255,255,255,128,127,251,255,252,247,239,247,252,255,251,224,159,127,255,255,255,255,255,255,127,126,125,123,119,111,95,95,95,63,63,63,63,63,62,93,93,91,107,119])
# 23x3 for 1 frames
hazeblit = bytearray([4,0,5,0,4,0,5,0,4,0,5,0,4,0,5,0,4,0,5,0,4,0,5])
haze = bytearray([3,7,2,7,3,7,2,7,3,7,2,7,3,7,2,7,3,7,2,7,3,7,2])
heart = bytearray([113,110,94,61,60,94,110,113])
# 72x40 for 2 frames
FinalBoss = bytearray([255,129,189,1,165,129,61,1,41,33,61,37,37,37,37,37,37,37,37,37,37,37,37,37,165,165,37,37,165,165,165,165,165,165,165,37,37,37,37,37,37,37,37,37,37,37,37,37,165,165,165,165,165,165,165,189,129,255,255,255,255,255,255,255,223,253,255,253,125,247,223,255,1,10,3,11,0,2,128,193,224,224,112,152,0,184,56,56,2,192,224,224,240,240,254,254,255,255,223,206,15,7,7,7,7,131,129,8,0,3,3,0,0,28,28,28,0,0,0,1,0,0,1,1,0,249,31,61,31,255,31,63,31,255,255,255,255,255,252,255,187,103,155,1,0,128,248,252,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,253,254,254,255,255,255,254,254,252,240,0,0,0,0,0,0,0,128,192,96,224,96,96,96,113,255,252,255,255,31,252,255,255,255,255,255,255,255,255,119,206,49,0,0,7,207,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,31,140,204,192,64,96,160,128,131,0,0,0,0,240,248,252,254,158,14,30,255,255,255,255,255,255,255,255,255,255,247,204,51,0,53,110,87,240,81,227,83,243,83,224,17,51,19,35,19,48,81,115,83,243,83,224,81,243,211,243,211,128,1,3,19,19,51,48,81,115,83,99,80,127,213,238,245,255,253,255,255,252,248,0,0,7,31,255,255,252,248,252,255,255,255,255,255,255,255,255,255,255,238,153,102,0,255,129,189,129,165,129,189,129,169,161,61,37,37,37,37,165,165,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,165,165,165,165,165,165,165,165,165,165,165,37,165,37,165,165,165,165,165,189,129,255,255,255,255,255,255,255,247,255,255,255,247,255,95,255,1,5,11,3,15,7,175,143,231,243,251,254,254,252,238,242,248,248,224,224,224,240,240,208,192,224,240,248,252,158,206,226,194,230,239,227,227,193,176,26,15,143,143,167,7,7,198,207,13,15,13,5,15,255,31,5,31,255,31,7,31,255,255,255,255,255,253,255,85,38,77,3,0,248,252,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,240,195,195,131,0,16,16,48,96,96,224,96,96,113,255,252,255,255,31,252,255,255,255,255,255,255,255,255,185,102,152,0,0,1,7,15,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,31,255,95,239,79,196,228,224,240,240,240,240,208,64,0,0,14,6,6,6,7,3,3,3,7,255,255,255,255,255,123,230,25,0,64,240,223,240,209,227,211,243,211,224,81,243,83,227,83,240,81,227,211,195,211,224,209,243,211,227,211,240,209,227,83,51,147,128,193,195,195,227,208,255,245,254,255,255,255,255,143,195,241,252,124,6,130,193,240,224,192,192,192,192,192,224,248,255,255,255,255,255,247,204,179,0])
SprBoss = thumby.Sprite(72, 40, FinalBoss)
# 72x40 for 1 frames
Finalbosshurt = bytearray([255,129,189,129,165,129,189,129,169,161,189,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,189,129,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,171,21,171,3,175,23,175,143,231,243,251,255,255,253,239,243,251,251,243,241,235,241,251,211,203,241,251,249,255,159,239,227,235,247,239,227,235,241,251,59,127,223,191,255,191,127,251,247,255,239,253,255,255,255,79,31,79,239,255,255,255,159,63,159,223,255,255,255,255,127,255,255,170,249,254,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,248,243,231,199,142,29,62,57,123,123,123,123,123,122,126,127,126,63,31,255,253,252,254,252,255,255,255,255,187,247,255,127,254,255,255,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,31,255,255,255,255,255,255,255,255,254,254,254,254,254,62,30,14,6,2,2,1,1,1,1,1,3,15,255,255,255,255,255,255,223,255,255,255,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,240,255,255,255,255,255,255,255,255,255,255,249,253,248,224,224,240,224,192,192,192,128,128,128,192,240,248,255,255,255,247,223,255,203])
#48x12
SkySets = [
    bytearray([255,127,127,127,63,191,191,223,207,239,119,247,119,247,119,247,119,247,239,239,247,247,119,247,123,251,91,251,91,187,83,243,83,179,119,247,247,143,191,191,191,191,191,191,127,127,127,255,14,13,13,13,9,11,9,11,9,11,9,7,5,3,5,7,5,3,5,7,5,3,5,7,5,3,5,7,5,3,5,7,5,3,5,7,5,11,9,11,9,11,9,11,13,13,13,14]),
    bytearray([255,255,255,255,191,31,95,95,79,239,239,247,247,251,251,251,251,251,251,251,247,247,251,251,251,253,253,253,253,253,253,249,249,249,251,251,187,231,175,239,239,175,239,95,95,191,255,255,15,15,15,15,15,15,15,15,14,14,14,14,14,14,13,13,13,13,13,13,12,13,13,12,13,13,12,13,13,12,13,13,13,12,13,13,13,14,14,14,14,14,14,15,15,15,15,15]),
    bytearray([255,255,255,255,255,255,127,127,63,191,223,223,223,239,239,239,239,239,239,223,239,239,239,247,247,247,247,231,239,239,239,239,239,159,191,191,191,191,127,127,255,255,255,255,255,255,255,255,15,15,15,15,15,14,12,13,13,13,13,13,13,11,11,11,11,11,11,11,11,11,11,11,9,11,11,10,9,10,11,9,10,13,13,13,13,13,13,13,14,15,15,15,15,15,15,15])
]


#################
# TitleScreen   #
#################
# Mimic gameboy start screen
gc.collect
move=0;
#while(titlesequence):
thumby.display.brightness(50)
thumby.display.setFPS(1)
thumby.display.fill(1)
thumby.display.update()
thumby.display.setFont("/lib/font3x5.bin", 3, 5, 0)
thumby.display.drawText("(c) '95, Xintendo", 5, 10, 0)
thumby.display.update()
thumby.display.drawText("(c) '95, Creaturesinc", 5, 16, 0)
thumby.display.update()
thumby.display.drawText("(c) '95, GAME FREAK", 5, 23, 0)
thumby.display.update()
thumby.display.fill(0)    
thumby.display.update()
thumby.display.drawFilledRectangle(15, 10, 40, 20, 1)  # (x, y, w, h, color)
#(sprite, xPosition, yPosition, width, height, key, XMirror, YMirror, bitmapRound)
thumby.display.blit(FreakLogo, 32, 10, 5, 9, 1, 0, 0)
thumby.display.drawText("GAME FREAK", 20, 21, 0)
thumby.display.setFPS(10)
thumby.display.update()
thumby.display.blit(starmask, 60, 5, 12, 10, 0, 0, 0)
thumby.display.update()
thumby.display.blit(starblack, 60, 5, 12, 10, 1, 0, 0)
thumby.display.update()
thumby.display.blit(starwhite, 50, 10, 12, 10, 1, 0, 0)
thumby.display.blit(starmask, 50, 10, 12, 10, 0, 0, 0)
thumby.display.update()
thumby.display.blit(starwhite, 40, 20, 12, 10, 1, 0, 0)
thumby.display.blit(starmask, 40, 20, 12, 10, 0, 0, 0)
thumby.display.update()
thumby.display.blit(starwhite, 30, 25, 12, 10, 1, 0, 0)
thumby.display.blit(starmask, 30, 25, 12, 10, 0, 0, 0)
thumby.display.update()
thumby.display.blit(starmask, 20, 30, 12, 10, 0, 0, 0)
thumby.display.update()
thumby.display.setFPS(5)
thumby.display.fill(0) 
thumby.display.drawFilledRectangle(15, 10, 40, 20, 1)  # (x, y, w, h, color)
#(sprite, xPosition, yPosition, width, height, key, XMirror, YMirror)
thumby.display.blit(FreakLogo, 32, 10, 5, 9, 1, 0, 0)
thumby.display.drawText("GAME FREAK", 20, 21, 0)
thumby.display.update()
thumby.display.blit(hazeblit, 20, 30, 23, 3, 0, 1, 1)
thumby.display.blit(hazeblit, 30, 30, 23, 3, 0, 1, 1)
thumby.display.update()
thumby.display.blit(hazeblit, 25, 32, 23, 3, 0, 0, 1)
thumby.display.update()
gc.collect()     
#Mimic a classic opening sequence
brightness = 1
thumby.display.setFPS(30)
thumby.display.fill(1) # fill screen with white pixels
opensequence=True
while(opensequence):
    thumby.display.brightness(brightness)
    thumby.display.update()
    brightness += 1
    if brightness >= 127:
        brightness = 1
        opensequence = False
thumby.display.update()
thumby.display.setFont("/lib/font8x8.bin", 8, 8, 0)
thumby.display.setFPS(2)
thumby.display.fill(1)
thumby.display.drawText("Xintendo", 5, 0, 0)
thumby.display.update()
thumby.display.fill(1)
thumby.display.drawText("Xintendo", 5, 10, 0)
thumby.display.update()
thumby.display.fill(1)
thumby.display.drawText("Xintendo", 5, 15, 0)
thumby.display.update()
thumby.display.fill(1)
thumby.display.drawText("Xintendo", 5, 15, 0)
thumby.display.update()
looper=True
mover=0
thumby.display.setFPS(5)
thumby.display.setFont("/lib/font3x5.bin", 3, 5, 0)

#COLLECT TRASH COMMAND USED OFTEN TO MANAGE MEMORY
gc.enable() 
gc.collect()     


#start animation loop of Xirby Dreamland Opening
while looper:
    thumby.display.fill(1)
    y_position = 200 - mover
    if y_position >= 0:
        #(sprite, xPosition, yPosition, width, height, key, XMirror, YMirror)
        thumby.display.blit(GameTitle, 2, 10-(mover*2), 69, 36, 1, 0, 0)
        thumby.display.drawText("Vol. 1.", 140-(mover*5), 10, 0)
        thumby.display.drawText("Coco Clouds", 140-(mover*5), 16, 0)
        thumby.display.blit(haze, 10+mover, y_position-140, 23, 3, 1, 0, 0)
        thumby.display.blit(haze, 40-mover, y_position-140, 23, 3, 1, 1, 0) 
        thumby.display.blit(Xirbystarsmall, 135-(mover*6), 10, 16, 16, 1, 0, 0)
        thumby.display.blit(SkySets[0], -10, y_position-120, 48, 12, 1, 0, 0)
        thumby.display.blit(SkySets[0], 40, y_position-110, 48, 12, 1, 1, 0)
        thumby.display.blit(Xirbystarsmall, (-205)+(mover*5), 10, 16, 16, 1, 1, 0)
        thumby.display.blit(SkySets[1], 5, y_position-80, 48, 12, 1, 0, 0)
        thumby.display.blit(SkySets[2], 30, y_position-70, 48, 12, 1, 1, 0) 
        thumby.display.blit(enemy, (500)-(mover*5), 10, 16, 16, 1, 0, 0)
        thumby.display.blit(Xirbyumbrella, 300-(mover*2), y_position-70, 25, 30, 1, 0, 0) 
        thumby.display.blit(starwhite, 45, y_position-40, 12, 10, 1, 0, 0) 
        thumby.display.blit(starwhite, 60, y_position-25, 12, 10, 1, 1, 0) 
        thumby.display.blit(starwhite, 2, y_position-30, 12, 10, 1, 0, 0) 
        thumby.display.drawText(" C R E D I T : ", 15,y_position-15, 0)
        thumby.display.drawText("S A R A H  B A S S", 5, y_position-5, 0)
        thumby.display.blit(heart, 60, y_position+5, 8, 7, 1, 0, 0) 
        thumby.display.blit(heart, 15, y_position+10, 8, 7, 1, 0, 0) 
        thumby.display.blit(moon, 25, y_position+5, 20, 23, 1, 1, 0) 
        thumby.display.drawText(" E N J O Y ~ ! ", 15, y_position+30, 0)
        #print('Memory Free:', "{:,}".format(gc.mem_free()), 'bytes')
        #print('Memory Allocated:', "{:,}".format(gc.mem_alloc()), 'bytes')
        #COLLECT TRASH COMMAND USED OFTEN TO MANAGE MEMORY
        gc.collect()    
        thumby.display.update()
    else:
        looper = False
        thumby.display.fill(1)
        #COLLECT TRASH COMMAND USED OFTEN TO MANAGE MEMORY
        gc.collect()     
    mover+=2
    thumby.display.update()
while (abutton == 0):
    #print('Memory Free:', "{:,}".format(gc.mem_free()), 'bytes')
    #print('Memory Allocated:', "{:,}".format(gc.mem_alloc()), 'bytes')
     #COLLECT TRASH COMMAND USED OFTEN TO MANAGE MEMORY
    gc.collect() 
    Spr.setFrame(Spr.currentFrame+1)
    thumby.display.drawSprite(Spr)
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 0)
    thumby.display.drawText("Vol 1.", 1,2, 0)
    thumby.display.drawText("CocoClouds", 1,10, 0)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 0)
    thumby.display.drawText("PRESS START", 5,32, 0)
    thumby.display.update()
    if thumby.buttonA.pressed():
        abutton=abutton+1
    thumby.display.update()
thumby.display.fill(1)

thumby.display.update()    
