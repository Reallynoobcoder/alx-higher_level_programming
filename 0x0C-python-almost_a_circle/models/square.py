from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):

        num_args = len(args)

        if num_args >= 1:
            self.id = args[0]

        if num_args >= 2:
            self.size = args[1]

        if num_args >= 3:
            self.x = args[2]

        if num_args >= 4:
            self.y = args[3]
    
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                
    def to_dictionary(self):

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
