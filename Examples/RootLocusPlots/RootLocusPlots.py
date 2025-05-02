#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 09:09:40 2025

@author: anton
"""

import SLiCAP as sl 

sl.initProject("Root Locus Plots")
cir = sl.makeCircuit("kicad/RootLocusPlots/RootLocusPlots.kicad_sch", 
                     imgWidth=800)

# The classical root-locus plot shows the poles of the gain while
# varying (stepping) the DC gain of the operational amplifier.

# Create a step dictionary:
step_dict = {}
step_dict['params'] = "A_0"
step_dict['method'] = "lin"
step_dict['start']  = 0 
step_dict['stop']   = cir.getParValue("A_0")
step_dict['num']    = 100

# Create the poles analysis result using substitution of parameters,
# numeric=True, and stepdict=step_dict
RL1      = sl.doPoles(cir, pardefs='circuit', numeric=True, stepdict=step_dict)

# Create the root-locus plot
RL1_plot = sl.plotPZ("RL1", "Root-locus plot", RL1, show=True)

# Notice
# 1. The non-square plot
#    - We will resize the plot and use a MHz scale
# 2. The start points are not visible because there are no poles if A_0 = 0
#    - We will use a start value close to zero

step_dict["start"] = 1e-6

RL2      = sl.doPoles(cir, pardefs='circuit', numeric=True, stepdict=step_dict)
RL2_plot = sl.plotPZ("RL2", "Root-locus plot", RL2, xmin=-25, xmax=0, 
                     xscale="M", ymin=-12.5, ymax=12.5, yscale="M", 
                     show=True)

# Another interesting root-locus plot shows the pole positions while
# varying the load capacitance:
    
step_dict['params'] = "C_ell"
step_dict['start']  = 0 
step_dict['stop']   = cir.getParValue("C_ell")
step_dict['num']    = 100

RL3      = sl.doPoles(cir, pardefs='circuit', numeric=True, stepdict=step_dict)
RL3_plot = sl.plotPZ("RL3", "Root-locus plot", RL3, xmin=-25, xmax=0, 
                     xscale="M", ymin=-12.5, ymax=12.5, yscale="M", 
                     show=True)