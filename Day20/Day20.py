import re
from collections import defaultdict
from math import sqrt


class Vec3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y,  self.z + other.z)

    def __len__(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __repr__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Particle:
    def __init__(self, id: int, pos: Vec3, vel: Vec3, acc: Vec3):
        self.id = id
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.dead = False

    def __repr__(self):
        if self.dead:
            return "P={id} --dead--".format(id=self.id)
        return "P={id} at {pos} vel: {vel} acc: {acc}".format(id=self.id,
                                                              pos=self.pos,
                                                              vel=self.vel,
                                                              acc=self.acc)

    def kill(self):
        self.dead = True

    def tick(self):
        if not self.dead:
            self.vel = self.vel + self.acc
            self.pos = self.pos + self.vel

    def get_acceleration(self):
        return len(self.acc)

    def get_velocity(self):
        return len(self.vel)

    def distance(self):
        return self.pos.manhattan()


def parse_input(in_data):
    particles = []

    for num, line in enumerate(in_data):
        numbers = [int(i) for i in re.findall(r'-?\d+', line)]

        pos = Vec3(*numbers[0:3])
        vel = Vec3(*numbers[3:6])
        acc = Vec3(*numbers[6:9])

        particles.append(Particle(num, pos, vel, acc))

    return particles


def simulate(particles: list, collisions=True):
    while True:
        for p in particles:  # type: Particle
            p.tick()

        # Important: Check stuff after updating all particles!
        if collisions:
            positions = defaultdict(list)
            for p in particles:
                if p.dead:
                    continue
                positions[tuple([p.pos.x, p.pos.y, p.pos.z])].append(p.id)
            for pos, parts in positions.items():
                if len(parts) > 1:
                    for p_id in parts:
                        particles[p_id].kill()
            print(sum(not p.dead for p in particles))
        else:
            smallest_dist = particles[0].pos.manhattan()
            smallest_id = 0
            for p in particles:
                dist = p.distance()
                if dist < smallest_dist:
                    smallest_dist = dist
                    smallest_id = p.id
            print(smallest_id)


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    test_particles = """p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"""
    test_particles = [line.strip() for line in test_particles.split("\n")]

    particles = parse_input(lines)

    simulate(particles)

