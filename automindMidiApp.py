# import re
import time
# import math
# import random
import os
# import colorsys
# import subprocess
# import importlib.util

from automindMidiConfig import *
import automindMidiVisualizer
from automindMidiVisualizer import gridObjectCreate, rootObjectsContainerClass
# from automindMidiVisualizer import

import pygame
import mido
import mido.backends.rtmidi
# from tkinter import filedialog
import threading
# import numpy

# def open_file():
#     # Open file dialog to select a file
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         try:
#             with open(file_path, 'r') as file:
#                 file_contents = file.read()
#                 global file_data
#                 file_data = file_contents
#                 file_ready_event.set()
#         except IOError:
#             tk.messagebox.showerror("Error", "Failed to open file.")
#     else:
#         tk.messagebox.showwarning("Warning", "No file selected.")

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
# globalMidiPorts.append("")

findPportsSamplesCount = 0
MIDI_MONITOR_TITLE = "MIDI monitor:"
MIDI_DEVICES_LIST_TITLE = "MIDI devices:"
def findPorts(decimateFreq = None):
    global globalMidiPorts,findPportsSamplesCount
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

# def findPortsTask():
#     while 1:
#         findPorts()
#         time.sleep(0.2)
    
# midiPortsThread = threading.Thread(target=findPortsTask)
# midiPortsThread.start()

# print_ports('Input Ports:', mido.get_input_names())
# print_ports('Output Ports:', mido.get_output_names())
# port = mido.open_output('AUTOMIND TOUCH MIDI:AUTOMIND TOUCH MIDI MIDI 1 24:0')
# with mido.open_input('AUTOMIND TOUCH MIDI:AUTOMIND TOUCH MIDI MIDI 1 24:0') as inport:
#     for msg in inport:
#         print(msg)


globalMidiMonitor = {}
globalMidiMonitor[MIDI_MONITOR_TITLE]= ["oh, hi mark"]
from automindMidiConfig import NOTIF_TITLE
globalNotification = {NOTIF_TITLE:[]}


rootObject = []

TITLE_OBJ_IDX = gridObjectCreate("guiBrickList", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],2))
rootObject[TITLE_OBJ_IDX].text = "AUTOMIND:"

# SENSORS_IDX = gridObjectCreate("guiBrickInteractive", rootObject, screen, grids, gridBx=SENSOR_GRIDBOX, gridMapping=SENSOR_GRID_MAPPING)
# gridObjectCreate("guiBrick",rootObject,screen,grids,(grids.gridDimensions[1] - 2))
# TEST = gridObjectCreate("guiBrickListInteractive", rootObject, screen, grids, gridBx=(grids.gridDimensions[0]/2,4))
# rootObject[TEST].text = 42
# MIDI_DEVICES_LIST_OBJ_IDX = gridObjectCreate("guiBrickDropListInteractive", rootObject, screen, grids, gridBx=(grids.gridDimensions[0],2))
MIDI_DEVICES_LIST_OBJ_IDX = gridObjectCreate("guiBrickListInteractive", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],6))

MIDI_MONITOR_LIST_OBJ_IDX = gridObjectCreate("guiBrickList", rootObject, screen, globalNotification, grids, gridBx=(grids.gridDimensions[0],int(6)))

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
            cnt = 0
        
        rootObject[TITLE_OBJ_IDX].text = f"AUTOMIND: {globalNotification}"
        
        
        rootObject[MIDI_DEVICES_LIST_OBJ_IDX].text = globalMidiPorts
        rootObject[MIDI_MONITOR_LIST_OBJ_IDX].text = globalMidiMonitor
        # rootObject[NOTIFICATIONS_OBJ_IDX].text = globalNotification
        screen.fill(BG_COLOR)
        rootObjectContainer.update(FRAMERATE)
    except:
        break

    # print(globalNotification)
    

    cnt+=1
pygame.quit()
os._exit(0)