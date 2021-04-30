
"""Disutils Setup Script"""
import cx_Freeze, os.path 

PYTHON_INSTALL_DIR          = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY']   = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY']    = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6') 


executables = [
    cx_Freeze.Executable(
        script          = '__init__.py',
        base            = 'Win32GUI', 
        targetName      = 'SnakeGame.exe',
        icon            = 'images/icon.ico',
        copyright       = 'Copyright (c) 2021 FinalDSASUBMISSION',
        shortcutName    = 'SnakeGame'
    )
]

shortcut_table = [
    (
        'DesktopShortcut',        # Shortcut
        'DesktopFolder',          # Directory_
        'SnakeGame',               # Name
        'TARGETDIR',              # Component_
        '[TARGETDIR]SnakeGame.exe',# Target
        None,                     # Arguments
        None,                     # Description
        None,                     # Hotkey
        None,                     # Icon
        None,                     # IconIndex
        None,                     # ShowCmd
        'TARGETDIR'               # WkDir
    )
   
]

cx_Freeze.setup(
    name    = 'SnakeGame',
    version = '1.0.0',
    author  = 'Caleb Mugisha,Linda Pacifique, David Mbugua',
    url     = 'https://github.com/alu-rwa-dsa/summative-linda_david_caleb',
    options = {
        'build_exe': {
            'packages': ['pygame', 'random', 'math', 'os', 'json'],
            'include_files': ['images/', 'LICENSE.md', 'README.md'],
        },
        'bdist_msi': {
            'data': {
                'Shortcut': shortcut_table
            }
        }
    },
