class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return str(self.name)

def insertion_sort(people):
    for item in range(len(people)):
        index = item
        while people[index] < people[index-1] and index >= 1:
            people[index] , people[index-1] = people[index-1] , people[index]
            index -= 1
    print(people)

if __name__ == "__main__":
    n = [Person('Adam', 23), Person('Ana', 17), Person('Kevin', 32), Person('Daniel', 37)]
    insertion_sort(n)

