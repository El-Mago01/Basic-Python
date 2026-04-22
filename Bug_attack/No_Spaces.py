def text_with_no_spaces(sentence):
    new_text = ""
    for char in sentence:
        if char != ' ':
            new_text += char
    return new_text


text = "New Document"
print(text_with_no_spaces(text))