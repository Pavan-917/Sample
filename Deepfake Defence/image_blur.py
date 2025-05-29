import cv2
import os

def pixelate_face(image_path, output_path):
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found.")
        return

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            face_roi = img[y:y+h, x:x+w]
            # Pixelate the face region
            small = cv2.resize(face_roi, (16, 16), interpolation=cv2.INTER_LINEAR)
            pixelated_face = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
            img[y:y+h, x:x+w] = pixelated_face

    cv2.imwrite(output_path, img)

if __name__ == "__main__":
    input_path = input("Enter input image path: ")
    output_path = os.path.join(os.path.dirname(input_path), '..', 'blurred', os.path.basename(input_path))
    pixelate_face(input_path, output_path)
    print(f"Pixelated face(s) saved to {output_path}")