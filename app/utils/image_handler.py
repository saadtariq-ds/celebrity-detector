"""
Image Handler Utility Functions

This module provides utility functions for processing images,
including face detection and annotation using OpenCV.
"""

import cv2
import numpy as np
from io import BytesIO

def process_image(image_file):
    """ 
    Process an uploaded image file by detecting the 
    largest face and drawing a bounding box around it. 
    
    - Args:
        image_file (FileStorage or similar object): 

    - Returns:
        - bytes: Encoded image bytes with bounding box (JPEG format).
            - tuple or None: Coordinates of the largest detected face 
              in the format (x, y, w, h). Returns None if no face is detected.
    """
    # Create an in-memory buffer to store image bytes
    in_memory_file = BytesIO()
    image_file.save(in_memory_file)

    # Convert image bytes to NumPy array
    image_bytes = in_memory_file.getvalue()
    numpy_array = np.frombuffer(image_bytes, np.uint8)

    # Decode the image from NumPy array to OpenCV format
    img = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)

    # Convert image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     # Load Haar Cascade model for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray,1.1,5)

    # If no faces are detected, return original image and None
    if len(faces)==0:
        return image_bytes,None
    
    # Select the largest detected face (by area)
    largest_face = max(faces,key=lambda r:r[2] *r[3])
    (x,y,w,h) = largest_face

    # Draw a green bounding box around the detected face
    cv2.rectangle(img, (x,y),(x+w , y+h) , (0,255,0),3 )

    # Encode the processed image back to JPEG format
    is_sucess , buffer = cv2.imencode(".jpg" , img)

    return buffer.tobytes(), largest_face