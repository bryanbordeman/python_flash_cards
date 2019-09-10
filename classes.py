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

    def run_trail(self):
        """Simulate running the trail."""
        print(f'Running to {self.dest}.\n')


verst = Trail("Mt. Verstovia", 4)
print(f'\nDestination: {verst.dest}')
verst.describe_trail()
verst.run_trail()

ms = Trail('Middle Sister', 10)

