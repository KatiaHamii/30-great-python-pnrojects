import re
from collections import Counter
from PyPDF2 import PdfReader

def extract_file_path(file: list[str] ) -> list[str]:
    with open(file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        print(len(reader.pages))
        pdf_text:list[str] = [words.extract_text() for words in reader.pages]
        print(pdf_text)

        return pdf_text

def count_words(words: list[str]) -> Counter:
    all_words: list[str] = []
    for text in words:
        split_text:list[str] = re.split(r'\s+[,;?!_]\s*', text.lower())

        all_words += [word for word in split_text if word]
        print(all_words)
        return Counter(all_words)





def main():
    text: str = extract_file_path('sample.pdf')
    counter:Counter = count_words(text)
    for word, freq in counter.most_common():
        print(f'{word:10} : {freq} times')

if __name__ == '__main__':
    main()
