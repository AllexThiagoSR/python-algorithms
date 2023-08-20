def is_palindrome_iterative(word: str):
    reversed_word = word.replace('', ' ').split()
    reversed_word.reverse()
    if len(word) < 1:
        return False
    return "".join(reversed_word).lower() == word.lower()


if __name__ == '__main__':
    print(is_palindrome_iterative(''))
