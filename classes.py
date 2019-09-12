from trails import Trail, BikeTrail


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
