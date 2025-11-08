class Gun:
    """Imitation gun"""

    def __init__(self) -> None:
        self.count = 0

    def shoot(self) -> None:
        print("pif" if self.count % 2 == 0 else "paf")
        self.count += 1

    def shots_count(self) -> int:
        return self.count

    def shots_reset(self) -> None:
        self.count = 0


gun = Gun()
gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
