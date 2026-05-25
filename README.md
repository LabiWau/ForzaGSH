# ForzaGSH (Gear Shift Helper) 

ForzaGSH is a lightweight Python tool designed to give drivers an audio shift-cue in Forza games by monitoring a specific pixel region of the screen (such as the RPM shift light on the HUD). 

It features an on-screen visual overlay helper to easily align the tracking area with your game's HUD.

## Features
* **Real-time Screen Monitoring:** Uses ultra-fast screen capturing (`mss`) to detect shifting indicators.
* **Visual Overlay:** A semi-transparent overlay to help configure position boundaries coordinates perfectly.
* **Audio Alerts:** Plays a clear audio signal via `pygame` the millisecond you hit the optimal shift point.

## Requirements 
Make sure you have Python 3 installed, then run:
```bash
pip install numpy mss pygame tk
```
## Installation and Setup
Clone the repository:
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/ForzaGSH.git](https://github.com/YOUR_GITHUB_USERNAME/ForzaGSH.git)
cd ForzaGSH
```

Add your Audio File:
Place your preffered shift sound file in the root directory of the project and name it shift_sound.wav.

Configure the Capture Region:
If your playing on a different resulution than FHD you might need to change the resolution. Try to tinker with left and top and youll understand how to position your capture region:
```bash
REGION = {"top": 850, "left": 1700, "width": 80, "height": 80}
```

Run the Script: 
Start the application via your terminal:
```bash
python forza.py
```
Once aligned, you can set SHOW_OVERLAY = False in the script to hide the setup box during actual gameplay.

## Ps.
This is my first project! If you want to give me tips or work together hmu
