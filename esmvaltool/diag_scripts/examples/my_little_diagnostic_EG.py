"""
Look at this module for guidance how to write your own.

Read the README_PERSONAL_DIAGNOSTIC file associated with this example;

Module for personal diagnostics (example).
Internal imports from exmvaltool work e.g.:

from esmvalcore.preprocessor import regrid
from esmvaltool.diag_scripts.shared.supermeans import get_supermean

Pipe output through logger;

Please consult the documentation for help with esmvaltool's functionalities
and best coding practices.
"""
# place your module imports here:

# operating system manipulations (e.g. path constructions)
import os

# to manipulate iris cubes
import iris
import matplotlib.pyplot as plt
import numpy as np

# import internal esmvaltool modules here
from esmvaltool.diag_scripts.shared import group_metadata, run_diagnostic, save_data
from esmvalcore.preprocessor import area_statistics
from esmvaltool.diag_scripts.shared._base import get_diagnostic_filename

def _plot_time_series(cfg, cube, dataset):
    """
    Example of personal diagnostic plotting function.

    Arguments:
        cfg - nested dictionary of metadata
        cube - the cube to plot
        dataset - name of the dataset to plot

    Returns:
        string; makes some time-series plots

    Note: this function is private; remove the '_'
    so you can make it public.
    """
    # custom local paths for e.g. plots are supported -
    # here is an example
    # root_dir = '/group_workspaces/jasmin2/cmip6_prep/'  # edit as per need
    # out_path = 'esmvaltool_users/valeriu/'   # edit as per need
    # local_path = os.path.join(root_dir, out_path)
    # but one can use the already defined esmvaltool output paths
    local_path = cfg['plot_dir']
    save_path = cfg['work_dir']
    
#    save_data('ERA5_PV', cfg, cube)
    # do the plotting dance
    plt.plot(cube.data, label=dataset)
    plt.xlabel('Time (months)')
#    plt.ylabel('Area average')
    plt.title('Time series')
    plt.tight_layout()
    plt.grid()
    plt.legend()
    png_name = 'Time_series_' + dataset + '.png'
    plt.savefig(os.path.join(local_path, png_name))
    plt.close()

    # no need to brag :)
    return 'I made some plots!'


def run_my_diagnostic(cfg):
    """
    Simple example of a diagnostic.
       Returns:
        string; runs the user diagnostic

    """
    # assemble the data dictionary keyed by dataset name
    # this makes use of the handy group_metadata function that
    # orders the data by 'dataset'; the resulting dictionary is
    # keyed on datasets e.g. dict = {'MPI-ESM-LR': [var1, var2...]}
    # where var1, var2 are dicts holding all needed information per variable
    my_files_dict = group_metadata(cfg['input_data'].values(), 'dataset')
#    print ("DICTIONARY", my_files_dict)

    # iterate over key(dataset) and values(list of vars)
#    for key, value in my_files_dict.items():
#        if key == "ERA5":
    for key, value in my_files_dict.items():
        diagnostic_file = get_diagnostic_filename(key, cfg)
        if key == "ERA5":
            for item in value: 
                if item['preprocessor'] == 'pv':
                    pv = iris.load_cube(item['filename'])
                    pv = pv.collapsed('air_pressure', iris.analysis.MEAN)
                    pv.data *=-1
                    pv.var_name = 'PV'
                elif item['preprocessor'] == 'pre_tas':
                    tas = iris.load_cube(item['filename'])
                    tas.var_name = 'Arctic_temperature'
                elif item['preprocessor'] == 'qbo':
                    qbo = iris.load_cube(item['filename'])
                    qbo.var_name = 'QBO'
                elif item['preprocessor'] == 'pressure_ural':
                    psl_Ural = iris.load_cube(item['filename'])
                    psl_Ural.var_name = 'Psl_Ural'
                elif item['preprocessor'] =='pressure_sib':
                    psl_Sib = iris.load_cube(item['filename'])
                    psl_Sib.var_name = 'Psl_Sib'
                elif item['preprocessor'] =='pressure_aleut':
                    psl_Aleut = iris.load_cube(item['filename'])
                    psl_Aleut.var_name = 'Psl_Aleut'
                elif item['preprocessor'] =='zonal_wind':
                    zon_wind = iris.load_cube(item['filename'])
                    zon_wind.var_name = 'zonal_wind'
            cube_list = iris.cube.CubeList([pv, tas, qbo, psl_Ural, psl_Sib, psl_Aleut, zon_wind])
            iris.save(cube_list, diagnostic_file)
        else:
            for item in value: 
                if item['preprocessor'] == 'bk_ice':
                    sic_BK = iris.load_cube(item['filename'])
                    sic_BK.var_name = 'BK_sic'
                elif item['preprocessor'] == 'ok_ice':
                    sic_Ok = iris.load_cube(item['filename'])
                    sic_Ok.var_name = 'Ok_sic'
            cube_list = iris.cube.CubeList([sic_BK, sic_Ok])
            iris.save(cube_list, diagnostic_file)

#        _plot_time_series(cfg, pv_fin, key)



    # that's it, we're done!
    return 'I am done with my first ESMValTool diagnostic!'


if __name__ == '__main__':
    # always use run_diagnostic() to get the config (the preprocessor
    # nested dictionary holding all the needed information)
    with run_diagnostic() as config:
        # list here the functions that need to run
        run_my_diagnostic(config)
