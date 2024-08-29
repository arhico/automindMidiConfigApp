from random import random

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

guiBricksNames = ["guiBrick", "guiBrickList", "guiBrickInfo", "guiBrickListInteractive", "guiBrickDropListInteractive"]

NOTIF_TITLE = "automind"

def infoPrint(notificatord, inputData):
    # global globalNotification
    print(inputData)
    notificatord = inputData

import pygame
import pygame.freetype    
pygame.init()
icon = pygame.image.load('./assets/automindMidiIcon.png')
pygame.display.set_icon(icon)
pygame.font.init()
TEXT_BRIGHTNESS = 0.95
TEXT_ALPHA = 0.8
TEXT_SIZE = int(12)
# TEXT_FAMILY = 'Consolas'
TEXT_FAMILY = './assets/JupiteroidLight.ttf'

# TEXT_FAMILY = 'Courier New'
# TEXT_FAMILY = 'Fixed Sys'
# TEXT_FAMILY = 'Mono'
pygame.display.set_caption("AUTOMIND MIDI CONFIGURATOR")
globalFont = pygame.freetype.Font(TEXT_FAMILY, TEXT_SIZE, resolution=96)
clock = pygame.time.Clock()

# globalFont.render_to()

BG_COLOR = (5,10,8)

SCREEN_W = 550
SCREEN_H = 580
globalText = ["oh, hi mark"]

PIXELS_PER_SYMBOL = TEXT_SIZE/12 * 100/12

RENDER_GRID = False
RENDER_FREE_CELLS = False
RENDER_FREE_CELLS_PIXELS_AT_CENTER = True
GRID_COLOR = (150,150,150,30)
GRID_SIZE_PX_X = 21
GRID_SIZE_PX_Y = GRID_SIZE_PX_X
# GRID_STEP_PX_Y = 50
GRID_CELL_BORDER_PX = (2,2)
# GRID_CELL_BORDER_PX = (0,0)

DEFAULT_RANGE_BOUNDS = (0,100)

DEFAULT_HOVER_COLOR_MULTS = (0.5, 1.4, 1.7)
DEFAULT_ACTIVE_COLOR_MULTS = (-1, -1, -1)

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
DEFAULT_SENSOR_COLOR = (60,90,180)
DEFAULT_SENSOR_HOVER_COLOR = colorMult(DEFAULT_SENSOR_COLOR, DEFAULT_HOVER_COLOR_MULTS)
DEFAULT_SENSOR_ACTIVE_COLOR = (DEFAULT_SENSOR_HOVER_COLOR)
DEFAULT_SENSOR_INACTIVE_COLOR = (100,100,100)
# DEFAULT_SENSORS_COLORS = (DEFAULT_SENSOR_COLOR, DEFAULT_SENSOR_HOVER_COLOR, DEFAULT_SENSOR_ACTIVE_COLOR)
DEFAULT_COLORS = [DEFAULT_SENSOR_COLOR, DEFAULT_SENSOR_ACTIVE_COLOR, DEFAULT_SENSOR_INACTIVE_COLOR]
DEFAULT_LED_COLORS = [(0,30,30),(0,255,0)]
DEFAULT_LED_SIZE_PX = (20,5)
LED_TIMEOUT_FRAMES = 6

# DEFAULT_SENSOR_INITIAL_DENSITY = 0.3

STATUS_BOX_GRID_MAPPING = (1,1)

MINIMUM_GRIDBOX = (1,1)
SENSOR_GRID_MAPPING = (8,3)
SENSOR_GRIDBOX = (3,3)
DEFAULT_STATUS_BOX_GRID_H = 4

# DEFAULT_TEXT_COLOR = (colorMult(DEFAULT_FADER_BODY_COLOR,DEFAULT_HOVER_COLOR_MULTS))

FRAMERATE = 40

SENSORSAPPING = [
  [0, 3, 6, 9, 12, 15, 18, 21],
  [1, 4, 7, 10, 13, 16, 19, 22],
  [2, 5, 8, 11, 14, 17, 20, 23],
]

privateAutomindTouchSensorCounter = 0
privateFadersCounter = 0

