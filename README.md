# LoL Playtime Control

This is a software tool designed to help League of Legends players manage and control their playtime effectively. It will track the amount of time spent in-game, and once the user has accumulated 1.5 hours of game-time for the day, it will forcefully close the League of Legends client. This program is non-intrusive and runs in the background, visible as a tray icon.

## Trust

It is understandable that using a third-party application the ability to close your game can be a concern. This is why the code is open-source and available for review, the installation process is also performed locally on your machine using the direct source code from this repository. You can prompt this repository https://github.com/iann838/lol-playtime-control to an AI model with reasoning capabilities (ChatGPT, Grok, etc.) for further insights and review.

This tool:
- Does not collect any personal data or usage statistics.
- Does not touch or interact with ingame-memory.
- Does not modify game files or settings.
- Does not abruptly terminate the game, only closes the client.

## Installation

1. Have [Python 3](https://www.python.org/downloads/) installed on your system.
2. Download this repository as ZIP. Top-right **[<> Code]** > **[Local]** > **[Download ZIP]**.
3. Extract the downloaded ZIP file to a folder.
4. Navigate into the folder (main.py visible on the directory).
5. Right-click > **[Open in Terminal]**.
6. Type `pip install .`, and hit Enter.

## Usage

1. Press `Win + R`, type `cmd`, and hit Enter.
2. Type `lol-playtime-control`, and hit Enter.

The tool should now be visible on a tray icon. Right-click the icon to access the menu.

## Startup

This tool can be configured to start automatically when you log in to your computer. To do this, create a shortcut to the `lol-playtime-control` executable and place it in your startup folder.

1. Press `Win + R`, type `cmd`, and hit Enter.
2. Type `where lol-playtime-control`, and hit Enter. This tells you the location of the executable.
3. Navigate to the location of the executable using File Explorer.
4. Right-click on the `.exe` file > **[Create shortcut]**.
5. Right-click on the created shortcut > **[Cut]**.
6. Press `Win + R`, type `shell:startup`, and hit Enter. This opens the startup folder.
7. Paste the created shortcut on the startup folder.

To remove the tool from startup, simply delete the shortcut from the startup folder.
