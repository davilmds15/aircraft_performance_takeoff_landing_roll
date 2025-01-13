#### LANDING ####
import numpy as np
from environmental_model import ISA

## INPUTS

mL = 66000  # [lb] landing mass
mL = 0.453592 * mL  # [kg]
mu = 0.4  # [-] friction coefficient
CLmax = 2.39  # Maximum lift coefficient
S = 950  # [ft^2] wing area
S = S * 0.3048**2  # [m^2]
CD0 = 0.015  # Zero-lift drag coefficient
k = 0.055  # Lift-induced drag factor
CLL = 0.1  # Lift coefficient during ground roll
g = 9.80665  # [m/s^2] gravity

# Multiplicative factors
# Intermediate values suggested by the literature were used
k2 = 1.25
kTD = 1.15

# Obstacle height
h0 = 50  # [ft]
h0 = h0 * 0.3048  # [m]

# Rotation time
TR = 2.5  # [s]

## FINAL APPROACH AND FLARE

# Sea-level air density
_, _, rho0, _, _, _ = ISA(0, 0)

# Stall speed
Vs = np.sqrt(2 * mL * g / (rho0 * S * CLmax))

# Speed V2
V2 = k2 * Vs

# Touchdown speed
VTD = kTD * Vs

# Average speed during the segment
kA = (k2 + kTD) / 2
VA = kA * Vs

# Average lift coefficient during the segment
CLA = CLmax / kA**2

# Average drag coefficient during the segment
CDA = CD0 + k * CLA**2

# Average drag force during final approach and flare
DA = 0.5 * rho0 * VA**2 * S * CDA

# Distance traveled
SA = np.sqrt(((mL * g / DA) * (h0 + (1 / (2 * g)) * (V2**2 - VTD**2)))**2 - h0**2)

print('Distance traveled on the ground during final approach and flare:', SA, 'm')

## ROTATION

SR = VTD * TR

print('Distance traveled during transition/rotation:', SR, 'm')

## GROUND ROLL

# Drag coefficient during ground roll
CDL = CD0 + k * CLL**2

# Distance traveled
SG = (mL / (rho0 * S * (CDL - mu * CLL))) * np.log(1 + ((rho0 * S * (CDL - mu * CLL)) / (mu * mL * g)) * (VTD**2 / 2))
print('Distance traveled during ground roll:', SG, 'm')

## TOTAL LANDING DISTANCE
SL = SA + SR + SG
print('Total landing distance:', SL, 'm')
