import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import re
from langdetect import detect
from webdriver_manager.chrome import ChromeDriverManager

def recommend_job(area_lists = []):

    options = Options()
    # options.add_argument('--headless')  # Add any other options you need

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    main_data=[]

    for area in area_lists:

        # PART 1
        url = "https://www.simplyhired.ca/search?q=" + area + "&l=Canada"
        driver.get(url)

        html_content = driver.page_source


        # PART 2
        soup = BeautifulSoup(html_content, 'html.parser')
        job_divs = soup.find_all('div', {'data-jobkey': True})
        job_keys = []

        for job_div in job_divs:
            job_key = job_div['data-jobkey']
            job_keys.append(job_key)

        print(job_keys[0:1])

        #PART 3
        for job_url in job_keys[0:10]:
            job_url = "https://www.simplyhired.ca/job/" + job_url
            driver.get(job_url)
            print(job_url)
            html_content = driver.page_source

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')


            # Extract Company Name if available
            company_name = None
            company_name_container = soup.find('div', {'data-testid': 'viewJobCompanyDetailsContainer'})
            if company_name_container:
                company_name_list = company_name_container.find_all('span', {'data-testid': 'viewJobCompanyName'})
                company_name = [item.text.strip() for item in company_name_list]
                
        #Extract Title     
            title = None
            title_container = soup.find('div', {'data-testid': 'viewJobHeadingContainer'})
            if title_container:
                title_list = title_container.find_all('h1', {'data-testid': 'viewJobTitle'})
                title = [item.text.strip() for item in title_list]
            
            
            # Extract Job location
            job_location_container = soup.find('span', {'data-testid': 'viewJobCompanyLocation'})
            job_location_list = job_location_container.find_all('span') if job_location_container else []
            job_location = next((item.text.strip() for item in job_location_list if item.text.strip()), None)  # Get the first non-empty location
                
                
                    # Initialize job_type to None
            job_type = None

            # Find job details container if available
            job_type_container = soup.find('div', {'data-testid': 'viewJobBodyJobDetailsContainer'})
            if job_type_container:
                # Try to find the job type tag within the container
                jobtype_tag = job_type_container.find('span', {'data-testid': 'detailText'})
                if jobtype_tag:
                    # If job type tag is found, extract its text
                    job_type = jobtype_tag.get_text().strip()
            
            
                    # Extract salary if available
            salary = None
            salary_list = soup.find('span', {'data-testid': 'viewJobBodyJobCompensation'})
            if salary_list:
                salary_element = salary_list.find('span', {'data-testid': 'detailText'})
                if salary_element:
                    salary = salary_element.text.strip()
                    
                    
                    # Initialize qualifications to an empty list
            qualifications = []

            # Find qualifications container if available
            qualifications_container = soup.find('div', {'data-testid': 'viewJobQualificationsContainer'})
            if qualifications_container:
                # Try to find all qualifications items within the container
                qualifications_list = qualifications_container.find_all('span', {'data-testid': 'viewJobQualificationItem'})
                # Iterate over each qualification item and extract its text
                qualifications = [item.text.strip() for item in qualifications_list]

            qualifications_str = ', '.join(qualifications)

    #         # Extract Full Job Description

                # Initialize full_job_description to an empty string
            full_job_description = ""

            # Find job description container if available
            job_description_container = soup.find('div', {'data-testid': 'viewJobBodyJobFullDescriptionContent'})
            if job_description_container:
                # Try to extract the text of the job description container
                full_job_description = job_description_container.text.strip()
                # Clean the job description by removing quotation marks
                full_job_description = re.sub(r'"', '', full_job_description)

            
            # Display the extracted information
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
           
            # Create a dictionary with the extracted details
        
            data = {
                'Job Title': [title],
                'Company Name': [company_name],
                'Job Type':[job_type],
                'Job Location': [job_location],
                'Salary': [salary],
                'Qualifications':[qualifications_str],
                'Job Description':[full_job_description],
                'Job URL': [job_url]
            
            }
        

            main_data.append(data)
    driver.quit()

    df = pd.DataFrame(main_data)
    # time.sleep(30)

    if main_data != []:
       return process_dataframe(main_data)
    else: 
        return []

def process_dataframex(main_data):
    print(main_data)

# Function to clean text
def clean_text(text):
    # Remove non-alphanumeric characters except for commas and periods
    text = re.sub(r'[^a-zA-Z0-9,. ]', '', str(text))  # Ensure text is converted to string
    return text

def remove_numbers(text):
    return re.sub(r'\d+', '', str(text))


# Function to detect language
def detect_language(text):
    try:
        return detect(text)
    except:
        return None


custom_stopwords = set(text.ENGLISH_STOP_WORDS)

# Define custom tokenizer function with stopwords, hyphens, commas, and numbers removal
def custom_tokenizer(text):

    # Remove numbers, stopwords, hyphens, and commas
    tokens = re.findall(r'\b[A-Za-z]+\b', text.lower())
    return [token for token in tokens if token not in custom_stopwords]


def process_dataframe(main_data):
    df = pd.DataFrame(main_data)

    if main_data != None or main_data != []:
        # Cleaning each column in the DataFrame
        for col in df.columns:
            df[col] = df[col].apply(clean_text)

        

        # Apply the function to each element in the DataFrame
        df["Company Name"] = df["Company Name"].apply(remove_numbers)

        
        # Apply language detection to each row in the DataFrame
        df['Language'] = df['Job Description'].apply(detect_language)

        # Filter out rows where French is detected
        df = df[df['Language'] != 'fr']

        # Remove the 'Language' column if not needed anymore
        df = df.drop(columns=['Language'])

        df.reset_index(drop=True, inplace=True)

        print("DataFrame after removing rows with French text:")
        

        # Calculate TF-IDF scores for bigrams with custom tokenizer for each qualification
        important_bigrams_list = []
        for qualification in df['Job Description']:
            # Check if the qualification contains any meaningful content
            if not re.findall(r'\b[A-Za-z]+\b', qualification):
                important_bigrams_list.append([])  # Append an empty list
                continue

            tfidf_vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, ngram_range=(2, 2))
            tfidf_matrix = tfidf_vectorizer.fit_transform([qualification])
            feature_names = tfidf_vectorizer.get_feature_names_out()

            # Map feature names to their corresponding TF-IDF scores
            word_scores = {}
            for word, score in zip(feature_names, tfidf_matrix.toarray()[0]):
                word_scores[word] = score

            # Sort bigrams by their TF-IDF scores
            sorted_bigrams = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)

            # Extract top 10 most important bigrams
            top_bigrams = [bigram for bigram, score in sorted_bigrams[:10]]
            important_bigrams_list.append(top_bigrams)

        # Create a new column in the DataFrame with the important bigrams
        df['Important Bigrams'] = important_bigrams_list

        data = {
            "Important Bigrams": [important_bigrams_list]
        }

        main_data.append(data)

        # df_final = df[['Job Title', 'Company Name', 'Qualifications', 'Important Bigrams']]
        # final_list = []

        # final_list.append(df_final)
        # print(main_data + final_list)

        return main_data