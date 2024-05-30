from nltk.sentiment import SentimentIntensityAnalyzer
import os
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

def write_sentiment_analysis(filename, sentiment_scores):
    save_dir = "../syntimentAnalysis"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, f"{filename.replace(".txt", "")}_syntimentAnalysis.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"{filename} Sentiment Analysis: {sentiment_scores}\n")
