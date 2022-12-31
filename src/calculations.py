from numpy import poly1d as polynomial_function_generator, polyfit as get_polynomial_coeficcients, mean, sqrt, log10, linspace
from constants import GRAVITY as G, PUMP_CURVE_HEAD_COLUMN_NAME, PUMP_CURVE_VOLUMETRIC_FLOW_COLUMN_NAME, SOLVER_DEFAULT_METHOD
from utils import get_circle_area, get_pipe_fitting_options_file_path
import matplotlib.pyplot as plt # remove because plot will be in another file
from utils import get_csv_as_dict # remove because plot will be in another file
from scipy.optimize import root as solve
import pandas as pd

def calculate(h1, h2, rho, mi, Di, L, eps, Qp, Hp, pipe_fittings):

    get_fitted_pump_head = polynomial_function_generator(get_polynomial_coeficcients(x=Qp, y=Hp, deg=2))
    
    Ac = get_circle_area(Di)
    
    Leq_D = get_equivalent_length_per_diameter(pipe_fittings)


    def get_system_head(Q):

        v = Q/Ac
        
        Re = get_reynolds(v, rho, Di, mi)
         
        f = get_friction_factor(Re, eps, Di)
        
        HT = f * (L/Di + Leq_D) * v**2/(2*G)

        return (h2 - h1) + HT
    
    
    f_obj = lambda Q: abs(get_system_head(Q) - get_fitted_pump_head(Q))
    
    Qguess = mean(Qp)
    Qop = solve(f_obj, Qguess, method=SOLVER_DEFAULT_METHOD).x

    return Qop, get_system_head, get_fitted_pump_head


def get_equivalent_length_per_diameter(pipe_fittings):
    
    file_path = get_pipe_fitting_options_file_path()
    options = pd.read_csv(file_path)
    
    equivalent_L_D = 0
    for id, quantity in pipe_fittings.items():
        L_D = options.loc[options.id == id, "L/D"].item()
        equivalent_L_D += quantity * L_D
    
    return equivalent_L_D


def get_reynolds(v, rho, D, mi):
    return D*v*rho/mi


def get_friction_factor(Re, eps, D):
    is_laminar = Re < 2100
    if is_laminar:
        return get_laminar_friction_factor(Re)
    
    rugosity_is_zero = eps == 0
    if rugosity_is_zero:
        return get_blausius_friction_factor(Re)
    
    return get_colebrook_friction_factor(Re, eps, D)


def get_blausius_friction_factor(Re):
    return 0.316/Re**0.25


def get_colebrook_friction_factor(Re, eps, D):
    
    f_obj = lambda f: 1/sqrt(f) + 2*log10((eps/D)/3.7 + 2.51/(Re*sqrt(f)))
    
    return solve(f_obj, 0.1, method=SOLVER_DEFAULT_METHOD).x


def get_laminar_friction_factor(Re):
    return 64/Re
