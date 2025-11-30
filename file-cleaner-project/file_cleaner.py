file = open("input.txt", "r")
text = file.read()
file.close()

cleaned_text = " ".join(text.split())
cleaned_text = cleaned_text.lower()

output = open("output.txt", "w")
output.write(cleaned_text)
output.close()

print("Text has been cleaned and saved to output.txt")