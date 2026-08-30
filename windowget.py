import pygetwindow as gw

def activateWindow(Game_name):
    """Activates the process window"""

    game = gw.getWindowsWithTitle(Game_name)
    
    if not game:
        print(f"{Game_name} is not running")
        exit()
    else:
        wind = game[0]
        if wind.isMinimized:
           wind.restore()
        wind.activate()