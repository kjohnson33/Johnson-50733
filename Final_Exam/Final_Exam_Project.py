import numpy as np
import matplotlib.pyplot as plt
import time
import math
import matplotlib.animation as animation

# Parameters
grid_size = 20
population_size = 400
infection_radius = 0.5
infection_rate = 0.9  # 90
mortality_rate = 0.001  # 0.1%
recovery_time = 100
max_velocity = 0.25
mask_effectiveness = 0.1  
mask_rate = 0.5  # 50% wear masks
deltat = 0.1
total_frames = 500

class Person:
    def __init__(self, x, y, velocity, masked=False):
        self.position = np.array([x, y], dtype=float)
        self.velocity = velocity
        self.infected = False
        self.immune = False
        self.dead = False
        self.infection_timer = 0
        self.masked = masked

    def move(self):
        if self.dead:
            return
        for i in range(2):
            self.position[i] += self.velocity[i]
            if self.position[i] < 0:
                self.position[i] = -self.position[i]
                self.velocity[i] = -self.velocity[i]
            elif self.position[i] > grid_size:
                self.position[i] = 2 * grid_size - self.position[i]
                self.velocity[i] = -self.velocity[i]

    def update_infection(self):
        if self.infected:
            self.infection_timer += 1
            if self.infection_timer >= recovery_time:
                if np.random.rand() < mortality_rate:
                    self.dead = True
                else:
                    self.immune = True
                self.infected = False

def distance(p1, p2):
    dx = p1.position[0] - p2.position[0]
    dy = p1.position[1] - p2.position[1]
    return math.sqrt(dx * dx + dy * dy)

def create_population(grid_size, mask_rate):
    people = []
    spacing = 1.0
    for x in range(grid_size):
        for y in range(grid_size):
            velocity = np.random.randn(2) * max_velocity
            masked = np.random.rand() < mask_rate
            person = Person(x * spacing, y * spacing, velocity, masked)
            people.append(person)
    np.random.choice(people).infected = True
    return people

def simulate(people, steps=500):
    infected_count = []
    for t in range(steps):
        for p in people:
            p.move()
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                p1, p2 = people[i], people[j]
                if p1.dead or p2.dead:
                    continue
                if distance(p1, p2) < infection_radius:
                    for a, b in [(p1, p2), (p2, p1)]:
                        if a.infected and not b.infected and not b.immune and not b.dead:
                            effective_infection_rate = infection_rate
                            if b.masked:
                                effective_infection_rate *= mask_effectiveness
                            if np.random.rand() < effective_infection_rate:
                                b.infected = True
                    p1.velocity, p2.velocity = p2.velocity, p1.velocity
        for p in people:
            p.update_infection()
        infected_count.append(sum(p.infected for p in people))
    return infected_count

def time_simulation(sizes=[50, 100, 150, 200, 250, 300, 350, 400]):
    times = []
    for pop_size in sizes:
        grid_size_local = int(np.sqrt(pop_size))
        start = time.time()
        people = create_population(grid_size_local, mask_rate)
        simulate(people)
        end = time.time()
        times.append(end - start)
        print(f"Population {pop_size} took {times[-1]:.2f} seconds.")
    return sizes, times, sizes[-1]  # Return final population

# === Run time simulation and plot ===
sizes, runtimes, final_population = time_simulation()
plt.plot(sizes, runtimes, marker='o')
plt.xlabel("Population Size")
plt.ylabel("Runtime (seconds)")
plt.title("Simulation Time vs Population Size")
plt.grid()
#plt.savefig("population_runtimes_finalexam.pdf", bbox_inches='tight', pad_inches=0.2)
#plt.savefig("population_runtimes_finalexam_1.pdf", bbox_inches='tight', pad_inches=0.2)
plt.savefig("population_runtimes_finalexam_2.pdf", bbox_inches='tight', pad_inches=0.2)
plt.show()

# === Use final population size for the next steps ===
final_grid_size = int(np.sqrt(final_population))

# === Masking Experiment ===
def masking_experiment(pop_size, grid_size):
    global mask_rate
    for mask_setting in [0.0, 0.5]:
        mask_rate = mask_setting
        people = create_population(grid_size, mask_rate)
        infected_over_time = simulate(people)
        label = f"{int(mask_setting * 100)}% Masked"
        plt.plot(infected_over_time, label=label)
    plt.xlabel("Time Step")
    plt.ylabel("Number of Infected People")
    plt.title(f"Pandemic Spread With and Without Masks (Pop: {pop_size})")
    plt.legend()
    #plt.savefig("mask_experiment_finalexam.pdf", bbox_inches='tight', pad_inches=0.2)
    #plt.savefig("mask_experiment_finalexam_1.pdf", bbox_inches='tight', pad_inches=0.2)
    plt.savefig("mask_experiment_finalexam_2.pdf", bbox_inches='tight', pad_inches=0.2)
    plt.show()

masking_experiment(final_population, final_grid_size)

# === Animation ===
people = create_population(final_grid_size, mask_rate)
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, final_grid_size)
ax.set_ylim(0, final_grid_size)
scat = ax.scatter([], [], s=10)

def update(frame):
    ax.set_title(f"Time = {frame * deltat:.1f}")
    for p in people:
        p.move()
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            p1, p2 = people[i], people[j]
            if p1.dead or p2.dead:
                continue
            if distance(p1, p2) < infection_radius:
                for a, b in [(p1, p2), (p2, p1)]:
                    if a.infected and not b.infected and not b.immune and not b.dead:
                        chance = infection_rate * (mask_effectiveness if b.masked else 1.0)
                        if np.random.rand() < chance:
                            b.infected = True
                p1.velocity, p2.velocity = p2.velocity, p1.velocity
    for p in people:
        p.update_infection()
    xs = [p.position[0] for p in people]
    ys = [p.position[1] for p in people]
    colors = ['red' if p.infected else 'blue' if p.immune else 'black' if p.dead else 'green' for p in people]
    scat.set_offsets(np.column_stack((xs, ys)))
    scat.set_color(colors)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=300, blit=True)
writer = animation.PillowWriter(fps=10.8, metadata=dict(artist='Sim'), bitrate=1800)
#ani.save('simulation_finalexam.gif', writer=writer)
#ani.save('simulation_finalexam_1.gif', writer=writer)
ani.save('simulation_finalexam_2.gif', writer=writer)
plt.show()
