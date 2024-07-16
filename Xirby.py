############################################################################
#                      __  ___      _           
#                      \ \/ (_)_ __| |__  _   _ 
#                       \  /| | '__| '_ \| | | |
#                       /  \| | |  | |_) | |_| |
#                      /_/\_\_|_|  |_.__/ \__, |
#                                         |___/ 
#
#              / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ 
#             ( C | o | c | o ) ( C | l | o | u | d | s )
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
gamespeed = 125000000
##############################################

machine.freq(gamespeed) #Game Speed
