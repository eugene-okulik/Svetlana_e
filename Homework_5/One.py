text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

words = text.split()
new_words = []

for word in words:
    if word[-1] in {'.', ','}:
        punctuation = word[-1]
        clean_word = word[:-1]
    else:
        punctuation = ""
        clean_word = word

    new_word = clean_word + "ing" + punctuation
    new_words.append(new_word)

new_text = " ".join(new_words)
print(new_text)
