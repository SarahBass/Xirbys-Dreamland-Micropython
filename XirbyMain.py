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
import utime
import machine
import animation

#Animation.py stores all the background Graphics

####GAME Maintenance ####
machine.freq(125000000)
#This line increases the performance of the microcontroller by using the ideal power consumption
gc.enable()
#Garbage Collection is essential to keep the memory used to 60,096 bytes

#Global Variables-------------------------# 
abutton = 0
GameRunning = False

#####################
#    Music          #
#####################
#Keeping the music in main helps it run more smoothly on a MicroController
#If you wanted to improve the organization but take a loss on smoothness you could call music functions from a Music.py
#I arranged the Music Notes within Human Comfort 0 to 1046
#Sounds above 2000Hz can cause hearing damage and be uncomfortable
#Be advised that although the Piezo buzzer reaches 0 - 40,000, You should probably stay within 0 - 2,000
#Xirby Song is remixed to avoid copyright, and was composed by myself using an arduino RP2040
#The C code from the arduino was then translated it to microPython

#Here are some great tools
#Use this to generate sounds and frequencies
#https://www.szynalski.com/tone-generator/
#Use this to listen and interpret sounds and frequencies
#https://theonlinemetronome.com/instrument-tuner

#My Thumby has a broken speaker, so I only tested music on emulator and arduino
#Sounds may vary on real device

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
    "AS4": 466,
    "A4": 440,
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
# Original Opening Music Designed by Myself (Just a transition to pull notes together)
"B3", "E4", "FS4", "GS4", "B3", "E4", "FS4", "GS4",
"B4", "E5", "FS5", "GS5", "B4", "E5", "FS5", "GS5",
# Original Boss Music Designed by Myself loosely based on "The Beat of the Bagpipe"
"C4", "G3", "AS3", "A3",
"G3", "C3", "C3", "G3", "G3", "G3",
"C4", "G3", "AS3", "A3",
"G3",
"C4", "G3", "AS3", "A3",
"G3", "C3", "C3", "G3", "G3", "G3",
"F3", "E3", "D3", "C3",
# Xirby Remix Main Game - Composed by taking Sheet Music notes, remixing lines, and lowering an octave
#The 0 gives it a beat stop, it sounds better at 0:40,000 or 0:4,000 - but I lowered it to under 2,000
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
#I replaced beat stops with double notes
SongList3 = [ "DS5", "D5", "C5", "Bf4", "F4", "D4", "GS4", "Bf4", "C5", "D5", "B4","B4",
"C5","C5", "G4","G4", "DS4", "D4", "C4","C4", "C4", "D4", "DS4", "C4", "Bf3", "C4", "G3","G3",
"C5", "G4", "DS4", "D4", "C4", "C4", "D4", "DS4", "F4", "D4", "Bf3", "C4", "G3", "C4",
"C5","C5", "G4","G4", "D4", "F4", "G4", "C4", "D4", "F4", "D4", "Bf3", "C4","C4",
"DS4", "DS4", "DS4", "DS4", "F4", "G4", "G4", "G4", "F4", "DS4", "D4", "D4", "D4", "D4", "DS4", "D4",
"DS4", "D4", "C4", "C4", "C4", "C4", "D4", "DS4", "DS4", "DS4", "D4", "C4", "Bf3", "Bf3", "Bf3", "Bf3", "C4", "D4",
"D5", "F5", "G5", "D5", "F5", "G5", "D5", "F5", "D5", "F5", "G5", "C6", "B5", "B5"]
#Game Start Music
#This has a nice feel with the background and gives some music break from main theme
SongList4 =[
"C5", "G4", "AS4", "A4",
"G4", "C4", "C4", "G4", "G4", "G4",
"C5", "G4", "AS4", "A4",
"G4",
"C5", "G4", "AS4", "A4",
"G4", "C4", "C4", "G4", "G4", "G4",
"F4", "E4", "D4", "C4",
"C4", "D5", "D5", "D5", "D5", "D5",
"D5", "D5", "D5", "C5", "E5",
"C5", "C5", "E5", "E5", "C5",
"F5", "D5", "D5", "E5",
"C5", "D5", "E5", "D5", "C5"]
#Continue Screen 
SongList5=["B3", "E4", "FS4", "GS4", "B3", "E4", "FS4", "GS4",
"B4", "E5", "FS5", "GS5", "B4", "E5", "FS5", "GS5"]

# Note durations (using a standard quarter note duration of 200ms for simplicity)
def PlayMusic(utimeTicksUS, SongList):
    NoteLengthMS = 200
    NoteLengthUS = NoteLengthMS * 1000 
    SongLength = len(SongList) * NoteLengthUS
    CurSongBeat = int((utimeTicksUS % SongLength)/NoteLengthUS)
    CurNote = SongList[CurSongBeat] 
    CurFreq = MusicNoteDict[CurNote]
    #print(CurFreq)
    thumby.audio.play(CurFreq, NoteLengthMS)
    return

BGMOffset = utime.ticks_us()

# Initialize animation parameters
mover = 0
looper = True
    
#####################################################
########### ENEMY and XIRBY #########################
#####################################################

####LOCAL GRAPHICS#######

#Average Xirby or Enemy is 16 x 16
#width=16
#height=16
#xPosition = int((thumby.display.width/2) - (width/2))
#yPosition = int((thumby.display.height/2) - (height/2))

# 16 x 16 for 1 frame
#Used as the Main Character Graphics
#The mask is a white outline behind the transparent outline character to give it a foreground look
Xirbystarsmall = bytearray([255,31,231,217,190,158,166,190,166,193,251,253,253,131,127,127,255,255,142,181,187,223,223,239,223,191,191,127,15,243,251,252])
Xirbymask = bytearray([0,0,224,248,254,254,254,254,254,248,248,252,252,128,0,0,0,0,0,49,59,31,31,15,31,63,63,127,15,3,3,0])

#Used as an enemy - This enemy is mostly black on a white background, so I don't need to load a mask
enemySprite = bytearray([255,113,109,29,139,199,71,129,134,65,199,151,19,75,113,254,190,157,205,192,217,227,242,193,49,194,243,225,212,173,157,254])
#This Sprite is used as a Health Meter
# 8 x 7 for 1 frame
heart = bytearray([113,110,94,61,60,94,110,113])

class Enemy:
    def __init__(self, x, y, width=16, height=16):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self):
        self.x -= 1
        if self.x < -self.width:
            self.x = 72

    def check_collision(self, xirby):
        return (
            self.x < xirby.x + xirby.width and
            self.x + self.width > xirby.x and
            self.y < xirby.y + xirby.height and
            self.y + self.height > xirby.y
        )

    def dodge(self):
        self.y -= 20
        if self.y < 0:
            self.y = 0

class Xirby:
    def __init__(self, width=16, height=16):
        self.width = width
        self.height = height
        self.x = int((thumby.display.width / 2) - (width / 2))
        self.y = int((thumby.display.height / 2) - (height / 2))
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage

xirby = Xirby()
enemies = [Enemy(72, y) for y in range(0, thumby.display.height, 20)]  # Adjust as needed for enemy spacing

#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
#                        OPENING SEQUENCE                         # 
#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=


#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
#                        START OF GAME                           # 
#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
