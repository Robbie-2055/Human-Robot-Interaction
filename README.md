#NAO Tutor Study Buddy Robot

This project leverages the NAO robot to serve as a Study Buddy, enhancing learning through interactive flashcards. The system integrates the NAO robot with a Flask application hosting a database of questions and answers. Users can select a subject area, and the robot retrieves flashcards through a URL provided by the Flask app, offering a dynamic learning experience.

##Features
1.	Interactive Learning: The NAO robot generates and presents flashcards.
2.	Dynamic Flashcards: Questions and answers are pulled from a centralized database.
3.	Flask Backend: A lightweight web application manages the database and serves data via HTTP requests.
4.	User-Friendly Interface: Select subject areas and receive curated flashcards.

##Prerequisites
1.	Python IDE
2.	SQLite or another database management system
3.	Choregraphe software


##Steps
1.	Download all the files in the folder above
2.	Extract the contents of the folder and keep in the same file
3.	Open the flask APP python file
4.	Ensure that location of the database in the flask APP matches the location of the database on your PC
5.	Run the flask APP. A URL should be generated 
6.	Open the choreographe file
7.	Open each box for each subject and ensure that the URL for each subject matches that generated by the FLASK APP should end  /data
8.	Run the choreographe project and have fun

##Usage
1.	Select a Topic:
o	Choose a subject area for flashcard generation via the NAO robot interface.
2.	Generate Flashcards:
o	The system retrieves relevant questions and answers from the database hosted on the flask APP 
3.	Interactive Learning:
o	The robot presents the flashcards and engages the user with questions, answers, and hints.
4.	Review and Feedback:
o	Users can review their performance and receive suggestions for improvement.


##Development Workflow
Key Components:
1.	Flashcard Generator:
o	Q&A’s are resourced from a database hosted on Flask APP
2.	NAO Robot Programming:
o	Interactive dialogue and movement programming in Choregraphe.
3.	Database Management:
o	Stores flashcard data for efficient access and retrieval.


