import time

def tfidf_rec(user_job_title, user_category, user_qualifications):
    import pickle
    import os
    import pandas as pd
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.decomposition import TruncatedSVD

    # Record start time
    start_time = time.time()
    
    absolute_path = os.path.join(os.getcwd(), "modules/tfidf_data.pkl")
    absolute_pat1h = os.path.join(os.getcwd(), "modules/data.pkl")
    
    with open(absolute_path, 'rb') as f:
        tfidf_vectorizer_job_title, tfidf_vectorizer_category, tfidf_vectorizer_qualifications, combined_tfidf_matrix = pickle.load(f)

    user_input_vector_job_title = tfidf_vectorizer_job_title.transform([user_job_title])
    user_input_vector_category = tfidf_vectorizer_category.transform([user_category])
    user_input_vector_qualifications = tfidf_vectorizer_qualifications.transform([user_qualifications])

    user_input_combined = np.concatenate((user_input_vector_job_title.toarray(),
                                          user_input_vector_category.toarray(),
                                          user_input_vector_qualifications.toarray()), axis=1)

    
    svd = TruncatedSVD(n_components=100)
    combined_tfidf_matrix = svd.fit_transform(combined_tfidf_matrix)
    user_input_combined = svd.transform(user_input_combined)

    
    similarity_scores = cosine_similarity(user_input_combined, combined_tfidf_matrix)

  
    unpickled_df = pd.read_pickle(absolute_pat1h)  

    N = 10
    
    top_n_indices = np.argsort(similarity_scores, axis=1)[:, -N:][0]
    top_n_similarity_scores = similarity_scores[0, top_n_indices]
    sorted_indices = np.argsort(top_n_similarity_scores)[::-1]  # Sort indices in descending order of similarity scores
    sorted_top_n_indices = top_n_indices[sorted_indices]
   
    unique_titles = set()
    recommended_jobs = []
    for i in sorted_top_n_indices:
        job_title = unpickled_df.loc[i]['Job Title'].strip("'")
        if job_title not in unique_titles:
            unique_titles.add(job_title)
            # Round similarity score to two decimal places
            rounded_score = round(similarity_scores[0][i], 2)
            recommended_jobs.append((rounded_score, job_title))
    
    # Record end time
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution Time: {:.2f} seconds".format(end_time - start_time))
    return recommended_jobs
