# assigning getters and setters to avoid setting bad field values
# and to provide improved output

class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # creating getter
    # @property allows you to refer to fields above (width/height)
    @property
    def height(self):
        # improving the output
        print("Retrieving the height")

        # the 2 underscores means it's a private field
        return self.__height

    # creating setter for height
    @height.setter
    def height(self, value):
        # make sure value passed in is a digit
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    # do the same for width
    @property
    def width(self):
        # improving the output
        print("Retrieving the width")

        # the 2 underscores means it's a private field
        return self.__width

    @width.setter
    def width(self, value):
        # make sure value passed in is a digit
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        # convert strings to ints
        return int(self.__width) * int(self.__height)

def main():
    aSquare = Square()

    # use getters and setters by asking user input
    height = input("Enter Height : ")
    width = input("Enter Width : ")

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("Width :", aSquare.width)

    print("The area is :", aSquare.getArea())

main()
