class Gun:
    def __init__(self) -> None:
        self.count = 0

    def shoot(self) -> None:
        print("pif" if self.count % 2 == 0 else "paf")
        self.count += 1


gun = Gun()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
