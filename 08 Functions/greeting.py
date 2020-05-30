'''Function inside a function'''

def display(name):
    def message():
        return "Hello "
    result = message() + name
    return result

print(display('Anubhav'))