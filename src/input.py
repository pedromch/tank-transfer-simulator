suction_tank_liquid_height = 0 # meters
discharge_tank_liquid_height = 40 # meters

fluid_specific_mass = 1e3 # kg/m3
fluid_viscosity = 1e-3 # kg/m3

tube_internal_diameter = 0.154 # meters
tube_length = 120 # meters 
tube_rugosity = 4.6e-2

pipe_fittings = { # leave empty if there is no pipe fitting
    1: 5, # type (id column of pipe_fitting_options.csv) : quantity 
    16: 2
}

pump_curve_file_path = r'c:\Users\pedro.machado\Desktop\project_1\assets\pump_curve_test.csv' # H in meters and Q in m3/h