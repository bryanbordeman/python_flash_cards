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


class BikeTrail(Trail):
    """Represent a bike trail"""

    def __inti__(self, dest, len=0):
        super().__init__(dest,len)
        self.paved = True
        self.bikes_only = True

    def ride_trail(self):
        """Simulates ridding the trail."""
        # print(f'Riding to {self.dest}. ')
        if self.bikes_only:
            print(f"You can't run this trail!")
        else:
            super().run_trail()


verst = Trail("Mt. Verstovia", 4)
print(f'\nDestination: {verst.dest}')
verst.describe_trail()
verst.run_trail()

ms = Trail('Middle Sister', 10)
ms.describe_trail()
ms.run_trail()

cross_trail = BikeTrail('Harber Moutain', 5)
cross_trail.bikes_only=False
cross_trail.run_trail()
