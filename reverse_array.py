
def reverse(data_list):
    init = 0
    end = len(data_list) - 1
    data_list = list(data_list)
    while init < end:
        data_list[init], data_list[end] = data_list[end] , data_list[init]
        init +=1
        end -=1
    return "".join(data_list)


if __name__ == "__main__":
    n = [1,22,3,45]
    print(n)
    reverse(n)
    print(n)

