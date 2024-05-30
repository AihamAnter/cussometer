# tfidf.py

from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(files):
    cuss_words_texts = []
    for text in files:
        if 'Cuss words found' in text:
            cuss_words_texts.append(text)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cuss_words_texts)
    feature_names = vectorizer.get_feature_names_out()
    return tfidf_matrix, feature_names

def calculate_tfidf_from_tokens(tokens_list):
    tfidf_matrix, feature_names = calculate_tfidf(tokens_list)
    with open('../tfidf_results.txt', 'w') as file:
        file.write("TF-IDF Matrix:\n")
        file.write(str(tfidf_matrix))
        file.write("\n\nFeature Names:\n")
        file.write('\n'.join(feature_names))