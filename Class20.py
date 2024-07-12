#Lambda inside a function

def add(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(add(2))