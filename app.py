from flask import Flask, request, jsonify
import cv2
import face_recognition
import os

app = Flask(__name__)

def find_face_encodings(image_path):
    image_path_new = os.path.join('uploads', os.path.basename(image_path))
    image = cv2.imread(image_path_new)
    if image is None:
        raise ValueError(f"Image not found or unreadable: {image_path}")
    face_enc = face_recognition.face_encodings(image)
    return face_enc[0] if face_enc else None

@app.route('/compare', methods=['POST'])
def compare_faces():
    # Save uploaded files
    image_1_file = request.files['image_1']
    image_2_file = request.files['image_2']

    image_1_path = os.path.join('uploads', image_1_file.filename)
    image_2_path = os.path.join('uploads', image_2_file.filename)

    image_1_file.save(image_1_path)
    image_2_file.save(image_2_path)
    
    try:
        image_1 = find_face_encodings(image_1_path)
        image_2 = find_face_encodings(image_2_path)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    if image_1 is None or image_2 is None:
        return jsonify({"error": "Face not found in one or both images"}), 400
    
    is_same = face_recognition.compare_faces([image_1], image_2)[0]
    
    if is_same:
        distance = face_recognition.face_distance([image_1], image_2)
        accuracy = 100 - round(distance[0] * 100)
        return jsonify({"is_same": True, "accuracy": accuracy})
    else:
        return jsonify({"is_same": False, "message": "The images are not the same"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
