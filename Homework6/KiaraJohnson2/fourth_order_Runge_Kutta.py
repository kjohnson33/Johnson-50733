import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(f, x_0, t_0, t_fin, N_steps):
    dt = (t_fin - t_0) / N_steps
    t_values = np.arange(t_0, t_fin + dt, dt)
    x_values = [x_0]

    for i in range(len(t_values) - 1):
        t = t_values[i]
        x = x_values[i]
        k1 = dt * f(x, t)
        k2 = dt * f(x + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * f(x + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * f(x + k3, t + dt)
        x_next = x + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x_values.append(x_next)

    return t_values, x_values

def plot_results(t, x, color, label='Solution', var_name='x(t)', title_name='plot of x(t) vs time'):
    plt.plot(t, x, color,label=label)
    plt.xlabel('Time')
    plt.ylabel(var_name)
    plt.title(f'{title_name}')
    plt.legend()
    
    plt.show()