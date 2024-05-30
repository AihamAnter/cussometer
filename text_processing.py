import string
import os
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from syntiment_analysis import analyze_sentiment, write_sentiment_analysis
from cussLib import profanityFilter
from wordCloud import generate_wordcloud

stop_words = set(stopwords.words('english'))

def tokenize_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)

        filtered_tokens = []
        for token in tokens:
            if token.lower() not in stop_words:
                filtered_tokens.append(token)
        print(filtered_tokens)
    return ' '.join(filtered_tokens)



def tokenize_files(directory_path):
    max_cuss_count = 0
    cuss_words_count = {}
    cussiest_file = None
    tokens_list = []


    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            tokens_list.append(filename + '\n')
            text = tokenize_text(file_path)
            tokens_list.append(text)
            sentiment_scores = analyze_sentiment(text)
            tokens_list.append(f"Sentiment Analysis: {sentiment_scores}\n")
            write_sentiment_analysis(filename, sentiment_scores)
            cuss_words, cuss_count = profanityFilter(text)

            if cuss_count > 0:
                tokens_list.append(f"Cuss words found: {cuss_words}\n")
                cuss_words_count[filename] = cuss_count
                generate_wordcloud(cuss_words, filename)

                if cuss_count > max_cuss_count:
                    max_cuss_count = cuss_count
                    cussiest_file = filename
            else:
                print("there are no cuss found")
                continue

            save_dir = "../cussUsed"

            if not os.path.exists(save_dir):  # if the folder does not exist! make it
                os.makedirs(save_dir)
            file_path = os.path.join(save_dir, f"{filename.replace(".txt", "")}_cuss_used.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"cuss words used: {cuss_words} \n Total Amount: {cuss_count} \n")

    if cussiest_file:
        save_cussiest_file_info(cussiest_file, max_cuss_count)

    if cuss_words_count:
        plot_cuss_words_count(cuss_words_count)

    return tokens_list


def save_cussiest_file_info(cussiest_file, max_cuss_count):
    with open('../cussiest_file.txt', 'w', encoding='utf-8') as file:
        file.write(f"The file with the most cuss words is: {cussiest_file}, with a total of {max_cuss_count} cuss words.")


def plot_cuss_words_count(cuss_words_count):
    plt.figure(figsize=(10, 6))
    plt.bar(cuss_words_count.keys(), cuss_words_count.values(), color='skyblue')
    plt.xlabel('File')
    plt.ylabel('Cuss Words Count')
    plt.title('Cuss Words Count in Text Files')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('../cuss_words_count.png')

