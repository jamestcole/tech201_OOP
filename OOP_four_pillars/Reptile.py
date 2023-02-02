from Animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None #Not all reptiles are tetrapods
        self.heart_chambers = [3, 4]
        self.amoitic_eggs = None

    def seek_heat(self):
        print("It's chilly outside, where is the sun ?")

    def hunt(self):
        print("Wait, wait, wait .. pounce")

    def use_venom(self):
        print("If I have got it , I am going to use it")

    def attract_through_scent(self):
        print("Time to spray some eut de toilette")

#jeremy_the_reptile = Reptile()

#jeremy_the_reptile.breathe()
#jeremy_the_reptile.hunt()
#jeremy_the_reptile.eat()