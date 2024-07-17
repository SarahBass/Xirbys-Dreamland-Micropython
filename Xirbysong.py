MusicNoteDict = {
    0: 40000,
    "C5": 523,
    "G4": 392,
    "AS4": 466,
    "A4": 440,
    "C4": 261,
    "F4": 349,
    "E4": 330,
    "D4": 294,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "CS5": 554,
    "FS5": 740,
    "GS5": 831,
    "An5": 880,
    "C6": 1046,
    "CS6": 1109,
    "FS6": 1480,
    "An6": 1760,
    "B4": 494,
    "GS6": 1661,
    "B5": 988,
    "E6": 1318,
    "F6": 1396,
    "G5": 784,
    "DS5": 622,
    "Bf4": 466,
    "G4": 392,
    "DS6": 1245,
    "D6": 1175,
    "Bf5": 932,
    "GS5": 831,
    "B5": 988,
    "G6" : 1567,
    "C7" : 2093,
     "B6" : 1975.53
}

SongList = [
    #Opening Music
"B4", "E5", "FS5", "GS5", "B4", "E5", "FS5", "GS5",
"B5", "E6", "FS6", "GS6", "B5", "E6", "FS6", "GS6",
    # Boss Music
"C5", "G4", "AS4", "A4",
"G4", "C4", "C4", "G4", "G4", "G4",
"C5", "G4", "AS4", "A4",
"G4",
"C5", "G4", "AS4", "A4",
"G4", "C4", "C4", "G4", "G4", "G4",
"F4", "E4", "D4", "C4",
    #Xirby Remix Main Game
"DS6", "D6", "C6", "Bf5", "F5", "D5", "GS5", "Bf5", "C6", "D6", "B5", 0,
"C6", 0, "G5", 0, "DS5", "D5", "C5", 0, "C5", "D5", "DS5", "C5", "Bf4", "C5", "G4", 0,
"C6", 0, "G5", 0, "DS5", "D5", "C5", "C5", "D5", "DS5", "F5", "D5", "Bf4", "C5", "G4", "C5", 0,
"C6", 0, "G5", 0, "D5", "F5", "G5", "C5", "D5", "F5", "D5", "Bf4", "C5", 0,
#Xirby Remix Part 2 
"DS5", "DS5", "DS5", "DS5", "F5", "G5", "G5", "G5", "F5", "DS5", "D5", "D5", "D5", "D5", "DS5", "D5",
"DS5", "D5", "C5", "C5", "C5", "C5", "D5", "DS5", "DS5", "DS5", "D5", "C5", "Bf4", "Bf4", "Bf4", "Bf4", "C5", "D5",
"D6", "F6", "G6", "D6", "F6", "G6", "D6", "F6", "D6", "F6", "G6", "C7", "B6", 0]
# Note durations (using a standard quarter note duration of 200ms for simplicity)
NoteLengthMS = 200

NoteLengthUS = NoteLengthMS * 1000 
SongLength = len(SongList) * NoteLengthUS

def PlayMusic(utimeTicksUS):
    CurSongBeat = int((utimeTicksUS % SongLength)/NoteLengthUS)
    CurNote = SongList[CurSongBeat] 
    CurFreq = MusicNoteDict[CurNote]
    #print(CurFreq)
    thumby.audio.play(CurFreq, NoteLengthMS)
    return

BGMOffset = utime.ticks_us()
while GameRunning:
    t0 = utime.ticks_us() # Check the time
    
    #MusicStuff
    PlayMusic(t0 - BGMOffset)
