import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import simps
from matplotlib.animation import FuncAnimation



# Set arguments
m = 1   # standard deviation of the mutational distribution.
s = math.sqrt(6)   # parameter used in defining fitness function.
a = 3   # the distance between the two peaks in the bimodal fitness function.
v = 0   # velocity of the environmental change.
c = 1   # parameter 1 used in defining initial distirbution.
d = 1  # parameter 2 used in defining initial distirbution.
L = 15   # integral interval.
t_steps = 50   # number of generations.
g_min, g_max = -L, L
g_values = np.linspace(g_min, g_max, 500)



# mutational distribution.
def f(g):
    return (1 / np.sqrt(2 * np.pi * m ** 2)) * np.exp(-g ** 2 / (2 * m ** 2))



# fitness function.
def W(g):
    # stabilising selection (unimodal fitness function):
    return np.exp(-g ** 2 / (2 * s ** 2))

    # generalisation of stabilising selection (bimodal fitness function):
    # return np.exp(-(g + a) ** 2 / (2 * s ** 2)) + np.exp(-(g - a) ** 2 / (2 * s ** 2))



# initial distribution Psi(g, 1).
def psi_initial(g):
    return np.sqrt(1 / (2 * c ** 2)) * np.exp(-(g + d) ** 2 / (2 * c ** 2))



# distribution for next generation Psi(g, t + 1).
def psi_next(g, t, psi_prev, L):
    g_prime_values = np.linspace(-L, L, 500)
    numerator = [f(g - g_prime + v) * W(g_prime) * psi_prev(g_prime) for g_prime in g_prime_values]
    denominator = [W(g_prime) * psi_prev(g_prime) for g_prime in g_prime_values]
    num_integral = simps(numerator, g_prime_values)
    denom_integral = simps(denominator, g_prime_values)
    return num_integral / denom_integral



# evolution for t_steps generations.
def compute_psi_over_time(t_steps, L):
    psi_t = [psi_initial(g_values)]
    for t in range(1, t_steps):
        psi_t_next = np.array([psi_next(g, t, lambda g_prime: np.interp(g_prime, g_values, psi_t[-1]), L) for g in g_values])
        psi_t.append(psi_t_next)
        print(t)
    return psi_t



# generate animate of the evolution process.
def animate_psi(psi_t):
    fig, ax = plt.subplots()
    line_pop, = ax.plot(g_values, psi_t[0], color = 'g', label = "Asexual population distribution")
    line_w, = ax.plot(g_values, W(g_values), color = 'r', label = "Fitness function")
    ax.set_xlim(-15, 15)
    ax.set_ylim(0, 1.3)
    param_text_1 = ax.text(0.95, 0.95, '', transform = ax.transAxes, ha = 'right', va = 'top', fontsize = 10)
    param_text_2 = ax.text(0.95, 0.90, '', transform = ax.transAxes, ha = 'right', va = 'top', fontsize = 10)
    param_text_3 = ax.text(0.95, 0.85, '', transform = ax.transAxes, ha = 'right', va = 'top', fontsize = 10)
    param_text_4 = ax.text(0.95, 0.80, '', transform = ax.transAxes, ha = 'right', va = 'top', fontsize = 10)
    ax.legend(loc = 'upper left')

    def update(t):
        try:
            line_pop.set_ydata(psi_t[t])
            ax.set_title(f"t = {t}")
            param_text_1.set_text(f"a = {a}")
            param_text_2.set_text(f"s = {s}")
            param_text_3.set_text(f"m = {m}")
            param_text_4.set_text(f"v = {v}")
        except IndexError as e:
            print(f"Error updating frame {t}: {e}")
        return line_pop, line_w, param_text_1, param_text_2, param_text_3, param_text_4

    anim = FuncAnimation(fig, update, frames = len(psi_t), interval = 200)
    return anim



# generate animation.
psi_t = compute_psi_over_time(t_steps, L)
anim = animate_psi(psi_t)

# save as GIF：
try:
    anim.save('Evolution_animation.gif', writer = 'imagemagick', fps = 10)
except Exception as e:
    print(f"Error saving animation: {e}")

plt.show()