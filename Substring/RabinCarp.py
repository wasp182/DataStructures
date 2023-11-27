class RabinKarp:
    def __init__(self,pattern,text):
        self.pattern = pattern
        self.text = text
        self.d = 26
        # modulo operator
        self.q = 31

    def search(self):
        m = len(self.pattern)
        n = len(self.text)
        hash_text = 0
        hash_pattern = 0
        h = 1
        for _ in range(m-1):
            h = (h*self.d) % self.q

        for i in range(m):
            hash_pattern = (self.d*hash_pattern+ord(self.pattern[i])) % self.q
            hash_text = (self.d*hash_text+ord(self.text[i])) % self.q

        # slide pattern one by one to check for match
        for i in range(n-m+1):
            if hash_text == hash_pattern:
                # naive approach
                j = 0
                while j < m:
                    if self.pattern[j] != self.text[i+j]:
                        break
                    j += 1
                if j == m:
                    print(f"found match at {i}")
            if i < n-m :
                #  remove hash of first letter         hash of one item shifted right , i+m index as starting index is 0
                hash_text = ((hash_text-ord(self.text[i])*h)*self.d + ord(self.text[i+m])) % self.q
                # this hash text is modulo output hence , we may get -ve value , we get convert to +ive counterpart
                if hash_text<0:
                    hash_text+ self.q

if __name__ == "__main__":
    algorithm = RabinKarp("look","this looks good")
    algorithm.search()
    
