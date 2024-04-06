from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Import the route handler function from recommend.py
from PreTrainedGPT.gpt2_model_interface import generate_cover_letter
from JobRecommendation.recommend_job import recommend_job

# Define a route for the API endpoint
@app.route('/api/job/pretrained', methods=['GET'])
def route_to_pretrained():
    job_description = """
    Job Information: Generate a cover letter for Retail Sales AssociateCashier at CAA Qubec that requires Bilingual,
    Spanish, Sales, Inventory management, Customer service, Basic math, English, Organizational skills, Communication skills, 
    Retail sales as major qualifications and retail sales, sales associate, assist customers, hour hour, ability work, 
    accurately maintain, alongside management, appealing stock, apply today, assisting managing as major requirements. 
    My name is Jane Doe, my education is Bachelor's Degree in Business Administration from McGill University, Montreal,
    Quebec Graduated: May 2015  and my skills are Bilingual (English and Spanish), Sales, Inventory Management, Customer 
    Service, Basic Math, Organizational Skills, Communication Skills, Retail Sales  and my work experience is Retail Sales
    Associate at Best Buy, Montreal, Quebec (June 2015 - Present): Assisted customers with product selection and queries. 
    Managed inventory accurately and worked alongside management
    to maintain an appealing stock display. Demonstrated excellent communication and organizational skills.. 
    """
    return generate_cover_letter(job_description)

# Define a route for the API endpoint
@app.route('/api/job/recommend', methods=['GET'])
def route_to_recommend():
    area_lists = ['account+manager']

    return recommend_job(area_lists)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)