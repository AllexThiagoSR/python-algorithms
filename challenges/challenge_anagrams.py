def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    mid = (start + end) // 2
    if (end - start) > 1:
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        return merge(word, start, mid, end)
    return merge(word, start, mid, end)


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word[general_index] = right[right_index]
            right_index = right_index + 1
    return word


def is_anagram(first_string, second_string):
    first_string_sorted = merge_sort(
        first_string.replace('', ' ').lower().split()
    )
    second_string_sorted = merge_sort(
        second_string.replace('', ' ').lower().split()
    )
    if len(first_string_sorted) == 1 or len(second_string_sorted) == 1:
        first_string_sorted.append('')
        second_string_sorted.append('')
    first_string = "".join(first_string_sorted)
    second_string = "".join(second_string_sorted)
    if len(first_string_sorted) == 0 or len(second_string_sorted) == 0:
        return first_string, second_string, False
    return first_string, second_string, first_string == second_string


print(is_anagram("f", "u"))
