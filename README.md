# Plate_Track_Reading

## License Plate Recognition System

This Python program is a **License Plate Recognition System** built using **PyQt5** for the user interface, **OpenCV** for image processing, **YOLOv8** for object detection, and **Tesseract** for Optical Character Recognition (OCR). The system detects vehicles and license plates in video streams and then extracts the text from the plates.

### Key Components:

1. **Custom YOLOv8 Model**:
   - License plate detection is performed using a custom-trained YOLOv8 model (`last.pt`). This model was specifically trained to detect license plates in vehicle images or video streams.

2. **Video Feed Integration**:
   - The program processes a video feed (`Plaka Video.mp4`) using **OpenCV** and displays it in real-time within the PyQt5 interface.
   - A **QTimer** is used to continuously update the video frames and detect both vehicles and license plates.

3. **Vehicle Detection**:
   - Vehicles are detected in the lower half of each video frame using the YOLOv8 model (`yolov8n.pt`).
   - When a vehicle is detected, a bounding box is drawn around it, and the vehicle image is displayed in the interface.

4. **License Plate Detection**:
   - After detecting a vehicle, the program uses the **custom-trained YOLOv8 model** (`last.pt`) to detect the license plate on the vehicle.
   - The detection is performed with a confidence threshold of 50% (`conf=0.5`).

5. **OCR (Optical Character Recognition)**:
   - The detected license plate region is processed using **Tesseract OCR** to read the license plate text.
   - The plate image is pre-processed with grayscaling, thresholding, and filtering to improve OCR accuracy.
   - The OCR uses a configuration that restricts results to alphanumeric characters (`tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`).

6. **Displaying Results**:
   - The detected vehicle and license plate are displayed on the interface. Bounding boxes are drawn around both the vehicle and the license plate.
   - The recognized license plate text is displayed in a table for easy reference.

7. **Interactive GUI**:
   - The GUI includes buttons for **Start**, **Stop** the video feed, and a button for **Detecting Plates** from the vehicle image displayed in the center of the interface.
   - License plate detection is triggered by pressing the "Plaka Tespiti" button, and the recognized plate text is shown in the table if detected.

This system combines real-time vehicle and license plate detection using a custom YOLO model with Tesseract for OCR, making it ideal for automated vehicle monitoring, traffic management, or parking systems.
