# tests/check_camera.py

import cv2

def main():
    cap = cv2.VideoCapture(0) # Try to open the default webcam (0)

    if not cap.isOpened():
        print("Couldn't access the camera!!!")
        return

    print("Camera opened successfully. Press ESC to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame!!!")
            break
        frame = cv2.flip(frame, 1) # Flip horizontally for a mirror effect
        cv2.imshow("Webcam Feed", frame) # Show the frame in a window
        if cv2.waitKey(1) & 0xFF == 27: # Exit on ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
