text = "Hello, World!\nThis is chaitanya sri pattanam."
with open("output.txt", "w") as file:
    file.write(text + "\n")
    file.write(text[::-1] + "\n")

print("Text written to output.txt")