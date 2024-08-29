# Configurator for touch MIDI controller named "AUTOMIND MIDI"
Based on pygame-ce it enables Automind MIDI touch controller device based on ESP32S2 to be tuned, tested and debugged.
Also acts as universal simple MIDI monitor.
WARNING! Almost nothing works now, code might be bad. Made public for friends to help with testing and developing

## About MIDI controller
Based on neteork of ESP32S2 SOCs
TODO

## How to get started
### Create virtual enviroment with python (tested: 3.11.2, 3.12.2)
```/usr/local/bin/python3.12 -m venv ./.venv --system-site-packages```
system-site-packages needed for build via pyinstaller
### Install dependencies from requirementsAutomindMidiApp.txt
```./.venv/bin/python ./.venv/bin/pip install -r ./requirementsAutomindMidiApp.txt``` 

### Run
```automindMidiApp.py```

### Compile binary with cx_Freeze
```setup.py build```