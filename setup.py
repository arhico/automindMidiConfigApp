from cx_Freeze import Executable, setup
import datetime, platform

from automindMidiConfig import APP_NAME_SNAKE, APP_VER, APP_NAME


executables = [Executable(
    script=f"./{APP_NAME_SNAKE}.py",
    base="gui",
    # compress=False,
    # copyDependentFiles=True,
    # appendScriptToExe=True,
    # appendScriptToLibrary=False,
    icon=f"./assets/{APP_NAME_SNAKE}Icon"
    )]

# BUILD_COUNTER = 3
includeFiles = ['./assets/']
BUILD = "Build" + str(datetime.datetime.now()).replace(" ","").replace("-", "").replace(":", "")[2:14]
PLATFORM = platform.system()

build_exe_options = {
    "build_exe": f'./build/{APP_NAME_SNAKE}V{APP_VER}{PLATFORM}{BUILD}',
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
    name=APP_NAME_SNAKE,
    version=APP_VER,
    description=APP_NAME,
    options={"build_exe": build_exe_options},
    executables=executables,
)