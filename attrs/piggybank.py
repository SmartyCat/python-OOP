class PiggyBank:
    pass


money_box1 = PiggyBank()
money_box1.coins = 10
money_box2 = PiggyBank()
money_box2.coins, money_box2.color = 15, "pink"

print(money_box1.__dict__, money_box2.__dict__)
