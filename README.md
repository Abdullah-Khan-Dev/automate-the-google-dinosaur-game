# T-Rex Game Bot

This project automates the Chrome T-Rex game using Selenium and OpenCV. The bot detects obstacles and controls the T-Rex to jump over them, aiming to achieve a high score without human intervention.

## Features

- Uses Selenium WebDriver to control the Chrome browser
- Utilizes OpenCV for image processing to detect obstacles
- Simulates keyboard inputs to make the T-Rex jump

## Requirements

- Python 3.x
- Selenium
- OpenCV
- Chrome WebDriver

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/t-rex-game-bot.git
   cd t-rex-game-bot
Install the required libraries:
```bash
pip install selenium opencv-python
```
2. **Download Chrome WebDriver:**

- ChromeDriver
- Ensure the ChromeDriver executable is in your PATH or in the project directory.
## Usage
1. **Run the script:**

```bash
python t_rex_game_bot.py
```
2. **The script will:**

- Open the T-Rex game in Chrome.
- Start the game by simulating a space bar press.
- Continuously capture the game screen and detect obstacles.
- Make the T-Rex jump over obstacles automatically.
## Customization
- You may need to adjust the region of interest (ROI) values in the script based on your screen resolution and the position of the T-Rex and obstacles.
- Modify the delay values to control the responsiveness and speed of the game.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements
- The T-Rex game is a fun Easter egg by Google Chrome.

## Disclaimer
This bot is created for educational purposes only. Please use it responsibly.