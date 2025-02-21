"""
Filename: screen_livepredict.py
Author: WormStan
Date: 2/20/2025
Description: Toolktis for live predict monitor target object.
"""

import cv2
import numpy as np
from ultralytics import YOLO
from mss import mss

def live_predict(model_path, monitor_number):
    model = YOLO(model_path)
    sct = mss()
    monitor = sct.monitors[monitor_number]
    
    while True:
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        results = model(img)
        annotated_img = results[0].plot()
        cv2.imshow("Monitor Detection", annotated_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()