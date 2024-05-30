import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(cuss_words, filename):
    save_dir = "../wordclouds" #new folder name
    if not os.path.exists(save_dir): #if the folder do not exist make it
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, f"{filename.replace(".txt","")}_cuss_words_wordcloud.png")

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(cuss_words))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud of Cuss Words in {filename}')
    plt.tight_layout()
    plt.savefig(file_path, dpi=300)

