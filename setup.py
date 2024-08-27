"""A very simple setup script to create a single executable.

hello.py is a very simple 'Hello, world' type script which also displays the
environment in which the script runs.

Run the build process by running the command 'python setup.py build'

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the script without Python
"""

from cx_Freeze import Executable, setup

executables = [Executable(
    script="./automindMidiApp.py",
    base="gui",
    # compress=False,
    # copyDependentFiles=True,
    # appendScriptToExe=True,
    # appendScriptToLibrary=False,
    icon="./assets/automindMidiIcon"
    )]

import datetime
import platform
# BUILD_COUNTER = 3
includeFiles = ['./assets/']
BUILD = str(datetime.datetime.now()).replace(" ","").replace("-", "")
BUILD = BUILD.replace(":", "")[2:14]
APP_VER = f"0.0.1.4"
APP_NAME = f'automindMidiAppV{APP_VER}'

PLATFORM = platform.system()

build_exe_options = {
    "build_exe": f'./build/{APP_NAME}{PLATFORM}Build{BUILD}',
    "excludes": ["unittest"],
    # "includes": ["mido", "pygame","rtmidi","tkinter"],
    # "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
    # "zip_include_packages": ["*"],
    # "bin_includes":["rtmidi"],
    # "bin_includes":["*"],
    "optimize":"2",
    "include_files":includeFiles
}

setup(
    name="AUTOMIND MIDI APP",
    version=APP_VER,
    description=APP_NAME,
    options={"build_exe": build_exe_options},
    executables=executables,
)