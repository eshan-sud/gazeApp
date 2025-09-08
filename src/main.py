# src/main.py

# app entry, consent + camera + gaze loop

import tkinter as tk
from tkinter import messagebox
import cv2
import threading

def on_accept():
    root.destroy()
    start_camera_loop()

def start_camera_loop():
    # Camera is only opened after explicit consent from user
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Camera (press q to quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("GazeApp: Camera Consent")
lbl = tk.Label(root, text="GazeApp will access your laptop camera locally.\nNo footage leaves your machine unless you explicitly save or opt-in.\nDo you consent?")
lbl.pack(padx=20, pady=10)
btn = tk.Button(root, text="I CONSENT", command=on_accept)
btn.pack(pady=(0,20))
root.mainloop()