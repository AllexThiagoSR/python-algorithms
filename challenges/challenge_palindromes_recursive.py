def is_palindrome_recursive(word, low_index, high_index):
    if (word == ''):
        return False
    if low_index == high_index or low_index > high_index:
        return True
    return (
        word[low_index] == word[high_index]
        and
        is_palindrome_recursive(word, low_index + 1, high_index - 1)
    )


print(is_palindrome_recursive('arara', 0, len('arara') - 1))
