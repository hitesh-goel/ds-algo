# https://www.interviewcake.com/question/python3/reverse-words


def reverse_words(message_chars):
    # 1. words are starting from the space except first one
    # 2. go through the entire array and search for the last space
    # 3. copy the word which is ahead space and update at the front of the array
    # 4. repeat 2 & 3
    # 5. return the array as string
    # issues with above approach
    # 1) difficult to append the array in start
    p = n = len(message_chars)
    result_arr = []
    while n >= 0:
        if message_chars[n - 1] == ' ' or n == 0:
            result_arr.append(''.join(message_chars[n: p]))
            p = n - 1
        n -= 1
    return ' '.join(result_arr)


def reverse_word(message_chars, s, e):
    st, et = int(s), int(e)
    while st < et:
        message_chars[st], message_chars[et] = message_chars[et], message_chars[st]
        st += 1
        et -= 1


# reverse the words without using extra space
def reverse_words_ic(message_chars):
    n, s, e = 0, 0, len(message_chars) - 1
    reverse_word(message_chars, s, e)

    while n <= e:
        if n == e or message_chars[n + 1] == ' ':
            reverse_word(message_chars, s, n)
            s = n + 2
        n += 1
    return ''.join(message_chars)


def main():
    message = ['c', 'a', 'k', 'e', ' ',
               'p', 'o', 'u', 'n', 'd', ' ',
               's', 't', 'e', 'a', 'l']
    assert reverse_words(message) == "steal pound cake"
    assert reverse_words_ic(message) == "steal pound cake"


if __name__ == '__main__':
    main()
