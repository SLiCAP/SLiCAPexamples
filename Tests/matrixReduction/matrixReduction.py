#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 10:46:41 2025

@author: anton
"""

import SLiCAP as sl 
from SLiCAP.SLiCAPmatrices import _reduceCircuit

sl.initProject("Circuit reduction test")

cir = sl.makeCircuit("kicad/reduceCircuit/reduceCircuit.kicad_sch", imgWidth=400)

sl.ini.reduce_circuit = False

R = sl.doLaplace(cir, transfer=None, detector="V_o")
sl.matrices2html(R)

D1 = sl.det(R.M)

R.M, R.Iv, R.Dv = _reduceCircuit(R)
sl.matrices2html(R)

D2 = sl.det(R.M)