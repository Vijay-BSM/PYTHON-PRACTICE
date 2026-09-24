class players:

    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

        players.player_count += 1


p1 = players("Vijay", 10)
p2 = players("Rahul", 15)
p3 = players("Arun", 20)

print(p1.name, p1.level)
print(p2.name, p2.level)
print(p3.name, p3.level)

print("Total players:", players.player_count)
