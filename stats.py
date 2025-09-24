def count_words(contents):
    return len(contents.split())

def count_characters(contents):
    results = {}
    for letter in contents:
        letter = letter.lower()
        if letter.isalpha():
            if not letter in results:
                results[letter] = 1
                continue
            results[letter] += 1
    return results
