'''This is INCOMPLETE PROGRAM'''


from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):                        # This is an Interface

    def __init__(self, scroll, click):
        self.click = click
        self.scroll = scroll

    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def scroll(self):
        pass

class Dell(TouchScreenLaptop):
    def __init__(self, scroll, click):
        super().__init__(scroll)

    def scroll(self):
        super().scroll()
        print('Scrolling')


class HP(TouchScreenLaptop):
    def __init__(self, scroll, click):
        super().__init__(scroll)


    def scroll(self):
        super().scroll()
        print('Scrolling')


class DellNotebook(Dell):
    def __init__(self, click):
        super().__init__(self, click)

    def click(self):
        super().click()
        print('Clicked')


class HPNotebook(HP):
    def __init__(self, click):
        super().__init__(self, click)

    def click(self):
        super().click()
        print('Clicked')


dell = DellNotebook(click=True)
print(dell.click())
print(dell.scroll())





'''Solution found on Udemy'''

#
# from abc import ABC, abstractmethod
#
#
# class TouchScreenLaptop(ABC):
#
#     def __init__(self):
#         super(TouchScreenLaptop, self).__init__()
#
#     @abstractmethod
#     def scroll(self):
#         pass
#
#     @abstractmethod
#     def click(self):
#         pass
#
#
# class HP(TouchScreenLaptop):
#
#     def scroll(self):
#         super().scroll()
#
#         print("HP Scroll Activated")
#
#
# class Dell(TouchScreenLaptop):
#
#     def scroll(self):
#         super().scroll()
#
#         print("Dell Scroll Activated")
#
#
# class HPNotebook(HP):
#
#     def click(self):
#         super().click()
#
#         print("HP Click Activated")
#
#
# class DellNotebook(Dell):
#
#     def click(self):
#         super().click()
#
#         print("Dell Click Activated")
#
#
# hp = HPNotebook()
#
# hp.scroll()
#
# hp.click()
#
# dell = DellNotebook()
#
# dell.scroll()
#
# dell.click()