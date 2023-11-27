class ZAlgorithm:
    def __init__(self,pattern,text):
        self.pattern = pattern
        self.text = text
        self.S = pattern+text
        print(f"String : {self.S}")
        self.Z_table = [0 for _ in range(len(self.S))]

    def search(self):
        self.construct_Ztable()
        for i in range(1,len(self.Z_table)):
            if self.Z_table[i] >= len(self.pattern):
                print(f"found match at {i-len(self.pattern)}")

    def naive_search(self, index_k):
        count = 0
        print(f"Naive search at {index_k}")
        if self.S[index_k] != self.S[0]:
            return 0
        else:
            while count+index_k < len(self.S) and self.S[index_k + count] == self.S[count] :
                count += 1
            print(count, index_k+count,self.S[count],self.S[index_k + count-1])
            return count

    def construct_Ztable(self):
        l,r = 1,1
        # k is iterating through S to find Z value
        k = 1
        while k < len(self.S):
            if l < k <= r:
                # inside the Z box
                p = k-l
                if self.Z_table[p] < r-k+1 :
                    print(f"Case 2 at {k}")
                    # Case 2 : we can use Zp to populate the current Z[k]
                    # since pth index has all information till p(k-l)+Zp index
                    self.Z_table[k] = self.Z_table[p]
                    print("index : {0} and Z : {1}".format(k,self.Z_table[k]))
                    print("Corresponding P values ".format(p,self.Z_table[p]))
                    k += 1
                else:
                    print(f"Case 3 at {k}")
                    # value of k is near Z box end
                    i = r + 1
                    # print(p,r,i)
                    # start checking the value outside Z box one by one
                    while i < len(self.S):
                        # update the Zz table as long as we keep getting a match
                        if self.S[p+i-r] == self.S[i]:
                            i += 1
                        # add additional iterations (i-i0 , where i0= r+1) to value at Zp
                        self.Z_table[k] = i-r-1 + self.Z_table[p]
                    print("index : {0} and Z : {1}".format(k,self.Z_table[k]))
                    print("Corresponding P values ".format(p,self.Z_table[p]))
                    k += 1
            else:
                # outside the Z box
                self.Z_table[k] = self.naive_search(k)
                # found a Z box here and updated the box param
                if self.Z_table[k]:
                    l = k
                    r = l+self.Z_table[k]-1
                # print(f"l and r : {l,r}")
                print("index : {0} and Z : {1}".format(k,self.Z_table[k]))
                k += 1

        return self.Z_table

if __name__ == "__main__":
    zalg = ZAlgorithm("AABZA","ABZCAABZAABZA")
    # t = zalg.construct_Ztable()
    # print("*****")
    # print(t)
    zalg.search()

    zalg2 = ZAlgorithm("TEST","THIS TEST")
    # t2 = zalg2.construct_Ztable()
    # print("*****")
    # print(t2)
    zalg2.search()
