#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Do nothing

###############################################################################
Author: Katja Weigel (IUP, Uni Bremen, Germany)
Application: Evgenia Galytska
###############################################################################

Description
-----------
    Do nothing

Configuration options
---------------------
    None

###############################################################################

"""

import logging
import os
from esmvaltool.diag_scripts.shared import run_diagnostic
# import iris
# import numpy as np
# from scipy import stats
# import esmvaltool.diag_scripts.shared as e
# import esmvaltool.diag_scripts.shared.names as n
# import matplotlib
# import matplotlib.pyplot as plt
# matplotlib.use('Agg')

logger = logging.getLogger(os.path.basename(__file__))

def main(cfg):
    """Run the diagnostic.

    Parameters
    ----------
    cfg : dict
        Configuration dictionary of the recipe.

    """
    ###########################################################################
    # Read recipe data
    ###########################################################################
    # Dataset data containers
#    data = e.Datasets(cfg)
#    logging.debug("Found datasets in recipe:\n%s", data)

    # Variables
 #   var = e.Variables(cfg)
 #   logging.debug("Found variables in recipe:\n%s", var)

    ###########################################################################
    # Read data
    ###########################################################################

   
    ###########################################################################
    # Process data
    ###########################################################################


if __name__ == '__main__':
    with run_diagnostic() as config:
        main(config)
