import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

# Define keypoint indices for comparison
nose_index = 1
chin_index = 152 
left_eye_index = 133
right_eye_index = 362 
left_cheek_index = 145
right_cheek_index = 374


# Functions to determine the gaze direction based on keypoint positions
def is_looking_left(nose_x, left_eye_x, left_cheek_x):
    """Determines if the person is looking left"""
    if nose_x < left_eye_x and nose_x < left_cheek_x:
        return True
    else:
        return False

def is_looking_right(nose_x, right_eye_x, right_cheek_x):
    """Determines if the person is looking right"""
    if nose_x > right_eye_x and nose_x > right_cheek_x:
        return True
    else:
        return False


def is_looking_up(nose_y, chin_y, left_eye_y, right_eye_y):
    """Determines if the person is looking up """
    # Calculate average eye y-coordinate
    avg_eye_y = (left_eye_y + right_eye_y) / 2

    # Check if nose is significantly higher than eyes and chin
    if nose_y < avg_eye_y and nose_y < chin_y:
        return True
    else:
        return False

def is_looking_down(nose_y, chin_y, left_eye_y, right_eye_y):
    """Determines if the person is looking down"""
    # Calculate average eye y-coordinate
    avg_eye_y = (left_eye_y + right_eye_y) / 2

    # Check if nose is significantly higher than eyes and chin
    if nose_y > avg_eye_y and nose_y > chin_y:
        return True
    else:
        return False


# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with Mediapipe face mesh
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            #X coordinates#
            nose_x = face_landmarks.landmark[nose_index].x
            left_eye_x = face_landmarks.landmark[left_eye_index].x + 0.05
            right_eye_x = face_landmarks.landmark[right_eye_index].x - 0.05
            left_cheek_x = face_landmarks.landmark[left_cheek_index].x + 0.05
            right_cheek_x = face_landmarks.landmark[right_cheek_index].x - 0.05

            #Y coordinates#
            nose_y_down = face_landmarks.landmark[nose_index].y + 0.15
            nose_y_up = face_landmarks.landmark[nose_index].y - 0.1
            chin_y = face_landmarks.landmark[chin_index].y 
            left_eye_y = face_landmarks.landmark[left_eye_index].y 
            right_eye_y = face_landmarks.landmark[right_eye_index].y

            

            # Determine gaze direction and display it
            if is_looking_left(nose_x, left_eye_x, left_cheek_x):
                cv2.putText(frame, "Distracted", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif is_looking_right(nose_x, right_eye_x, right_cheek_x):
                cv2.putText(frame, "Distracted", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif is_looking_up(nose_y_up, chin_y, left_eye_y, right_eye_y):
                cv2.putText(frame, "Distracted", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif is_looking_down(nose_y_down, chin_y, left_eye_y, right_eye_y):
                cv2.putText(frame, "Distracted", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Attentive", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            mp.solutions.drawing_utils.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 0), thickness=1)
            )

    # Display the resulting frame
    cv2.imshow('Face Mesh', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
