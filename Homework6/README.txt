Homework 6: Synthesis (Create Your Own Importable Python Package)


Description: 

The purpose of this project is to create a python package containing a flexible fourth-order Runge-Kutta python script that can be imported into a separate .py file to solve three ordinary differential equations (ODEs) resulting in three nicely formatted plots. 


Table of Contents:

	1. Dependencies (1)
	2. Explanation of the code fourth-order Runge-Kutta (RK4) and plot code (2)
	3. How to Use (3)


(1) Dependencies (programming language and libraries used): 

	1. Python
	2. Visual Studio Code (VS Code)
	3. NumPy 	
	4. Matplotlib
	
 
(2) Explanation of RK4 code

File name: fourth_order_Runge_Kutta

The components of this code are the "runge_kutta_4" and "plot_results" functions. The "runge_kutta_4" function solves ODEs in the form: dx/dt = f(x,t). The "plot_results" function does exactly that, plots the results.

	"runge_kutta_4" function

		Parameters and Outputs:

			f: right-hand side of the differential equation
			x_0: initial value 
			t_0: start time
			t_fin: end time
			N_steps: number of steps
			t_values: array of time values
			x_values: arrary of solution values
	
		Note: dt is the time step
	
	"plot_results" function
	
		Parameters and Outputs:
		t: time array
		x: solution array
		color: color for the graph of the line
		label: the label/name for the line
		var_name: y-axis (variable being measured)
		title_name: title of the plot
		Outputs: returns the plot
	

 
(3) How to Use
	1. Import package to the Homework6Problems.py file: from KiaraJohnson2 import fourth_order_Runge_Kutta as rk4
	2. Define the ODE as a function in the form: 

		def name_of_ODE(variable_measured, t):
			values of variables and constants
			return equation_of_ODE

		Example: 
			def random_deq(x, t):
				a, b, c = 2, 5, 3
				return (a) * (x**2) + b * x + c


	3. Call the RK4 and plot functions as follows below:

		t_vals, x_vals = rk4.runge_kutta_4(f, x0, t0, tf, steps)
		rk4.plot_results(t_vals, x_vals, color='your_color', label='your_label', var_name='your_variable', title_name='your_title')



 