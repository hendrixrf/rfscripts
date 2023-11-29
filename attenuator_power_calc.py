import numpy as np
import matplotlib.pyplot as plt


def show():
    print("Power calculations for PI-type attenuators")
    print("")
    print("Vin     R2    Vout")
    print("---|---/\/---|---")
    print("   |         |")
    print("   \         \\")
    print("R1 /      R3 /")
    print("   \         \\")
    print("   |         |")
    print("   |         |")
    print("-----------------")

def calculate_power_on_resistors(Pin_dBm, R1, R2, R3):
    Pin_W = (10**(Pin_dBm/10))/1000
    Vin_rms = np.sqrt(50*Pin_W)
    PR1 = (Vin_rms**2)/R1
    PR2 = (Vin_rms*(1-(R3/(R2+R3)))**2)/R2
    PR3 = ((Vin_rms*(R3/(R2+R3)))**2)/R3
    print("")
    print("R1 {:.4f} W".format(PR1))
    print("R2 {:.4f} W".format(PR2))
    print("R3 {:.4f} W".format(PR3))


def calculate_attenuator_resistors(att_db, Pin_dB=30):
    L = 10**(att_db/10)
    A = (L+1)/(L-1)
    
    R2 = (L-1)/2*np.sqrt(50*50/L)
    R1 = 1/((A/50)-(1/R2))
    R3 = R1
    show()
    print("For Pin={} dBm".format(Pin_dB))
    print("")
    print("R1 {:.2f} Ohm".format(R1))
    print("R2 {:.2f} Ohm".format(R2))
    print("R3 {:.2f} Ohm".format(R3))

    calculate_power_on_resistors(Pin_dB, R1, R2, R3)

calculate_attenuator_resistors(3.7, 20)

#values = np.linspace(0, 30, 31)

#vout_peak_for_dbm = 2*np.sqrt(2*50*1e-3*10**(values/10))

#vout_rms = vout_peak_for_dbm / np.sqrt(2)

#table = {}

#for A, B in zip(values, vout_peak_for_dbm):
#    table[A] = B

#print(table)
#plt.plot(values, vout_peak_for_dbm)
#plt.show()
