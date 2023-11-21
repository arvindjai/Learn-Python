# Create a program that takes a sentence as input and counts the number of words in it.
sentence = input("Enter any sentence: ")
list_sen = list(sentence.split())
print(list_sen)
word_count = len(list_sen)
print(f"word count in sentence is : {word_count} ")