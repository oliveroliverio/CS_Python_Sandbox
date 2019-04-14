# Real world objects: Attributes & capabilities
# Dog attributes (fields/variables) : height, weight, favorite food
# Dog capabilities (methods/functions) : run, walk, eat, shit, piss

# create dog object from template or class
class Dog:
    # you set default things like height, weight, etc w/ __init__
    # self allows object to refer to itself, like you would refer to yourself as "my"
    # why use this?  to create custom dogs from this class, but you need defaults
    # the defaults are blank so that you can create a dog w/out a height, weight or name
    # but can be defined programmatically
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


# execute main function here
main()
