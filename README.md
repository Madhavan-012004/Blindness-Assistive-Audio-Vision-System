# Blindness Assistive Audio Vision System
![image](https://github.com/user-attachments/assets/f976dabc-ae5f-4023-bd9d-cc2034510e63)
The **Blindness Assistive Audio Vision System** is an innovative, smart wearable solution developed to enhance the daily life and independence of individuals with visual impairments. Designed as a lightweight headband embedded with a compact camera and powered by a Raspberry Pi, this system captures visual data from the user's surroundings and translates it into clear, real-time audio feedback.

The core goal of this project is to bridge the gap between the visual world and blind or visually impaired users by using cutting-edge computer vision, natural language processing, and speech technologies. It helps users perceive their environment more effectively, understand their surroundings, and interact with others confidently.

This intelligent headband prototype performs multiple assistive tasks using five integrated modules:

- **Object Detection**: The device identifies objects in front of the user — such as vehicles, furniture, or obstacles — and announces them via audio, allowing the user to move safely and efficiently.
- **Text Recognition (OCR)**: The system can scan printed or digital text in the environment (e.g., on signboards or documents) and read it aloud. It supports multiple languages for both text recognition and speech output, ensuring accessibility for diverse users.
- **Sign to Speech**: One of the system’s standout features is its ability to act as a bridge between visually impaired users and individuals who cannot speak. It captures sign language gestures via the camera, compares them with a custom-built sign language dataset, and converts them into meaningful voice messages. This facilitates seamless two-way communication.
- **Voice Command**: The system is completely voice-activated. Users can give commands like “read text” or “identify object” to activate specific modules. The voice bot can also speak slowly if needed, repeat outputs upon request, and support multilingual interactions. This module ensures hands-free control and a smooth user experience.
- **Audio Feedback**: Every action taken by the system is translated into precise voice outputs delivered through Bluetooth-enabled earpods, ensuring privacy and clarity.

This headband is designed with comfort, portability, and user-friendliness in mind. Users can wear it throughout their daily activities without discomfort. The voice interaction capabilities mean the system only responds when commanded, ensuring it doesn’t interfere unnecessarily with the user’s experience.

The **Blindness Assistive Audio Vision System** empowers users to navigate unfamiliar environments, understand signage, and interact with others in ways that were previously challenging or inaccessible. It is more than a prototype—it is a step forward in assistive technology, bringing inclusivity and autonomy to the forefront.

With its modular architecture, the system can be further expanded to support additional assistive features, like facial recognition or GPS-based navigation. As a student-led mini project, it lays a strong foundation for future development and real-world applications aimed at promoting social equity and technological empowerment.

In summary, this project blends practical utility with advanced AI techniques to provide a meaningful and accessible solution to real-world challenges faced by the visually impaired community.


## Project Objectives

The **Blindness Assistive Audio Vision System** was developed with a mission to improve the quality of life for individuals with visual impairments by giving them a more autonomous and informed way to interact with their environment. The system merges various emerging technologies—computer vision, speech synthesis, and natural language processing—into a compact, wearable form that provides auditory descriptions of the world around the user. The following objectives outline the core goals and impact of the project:

- **Convert Visual Data into Real-Time Audio Feedback**  
  The central objective of the system is to bridge the gap between visual and non-visual perception. By using a camera mounted on a wearable headband, the system captures images and video in real-time. These visuals are processed using machine learning models to detect objects, read text, and interpret human emotions or gestures. The processed results are then converted into voice messages and delivered to the user via Bluetooth earpods. This real-time conversion of visual information into auditory feedback empowers users to perceive and understand their environment without relying on sight.

- **Offer Multi-Modal Assistance: Object Detection, Text Reading, and Sign-to-Speech**  
  The project supports three major assistive capabilities: identifying physical objects, recognizing and reading printed or digital text, and enabling communication between the visually impaired and mute individuals through gesture recognition. These three core functions make the system a versatile tool for a variety of real-life scenarios—like walking through public spaces, reading signage or documents, and engaging in meaningful communication. By addressing several key challenges at once, the system becomes an all-in-one accessibility aid.

- **Enable Seamless Hands-Free Control via Voice Commands**  
  To enhance usability, the system features a robust voice command module. The user can trigger various functions by speaking simple predefined phrases such as “read text,” “identify object,” or “translate sign.” This voice-controlled interface eliminates the need for physical buttons or touchscreens, which can be inconvenient or inaccessible for some users. It also ensures a seamless, intuitive interaction flow that adapts to the user’s pace and preferences.

- **Ensure Wearability, Comfort, and Daily Practicality**  
  Since the device is designed to be worn throughout the day, a key objective was to ensure it is both lightweight and comfortable. The hardware components—camera, Raspberry Pi, microphone, and battery—are integrated neatly into a soft, adjustable headband. The entire system is designed to be non-intrusive and user-friendly so that it can be worn in various indoor and outdoor environments without hindrance.

- **Support Multilingual Functionality for Inclusive Access**  
  Recognizing the diversity of potential users, the system includes multilingual support for both text reading and voice output. This ensures that users from different linguistic backgrounds can understand the feedback and interact with the device in their native language. The voice bot can even slow down speech or repeat outputs if the user has difficulty understanding, further improving clarity and accessibility.

- **Facilitate Communication with Mute Individuals Through Sign Language Recognition**  
  One of the most impactful objectives is enabling visually impaired users to understand mute individuals through the "Sign to Speech" module. This feature uses a custom-built dataset of sign language symbols. When a mute individual performs a gesture in front of the camera, the system recognizes the symbol and speaks out the meaning to the blind user. This fosters a new channel of communication between differently-abled individuals.

Together, these objectives define a comprehensive, human-centered solution aimed at breaking down communication and navigation barriers for the visually impaired, ultimately promoting independence, inclusivity, and confidence.


## Modules Overview

**1. Object Detection Module**
![image](https://github.com/user-attachments/assets/aa5d020d-5979-49a8-aeff-273b88aa9e7f)

The Object Detection Module is responsible for identifying and categorizing the various objects in the user's environment and conveying this information in real-time through audio feedback. At the heart of this module lies a camera integrated into the wearable headband, which continuously captures visual data. The captured video frames are processed by the Raspberry Pi using pre-trained object detection models such as YOLO (You Only Look Once) or MobileNet SSD, which are optimized for real-time performance on edge devices.

The system is trained to recognize commonly encountered objects like vehicles, furniture, street signs, pedestrians, doors, staircases, and other environmental elements that are relevant to daily navigation. Upon identification, the object label is translated into a voice message that is relayed to the user through Bluetooth earpods.

This module helps users avoid obstacles, locate specific items, and maintain spatial awareness. It significantly boosts confidence in unfamiliar settings, enabling a more independent lifestyle. It also supports custom object training, allowing the user to add unique or personal items to the detection dataset for a more tailored experience.

The primary goals of this module include:

Enhancing navigation in indoor and outdoor environments.

Alerting users of immediate obstacles or hazards.

Informing users of useful items or infrastructure around them.

The integration of real-time processing and audio delivery makes this module both practical and efficient for visually impaired individuals navigating dynamic environments.

**2. Text Recognition (OCR) Module**
![image](https://github.com/user-attachments/assets/008795bf-620a-4b55-9997-c8b3037c2ffa)
The Text Recognition Module, powered by Optical Character Recognition (OCR), allows the system to read textual content from the user’s surroundings. This could include printed documents, signboards, digital screens, or product labels. A real-time video feed from the headband's camera is used to scan text in various fonts, sizes, and backgrounds.

Using OCR libraries like Tesseract OCR, the system extracts the text from the captured image and processes it into structured data. This data is then passed to a Text-to-Speech (TTS) engine, which converts it into spoken words and delivers it to the user via the audio system.

A significant feature of this module is its multilingual capability. Users can configure the system to detect and read out text in their preferred language, making it globally accessible. The audio output can be slowed down or repeated upon request, catering to users with varying comprehension speeds.

Real-world applications include:

Reading street or store signs.

Interpreting menus, instructions, or event flyers.

Scanning and reading printed documents or books.

By making printed and digital text accessible through sound, this module bridges the gap between static visual information and auditory accessibility.

**3. Sign to Speech Module**
![image](https://github.com/user-attachments/assets/d88a1d33-5016-4444-8a41-44424466ec65)
The Sign to Speech Module introduces a novel form of inclusive communication by enabling interaction between a visually impaired user and a mute person who relies on sign language. This module uses gesture recognition to interpret hand signs shown by the non-verbal individual and convert them into spoken words for the visually impaired listener.

The camera integrated into the wearable device captures the gestures performed in front of it. These visual inputs are processed using machine learning algorithms hosted on the Raspberry Pi. The captured sign is then compared with a custom-built dataset that contains a predefined set of sign language symbols. If a match is found, the corresponding meaning is retrieved and converted into speech using the Text-to-Speech engine.

This process happens in near real-time, ensuring smooth and effective two-way communication. It is especially valuable in healthcare, educational, and social settings where communication between differently-abled individuals is essential.

Features include:

Custom dataset tailored to commonly used signs.

Real-time gesture recognition.

Multilingual speech output for global usability.

This module represents a significant step toward truly inclusive design by connecting two user groups—visually impaired and mute—through intelligent vision and voice technologies.

**4. Voice Command Module**
![image](https://github.com/user-attachments/assets/3ab8734e-259b-4024-b79e-f38bdd9d97f8)
The Voice Command Module serves as the primary user interface for controlling the device in a hands-free manner. This module is essential for ease of use, particularly for individuals who may also have motor impairments. Users can activate specific modules or request actions by speaking simple commands, such as "detect object," "read text," or "repeat message."

Upon detecting a voice input, the system uses Natural Language Processing (NLP) to interpret the command and initiate the corresponding function. The voice bot integrated within the system enhances user engagement by:

Responding only when prompted, preserving battery life and reducing unnecessary feedback.

Offering multilingual responses, allowing users to operate the device in their preferred language.

Slowing down speech if the output is unclear.

Repeating the audio response on user request for better clarity.

This module ensures that users can control all aspects of the device without the need for physical interaction. The flexible command structure and natural responses make the device highly intuitive. The system can recognize a variety of accents and dialects, and is trained to filter background noise for clearer voice recognition, even in crowded or noisy environments.

The hands-free functionality provided by the voice command module is crucial for maintaining user autonomy and comfort in diverse usage scenarios.

**5. Audio Feedback Module**

The Audio Feedback Module is the final layer of interaction in the system, responsible for delivering processed information to the user in an accessible and understandable format. Once data from other modules—like object detection, OCR, or sign recognition—is processed, this module converts it into audio output using a Text-to-Speech (TTS) engine.

The output is delivered through Bluetooth-connected earpods to ensure a private and distraction-free experience. The TTS system supports multiple languages and can adjust speech rate and tone based on the user’s preferences. For example, users can command the bot to slow down, repeat a message, or switch language if required.

The real-time nature of the feedback is essential. Delays can lead to disorientation or missed information, especially in dynamic environments. Therefore, this module is optimized for speed and clarity, ensuring minimal latency and high accuracy.

Key highlights:

Clear, real-time voice feedback for all visual inputs.

Support for multiple languages and user-controlled playback settings.

Integrated with user commands for on-demand repetition or clarification.

This module is what brings the entire system together, acting as the user’s window to the world through sound. It ensures that information is not only gathered and processed but also effectively communicated to the user in a way that is useful, reliable, and comfortable.

By integrating intuitive audio output with smart detection systems, this module serves as the final but most crucial step in ensuring full accessibility and independence for visually impaired individuals.

   ## Technologies Used

- **Hardware**:
  - Raspberry Pi
    ![image](https://github.com/user-attachments/assets/02639902-98b6-4214-bd0d-911fbeeae9a9)
  - Compact USB Camera
    ![image](https://github.com/user-attachments/assets/51347260-4084-4351-9237-386cd6d57770)
  - Bluetooth Ear Pod
    ![image](https://github.com/user-attachments/assets/d400ff84-6673-474c-ad25-3ff8503c5942)
  - USB Type-B Cable
    ![image](https://github.com/user-attachments/assets/6e29efeb-6438-47e7-9441-211725f73065)
  - Camera Connection Wire
    ![image](https://github.com/user-attachments/assets/a3f35005-9cce-4781-a00b-ea5605766ef2)


- **Software & Libraries**:
  - Python
  - OpenCV
  - TensorFlow / Keras
  - Tesseract OCR
  - SpeechRecognition
  - Pyttsx3 (Text-to-Speech)
 

## 🛠 Installation & Setup

Setting up the **Blindness Assistive Audio Vision System** involves a combination of software installation and hardware configuration. The following step-by-step instructions will help you clone the project, install required libraries, connect hardware components, and run the application successfully.


## Clone the GitHub Repository

To begin, clone the project repository onto your Raspberry Pi (or development system if testing without hardware):
git clone https://github.com/GnaneshCharlin/blind-assistive-audio-vision.git
cd blind-assistive-audio-vision
This command creates a local copy of the project folder where all the necessary code and configurations are stored.

## Install Required Dependencies
The project depends on several Python libraries for image processing, speech synthesis, OCR, and voice recognition. All the required libraries are listed in the requirements.txt file.
Run the following command to install them:
pip install -r requirements.txt
Make sure your Python environment is up to date. It's recommended to use Python 3.7 or higher. Some key dependencies include:

OpenCV (cv2) – For image capture and processing.

pytesseract – For Optical Character Recognition (OCR).

pyttsx3 or gTTS – For converting text into speech.

speechrecognition – To interpret user voice commands.

numpy, imutils – Supporting libraries for processing.

If Tesseract-OCR is not installed on your system, make sure to install it using:
sudo apt-get install tesseract-ocr

## Connect Hardware Components
Now that the software is installed, let’s connect the hardware. The system consists of the following components:
Raspberry Pi (Model 3B+ or later)

USB or Pi-compatible camera

Bluetooth-enabled earpods

Custom wearable headband (for real-time use)

**Follow these steps:**

📷 Attach Camera
Connect your USB webcam to the USB port on the Raspberry Pi. If you're using the Raspberry Pi camera module, ensure the ribbon cable is inserted properly into the Pi's camera slot and enabled in raspi-config.
sudo raspi-config
# Go to Interface Options → Enable Camera
🎧 Pair Bluetooth Earpod
Make sure your Raspberry Pi supports Bluetooth. Run the following to pair your Bluetooth device:
bluetoothctl
scan on
pair <device-mac-address>
connect <device-mac-address>
trust <device-mac-address>
Make sure that audio output is directed to your Bluetooth device.

**Headband Setup**
Carefully mount the Raspberry Pi and camera onto the soft headband. Ensure the camera faces outward and remains stable during user movement. Secure the earpods for comfortable wear.

## Run the Application
Once everything is set up, launch the main script:
python main.py
This command initiates the core program, which activates the camera, loads the trained models, initializes speech engines, and listens for voice commands.

At this point, the device is ready to interpret its environment and deliver audio feedback.

**Usage Instructions**
Using the device is simple and intuitive. Here's how you interact with it during real-time operation.

**Step 1: Power On**
Ensure your Raspberry Pi is powered on and connected to a power bank or power adapter. Boot into the system and navigate to the project directory.

**Step 2: Voice Command Activation**
Once the main.py script is running, you can interact with the device using simple voice commands. These trigger the respective modules.

 **Supported Commands:**
"read text" – Activates the Text Recognition (OCR) Module.

"identify object" – Triggers the Object Detection Module.

"start communication" – Initiates the Sign to Speech Module.

"repeat message" – Repeats the last audio output.

"speak slowly" – Slows down the voice output speed.

"change language" – Switches to another supported language (if configured).

"stop" – Terminates current operation or ends the session.

**Step 3: Continuous Usage**
The system runs in a loop, listening and responding to commands as per the user's request.

Audio feedback is delivered via the connected Bluetooth earpods.

The bot only responds when activated by voice, reducing unnecessary noise and preserving energy.

**Multilingual Support**
The system supports multilingual output for both scanned text and verbal messages. Make sure your configuration file or script enables the required language setting (en, ta, hi, etc.).

For multilingual OCR, update the Tesseract language model during installation:
sudo apt-get install tesseract-ocr-tam tesseract-ocr-hin  # Tamil, Hindi
🤝 How to Contribute
We welcome all contributors who want to improve this system or extend its capabilities.

If you’d like to contribute:

**Steps to Contribute**
Fork this repository to your GitHub account.
Clone the forked repository locally:
git clone https://github.com/your-username/blind-assistive-audio-vision.git
cd blind-assistive-audio-vision

**Create a new branch:**
git checkout -b feature-branch-name
Make your changes, and commit:
git commit -m "Added new feature or fixed bug"

**Push your changes:**
git push origin feature-branch-name
Open a Pull Request (PR) from your fork on GitHub, clearly explaining:

What you’ve changed.

Why you made the change.

How it improves the project.

**Contribution Guidelines**
Ensure code is clean and well-documented.

Follow the existing naming conventions and modular structure.

Include test cases or usage examples if applicable.

Don't forget to update the README if you introduce a new module or dependency.

**Areas Where You Can Help**
Add new gesture recognition models for more signs.

Improve multilingual support.

Optimize object detection for low-light conditions.

Add hardware alternatives like AI camera modules.

Create a mobile app version to control the device remotely.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact & Team

For any questions or feedback, please reach out to our team:

- **Gnanesh Charlin A**  
  Email: gnanesh1charlin2@gmail.com  
  GitHub: [GnaneshCharlin](https://github.com/GnaneshCharlin)  
  LinkedIn: [linkedin.com/in/gnaneshcharlin](https://www.linkedin.com/in/gnaneshcharlin)

- **Maadhavan M**
  Email: madeepika001@gmail.com
- **Ashraf Sheriff A**
  Email: aasharafsheriff@gmail.com
  
**Feel free to contact any of us regarding the project!**







