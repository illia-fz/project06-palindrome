def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    text = input('Enter a string: ')
    if is_palindrome(text):
        print('It is a palindrome.')
    else:
        print('It is not a palindrome.')
