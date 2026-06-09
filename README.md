🤌 Hand Gesture Volume Control
Control your Windows system volume using hand gestures via webcam. Built with OpenCV, MediaPipe, and PyCAW.
 Demo 

 OpenCV 

 MediaPipe 
✨ Features
🎥 Real-time hand tracking using MediaPipe
🔊 Gesture-based volume control — pinch thumb & index finger to adjust volume
📊 Visual volume bar with percentage display
🖐️ Hand skeleton overlay with landmark visualization
⚡ FPS counter for performance monitoring
📥 Auto-downloads MediaPipe hand model on first run
🖼️ How It Works
Table
Gesture	Action
Thumb + Index close together 🔗	Volume DOWN 🔉
Thumb + Index far apart ✌️	Volume UP 🔊
The distance between your thumb tip (landmark 4) and index finger tip (landmark 8) is mapped to your system volume level.
🚀 Quick Start
1. Clone the Repository
bash
git clone https://github.com/yourusername/hand-gesture-volume-control.git
cd hand-gesture-volume-control
2. Install Dependencies
bash
pip install -r requirements.txt
⚠️ Note: pycaw only works on Windows. This project is Windows-only.
3. Run the Application
bash
python main.py
4. Controls
Table
Key	Action
Q	Quit the application
📁 Project Structure
plain
hand-gesture-volume-control/
├── main.py                 # Main application script
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── hand_landmarker.task   # Auto-downloaded MediaPipe model (on first run)
📦 Requirements
txt
opencv-python==4.13.0.92
numpy==2.4.6
mediapipe==0.10.14
pycaw==20251023
System Requirements
OS: Windows 10/11 (PyCAW requires Windows)
Python: 3.8 or higher
Webcam: Built-in or external USB camera
🛠️ Installation Guide (Step-by-Step)
Step 1: Install Python
Download and install Python 3.8+ from python.org. Make sure to check "Add Python to PATH" during installation.
Step 2: Create Virtual Environment (Recommended)
bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Or on PowerShell
venv\Scripts\Activate.ps1
Step 3: Install Packages
bash
pip install -r requirements.txt
Step 4: Run
bash
python main.py
🎯 Usage Tips
Good Lighting: Ensure your hand is well-lit for better tracking
Clear Background: Plain background improves detection accuracy
Hand Position: Keep your hand within the camera frame
Smooth Movements: Move fingers slowly for precise volume control
Distance Range:
25px between fingers = 0% volume (mute)
220px between fingers = 100% volume (max)
🐛 Troubleshooting
Table
Problem	Solution
❌ Camera not found	Check if another app is using the camera. Try cap = cv2.VideoCapture(1) for external webcam
❌ Model download fails	Check internet connection. Manually download from MediaPipe Models
❌ Volume not changing	Run as Administrator. Check if PyCAW is installed correctly
🐢 Low FPS	Close other applications. Reduce camera resolution if needed
🖐️ Hand not detected	Move hand closer to camera. Improve lighting conditions
📝 Code Overview
Python
# Core workflow:
1. Capture webcam frame
2. Convert to RGB for MediaPipe
3. Detect hand landmarks
4. Calculate thumb-index distance
5. Map distance to volume range
6. Set system volume via PyCAW
7. Draw UI overlay (volume bar, FPS, landmarks)
🤝 Contributing
Contributions are welcome! Feel free to:
🐛 Report bugs via Issues
💡 Suggest new features
🔧 Submit pull requests
📄 License
This project is licensed under the MIT License — feel free to use, modify, and distribute.
🙏 Acknowledgments
MediaPipe by Google for hand tracking
PyCAW for Windows audio control
OpenCV for computer vision utilities
📬 Contact
Number: 01318891604
GitHub: fahim202342
Email: mf143416@gmail.com
⭐ Star this repo if you found it helpful!
