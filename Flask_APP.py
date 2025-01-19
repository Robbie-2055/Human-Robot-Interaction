from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Database path
db_path = r'C:\Users\rokan\OneDrive\Documents\UWE-Robotics Course\Year 3\Human Robot interaction technologies\Report\FlashCards.db'

@app.route('/data', methods=['GET'])
def get_data():
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query data from the database
    cursor.execute("SELECT * FROM QuestionsAndAnswers")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert rows to a list of dictionaries or JSON-friendly format
    data = [{'id': row[0], 'question': row[1], 'answer': row[2]} for row in rows]

    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # This allows the API to be accessed on any IP



