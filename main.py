import cv2
import numpy as np
import math
import time
import os
import urllib.request
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pycaw.pycaw import AudioUtilities

# =========================
# CAMERA
# =========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not found!")
    exit()

print("✅ Camera started")

# =========================
# MODEL DOWNLOAD
# =========================
MODEL_PATH = "hand_landmarker.task"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"

if not os.path.exists(MODEL_PATH):
    print("Downloading model...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

print("✅ Model ready")

# =========================
# AUDIO
# =========================
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume

volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

print(f"Volume Range: {minVol:.1f} dB to {maxVol:.1f} dB")

# =========================
# HAND TRACKER
# =========================
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)
print("Hand tracker ready!")

# =========================
# FPS TIMER
# =========================
pTime = 0

# =========================
# LOOP
# =========================
while True:
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # FPS
    cTime = time.time()
    fps = int(1 / (cTime - pTime)) if (cTime - pTime) != 0 else 0
    pTime = cTime

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        lm = result.hand_landmarks[0]

        # Draw all hand landmarks (green lines + red dots)
        connections = mp.solutions.hands.HAND_CONNECTIONS
        for connection in connections:
            start_idx = connection[0]
            end_idx = connection[1]
            x_start = int(lm[start_idx].x * w)
            y_start = int(lm[start_idx].y * h)
            x_end = int(lm[end_idx].x * w)
            y_end = int(lm[end_idx].y * h)
            cv2.line(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)

        for i, landmark in enumerate(lm):
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), cv2.FILLED)

        # Thumb tip (4) and Index finger tip (8)
        x1, y1 = int(lm[4].x * w), int(lm[4].y * h)
        x2, y2 = int(lm[8].x * w), int(lm[8].y * h)

        # Draw circles on thumb and index
        cv2.circle(frame, (x1, y1), 12, (255, 0, 255), cv2.FILLED)  # Pink - Thumb
        cv2.circle(frame, (x2, y2), 12, (0, 255, 0), cv2.FILLED)  # Green - Index
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Calculate distance
        length = math.hypot(x2 - x1, y2 - y1)

        # Map to volume
        vol = np.interp(length, [25, 220], [minVol, maxVol])
        volBar = np.interp(length, [25, 220], [400, 150])
        volPer = int(np.interp(length, [25, 220], [0, 100]))

        volume.SetMasterVolumeLevel(vol, None)

        # Draw Volume Bar (left side)
        cv2.rectangle(frame, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(frame, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        cv2.putText(frame, f'{volPer} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 3)

    # FPS Display
    cv2.putText(frame, f'FPS: {fps}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Gesture Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()