import json
from .instrument import Instrument
from .unitcell import UnitCell
from .gisaxs import GISAXS
from. output import Output

def run_hipgisaxs(instrumentation_file, sample_file, output_file):


    # create instrumentation object
    with open(instrumentation_file, 'r') as f:
        instrument = Instrument(json.load(f))
        
    # create sample object
    with open(sample_file, 'r') as f:
        sample = UnitCell(json.load(f))
    
    gisaxs = GISAXS(instrument, sample)
    result = gisaxs.run()

    # Save the output
    with open(output_file) as f:
        output = Output(json.load(f))
    output.save(result)