class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    def talk(self):
        print(self.name + ' says meow!')
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("This cat has no more lives to lose :(")

class NoisyCat(Cat):
    def talk(self):
        Cat.talk(self)
        Cat.talk(self)
