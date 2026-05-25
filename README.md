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
