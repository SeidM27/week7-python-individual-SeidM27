# Project 4 — Word Counter
# Author: Seid Mamuti

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# TODO: total word count using len()

# TODO: character count (no spaces)
# Hint: sentence.replace(" ", "") removes all spaces, then use len()

# TODO: word frequency dictionary
# frequency = {}
# for word in words:
#     ...

# TODO: print total words, total characters, then word frequency
# Project 4 - Word Counter
# Author: Seid Mamuti
sentence = input("Enter a sentence: ")
# Convert to lowercase and split into words
words = sentence.lower().split()
# Count total words
total_words = len(words)
# Count characters excluding spaces
total_characters = len(sentence.replace(" ", ""))
# Build word frequency dictionary
frequency = {}
for word in words:
if word in frequency:
frequency[word] += 1
else:
frequency[word] = 1
# Print results
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_characters}")
print("Word frequency:")
for word, count in frequency.items():
print(f" {word:<5} -> {count}")
