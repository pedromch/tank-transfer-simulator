from input import *
from input_validator import validate as validate_input
from data_plotter import plot_data
from calculations import calculate
from utils import get_csv_as_dict, per_hour_to_per_second
from constants import PUMP_CURVE_HEAD_COLUMN_NAME, PUMP_CURVE_VOLUMETRIC_FLOW_COLUMN_NAME

validate_input(
    h1=suction_tank_liquid_height,
    h2=discharge_tank_liquid_height,
    rho=fluid_specific_mass,
    mi=fluid_viscosity,
    Di=tube_internal_diameter,
    L=tube_length,
    eps=tube_rugosity,
    pipe_fittings=pipe_fittings,
    pump_curve_file_path=pump_curve_file_path
)

pump_curve_dict = get_csv_as_dict(pump_curve_file_path)
Qp, Hp = [pump_curve_dict[key] for key in [PUMP_CURVE_VOLUMETRIC_FLOW_COLUMN_NAME, PUMP_CURVE_HEAD_COLUMN_NAME]]
Qp = per_hour_to_per_second(Qp)

Qop, system_head_func, pump_head_func = calculate(
    h1=suction_tank_liquid_height,
    h2=discharge_tank_liquid_height,
    rho=fluid_specific_mass,
    mi=fluid_viscosity,
    Di=tube_internal_diameter,
    L=tube_length,
    eps=tube_rugosity,
    Qp=Qp,
    Hp=Hp,
    pipe_fittings=pipe_fittings
)


plot_data(
    Qop=Qop,
    Qp=Qp,
    Hp=Hp,
    system_head_func=system_head_func,
    pump_head_func=pump_head_func
)

