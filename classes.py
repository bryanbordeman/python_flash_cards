class Trail():
    """A class to represent trails."""
    def __init__(self, dest, len=0):
        self.dest = dest
        self.len = len

    def describe_trail(self):
        """Print a description of trail."""
        dest = f'this trail goes to {self.dest}.'

        if self.len:
            dest += f'\nThe trail is {self.len}km.'
        print(dest)


mytrail = Trail('Tawoco', 20)

mytrail.describe_trail()
