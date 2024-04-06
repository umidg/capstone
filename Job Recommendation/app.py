from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Import the route handler function from recommend.py
from recommend_job import recommend_job

# Define a route for the API endpoint
@app.route('/api/job/recommend', methods=['GET'])
def route_to_recommend():
    area_lists = ['account+manager']

    return recommend_job(area_lists)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)