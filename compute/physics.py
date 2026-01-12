gravity_constant = 6.674 * 10 ** -11


# kinematics equations
def final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)


def displacement(initial_velocity, acceleration, time):
    return initial_velocity * time + 0.5 * acceleration * time ** 2


def velocity_squared(initial_velocity, acceleration, displacement):
    return 2 * acceleration * displacement + initial_velocity ** 2


def average_velocity(initial_velocity, final_velocity):
    return (initial_velocity + final_velocity) / 2


def thrust(mass_flow_rate, exhaust_velocity, exhaust_pressure, ambient_pressure, nozzle_exit_area):
    return mass_flow_rate * exhaust_velocity + nozzle_exit_area * (exhaust_pressure - ambient_pressure)


def force(mass, acceleration):
    return mass * acceleration


def universal_graviation(mass1, mass2, distance):
    return gravity_constant * ((mass1 * mass2) / distance ** 2)
