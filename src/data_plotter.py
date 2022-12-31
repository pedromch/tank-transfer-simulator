from numpy import linspace, concatenate
from matplotlib import pyplot as plt
from utils import per_second_to_per_hour

def plot_data(Qop, Qp, Hp, system_head_func, pump_head_func):
    
    Hop = system_head_func(Qop)
    
    Qmax = Qop*1.1 if Qop > max(Qp) else max(Qp)
    
    # TODO: make it possible to start from 0
    Qaxis = linspace(0.002, Qmax, 50)
    Hpaxis = pump_head_func(Qaxis)
    # TODO: standardize types being sent and retrieved from system_head_func
    Hsaxis = concatenate([system_head_func(Q) for Q in Qaxis])
    
    Hmax = max(concatenate([Hpaxis, Hsaxis]))*1.1

    _, ax = plt.subplots()
    # TODO: avoid calling per_second_to_per_hour multiple times
    ax.plot(per_second_to_per_hour(Qp), Hp, "ob", mfc='none', label="Pump Data Points")
    ax.plot(per_second_to_per_hour(Qaxis), Hpaxis, "b", label="Fitted Pump Curve")
    ax.plot(per_second_to_per_hour(Qaxis), Hsaxis, "g", label="System Curve")
    ax.plot(per_second_to_per_hour(Qop), Hop, "or", label="Operation Point")
    ax.annotate(f"Q = {per_second_to_per_hour(Qop)[0]:.2f}", xy=(per_second_to_per_hour(Qop),Hop), xytext=(-7,7), textcoords='offset points')
    ax.legend()
    ax.set_xlim(0, per_second_to_per_hour(Qmax*1.1))
    ax.set_xlabel(r"Q (m$^3$/h)")
    ax.set_ylim(0, Hmax*1.1)
    ax.set_ylabel(r"H (m)")
    ax.set_title("Pump Curve, System Curve and Operation Point")
    plt.show()