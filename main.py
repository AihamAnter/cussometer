
from text_processing import tokenize_files
from tfidf import calculate_tfidf_from_tokens

if __name__ == "__main__":
    directory_path = r'C:\Users\hebaa\PycharmProjects\pythonProject\cussometer\texts'
    tokens_list = tokenize_files(directory_path)
    calculate_tfidf_from_tokens(tokens_list)
