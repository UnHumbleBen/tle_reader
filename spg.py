import math

# the SGP type “mean” mean motion at epoch
n0 = 0
# Newton’s universal gravitational constant
G = 0
# mass of the Earth
M = 0
# √GM
k_e = math.sqrt(G * M)
# the second gravitational zonal harmonic of the Earth
J2 = 0
# the equatorial radius of the Earth
a_e = 0
# the “mean” inclination at epoch
i0 = 0
# the “mean” eccentricity at epoch
e0 = 0
# the “mean” mean anomaly at epoch
M0 = 0
# the “mean” argument of perigee at epoch
w0 = 0
# the “mean” longitude of ascending node at epoch
omega0 = 0
# the time rate of change of “mean” mean motion at epoch
n0_dot = 0
# the second time rate of change of “mean” mean motion at epoch
n0_double_dot = 0
# the third gravitational zonal harmonic of the Earth
J3 = 0
# SPG MODEL

# constants
a1 = (k_e / n0) ** (2 / 3)
delta1 = (3 / 4) * J2 * (a_e ** 2) / (a1 ** 2) * (3 * (math.cos(i0) ** 2) - 1) / ((1 - e0 ** 2) ** (3 / 2))
a0 = a1 * (1 - delta1 / 3 - delta1 ** 2 - (131 / 81) * delta1 ** 3)
p0 = a0(1 - e0 ** 2)
q0 = a0(1 - e0)
L0 = M0 + w0 + omega0
d_omega_d_t = -(3 / 2) * J2 * (a_e ** 2) / (p0 ** 2) * n0 * math.cos(i0)
d_w_d_t = (3 / 4) * J2 * (a_e ** 2) / (p0 ** 2) * n0 * (5 * (math.cos(i0) ** 2) - 1)

# secular effects of atmospheric drag and gravitation
# time since epoch
time_since_epoch = 0
a = a0 * (n0 / (n0 + 2 * (n0_dot / 2) * time_since_epoch) + 3 * (n0_double_dot / 6) * time_since_epoch ** 2) ** (2 / 3)
e = 0
if a > q0:
    e = 1 - q0 / a
else:
    e = 10 ** -6

p = a * (1 - e ** 2)
omega_s_0 = omega0 + d_omega_d_t * time_since_epoch
w_s_0 = w0 + d_w_d_t * time_since_epoch
L_s = L0 + (n0 + d_w_d_t + d_omega_d_t) * time_since_epoch + n0_dot / 2 * (
        time_since_epoch ** 2) + n0_double_dot / 6 * (time_since_epoch) ** 3
# Long-period periodics
a_x_NSL = e * math.cos(w_s_0)
a_y_NSL = e * math.sin(w_s_0) - 1 / 2 * J3 / J2 * a_e / p * math.sin(i0)
L = L_s - 1 / 4 * J3 / J2 * a_e / p * a_x_NSL * math.sin(i0) * ((3 + 5 * math.cos(i0) / (1 + math.cos(i0))))
# Kepler's equation
U = L - omega_s_0
E_plus_w_1 = U
delta_E_plus_w_1 = (U - a_y_NSL * math.cos(E_plus_w_1) + a_x_NSL * math.sin(E_plus_w_1) - E_plus_w_1) / (
        -a_y_NSL * math.sin(E_plus_w_1) - a_x_NSL * math.cos(E_plus_w_1) + 1)
E_plus_w_2 = E_plus_w_1 + delta_E_plus_w_1

E_plus_w = E_plus_w_2
# intermediate (partially oscilating quantities)
e_cos_E = a_x_NSL * math.cos(E_plus_w) + a_y_NSL * math.sin(E_plus_w)
e_sin_E = a_x_NSL * math.sin(E_plus_w) + a_y_NSL * math.cos(E_plus_w)
e_L_squared = a_x_NSL ** 2 + a_y_NSL ** 2
p_L = a * (1 - e_L_squared)
r = a * (1 - e_cos_E)
r_dot = k_e * math.sqrt(a) / r * e_sin_E
r_v_dot = k_e * math.sqrt(p_L) / r
sin_u = a / r * (math.sin(E_plus_w) - a_y_NSL - a_x_NSL * (e_sin_E) / (1 + math.sqrt(1 - e_L_squared)))
cos_u = a / r * (math.cos(E_plus_w) - a_x_NSL + a_y_NSL * (e_sin_E) / (1 - math.sqrt(1 - e_L_squared)))
u = math.atan(sin_u / cos_u)

# short-period perturbations
r_k = r + 1 / 4 * J2 * a_e ** 2 / p_L * math.sin(i0) ** 2 * math.cos(2 * u)
u_k = u - 1 / 8 * J2 * a_e ** 2 / p_L ** 2 * (7 * math.cos(i0) ** 2 - 1) * math.sin(2 * u)
omega_k = omega_s_0 + 3 / 4 * J2 * a_e ** 2 / p_L ** 2 * math.cos(i0) * math.sin(2 * u)
i_k = i0 + 3 / 4 * J2 * a_e ** 2 / p_L ** 2 * math.sin(i0) * math.cos(i0) * math.cos(2 * u)

# unit orientation vectors

