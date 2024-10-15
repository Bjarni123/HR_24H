used_words = set()

try:
    while True:
        the_input = input().strip()
        if not the_input:
            break

        sentence = []
        for word in the_input.split(' '):
            if word.lower() in used_words:
                print('.', end=' ')
            else:
                print(word, end=' ')
                used_words.add(word.lower())
        print()
except EOFError:
    pass