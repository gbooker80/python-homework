import re
file = 'paragraph_1.txt'
# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:
    lines = text.read()
    words = lines.split()
    number_words = len(words)
    sentences = len(re.findall(r'\.', lines))
    letters = len(re.findall('[A-Za-z]', lines))
    average_letter_count = round((letters/number_words), 1)
    Average_Sen_Length = number_words/sentences
    print('Paragraph Analysis')
    print('------------------------------------------')
    print("Approximate Word Count: " + str(number_words) + " Words")
    print("Approximate Sentence Count: " + str(sentences) + " Sentences")
    print("Average Letter Count (Per Word): " + str(average_letter_count) + " Letters")
    print("Average Sentence Length: " + str(Average_Sen_Length) + " Words")
    print('------------------------------------------')







