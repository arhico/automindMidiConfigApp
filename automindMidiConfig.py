from random import random
import os
import json
from os import walk
import pygame
import pygame.freetype 
import time
textFont = 0
timeRunning = 0
START_TIME = time.time()

def saveConfig(file, config = None):
    global timeRunning, textFont
    if config is None:
        config = {"timeRunning":timeRunning, "textFont":textFont}
    with open(file, 'w') as f:
        json.dump(config, f)
    print(f"Saved config: {config}")
    
def configLoad(file):
    global START_TIME, timeRunning, textFont
    try:
        with open(file, 'r') as f:
            config = json.load(f)
            # textFont = int(config["textFont"])
            prop = "timeRunning"
            try:
                START_TIME -= int(config[prop])/1000
            except:
                print(f"Failed to find property {prop} in {file}")
            print(f"Loaded config: {config}")
    except:
        print("No config file found. Creating one")
        saveConfig(file, {"textFont":textFont})

    
def colorRandom(alpha = None):
    if alpha is None:
        return (int(255*random()),int(255*random()),int(255*random()))
    else:
        return (int(255*random()),int(255*random()),int(255*random()),int(alpha))

def colorMult(color, mult = None):
    if mult is None:
        return color
    retVal = [int(color[0]*mult[0]),int(color[1]*mult[1]),int(color[2]*mult[2])]
    for idx in range(retVal.__len__()):
        if retVal[idx]<0:
            retVal[idx] = abs(retVal[idx])
            if retVal[idx] > 255:
                retVal[idx] = 255
            retVal[idx] = 255 - retVal[idx]
        else:
            if retVal[idx] > 255:
                retVal[idx] = 255
    return tuple(retVal)

def colorInvert(color):
    return colorMult(color, (-1,-1,-1))

guiBricksNames = ["guiBrick", "guiBrickList", "guiBrickInfo", "guiBrickListInteractive", "guiBrickDropListInteractive", "guiBrickDropListInteractiveScrollable"]

NOTIF_TITLE = "automind"

def infoPrint(notificatord, inputData):
    # global globalNotification
    print(inputData)
    notificatord = inputData
   
pygame.init()
ASSETS_PATH = './assets/'
FONTS_PATH = ASSETS_PATH + 'fonts/'
icon = pygame.image.load(f'{ASSETS_PATH}automindMidiIcon.png')
CONFIG_FILE_NAME = "automindAppConfig.json"
pygame.display.set_icon(icon)
pygame.font.init()
TEXT_BRIGHTNESS = 0.95
TEXT_ALPHA = 0.8
DEFAULT_TEXT_SIZE = int(18)

configLoad(CONFIG_FILE_NAME)

# print(filenames)

TEXT_FAMILY = f'{FONTS_PATH}bedstead-condensed.otf'

pygame.display.set_caption("Automind MIDI Configurator")

def globalFontUpdate(fontFile, fontResolution=None):
    return pygame.freetype.Font(fontFile, size=DEFAULT_TEXT_SIZE)

# filenames = next(walk(FONTS_PATH), (None, None, []))[2]  # [] if no file

globalFont = globalFontUpdate(TEXT_FAMILY)

clock = pygame.time.Clock()

BG_COLOR = (20,15,10)

SCREEN_W = 550
SCREEN_H = 580
globalText = ["oh, hi mark"]

PIXELS_PER_SYMBOL = DEFAULT_TEXT_SIZE/12 * 80/12

RENDER_GRID = False
RENDER_FREE_CELLS = False
RENDER_FREE_CELLS_PIXELS_AT_CENTER = True
GRID_COLOR = (150,150,150,30)
GRID_SIZE_PX_X = 22
GRID_SIZE_PX_Y = GRID_SIZE_PX_X
# GRID_STEP_PX_Y = 50
GRID_CELL_BORDER_PX = (2,2)
# GRID_CELL_BORDER_PX = (0,0)
BRICKS_OUTLINE_RADIUS_PX = 3

BRICKS_OUTLINE_WIDTH_PX = 3

DEFAULT_RANGE_BOUNDS = (0,100)

HOVER_COLOR_MULTS = (1.5, 1.5, 1.4)
ACTIVE_COLOR_MULTS = (-1, -1, -1)

LP_SLOW_COEF = 0.95
LP_FAST_COEF = 0.6

FADERS_GRID_MAPPING = (16,1)
FADER_GRIDBOX = (1,5)
# DEFAULT_FADER_HANDLE_HEIGHT = 2
# DEFAULT_FADER_BODY_COLOR = (100,100,200)
# DEFAULT_FADER_HANDLE_COLOR = (200,200,200)
# DEFAULT_FADER_TICKS_COLOR = (20,20,20)
# DEFAULT_FADER_COLORS = (DEFAULT_FADER_BODY_COLOR, DEFAULT_FADER_HANDLE_COLOR, DEFAULT_FADER_TICKS_COLOR)

# SENSORS_GRID_MAPPING = (8,3)
# SENSOR_GRID_BOX = (3,3)
# SENSOR_GRID_BOX_OFFSET = (5,5)
SENSOR_COLOR = (20,60,150)
SENSOR_HOVER_COLOR = colorMult(SENSOR_COLOR, HOVER_COLOR_MULTS)
SENSOR_ACTIVE_COLOR = (SENSOR_HOVER_COLOR)
SENSOR_INACTIVE_COLOR = (70,70,60)
# DEFAULT_SENSORS_COLORS = (DEFAULT_SENSOR_COLOR, DEFAULT_SENSOR_HOVER_COLOR, DEFAULT_SENSOR_ACTIVE_COLOR)
DEFAULT_COLORS = [SENSOR_COLOR, SENSOR_ACTIVE_COLOR, SENSOR_INACTIVE_COLOR]
LED_COLORS = [(20,20,25),(255,140,80)]
LED_SIZE_PX = (GRID_SIZE_PX_X, BRICKS_OUTLINE_WIDTH_PX)
LED_TIMEOUT_FRAMES = 4

# DEFAULT_SENSOR_INITIAL_DENSITY = 0.3

STATUS_BOX_GRID_MAPPING = (1,1)

MINIMUM_GRIDBOX = (1,1)
SENSOR_GRID_MAPPING = (8,3)
SENSOR_GRIDBOX = (3,3)
DEFAULT_STATUS_BOX_GRID_H = 4

# DEFAULT_TEXT_COLOR = (colorMult(DEFAULT_FADER_BODY_COLOR,DEFAULT_HOVER_COLOR_MULTS))

FRAMERATE = 60

SENSORSAPPING = [
  [0, 3, 6, 9, 12, 15, 18, 21],
  [1, 4, 7, 10, 13, 16, 19, 22],
  [2, 5, 8, 11, 14, 17, 20, 23],
]

privateAutomindTouchSensorCounter = 0
privateFadersCounter = 0

