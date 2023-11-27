def is_anagram(w1 : str , w2 : str):
    if len(w1) != len(w2):
        return False
    elif sorted(w1.casefold()) == sorted(w2.casefold()):
        # above is O(N*LogN) runtime
        return True
    else: return False


print(is_anagram("restful","fluster"))