# Sentinel

<p align="center">
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/57d75eca-881e-4807-b288-4b5222606c27" width="600" />
</p>

# Project Aim
The aim of this project was to design, manufacture, and program a robotic system capable of human face detection and real-time tracking. The primary objective was to develop a system that could autonomously identify human faces within a frame and subsequently track and center the detected faces to maintain visual focus during motion. This project integrates machine learning and deep learning techniques to achieve robust and efficient human tracking functionality.

Some applications of this project are:
1. <b>Video Surveillance and Security Systems</b>: Implementing human tracking can enhance surveillance systems by automatically monitoring and analyzing human movement in real time, thereby improving security measures.
2. <b>Automated Filming and Photography</b>: Using a human tracking bot, cameras can autonomously capture footage or photos while ensuring the subjects (humans) remain in focus and centered within the frame.
3. <b>Human-Computer Interaction (HCI)</b>: Enhance HCI applications by tracking users' gestures and movements, allowing for more intuitive and responsive interactions with computers or devices.
4. <b>Object Tracking in Industrial Automation</b>: Extend the human tracking model to identify and track specific objects or components in manufacturing or assembly line processes.
5. <b>Wildlife Monitoring and Conservation</b>: Adapt the tracking capabilities to monitor wildlife movements and behaviors for conservation efforts or wildlife research.
6. <b>Sports Analysis and Training</b>: Use tracking technology to analyze athletes' movements during training or competitions, providing valuable insights for performance improvement.

These applications demonstrate the versatility and potential of human tracking technology beyond its initial scope, showcasing how machine learning and deep learning can be leveraged for various innovative purposes across different domains.

## Installation ##
### Pan Tilt Camera Rig ###
I 3D printed the camera rig, the Autodesk Fusion files, and the STL files can be found in the '3D Print' folder. Alternately pan tilt camera rig can be bought with servo motors attached.

<p align="center">
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/b50c1ad4-dba1-49fb-8f74-93a3b5410d3b" width="200" height = "225"/>
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/6d6a03f8-c85d-48bd-ab35-762ff85f7a86" width="225" height = "225"/>
</p>

### Code ###
Need to install the following libraries for Python using pip:
*  ultralytics
*  OpenCV
*  pyfirmata
  
Need to install the following library in Arduino IDE:
*  firmata

### Arduino Circuit Diagram ###
<p align="center">
<img src="https://github.com/Chinmay-Deep-Sahoo/Sentinel/assets/118956460/9e043deb-04ba-47ba-8dd0-3f6d83216a3c" width="700"/>
</p>
Need to upload standardfirmata.ino to your Arduino. It is also present as an example in the Arduino IDE.

# Procedure #
## Human Face Detection

I am using [YoloV8](https://docs.ultralytics.com) for detecting human face in the image captured by the camera. 
