# Aircraft Performance Scripts: Takeoff and Landing Calculations  

This repository contains Python scripts to model and calculate the performance of an aircraft during takeoff and landing phases. These scripts are useful for aerospace engineering applications and include detailed aerodynamic and environmental considerations.  

## Scripts  

### `takeoff.py`  
This script calculates the components of the takeoff distance for an aircraft:  
- **Takeoff run distance:** The ground distance traveled during the acceleration phase up to the rotation speed.  
- **Rotation distance:** The distance covered during the rotation phase when the aircraft transitions from ground roll to lift-off.  
- **Transition roll distance:** The segment where the aircraft climbs and clears a specified obstacle height (typically 50 ft for general aviation).  

The script uses aerodynamic coefficients, power settings, and environmental parameters, such as air density, to model the takeoff phases. It also imports the **ISA (International Standard Atmosphere)** model from `environmental_model.py` to calculate atmospheric properties at different altitudes.  

### `landing.py`  
This script calculates the components of the landing distance for an aircraft:  
- **Final approach and flare distance:** The distance covered from the final approach to touchdown.  
- **Rotation/transition distance:** The distance traveled during the transition from touchdown to full weight on the wheels.  
- **Ground roll distance:** The distance required to decelerate the aircraft to a stop using aerodynamic and tire friction forces.  

Like the takeoff script, it uses aerodynamic coefficients, aircraft weight, and environmental parameters to determine the distances. The **ISA model** is utilized for atmospheric calculations.  

### `environmental_model.py`  
This module defines the **ISA (International Standard Atmosphere)** model. It calculates atmospheric properties such as:  
- Temperature  
- Pressure  
- Air density  
- Speed of sound  

These properties are computed for a given altitude and temperature deviation. The outputs are critical inputs for the takeoff and landing calculations.  

## Usage  
1. Ensure all scripts (`takeoff.py`, `landing.py`, `environmental_model.py`) are in the same directory.  
2. Modify the input parameters in `takeoff.py` or `landing.py` as needed.  
3. Run the scripts to compute takeoff and landing distances.  

## Applications  
These scripts are designed for:  
- Studying aircraft performance.  
- Aerodynamic modeling.  
- Aircraft design and analysis.  

---

Feel free to explore and adapt these scripts for your specific needs! Contributions are welcome.
