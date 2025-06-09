# Blindness Assistive Audio Vision System

The **Blindness Assistive Audio Vision System** is a smart, wearable headband designed to assist individuals with visual impairments by providing real-time audio feedback based on visual data. Developed as a compact and user-friendly prototype, the system leverages computer vision and speech technologies to translate surroundings into meaningful audio cues, enhancing independent navigation and awareness.

## Project Objectives

- Transform visual information into audio format for real-world accessibility.
- Provide real-time object detection, text reading, and communication assistance.
- Enable hands-free operation through voice command functionality.
- Design a lightweight, wearable system suitable for daily use.

## Modules Overview

1. **Object Detection Module**  
   Recognizes common objects (e.g., vehicles, furniture) and informs the user via audio feedback.

2. **Text Recognition (OCR) Module**  
   Reads text from surroundings such as signboards or printed material and converts it to speech. Supports multiple languages for both text scanning and audio playback, enhancing usability across diverse users.

3. **Sign to Speech Module**  
   Facilitates conversation between a visually impaired user and a person who cannot speak by interpreting sign language gestures. The camera captures gestures, which are processed by the Raspberry Pi using a **custom-built sign language dataset**. Recognized symbols are converted into voice notes for the blind user.

4. **Voice Command Module**  
   Enables hands-free control of the device through user voice commands. The voice bot:
   - Responds only when prompted by the user.
   - Can speak in multiple languages based on user preference.
   - If the audio output is unclear, it can slow down the speech.
   - On user request, repeats the audio output to ensure understanding.

5. **Audio Feedback Module**  
   Converts processed data into clear audio messages delivered to the user via Bluetooth earpods in real time.

   ## Technologies Used

- **Hardware**:
  - Raspberry Pi
  - Compact USB Camera
  - Bluetooth Ear Pod
  - USB Type-B Cable
  - Camera Connection Wire

- **Software & Libraries**:
  - Python
  - OpenCV
  - TensorFlow / Keras
  - Tesseract OCR
  - SpeechRecognition
  - Pyttsx3 (Text-to-Speech)
 

## 🛠 Installation & Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/blind-assistive-audio-vision.git
   cd blind-assistive-audio-vision
   
**Install dependencies**:
pip install -r requirements.txt

**Connect hardware components**:
-Attach the USB camera to the Raspberry Pi.
-Ensure Bluetooth earpod is paired.
-Position the headband securely.

**Run the application**:
-python main.py


## Usage Instructions

- **Start the device**: Power up the Raspberry Pi and run the main script.
- **Voice Commands**:
  - Say `"read text"` to activate OCR.
  - Say `"identify object"` to scan surroundings.
  - Say `"start communication"` to activate sign language recognition.
- The system will provide immediate audio responses through the Bluetooth earpod.

- ## How to Contribute

We welcome contributions to improve the Blindness Assistive Audio Vision System! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request explaining your changes.

Please ensure your code follows the project’s coding standards and includes relevant tests if applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact & Team

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







