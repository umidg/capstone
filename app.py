import json
from flask import Flask, jsonify, request, send_from_directory, make_response
from flask_cors import CORS, cross_origin
from modules.recomendation import tfidf_rec
from modules.scrapper import recommend_job
from modules.preTrained import generate_cover_letter
import os
from modules.custom import generate_cover_letter

app = Flask(__name__)

CORS(app)

@app.route('/')
def serve_home():
    return send_from_directory('./jobbuddys/out', 'index.html')


@app.route('/api/hello', methods=['GET'])
def cover_letter():
    return "Hello from APIs"

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('./jobbuddys/out', path)

@app.route('/api/jobs', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', methods=['POST', 'OPTIONS'])
def get_employees():
    data = request.json
    job_title = data["job_title"]
    lists = recommend_job(area_lists=[job_title])
    return jsonify(lists)

@app.route('/api/cover_letter_free', methods=['POST'])
def cover_letter_generator():
    data = request.json
    name = data['full_name']
    job_title = data['job_title']
    company = data['company']
    required_qualifications = data['qualifications']
    major_requirements = data['bigrams']
    education = data['education']
    skills = data['skills']
    work_experience = data['experience']
    print(f'''Job Information: Generate a cover letter for {job_title} at {company} that requires {required_qualifications} as major qualifications and {major_requirements} as major requirements. My name is {name}, my education is {education} and my skills are {skills} and my work experience is {work_experience}...''')
    cv = generate_cover_letter(job_description=f'''Job Information: Generate a cover letter for {job_title} at {company} that requires {required_qualifications} as major qualifications and {major_requirements} as major requirements. My name is {name}, my education is {education} and my skills are {skills} and my work experience is {work_experience}...''', applicant_name=name, company_name=company)
    print(cv)
    return cv   

@app.route('/api/cover_letter_premium', methods=['POST'])
def cover_letter_generator_premium():
    data = request.json
    name = data['full_name']
    job_title = data['job_title']
    company = data['company']
    required_qualifications = data['qualifications']
    major_requirements = data['bigrams']
    education = data['education']
    skills = data['skills']
    work_experience = data['experience']
    input_prompt = f'''Job Information: Generate a cover letter for {job_title} at {company} that requires {required_qualifications} as major qualifications and {major_requirements} as major requirements. My name is {name}, my education is {education}  and my skills are {skills}  and my work experience is {work_experience}...'''
    a = generate_cover_letter(input_prompt)
    print(a,"this is a")
    return {'cover_letter':a}
     
if __name__ == '__main__':
    # app.run(port=5000)
   app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5001)))


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response