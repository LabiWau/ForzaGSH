import threading
import time
import tkinter as tk
import os
import numpy as np
import mss
import pygame

# ================= CONFIGURATION =================

# Set the coordinates and size of the partition to monitor
# (Adjust these based on your screen resolution and Forza HUD)
REGION = {"top": 850, "left": 1700, "width": 80, "height": 80}

# Your sound file (make sure it's in the same folder as this script)
SOUND_FILE = "shift_sound.wav"

# Show a visible block on screen to help you position the region
SHOW_OVERLAY = True

# Cooldown to prevent the sound from playing 60 times a second 
# while the red light is visible (in seconds)
COOLDOWN_SECONDS = 0.5

# =================================================

def monitor_loop():
    """Background thread that captures the screen and checks for the target color."""
    
    pygame.mixer.init()
    sound_loaded = False
    
    # Check if the sound file exists so the script doesn't crash if it's missing
    if os.path.exists(SOUND_FILE):
        shift_sound = pygame.mixer.Sound(SOUND_FILE)
        sound_loaded = True
        print(f"Sound '{SOUND_FILE}' loaded successfully.")
    else:
        print(f"Warning: '{SOUND_FILE}' not found. Audio will be skipped.")

    last_play_time = 0

    with mss.mss() as sct:
        print("Screen monitoring started...")
        while True:
            img = np.array(sct.grab(REGION))
            
            B = img[:, :, 0]
            G = img[:, :, 1]
            R = img[:, :, 2]
            
            is_target_color = (R > 190) & (G < 45) & (B > 90) & (B < 165)
            
            if np.any(is_target_color):
                current_time = time.time()

                if current_time - last_play_time > COOLDOWN_SECONDS:
                    print("Shift color detected! SHIFT UP!")
                    if sound_loaded:
                        shift_sound.play()
                    last_play_time = current_time
            # If you dont care about CPU usage and want faster responsetimes, comment out line 63
            time.sleep(0.05)


def create_overlay():
    root = tk.Tk()
    
    root.overrideredirect(True)
    
    root.attributes('-topmost', True)
    
    # Change the transparency of the window (0.1 = 10%)
    root.attributes('-alpha', 0.3)
    
    root.config(bg='#e6037e')
    
    root.geometry(f"{REGION['width']}x{REGION['height']}+{REGION['left']}+{REGION['top']}")
    
    def check():
        root.after(500, check)
    root.after(500, check)
    
    print("Overlay is active. Press Ctrl+C in the terminal to exit the program.")
    root.mainloop()


if __name__ == "__main__":

    monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
    monitor_thread.start()

    if SHOW_OVERLAY:
        try:
            create_overlay()
        except KeyboardInterrupt:
            print("Exiting...")
    else:
        print("Press Ctrl+C in the terminal to exit.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
