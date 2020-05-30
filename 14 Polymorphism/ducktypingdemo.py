'''Duck Typing Demo calling callTalk(obj) function, where 'obj' can be of any class'''

class Duck:
    def talk(self):
        print("Quack Quack")


class Human:
    def talk(self):
        print("Hello")


def callTalk(obj):                      # Calls and Executes the talk() function of the class oh whom object is passed as 'obj'
    obj.talk()


d = Duck()
callTalk(d)

h = Human()
callTalk(h)