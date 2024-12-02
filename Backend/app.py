from flask import Flask, request, jsonify
import os
import subprocess
import cv2
from pathlib import Path
import torch

# Initialize Flask app
app = Flask(__name__)

# Paths to models and output directories
GFPGAN_PATH = "backend/models/GFPGAN"
CODEFORMER_PATH = "backend/models/CodeFormer"
MODEL_DIR = "backend/models"
UPLOADS_DIR = "backend/uploads"
ENHANCED_DIR = os.path.join(UPLOADS_DIR, "enhanced_faces")
RESTORED_DIR = os.path.join(UPLOADS_DIR, "restored_faces")

# Ensure necessary directories exist
Path(ENHANCED_DIR).mkdir(parents=True, exist_ok=True)
Path(RESTORED_DIR).mkdir(parents=True, exist_ok=True)

# Face Extraction (RetinaFace)
@app.route('/extract-faces', methods=['POST'])
def extract_faces():
    data = request.json
    frames_directory = data.get("frames_directory", "")
    confidence_threshold = data.get("confidence_threshold", 0.5)
    padding = data.get("padding", 0.2)

    # Extract faces with RetinaFace (implement your function here or use pre-existing code)
    face_count = extract_faces_retina(frames_directory, confidence_threshold, padding)
    return jsonify({"faces_extracted": face_count})

# Face Enhancement (GFPGAN)
@app.route('/enhance-faces', methods=['POST'])
def enhance_faces():
    data = request.json
    input_directory = data.get("input_directory", "")
    
    subprocess.run([
        "python", f"{GFPGAN_PATH}/inference_gfpgan.py",
        "-i", input_directory,
        "-o", ENHANCED_DIR,
        "-v", "1.3",
        "-s", "2"
    ])
    enhanced_faces = len(os.listdir(ENHANCED_DIR))
    return jsonify({"enhanced_faces": enhanced_faces, "output_directory": ENHANCED_DIR})

# Face Restoration (CodeFormer)
@app.route('/restore-faces', methods=['POST'])
def restore_faces():
    data = request.json
    input_directory = data.get("input_directory", ENHANCED_DIR)  # Use enhanced faces as input

    subprocess.run([
        "python", f"{CODEFORMER_PATH}/inference_codeformer.py",
        "-w", "0.7",
        "-s", "1",
        "--input_path", input_directory,
        "--output_path", RESTORED_DIR
    ])
    restored_faces = len(os.listdir(RESTORED_DIR))
    return jsonify({"restored_faces": restored_faces, "output_directory": RESTORED_DIR})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
