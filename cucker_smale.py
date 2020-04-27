import numpy as np

BOUNCE = False
LAMBDA = 100


class Flock:
    def __init__(self, population=50):
        self.population = population

        self.positions = np.zeros((population, 2))
        self.velocities = np.zeros((population, 2))
        self.directions = np.zeros((population, 2))

        self.dimensions = (800, 600)

    def do_frame(self, millis=16.7):
        psi = np.array([[(vel_i - vel_j) / (1 + 1 / 100 * np.linalg.norm(pos_i - pos_j) ** 2)
                         for pos_i, vel_i in zip(self.positions, self.velocities)]
                        for pos_j, vel_j in zip(self.positions, self.velocities)])
        # print(psi)

        self.velocities += millis/1000 * LAMBDA / self.population * np.sum(psi, axis=1)

        # print(np.sum(self.velocities, axis=0))

        self.positions += millis/1000 * self.velocities
        self.directions = self.velocities / np.linalg.norm(self.velocities, axis=1, keepdims=True)

        if BOUNCE:
            for pos, vel in zip(self.positions, self.velocities):
                if pos[0] < 0 and vel[0] < 0:
                    vel[0] *= -1
                if pos[1] < 0 and vel[1] < 0:
                    vel[1] *= -1
                if pos[0] > self.dimensions[0] and vel[0] > 0:
                    vel[0] *= -1
                if pos[1] > self.dimensions[1] and vel[1] > 0:
                    vel[1] *= -1
