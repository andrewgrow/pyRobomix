from cx_Freeze import setup, Executable

base = None

executables = [Executable("blackJack.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "ProgNameWillBeHere",
    options = options,
    version = "1.0.0",
    description = 'DescriptionWillBeHere',
    executables = executables
)