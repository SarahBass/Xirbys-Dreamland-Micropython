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
import math
import machine
import random
import time
import utime

gc.enable() #Garbage Collection

from framebuf import FrameBuffer, MONO_VLSB #

#Global Variables-------------------------# 
XVel = 0.06
YVel = 0
YPos = 0
Gravity = 0.15
MaxFPS = 60
Points = 0
GameRunning = True
EnemyPos = random.randint(72, 300)
CloudPos = random.randint(60, 200)
CoinPos = random.randint(60, 200)
JumpSoundTimer = 0
GameSpeed = 125000000

#Maintenance-------------------------# 

machine.freq(GameSpeed) #Game Speed

#COLLECT TRASH COMMAND USED OFTEN TO MANAGE MEMORY
gc.enable() 
gc.collect()     
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())    

########### SPRITE ARRAYS ###########

# 69x36 for 1 frames
GameTitle = bytearray([255,255,255,255,255,31,207,207,159,63,127,15,199,247,247,39,15,231,231,231,7,3,51,59,249,249,29,29,189,249,123,33,9,29,253,253,253,157,157,253,249,123,3,1,29,125,249,227,231,251,61,29,0,14,224,243,247,55,55,247,239,31,255,255,255,255,255,255,255,255,255,255,255,255,252,121,3,199,224,248,62,31,7,224,224,192,1,15,127,254,240,0,0,63,127,127,3,7,15,30,60,16,0,31,63,63,49,49,63,63,62,12,0,0,0,63,63,1,0,0,60,124,112,224,255,127,120,0,248,254,255,255,255,255,255,255,255,255,255,255,255,255,255,127,56,51,23,3,128,192,192,192,192,129,1,1,192,240,48,16,0,0,0,248,28,60,240,192,0,248,60,248,240,56,60,248,0,0,0,192,254,127,15,3,0,192,240,188,134,254,0,0,0,224,192,1,3,227,7,7,15,207,207,223,191,63,127,243,225,204,30,126,198,134,12,188,248,243,7,12,249,255,63,57,112,7,223,223,211,219,192,231,231,241,249,249,243,246,240,248,248,251,248,248,251,248,240,192,223,223,216,208,208,195,249,248,248,240,247,243,248,128,191,129,227,207,191,128,152,63,111,32,48,153,207,224,15,15,15,15,12,9,3,6,3,11,9,12,14,14,14,14,15,14,14,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15])
# 17x18 for 2 frames
XirbyJumpsBlit = bytearray([62,227,1,1,7,2,3,1,1,225,1,2,227,1,225,190,0,0,1,6,120,136,228,228,200,112,64,64,194,224,176,200,111,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,192,112,24,8,12,4,4,4,4,8,24,48,192,0,0,0,7,24,224,32,144,144,32,192,3,8,8,131,192,35,190,224,0,0,0,1,2,3,3,3,1,1,1,3,3,2,3,1,0])
# 14x14 for 2 frames
XirbyRunsBlit = bytearray([0,240,136,4,2,1,129,1,1,98,4,56,192,0,7,9,19,19,14,10,11,8,24,44,37,38,27,0,224,16,8,4,2,1,1,1,113,3,114,12,240,128,0,1,2,14,21,41,40,40,24,41,24,4,2,1])
# 48x12 for 1 frames for 3 cloud types
Skysets = [bytearray([255,127,127,127,63,191,191,223,207,239,119,247,119,247,119,247,119,247,239,239,247,247,119,247,123,251,91,251,91,187,83,243,83,179,119,247,247,143,191,191,191,191,191,191,127,127,127,255,14,13,13,13,9,11,9,11,9,11,9,7,5,3,5,7,5,3,5,7,5,3,5,7,5,3,5,7,5,3,5,7,5,3,5,7,5,11,9,11,9,11,9,11,13,13,13,14]),
          [bytearray([255,255,255,255,191,31,95,95,79,239,239,247,247,251,251,251,251,251,251,251,247,247,251,251,251,253,253,253,253,253,253,249,249,249,251,251,187,231,175,239,239,175,239,95,95,191,255,255,15,15,15,15,15,15,15,15,14,14,14,14,14,14,13,13,13,13,13,13,12,13,13,12,13,13,12,13,13,12,13,13,13,12,13,13,13,14,14,14,14,14,14,15,15,15,15,15]),
          [bytearray([255,255,255,255,255,255,127,127,63,191,223,223,223,239,239,239,239,239,239,223,239,239,239,247,247,247,247,231,239,239,239,239,239,159,191,191,191,191,127,127,255,255,255,255,255,255,255,255,15,15,15,15,15,14,12,13,13,13,13,13,13,11,11,11,11,11,11,11,11,11,11,11,9,11,11,10,9,10,11,9,10,13,13,13,13,13,13,13,14,15,15,15,15,15,15,15])]
CloudSpr = SkySets[0]
# 12x10 for 1 frames
starstaticblit = bytearray([16,40,200,8,6,1,129,6,8,200,40,16,0,0,1,2,2,3,1,2,2,1,0,0])
# 11x13 for 4 frames
starblit = bytearray([64,0,64,0,64,245,64,0,64,0,64,0,0,0,0,0,21,0,0,0,0,0,0,0,64,0,64,244,64,0,64,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,64,240,64,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# 23x3 for 1 frames
hazeblit = bytearray([4,0,5,0,4,0,5,0,4,0,5,0,4,0,5,0,4,0,5,0,4,0,5])
# 5x5 for 3 frames
sparkleblit = bytearray([0,10,0,10,0,4,10,17,10,4,21,0,17,0,21])
# 6x6 for 2 frames
squareblit = bytearray([63,33,33,33,33,63,63,63,51,51,63,63])
# 8x7 for 1 frames
heartstaticblit = bytearray([14,17,33,66,67,33,17,14])
# 5x12 for 1 frames
musicnotestaticblit = bytearray([0,3,30,100,136,4,10,14,6,3])
# 30x29 for 2 frames
Xirbyheadphones = bytearray([255,231,15,223,191,255,255,255,255,255,255,127,127,127,63,191,191,191,191,191,63,127,255,255,255,255,255,255,255,255,223,175,143,204,227,255,31,231,227,133,242,249,253,60,220,254,62,222,254,254,252,240,230,142,156,201,227,199,63,255,171,171,171,171,171,171,160,13,253,249,231,223,191,127,251,255,255,255,255,31,231,243,249,253,249,243,7,1,40,43,31,31,31,31,31,27,17,1,0,1,7,7,3,0,1,1,1,1,0,3,7,7,7,3,0,0,0,16,16,25,255,252,225,155,119,255,255,255,255,255,255,127,127,127,63,191,191,191,191,191,63,127,255,255,255,255,255,255,255,255,251,245,241,249,252,255,31,231,227,133,242,249,253,156,236,254,158,238,254,254,252,240,230,142,156,201,227,199,63,255,171,171,171,171,171,171,160,13,253,249,231,223,191,127,253,255,255,255,255,31,231,243,249,253,249,243,7,1,40,43,31,31,31,31,31,29,25,24,16,17,7,7,3,0,1,1,1,1,0,3,7,7,7,3,0,0,0,16,16,25])
# 72x40 for 2 frames
FinalBoss = bytearray([255,129,189,1,165,129,61,1,41,33,61,37,37,37,37,37,37,37,37,37,37,37,37,37,165,165,37,37,165,165,165,165,165,165,165,37,37,37,37,37,37,37,37,37,37,37,37,37,165,165,165,165,165,165,165,189,129,255,255,255,255,255,255,255,223,253,255,253,125,247,223,255,1,10,3,11,0,2,128,193,224,224,112,152,0,184,56,56,2,192,224,224,240,240,254,254,255,255,223,206,15,7,7,7,7,131,129,8,0,3,3,0,0,28,28,28,0,0,0,1,0,0,1,1,0,249,31,61,31,255,31,63,31,255,255,255,255,255,252,255,187,103,155,1,0,128,248,252,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,253,254,254,255,255,255,254,254,252,240,0,0,0,0,0,0,0,128,192,96,224,96,96,96,113,255,252,255,255,31,252,255,255,255,255,255,255,255,255,119,206,49,0,0,7,207,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,31,140,204,192,64,96,160,128,131,0,0,0,0,240,248,252,254,158,14,30,255,255,255,255,255,255,255,255,255,255,247,204,51,0,53,110,87,240,81,227,83,243,83,224,17,51,19,35,19,48,81,115,83,243,83,224,81,243,211,243,211,128,1,3,19,19,51,48,81,115,83,99,80,127,213,238,245,255,253,255,255,252,248,0,0,7,31,255,255,252,248,252,255,255,255,255,255,255,255,255,255,255,238,153,102,0,255,129,189,129,165,129,189,129,169,161,61,37,37,37,37,165,165,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,165,165,165,165,165,165,165,165,165,165,165,37,165,37,165,165,165,165,165,189,129,255,255,255,255,255,255,255,247,255,255,255,247,255,95,255,1,5,11,3,15,7,175,143,231,243,251,254,254,252,238,242,248,248,224,224,224,240,240,208,192,224,240,248,252,158,206,226,194,230,239,227,227,193,176,26,15,143,143,167,7,7,198,207,13,15,13,5,15,255,31,5,31,255,31,7,31,255,255,255,255,255,253,255,85,38,77,3,0,248,252,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,240,195,195,131,0,16,16,48,96,96,224,96,96,113,255,252,255,255,31,252,255,255,255,255,255,255,255,255,185,102,152,0,0,1,7,15,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,31,255,95,239,79,196,228,224,240,240,240,240,208,64,0,0,14,6,6,6,7,3,3,3,7,255,255,255,255,255,123,230,25,0,64,240,223,240,209,227,211,243,211,224,81,243,83,227,83,240,81,227,211,195,211,224,209,243,211,227,211,240,209,227,83,51,147,128,193,195,195,227,208,255,245,254,255,255,255,255,143,195,241,252,124,6,130,193,240,224,192,192,192,192,192,224,248,255,255,255,255,255,247,204,179,0])
# 72x40 for 1 frames
Finalbosshurt = bytearray([255,129,189,129,165,129,189,129,169,161,189,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,189,129,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,171,21,171,3,175,23,175,143,231,243,251,255,255,253,239,243,251,251,243,241,235,241,251,211,203,241,251,249,255,159,239,227,235,247,239,227,235,241,251,59,127,223,191,255,191,127,251,247,255,239,253,255,255,255,79,31,79,239,255,255,255,159,63,159,223,255,255,255,255,127,255,255,170,249,254,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,248,243,231,199,142,29,62,57,123,123,123,123,123,122,126,127,126,63,31,255,253,252,254,252,255,255,255,255,187,247,255,127,254,255,255,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,223,31,223,223,223,223,31,255,255,255,255,255,255,255,255,254,254,254,254,254,62,30,14,6,2,2,1,1,1,1,1,3,15,255,255,255,255,255,255,223,255,255,255,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,243,240,241,243,243,243,240,255,255,255,255,255,255,255,255,255,255,249,253,248,224,224,240,224,192,192,192,128,128,128,192,240,248,255,255,255,247,223,255,203])
