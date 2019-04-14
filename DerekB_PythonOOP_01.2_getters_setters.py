# assigning getters and setters to avoid

# create dog object from template or class
class Dog:

    def __init__(self, name="", height=0, weight=0):
        # "my" (or "self") name is <whatever they passed into the first param above
        self.name = name
        # same thing for height, weight, etc
        self.height = height
        self.weight = weight

    # now define default capabilities
    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

# define main() method, where all the execution occurs
def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()

    bowser = Dog("Bowser", 800, 234)
    bowser.run()

# execute main function here
main()
