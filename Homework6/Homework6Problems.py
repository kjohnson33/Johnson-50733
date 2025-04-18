from KiaraJohnson2 import fourth_order_Runge_Kutta as rk4


# Problem 1: Radioactive Decay

# N_0 = 1000
lamb = 3.84e-5

def radioactive_decay(N_0, t):
    return -lamb * N_0


t_vals, x_vals = rk4.runge_kutta_4(radioactive_decay, 1000, 0, 100, 1000)
rk4.plot_results(t_vals, x_vals, color='green', label='dN/dt', var_name='Number of Nuclei', title_name='Radioactive Decay')



# Problem 2 : Logistic Growth

r = 0.45
P = 10
K = 100

def logistic_growth(P, t):
    r, K = 0.45, 100
    return r * P * (1 - P / K)

t_vals, x_vals = rk4.runge_kutta_4(logistic_growth, 10, 0, 50, 1000)
rk4.plot_results(t_vals, x_vals, color='purple', label='dP/dt', var_name='Population Size', title_name='Logistic Growth')



# Problem 3 : Ion Flow Through Membranes

C = 1.0     # membrane capacitance
g = 0.3     # conductance
E = -70.0   # reversal potential

def ion_flow(V, t):
    return (-g * (V - E)) / C

t_vals, x_vals = rk4.runge_kutta_4(ion_flow, 50, 0, 50, 1000)
rk4.plot_results(t_vals, x_vals, color='blue', label='dV/dt', var_name='Membrane Potential (mV)', title_name='Ion Channel Flow')