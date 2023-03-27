def cesar_cypher(text, key, alf=None):
    if alf is None:
        alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    elif alf.__len__() < 2:
        return text.lower()

    new_text = ""
    text = text.lower()
    for c in text:
        if c in alf:
            cur_i = (alf.index(c) + key) % alf.__len__()
            new_text += alf[cur_i]
        else:
            new_text += c
    return new_text


print(cesar_cypher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", -47))
print(cesar_cypher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 3, ['a', 'B']))
print(cesar_cypher("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 3, 'aB'))
