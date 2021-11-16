from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import os

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection


app = Flask(__name__)
cap = cv2.VideoCapture(0)
cap.release()

def gen_frames_student():
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.75) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty cap frame.")
                continue
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Draw the face mesh annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    print(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
                    mp_drawing.draw_detection(image, detection)
            image = image[90:631, 160:1121]
            ret, buffer = cv2.imencode('.jpg', cv2.flip(image, 1))
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def gen_frames_admin():
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.75) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty cap frame.")
                continue
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Draw the face mesh annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    print(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
                    mp_drawing.draw_detection(image, detection)
            ret, buffer = cv2.imencode('.jpg', cv2.flip(image, 1))
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def gen_frames_position():
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.75) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty cap frame.")
                continue
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Draw the face mesh annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    p = mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.NOSE_TIP)
                    nose = (int(1280*p.x), int(720*p.y))
                    print(nose)
                    mp_drawing.draw_detection(image, detection)
                    image = cv2.arrowedLine(image, nose, (640, 360), (0, 255, 0), 5) 
            ret, buffer = cv2.imencode('.jpg', cv2.flip(image, 1))
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def free_webcam():
    if cap.isOpened():
        cap.release()

@app.route('/')
@app.route('/index')
def index():
    free_webcam()
    return render_template('index.html')

@app.route('/video_student')
def video_student():
    return render_template('video_student.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/video_student_position')
def video_student_position():
    return render_template('video_student_position.html')

@app.route('/video_admin')
def video_admin():
    return render_template('video_admin.html')


@app.route('/video_feed_student')
def video_feed_student():
    return Response(gen_frames_student(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_student_position')
def video_feed_position():
    return Response(gen_frames_position(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_admin')
def video_feed_admin():
    return Response(gen_frames_admin(), mimetype='multipart/x-mixed-replace; boundary=frame')

registry = os.path.join('static', 'Images')

if __name__ == '__main__':
    app.run(debug=True)