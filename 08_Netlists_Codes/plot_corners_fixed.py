import numpy as np
import matplotlib.pyplot as plt

corners = ['tt', 'ff', 'ss', 'fs', 'sf']
corner_names = ['TT (Typical)', 'FF (Fast-Fast)', 'SS (Slow-Slow)', 'FS (Fast-Slow)', 'SF (Slow-Fast)']

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, (corner, name) in enumerate(zip(corners, corner_names)):
    filename = f'corner_{corner}_new.txt'
    print(f"Processing {filename}...")
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        # Find the first data section
        data = []
        in_data = False
        for line in lines:
            if 'Index' in line and 'time' in line:
                in_data = True
                continue
            if in_data and line.strip() and not line.startswith('----'):
                if 'Index' in line:
                    break
                try:
                    parts = line.strip().split()
                    if len(parts) >= 4 and parts[0].replace('.', '').replace('-', '').isdigit():
                        data.append([float(parts[1]), float(parts[2]), float(parts[3])])
                except:
                    pass
        
        if data:
            data = np.array(data)
            time = data[:, 0]
            v_in = data[:, 1]
            i_in = data[:, 2]
            
            dt = time[1] - time[0] if len(time) > 1 else 1e-9
            flux = np.cumsum(v_in) * dt
            flux_uwb = flux * 1e6
            current_pa = i_in * 1e12
            
            axes[idx].plot(flux_uwb, current_pa, 'b-', linewidth=1.5)
            axes[idx].set_title(name, fontsize=12)
            axes[idx].set_xlabel('Flux (μWb)', fontsize=10)
            axes[idx].set_ylabel('Current (pA)', fontsize=10)
            axes[idx].grid(True, alpha=0.3)
            axes[idx].axhline(0, color='black', linewidth=0.5)
            axes[idx].axvline(0, color='black', linewidth=0.5)
            
            print(f"  ✓ {name}: Flux range {flux_uwb.min():.3f} to {flux_uwb.max():.3f} μWb")
        else:
            axes[idx].text(0.5, 0.5, f'{name}\nNo data', ha='center', va='center')
            axes[idx].axis('off')
            print(f"  ✗ {name}: No data found")
    except Exception as e:
        print(f"  ✗ {name}: Error - {e}")
        axes[idx].text(0.5, 0.5, f'{name}\nError', ha='center', va='center')
        axes[idx].axis('off')

axes[5].axis('off')
plt.suptitle('Corner Analysis: Pinched Hysteresis Loops @ 10 kHz\n(9-MOSFET Meminductor)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/home/araj_7/Desktop/corner_phl_fixed.png', dpi=150)
plt.show()
print("\nPlot saved as corner_phl_fixed.png")
