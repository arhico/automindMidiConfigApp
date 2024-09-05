import random
import time, json, math
import pygame

textFont = 0
timeRunning = 0
START_TIME = time.time()
guiBricksNames = ["guiBrick", "guiBrickList", "guiBrickInfo", "guiBrickListInteractive", "guiBrickDropListInteractive"]

class lowpassAssymetrical(object):
    def __init__(self) -> None:
        self.filteredValue = [0.0,0.0,0.0]     
    def update(self, inValue, coeffitient = 0.999):
        distance = [1,1,1]
        modCoeffitient = coeffitient
        for value in range(inValue.__len__()):
            try:
                distance[value] = inValue[value] / self.filteredValue[value]
            except:
                try:
                    distance[value] = self.filteredValue[value]/inValue[value]
                except:
                    pass
                pass
            # how far we are from target value
            distance[value] = 1 - distance[value]
            if distance[value] < 0:
                distance[value] = 0
            modCoeffitient += distance[value]/2.2
            if modCoeffitient > 0.997:
                modCoeffitient = 0.997
            self.filteredValue[value] = modCoeffitient * self.filteredValue[value] + (1-modCoeffitient) * inValue[value]
        return self.filteredValue

@staticmethod
def saveConfig(file, config = None):
    global timeRunning, textFont
    if config is None:
        config = {"timeRunning":timeRunning, "textFont":textFont}
    with open(file, 'w') as f:
        json.dump(config, f)
    print(f"Saved config: {config}")   
@staticmethod
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
@staticmethod
def infoPrint(notificatord, inputData):
    # global globalNotification
    print(inputData)
    notificatord = inputData
@staticmethod
def globalFontUpdate(fontFile, size, fontResolution=None):
    return pygame.freetype.Font(fontFile, size)
@staticmethod
def colorRandom(alpha = None):
    if alpha is None:
        return (int(255*random()),int(255*random()),int(255*random()))
    else:
        return (int(255*random()),int(255*random()),int(255*random()),int(alpha))
@staticmethod
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
@staticmethod
def colorInvert(color):
    return colorMult(color, (-1,-1,-1))
