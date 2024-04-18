# Sentinel

<p align="center">
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/57d75eca-881e-4807-b288-4b5222606c27" width="600" />
</p>

# Table of Content #
* [Project Aim](#pa)
    * [Key Features](#kf)
    * [Applications](#a)
* [Installation](#i)
     * [Pan Tilt Camera Rig](#ptcr)
     * [Python Libraries](#pl)
     * [Arduino Library](#al)
     * [Arduino Circuit Diagram](#acd)
     * [Uploading Firmata to Arduino](#ufa)
* [Usage](#u)
* [Demo](#d)
* [Code Overview](#co)

# Project Aim <a name="pa"></a>
The goal of this project was to develop a robotic system capable of autonomously detecting and tracking human faces in real-time. The primary objective was to design, manufacture, and program a robot that could identify human faces within a frame and dynamically track and center these faces to maintain visual focus during motion. This project integrates machine learning and deep learning techniques to achieve robust and efficient human tracking functionality.

### Key Features <a name="kf"></a>
*  Real-time human face detection and tracking.
*  Autonomous centering of detected faces within the frame.
*  Integration of advanced machine learning algorithms for accurate and reliable tracking.

### Applications <a name="a"></a>
1. Video surveillance and security systems enhancement
2. Automated filming and photography for capturing human-centric footage
3. Human-computer interaction improvements by enabling intuitive gestures and movement tracking.
4. Object tracking in industrial automation processes.
5. Wildlife monitoring and conservation efforts.
6. Sports analysis and training for performance improvement.

This project demonstrates how machine learning and deep learning technologies can be leveraged to expand the capabilities of robotic systems, paving the way for innovative and practical applications across different domains.

# Installation <a name="i"></a>
### Pan Tilt Camera Rig <a name="ptcr"></a>
If you prefer to 3D print the camera rig, you can find the Autodesk Fusion files and STL files in the '3D Print' folder of this repository. Alternatively, you can purchase a pan tilt camera rig with servo motors already attached.

<p align="center">
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/b50c1ad4-dba1-49fb-8f74-93a3b5410d3b" width="200" height = "225"/>
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/6d6a03f8-c85d-48bd-ab35-762ff85f7a86" width="225" height = "225"/>
</p>

### Python Libraries <a name="pl"></a>
Need to install the following libraries for Python using pip:
```
pip install ultralytics
pip install opencv-python
pip install pyfirmata
```

### Arduino Library <a name="al"></a>
You'll also need to install the firmata library in the Arduino IDE. Follow these steps:
1. Open the Arduino IDE.
2. Navigate to Sketch > Include Library > Manage Libraries.
3. Search for "firmata" and install the library.

### Arduino Circuit Diagram <a name="acd"></a>
Refer to the provided circuit diagram to connect the Arduino with the pan-tilt camera rig and other components, remember the Arduino PINs to which the signal wires of the servo motors are connected.
<p align="center">
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/9e043deb-04ba-47ba-8dd0-3f6d83216a3c" width="800"/>
</p>

### Uploading Firmware to Arduino <a name="ufa"></a>
Upload the StandardFirmata sketch to your Arduino board. This sketch is included as an example in the Arduino IDE. Follow these steps:
1. Open the Arduino IDE.
2. Go to File > Examples > Firmata > StandardFirmata.
3. Upload the sketch to your Arduino board.

# Usage <a name="u"></a>
1. Running the Scripts:
  * Ensure all necessary libraries are installed and the Arduino board is connected to your PC.
  * To use the mounted camera for human face detection and tracking, run the following command:
```
python Final-Dyn.py
```
  * If you want to use a secondary static camera instead, run the following command:
```
python Final-Static.py
```
2. Diagnosis and Servo Control:
* Utilize the provided helper script arduino_both.py for diagnosis and to control the servo motors via the terminal. This script can be helpful for troubleshooting and verifying servo motor functionality.
```
python arduino_both.py
```
3. Additional Notes:
* Ensure that the correct COM port for your Arduino board is specified within the Python scripts.
* Adjust any parameters or settings within the scripts (if applicable) to customize the behavior of the human tracking bot based on your requirements.


# Demo <a name="d"></a>
Watch the following videos to see the human-tracking robot in action! These demonstrations showcase the capabilities of the robot in autonomously detecting and tracking human faces in real time. Feel free to observe the accurate movements of the pan-tilt camera rig as it maintains visual focus on the detected faces. Note: I am using the 'Final-Dyn.py' script as I am using the mounted dynamic camera as my only camera.

<div align="center">
  <video src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/c4d9599b-4956-42de-b968-6013ff5e8dbc" width="400" /> 
</div>
<div align = "center">
  <video src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/249b7897-96e3-4a7e-8a21-fefe497ed286" width="400" />
</div>


# Code Overview <a name="co"></a>

In this project, I leverage the [YoloV8](https://docs.ultralytics.com) model for detecting human faces in the images captured by the camera. The following steps outline the process:
1. YoloV8 is used to detect human faces within the captured images. The model outputs bounding boxes $(X_1, Y_1)$ to $(X_2, Y_2)$ that enclose the detected faces.
2. Calculating Vector for Tracking:
* To track the detected face, a vector is calculated from the center of the image to the center of the bounding box. This vector is calculated using:
  * $start = ( \frac{W}{2}, \frac{L}{2} )$  Where $W$ and $L$ are the width and length of the image respectively.
  * $end = ( \frac{X_1 + X_2}{2}, \frac{Y_1 + Y_2}{2} )$ which represents the center of the bounding box.
3. Calculating Servo Motor Angles:
* Using the calculated vector, angles $a_x$ and $a_y$ are computed to rotate the servo motors:
  * $a_x = \frac{start_x - end_x}{\frac{L}{2}} \times amax_x$
  * $a_y = \frac{end_y - start_y}{\frac{W}{2}} \times amax_y$
* Here, amax_x and amax_y represent the maximum change in angles for servo motor control in the respective directions.
4. Sending Control Signals to Arduino:
* The calculated angles $a_x$ and $a_y$ are then sent to the Arduino board using the pyfirmata library to control the servo motors accordingly.

### Note ###
A 'ctr' variable is introduced in the code to slow down the inference frequency of the Yolo face detection model. This approach helps maintain stability and allows for running heavier machine learning models in real time without significant performance impact.
