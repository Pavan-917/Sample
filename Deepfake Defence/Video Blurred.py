import cv2
import os

def pixelate_face_video(input_video_path, output_video_path):
    # Load the video
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Could not open video.")
        return

    # Get video properties
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face_roi = frame[y:y+h, x:x+w]
            # Pixelate the face region
            small = cv2.resize(face_roi, (16, 16), interpolation=cv2.INTER_LINEAR)
            pixelated_face = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = pixelated_face

        out.write(frame)

    cap.release()
    out.release()
    print(f"Pixelated video saved to {output_video_path}")

# Example usage:
# pixelate_face_video("input.mp4", "output_blurred.mp4")