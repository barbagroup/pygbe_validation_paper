import numpy
import time
import sys
import os
from argparse import ArgumentParser

import pygbe
from pygbe.util.read_data import read_fields
from pygbe.main import main

from cext_wavelength_scanning import create_diel_list, Cext_wave_scan, Cext_analytical


def read_inputs(args):
    """
    Parse command-line arguments to read arguments in main.
    """

    parser = ArgumentParser(description='Read path where input files are located')
    parser.add_argument('-if',
                        '--infiles',
                        type=str,
                        help="Absolute path where input files are located (downloaded from zenodo)")
    
    return parser.parse_args(args)
    


def main(argv=sys.argv):

    argv=sys.argv
    args = read_inputs(argv[1:])

    in_files_path = args.infiles

    #Import surface data
    wave_s, diel_rs, diel_is = numpy.loadtxt('../dielectric_data/4H-SIC_permittivity_10-12_microns.csv', skiprows=1, unpack=True)

    air_diel = [1. + 1j*0.] * len(wave_s)
    #Creating dielectric list first dielectric outside, then inside
    diel_list = [list(eps) for eps in zip(air_diel, diel_rs + 1j*diel_is)]

    #Set enviornment variable for PyGBe
    folder_path = in_files_path + 'cube_535nm'
    full_path = os.path.abspath(folder_path)+'/'
    os.environ['PYGBE_PROBLEM_FOLDER'] = full_path

    #Creating dictionary field. We will modify the 'E' key in the for loop.
    field_dict_pillars = read_fields(full_path + 'cube_15K.config')


    #Calculate Cext(lambda) for pillars' surface
    tic_ss = time.time()
    e_field = -1.
    wave, Cext_pillars = Cext_wave_scan(e_field, wave_s, diel_list, field_dict_pillars, full_path) 
    toc_ss = time.time()



    numpy.savetxt('../results_data/cube_535nm_res/'+'cube_15K'+'10-20microns.txt', 
                  list(zip(wave, Cext_pillars)),
                  fmt = '%.9f %.9f', 
                  header = 'lambda [Ang], Cext [nm^2]') 

    time_simulation = (toc_ss - tic_ss) 

    with open('../results_data/cube_535nm_res/Time_'+'cube_15K'+'.txt', 'w') as f:
        print('time_total: {} s'.format(time_simulation), file=f)

if __name__ == "__main__":
    main(sys.argv)
