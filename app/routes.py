"""
Main Flask Routes

This module defines the main application routes for handling:
1. Image uploads for celebrity detection
2. User questions about detected celebrities
"""

from flask import Blueprint, render_template, request
import base64

from app.utils.image_handler import process_image
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.question_answering import QAEngine


# Create Flask Blueprint
main = Blueprint("main", __name__)

# Initialize service classes once (recommended for performance)
celebrity_detector = CelebrityDetector()
qa_engine = QAEngine()


@main.route("/", methods=["GET", "POST"])
def index():
    """
    Main application route.

    Handles:
    - Image upload and celebrity detection
    - Question answering about the detected celebrity

    Returns:
        Rendered HTML template with detection results and answers.
    """

    # Initialize template variables
    celebrity_information = ""
    result_img_data = ""
    user_question = ""
    answer = ""

    # Handle POST requests
    if request.method == "POST":

        # -------- IMAGE UPLOAD FLOW --------
        if "image" in request.files:
            image_file = request.files["image"]

            if image_file:
                # Process image and detect face
                img_bytes, face_box = process_image(image_file)

                # Identify celebrity from the image
                celebrity_information, celebrity_name = celebrity_detector.identify_celebrity(img_bytes)

                if face_box is not None:
                    # Encode processed image for HTML rendering
                    result_img_data = base64.b64encode(img_bytes).decode()
                else:
                    # No face detected fallback
                    celebrity_information = "No face detected. Please try another image."

        # -------- QUESTION ANSWERING FLOW --------
        elif "question" in request.form:
            # Retrieve user question and hidden form fields
            user_question = request.form["question"]
            celebrity_name = request.form["celebrity_name"]
            celebrity_information = request.form["celebrity_information"]
            result_img_data = request.form["result_img_data"]

            # Ask question about the detected celebrity
            answer = qa_engine.ask_about_celebrity(celebrity_name, user_question)

    # Render UI with updated values
    return render_template(
        "index.html",
        celebrity_information=celebrity_information,
        result_img_data=result_img_data,
        user_question=user_question,
        answer=answer
    )
