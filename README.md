# AUTOMAT-auction

An automated Python bot/macro for the Forza Horizon auction house. This script automates the process of rapidly searching for and buying out cars using pixel color detection and simulated keyboard inputs. 

The bot navigates menus, waits for the UI to load by reading specific screen pixels, and rapidly executes the inputs required to successfully buy out a car before other players.

## Features

* **Automated Navigation:** Automatically enters the auction house and navigates menus.
* **Fast Pixel Reading:** Uses the `mss` library to instantly read screen pixel colors to determine the state of the game UI (e.g., waiting for the auction list or buyout menu to appear).
* **Keyboard Macros:** Uses the `keyboard` library to spam inputs at precise intervals.
* **Window Management:** Automatically detects, restores, and brings the game window to the foreground.

## Requirements

* **Python 3.x**
* Windows OS (due to the `pygetwindow` and `keyboard` libraries).
* The game running at a specific resolution (Note: The script uses hardcoded pixel coordinates, which are likely calibrated for a 1920x1080 display. If you use a different resolution, you may need to update the coordinates in `main.py`).

### Dependencies

Install the required Python packages using pip:

```bash
pip install mss pygetwindow keyboard
```

## Usage

1. Ensure your game (configured as "Forza Horizon 6" in `main.py`) is running. 
2. Make sure your game is set to the correct resolution that matches the hardcoded pixel coordinates.
3. Open a terminal as **Administrator** (the `keyboard` module may require admin privileges to send keystrokes to certain applications).
4. Run the main script:

```bash
python main.py
```

5. When prompted, enter the number of attempts/cycles you want the bot to run. Enter `0` for an infinite loop.

## Project Structure

* **`main.py`**: The main orchestrator. It manages the loop, reads pixels to check UI states, and calls the appropriate macros.
* **`macro.py`**: Contains the precise keyboard sequences and timings for navigating menus (`menu_to_auction`), spamming keys (`y_spam`), and buying out cars (`buyout`).
* **`pixelReadS.py`**: A fast, minimal wrapper around `mss` for grabbing a specific pixel's color and comparing it to an expected hex value.
* **`windowget.py`**: Utility script utilizing `pygetwindow` to find the game window by title, unminimize it, and bring it into focus.

## Configuration & Tweaking

If the bot isn't clicking correctly or gets stuck, you may need to adjust the following variables in `main.py` to match your display:

* `auction_pixel = pr.PixelRead(1562, 177, 0xCAFF02)` (Adjust X, Y, and Hex Color)
* `ac_menu_pixel = pr.PixelRead(1261, 649, 0XFFFFFF)` (Adjust X, Y, and Hex Color)

Timing adjustments can be made inside `macro.py` if the game UI is loading slower or faster than the macro executes.

## Disclaimer

Use this tool at your own risk. Automated scripts and macros may violate the Terms of Service of the game and could result in account bans or suspensions. This project is for educational purposes.

