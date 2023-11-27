def naive_search(pattern,text):
    m = len(pattern)
    n = len(text)

    for i in range(n-m+1):
        j = 0
        while j<m:
            if pattern[j] != text[i+j]:
                break
            else:
                j += 1
                continue
        if j==m:
            print(f"Match found at index {i+1}")
            return
    print("No match found")

if __name__ == "__main__":
    naive_search("look","this is a random test")

