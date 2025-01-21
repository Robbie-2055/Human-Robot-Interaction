# NAO Tutor Study Buddy Robot

This project leverages the NAO robot to serve as a Study Buddy, enhancing learning through interactive flashcards. The system integrates the NAO robot with a Flask application hosting a database of questions and answers. Users can select a subject area, and the robot retrieves flashcards through a URL provided by the Flask app, offering a dynamic learning experience.

![IMG_6621](https://github.com/user-attachments/assets/4b5eff49-567b-4ffc-ac91-37e861bf9b7e)


## Features
1.	Interactive Learning: The NAO robot generates and presents flashcards.
2.	Dynamic Flashcards: Questions and answers are pulled from a centralized database.
3.	Flask Backend: A lightweight web application manages the database and serves data via HTTP requests.
4.	User-Friendly Interface: Select subject areas and receive curated flashcards.

## Prerequisites
1.	Python IDE
2.	SQLite or another database management system
3.	Choregraphe software


## Steps
1.	Download all the files in the folder above
2.	Extract the contents of the folder and keep in the same file
3.	Open the flask APP python file
4.	Ensure that location of the database in the flask APP matches the location of the database on your PC
5.	Run the flask APP. A URL should be generated 
6.	Open the choreographe file
7.	Open each box for each subject and ensure that the URL for each subject matches that generated by the FLASK APP should end  /data
8.	Run the choreographe project and have fun

## Usage
1.	Select a Topic:
Choose a subject area for flashcard generation via the NAO robot interface.
2.	Generate Flashcards:
The system retrieves relevant questions and answers from the database hosted on the flask APP 
3.	Interactive Learning:
The robot presents the flashcards and engages the user with questions, answers, and hints.
4.	Review and Feedback:
Users can review their performance and receive suggestions for improvement.


## Development Workflow
Key Components:
1.	Flashcard Generator:
Q&A’s are resourced from a database hosted on Flask APP
2.	NAO Robot Programming:
Interactive dialogue and movement programming in Choregraphe.
3.	Database Management:
Stores flashcard data for efficient access and retrieval.








# Face gaze Detection 

This project uses MediaPipe's Face Mesh solution to detect the gaze direction of a person. Based on the detected gaze direction, the system classifies whether the person is "Attentive" or "Distracted". This is achieved by analyzing the relative positions of key facial landmarks. This is an external project that would be used to feed information to the NAO on the learner's attention during the session

## Facial Key points
![face with key points](https://github.com/user-attachments/assets/7a697adb-bcba-4984-adce-404f14e4e96f)

## Features

1. **Real-time Face Mesh Detection:** Using the webcam, the system detects facial landmarks and estimates gaze direction.
2. **Display of Gaze Status:** The system shows "Distracted" when the person is looking away from the center (either left, right, up, or down) and "Attentive" when the person is facing forward.

## Requirements

1. Python
2. OpenCv
3. Media Pipe

## How it works

1. **Webcam Input:** The webcam is used to capture real-time video frames.
2. **Face Mesh Processing:** MediaPipe processes each frame to detect facial landmarks.
3. **Gaze Calculation:** The script checks the relative position of the nose, eyes, ,chin and cheeks to determine the gaze direction
4. **Gaze Status:** The status ("Distracted" or "Attentive") is displayed on the frame based on the gaze direction.

## Student Attention detection



https://github.com/user-attachments/assets/f24cd993-36ca-42bb-b9c6-d9fa9f262295


