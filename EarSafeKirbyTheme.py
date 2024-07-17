MusicNoteDict = {
    0: 2093,
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


SongList = [
    # Opening Music
    "B3", "E4", "FS4", "GS4", "B3", "E4", "FS4", "GS4",
    "B4", "E5", "FS5", "GS5", "B4", "E5", "FS5", "GS5",
    # Boss Music
    "C4", "G3", "AS3", "A3",
    "G3", "C3", "C3", "G3", "G3", "G3",
    "C4", "G3", "AS3", "A3",
    "G3",
    "C4", "G3", "AS3", "A3",
    "G3", "C3", "C3", "G3", "G3", "G3",
    "F3", "E3", "D3", "C3",
    # Xirby Remix Main Game
    "DS5", "D5", "C5", "Bf4", "F4", "D4", "GS4", "Bf4", "C5", "D5", "B4", 0,
    "C5", 0, "G4", 0, "DS4", "D4", "C4", 0, "C4", "D4", "DS4", "C4", "Bf3", "C4", "G3", 0,
    "C5", 0, "G4", 0, "DS4", "D4", "C4", "C4", "D4", "DS4", "F4", "D4", "Bf3", "C4", "G3", "C4", 0,
    "C5", 0, "G4", 0, "D4", "F4", "G4", "C4", "D4", "F4", "D4", "Bf3", "C4", 0,
    # Xirby Remix Part 2
    "DS4", "DS4", "DS4", "DS4", "F4", "G4", "G4", "G4", "F4", "DS4", "D4", "D4", "D4", "D4", "DS4", "D4",
    "DS4", "D4", "C4", "C4", "C4", "C4", "D4", "DS4", "DS4", "DS4", "D4", "C4", "Bf3", "Bf3", "Bf3", "Bf3", "C4", "D4",
    "D5", "F5", "G5", "D5", "F5", "G5", "D5", "F5", "D5", "F5", "G5", "C6", "B5", 0
]
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
