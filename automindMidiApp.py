import time
import os

from automindMidiConfig import *
import automindMidiVisualizer
from automindMidiVisualizer import gridObjectCreate, rootObjectsContainerClass

import pygame
import mido
import mido.backends.rtmidi
import threading

grids = automindMidiVisualizer.gridClass()

def sysexRead():
    while 1:
        time.sleep(1)
        pass

sysexThread = threading.Thread(target=sysexRead)
sysexThread.start()

screenFlags = pygame.SRCALPHA

screen = pygame.display.set_mode(grids.quantizedScreensize, flags=screenFlags, depth=32)
grids.setPygameSurface(screen)

globalMidiPorts = {}

findPportsSamplesCount = 0
MIDI_MONITOR_TITLE = "midi monitor"
MIDI_DEVICES_LIST_TITLE = "midi devices"
def findPorts(decimateFreq = None):
    global globalMidiPorts,findPportsSamplesCount,timeRunning
    if not decimateFreq is None:
        findPportsSamplesCount+=1
        if findPportsSamplesCount % decimateFreq:
            return
        else:
            findPportsSamplesCount = 0
    temp = mido.get_input_names()
    globalMidiPorts[MIDI_DEVICES_LIST_TITLE] = temp
    # print(f'{str(globalMidiPorts)}')
    findPportsSamplesCount+=1
    return globalMidiPorts

globalMidiMonitor = {}
globalMidiMonitor = {MIDI_MONITOR_TITLE:[textFont]}
globalNotification = {NOTIF_TITLE:[]}

rootObject = []

TITLE_OBJ_IDX = gridObjectCreate("guiBrickInfo", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],3))

# SENSORS_IDX = gridObjectCreate("guiBrickInteractive", rootObject, screen, grids, gridBx=SENSOR_GRIDBOX, gridMapping=SENSOR_GRID_MAPPING)
# gridObjectCreate("guiBrick",rootObject,screen,grids,(grids.gridDimensions[1] - 2))
# TEST = gridObjectCreate("guiBrickListInteractive", rootObject, screen, grids, gridBx=(grids.gridDimensions[0]/2,4))
# rootObject[TEST].text = 42
# MIDI_DEVICES_LIST_OBJ_IDX = gridObjectCreate("guiBrickDropListInteractive", rootObject, screen, grids, gridBx=(grids.gridDimensions[0],2))
MIDI_DEVICES_LIST_OBJ_IDX = gridObjectCreate("guiBrickListInteractive", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],6))
# _ = gridObjectCreate("guiBrickList", rootObject, screen, globalNotification, grids, gridBx=(3,6))

MIDI_MONITOR_LIST_OBJ_IDX = gridObjectCreate("guiBrickList", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],int(6)))
DBG_OBJ_IDX = gridObjectCreate("guiBrickInfo", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],int(6)))

# NOTIFICATIONS_OBJ_IDX = gridObjectCreate("guiBrickList", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],int(3)))

rootObjectContainer = rootObjectsContainerClass(screen, clock, objects=[[grids],rootObject])

def monitorThread():
    global globalMidiMonitor
    prevInterfaceSelection = ""
    while 1:
        try:
            currentSelection = rootObject[MIDI_DEVICES_LIST_OBJ_IDX].selected[0]
        except:
            currentSelection = 0
        if currentSelection is None:
            currentSelection = 0
        # print(currentSelection)
        if currentSelection != prevInterfaceSelection:
            # rootObject[MIDI_DEVICES_LIST_OBJ_IDX].changed = True 
            
            # if not prevInterfaceSelection is None:
            try:
                inport.close()
                time.sleep(1)
            except:
                pass
            prevInterfaceSelection = currentSelection
            if not currentSelection == 0:
                # time.sleep(1)
                inport = mido.open_input(globalMidiPorts[MIDI_DEVICES_LIST_TITLE][rootObject[MIDI_DEVICES_LIST_OBJ_IDX].selected[0]-1],autoreset=True)
        if currentSelection >= 1:
            if rootObject[MIDI_DEVICES_LIST_OBJ_IDX].selected[1][currentSelection-1] in rootObject[MIDI_DEVICES_LIST_OBJ_IDX].selected[1]:
                for msg in inport.iter_pending():
                    # print(msg)
                    if globalMidiMonitor[MIDI_MONITOR_TITLE].__len__() >= rootObject[MIDI_MONITOR_LIST_OBJ_IDX].gridBox[1]-2:
                        globalMidiMonitor[MIDI_MONITOR_TITLE].reverse()
                        globalMidiMonitor[MIDI_MONITOR_TITLE].pop(0)
                    globalMidiMonitor[MIDI_MONITOR_TITLE].append(str(msg))
                    globalMidiMonitor[MIDI_MONITOR_TITLE].reverse()

# midiMonitorThread = threading.Thread(target=monitorThread)
# midiMonitorThread.start()

cnt = 0

while 1:
    try:
        findPorts(FRAMERATE/5)
        if not rootObject[TITLE_OBJ_IDX].changed and not cnt % (LED_TIMEOUT_FRAMES * 2):
            rootObject[TITLE_OBJ_IDX].changed = True
            timeRunning = int((time.time()-START_TIME)*1000)
            cnt = 0
        # modNotif = {}
        modNotif = {str(NOTIF_TITLE+' '+str(timeRunning)):globalNotification[NOTIF_TITLE]}
        rootObject[TITLE_OBJ_IDX].text = modNotif
        rootObject[MIDI_DEVICES_LIST_OBJ_IDX].text = globalMidiPorts
        rootObject[MIDI_MONITOR_LIST_OBJ_IDX].text =  globalMidiMonitor        
        rootObject[DBG_OBJ_IDX].text =  timeRunning
        # rootObject[NOTIFICATIONS_OBJ_IDX].text = globalNotification
        screen.fill(BG_COLOR)
        rootObjectContainer.update(FRAMERATE)
    except:
        break
    cnt+=1
        # config = 
saveConfig(CONFIG_FILE_NAME,{"timeRunning":timeRunning, "textFont":textFont})
pygame.quit()
os._exit(0)