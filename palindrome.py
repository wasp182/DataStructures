import reverse_array


def isPalindrome(word):
    rev_word = reverse_array.reverse(word)
    print(rev_word)
    if word.casefold() == rev_word.casefold():
        return True
    else: return False

if __name__ == "__main__":
    print(isPalindrome("raaR"))
