#### TAKEOFF ####
import numpy as np
from environmental_model import ISA
## INPUTS

m=2550;    # [kg] airplane mass
hc=10.000; # [ft] cruise flight altitude
hc=hc*0.3048;   # [m]
Vc=172;     # [KTAS] cruise flight altitude
Vc=Vc*0.5144;  # [m/s]
S = 19.4;   # [m^2] wing area 
Pmax = 750;    # [hp] max power 
Pmax=745.7*Pmax;   # [W]
Vs = 67;   # [knots] stall speed
Vs=Vs*0.5144;  # [m/s]
CD0c = 0.021; 
CD0fTO = 0.004;
CD0LG = 0.007;
b = 11.14; # [m] wing spam 
e = 0.86; 
DCLfTO = 0.4;
hTO=0; # [ft] takeoff altitude
g=9.80665; # [m/s^2] gravity


## Takeoff run

VR=1.1*Vs; # rotation speed
mu=0.04;   # tires friction coeff
etaTO=0.6; # propeler eficiency during takeoff run

# cruise flight CL
_,_,rho,_,_,_=ISA(hc,0); 
CLc=(2*m*g)/(rho*S*Vc**2)
 
# takeoff run CL 
CLTO=CLc+DCLfTO

# takeoff run C0
CD0TO=CD0c+CD0fTO+CD0LG;

# induced drag
A=b**2/S
K=1/(np.pi*e*A)

# takeoff run CD
CDTO = CD0TO + K*CLTO**2

# Takeoff run distance for a constant thrust 
F0 = etaTO*Pmax/VR # averge take off thrust
_,_,rhoTO,_,_,_=ISA(hTO,0);
SG=(m/(rhoTO*S*(mu*CLTO-CDTO)))*np.log(1+(VR**2/2)*(rhoTO*S*(mu*CLTO-CDTO))/(F0-mu*m*g));
print('Takeoff run distance:', SG, 'm');


# ROTATION
TR = 1 # [s] ROTATION TIME
SR = VR*TR
print('Takeoff run distance at rotation:', SR, 'm');

# TRANSITION

# VL0 and V2 speeds multiplicative factors (General aviation airplane)
kLO=1.1;
k2=1.2;  

# Average propeler efficiency
etaif = 0.8; # [-]

# Obstacle high (general aviation)
h0 = 50 # [ft]
h0=h0*0.3048 # m

# Reference speeds of the segment
VLO=kLO*Vs;V2=k2*Vs;

# Average speed multiplier factor
kif=(kLO+k2)/2;

# Average speed
Vif=kif*Vs;

# Average Thrust
Fif=etaif*Pmax/Vif;

# Average lift coefficient
CLmax=2*m*g/(rhoTO*S*Vs**2);
CLif=CLmax/kif**2;

# Average drag coefficient
CDif=CD0TO+K*CLif**2;

# Average drag force
Dif=0.5*rhoTO*Vif**2*S*CDif;

# Distance traveled on the ground during the segment
SA=np.sqrt(((m*g/(Fif-Dif))*((V2**2-VLO**2)/(2*g)+h0))**2-h0**2);

print('Transition roll distance:', SA, 'm');


# TOTAL

STO=SG+SR+SA;
print('Total takeoff distance:', STO, 'm');


























