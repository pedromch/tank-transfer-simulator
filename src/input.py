suction_tank_liquid_height = 0 # meters
discharge_tank_liquid_height = 40 # meters


fluid_specific_mass = 1e3 # kg/m3
fluid_viscosity = 1e-3 # kg/m3


tube_internal_diameter = 0.154 # meters
tube_length = 120 # meters 
tube_rugosity = 4.6e-2 # adimensional


'''
Leave empty (a.k.a {}) if there is no pipe fitting.
The expected format is: {type: quantity} where type is the id column of pipe_fitting_options.csv
Check assets/pipe_fitting_options.csv for the available types. To add more types, just add more lines to the said .csv.
You can select multiple types by adding more lines to the dictionary
'''
pipe_fittings = { # leave empty if there is no pipe fitting
    1: 5, # type (id column of pipe_fitting_options.csv) : quantity 
    16: 2
}


'''
Path to the .csv
H must be in meters and Q in m3/h
Check assets/bomb_curve_template.csv for an example.
'''
pump_curve_file_path = r''