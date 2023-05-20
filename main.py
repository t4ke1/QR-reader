import pyautogui
import cv2
import numpy as np
import os
from pyzbar.pyzbar import decode

input("Press any key to take screenshoot...")
# Create screenshot and save to file
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

# Load screenshot and make it black-white colors only
img = cv2.imread('screenshot.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get QR from screenshot
qr_codes = decode(gray)

# Output information from QR code
if qr_codes:
    for qr in qr_codes:
        print("QR Code data:", qr.data.decode("utf-8"))
else:
    print("QR Code not found!")
# Delete screenshot
os.remove('screenshot.png')
input("Press any key to continue...")
