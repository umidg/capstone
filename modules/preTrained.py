# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# def generate_cover_letter(job_description):
#     # Load the fine-tuned model
#     model_path = 'modules/gpt2-local'
#     tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#     model = GPT2LMHeadModel.from_pretrained(model_path)

#     # Encode the job description and generate a cover letter
#     input_ids = tokenizer.encode(job_description, return_tensors="pt")
#     output = model.generate(input_ids, max_new_tokens=500, num_return_sequences=1, no_repeat_ngram_size=2)

#     # Decode the generated cover letter
#     generated_cover_letter = tokenizer.decode(output[0], skip_special_tokens=True)

#     # Find the index of "Sincerely" in the cover letter
#     Dear_index = generated_cover_letter.find("Dear")
#     sincerely_index = generated_cover_letter.find("Sincerely")

#     # Remove the content after "Sincerely"
#     cleaned_cover_letter = generated_cover_letter[Dear_index:sincerely_index+20]

#     # Return the cover letter as a dictionary
#     return {"cover_letter": cleaned_cover_letter}

# # job_description = """
# # Job Information: Generate a cover letter for Retail Sales AssociateCashier at CAA Qubec that requires Bilingual,
# # Spanish, Sales, Inventory management, Customer service, Basic math, English, Organizational skills, Communication skills, 
# # Retail sales as major qualifications and retail sales, sales associate, assist customers, hour hour, ability work, 
# # accurately maintain, alongside management, appealing stock, apply today, assisting managing as major requirements. 
# # My name is Jane Doe, my education is Bachelor's Degree in Business Administration from McGill University, Montreal,
# # Quebec Graduated: May 2015  and my skills are Bilingual (English and Spanish), Sales, Inventory Management, Customer 
# # Service, Basic Math, Organizational Skills, Communication Skills, Retail Sales  and my work experience is Retail Sales
# # Associate at Best Buy, Montreal, Quebec (June 2015 - Present): Assisted customers with product selection and queries. 
# # Managed inventory accurately and worked alongside management
# # to maintain an appealing stock display. Demonstrated excellent communication and organizational skills.. 
# # """
# # cover_letter = generate_cover_letter(job_description)
# # print("Generated Cover Letter:")
# # print(cover_letter)
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_cover_letter(job_description, applicant_name, company_name):
    # Load the fine-tuned model
    model_path = 'modules/gpt2-local'
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained(model_path)

    # Personalize the job description with the specific company and applicant name
    # personalized_job_description = job_description.replace("COMPANY_NAME", company_name).replace("APPLICANT_NAME", applicant_name)

    # Encode the job description and generate a cover letter
    input_ids = tokenizer.encode(job_description, return_tensors="pt")
    output = model.generate(input_ids, max_new_tokens=500, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the generated cover letter
    generated_cover_letter = tokenizer.decode(output[0], skip_special_tokens=True)

    # Find the index of "Dear" and "Sincerely" to isolate the main content of the cover letter
    Dear_index = generated_cover_letter.find("Dear")
    sincerely_index = generated_cover_letter.find("Sincerely")

    # Remove the content after "Sincerely" if it exists, otherwise use the whole letter
    if sincerely_index != -1:
        cleaned_cover_letter = generated_cover_letter[Dear_index:sincerely_index+len("Sincerely")+1]
    else:
        cleaned_cover_letter = generated_cover_letter[Dear_index:]

    # Return the cover letter as a dictionary
    return {"cover_letter": cleaned_cover_letter}

# Example usage with placeholders for job_description, applicant_name, and company_name
# cover_letter = generate_cover_letter(job_description, "Jane Doe", "Meridian Farm Market")
# print("Generated Cover Letter:")
# print(cover_letter['cover_letter'])