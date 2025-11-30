text = input("Enter the text to analyze: ")

total_char = len(text)

words = text.split()
word_count = len(words)

sentence_count = text.count('.') + text.count('!')+ text.count('?')

word_frequency = {}

for word in words:
    word = word.lower()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

most_common_word = max(word_frequency, key = word_frequency.get)

print("Total characters:", total_char)
print("Total words:", word_count)
print("Total sentences:", sentence_count)
print("Most common word:", most_common_word)