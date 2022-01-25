class Warrior:

    hit_points = 20

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.live = True

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def got_hit(self):
        self.health -= self.hit_points
        if self.health <= 0:
            self.live = False
            return 0
        else:
            return self.health

    def is_alive(self):
        return self.live
