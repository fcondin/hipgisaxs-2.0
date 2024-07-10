import math
import numpy as np


from .detector import Detector

class Instrument:
    def __init__(self, **kwargs):
        self.detector = Detector(**kwargs['detector'])
        self.energy = kwargs['energy']
        self.distance = kwargs['distance']
        self.incident_angle = kwargs['incident_angle']
        self.ewald_radius = 2 * math.pi * self.energy / 1239.84 # in nm

