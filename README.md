# Meminductor Emulator Project - Final Submission

## Project Title
Electronically Tunable MOSFET-C Only Meminductor Emulator and Its Application



## Folder Structure

| Folder | Contents |
|--------|----------|
| 01_PHL_Results | Pinched Hysteresis Loop at 10 kHz |
| 02_Frequency_Sweep | PHL at 10kHz, 50kHz, 100kHz, 200kHz |
| 03_Voltage_Sweep | PHL at 0.05V, 0.1V, 0.2V, 0.3V |
| 04_Corner_Analysis | TT, FF, SS, FS, SF corners |
| 05_Monte_Carlo | 200 runs, Gaussian distribution |
| 06_Chaotic_Oscillator | Double scroll attractor |
| 07_Neural_Spikes | Spike generation (Fig. 15) |
| 08_Netlists_Codes | ngspice netlists and Python scripts |
| 09_Papers | Reference papers |
| 10_Simulation_Reports | Raw simulation output data |

## Key Results Summary

- ✅ Pinched Hysteresis Loop @ 10 kHz
- ✅ Frequency sweep validates 1/ω² term
- ✅ Voltage sweep validates Vm term
- ✅ Corner analysis (5 corners) complete
- ✅ Monte Carlo (200 runs, 5% variation)
- ✅ Chaotic oscillator - double scroll attractor
- ✅ Neural spike generator (Fig. 15)

## How to Run

```bash
cd 08_Netlists_Codes
ngspice -b meminductor_final.cir > output.txt
python3 plot_phl_enhanced.py
