import numpy as np
import json


horizontal = (-0.5, 0.5, 512)
vertical = (0, 1, 512)
incident = 0.16

alpha = np.linspace(np.deg2rad(vertical[0]),   np.deg2rad(vertical[1]),   vertical[2])
theta = np.linspace(np.deg2rad(horizontal[0]), np.deg2rad(horizontal[1]), horizontal[2])
theta, alpha  = np.meshgrid(theta, alpha)



config = {
    'wavelen': 0.123984, # nanometer
    'incident': 0.16,
    'theta': theta.tolist(),
    'alpha': alpha.tolist(),
    'delta': 1.0E-06,
    'beta':  1.E-08,
    'datafile': '/home/dkumar/data/roth/Location_xyz_rot_XYZEul.npy',
    'cylinder': { 'radius': 10., 'height': 100 }
}

with open('../json/config.json', 'w') as fp:
    json.dump(config, fp)

