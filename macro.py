import time
import keyboard

def run_macro(steps, initial_delay=0.0):
    """Run a timed macro using key-down/key-up pairs."""
    time.sleep(initial_delay)
    for key, hold_time, delay_after in steps:
        keyboard.press(key)
        time.sleep(hold_time)
        keyboard.release(key)
        time.sleep(delay_after)

def menu_to_auction():
    """Macro to move from menu to auction house"""
    run_macro([
        ('enter', 0.141, 0.453),
        ('enter', 0.078, 0.25)
    ], initial_delay=0.6)

def y_spam():
    """Macro for y key spamming"""
    run_macro([
        ('y', 0.050, 0.050),
        ('y', 0.050, 0.050)
    ])

def buyout():
    """Macro for Buyout from auction house."""
    run_macro([
        ('down', 0.094, 0.100),
        ('enter', 0.050, 0.094), # using 0.050s for implicit hold times
        ('enter', 0.050, 0.094),
        ('enter', 0.050, 0.094),
        ('enter', 0.050, 0.500)
    ], initial_delay=0.0)

def esc():
    """Macro for 'esc' key"""
    run_macro([
        ('esc',0.1,0.5)
    ])