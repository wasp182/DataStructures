import random
import string

def pi_table(pattern):
    i = 1
    pattern_count = 0
    pi_table = [0 for _ in range(len(pattern))]
    while i < len(pattern):
        if pattern[i]==pattern[pattern_count]:
            pattern_count += 1
            pi_table[i] = pattern_count
            i += 1
        else:
             if pattern_count != 0:
                pattern_count = pi_table[pattern_count-1]
             else:
                 pi_table[i]=0
                 i+=1
    return pi_table

def pi_table_2(pattern):
    pi_table = [0 for _ in range(len(pattern))]
    for i in range(1,len(pattern)):
        if pattern[i] == pattern[pi_table[i-1]]:
            pi_table[i] = pi_table[i-1]+1
        # pattern is not found at certain position then we reset
        elif pi_table[i-1] !=0 :
            pi_table[i] = 0
    return pi_table

def search_KMP(text,pattern):
    i , j = 0 ,0
    table = pi_table(pattern)
    for i in range(len(text)+1):
        if j < len(pattern):
            if text[i] == pattern[j]:
                j += 1
            else:
                j = table[j-1]
                if text[i] == pattern[j]:
                    j += 1
                else:
                    continue
        elif j == len(pattern):
            print(f"found match at {i-j}")
            # found one pattern and now we have to re initialise the j
            if j != 0:
                j = table[j-1]


if __name__ =="__main__":
    print(pi_table("aafabaafab"))
    print(pi_table_2("aafabaafab"))

    print(pi_table("qwereqwerwqwertrr"))
    print(pi_table_2("qwereqwerwqwertrr"))

    # test case
    s1 = ''.join(random.choices(string.ascii_uppercase, k = 100))
    print(s1)
    print(pi_table(s1))
    print(pi_table(s1)==pi_table_2(s1))
    print("****")
    print(search_KMP("this is a test case easily tested test test test test test","test"))


