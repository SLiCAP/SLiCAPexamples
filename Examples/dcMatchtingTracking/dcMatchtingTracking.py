#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 2023
Updated on Thu Jan 02 2025

@author: anton

voltage and current sources:

    - The 'dcvar' parameter is absolute variance (squared standard deviation
      sigma), in V^2 or A^2, respectively:

      V nodeP nodeN V value={V_DC} dcvar={(sigma_V*V_DC)^2}

    - Temperature dependency can be modeled by making the value a function of
      the absolute temperature T, or of a relative deviation from the
      default temperature:

      V nodeP nodeN R value={V_DC*(1+T_Delta*TC_V)}
      
      where T_Delta is the deviation from the default temperature, and TC_V the
      relative temperature coefficient.

    - Tolerances on the temperature coefficient can be added by letting the
      variance depend on temperature:

      V nodeP nodeN V value={V_DC*(1+T_Delta*TC_V)} dcvar={(sigma_V*V_DC)^2 + (sigma_TC_V*V_DC*T_Delta)^2}

    - Matching and temperature tracking for voltage sources and current sources
      have not (yet) been implemented.

Resistors

    - 'dcvar' parameter is the non matching part of the relative variance
      (squared relative standard deviation sigma). Hence, an individual relative
      standard deviation of 1% corresponds with 0.0001.

      R nodeP nodeN R value={R_a} dcvar={sigma_R^2}

      The temperature behavior can be modeled by letting the resistance depend 
      on temperature:

      R nodeP nodeN R value={R_a * (1 + T_Delta*TC_R)} dcvar={sigma_R^2}

      where T_Delta is the difference between the temperature at which the 
      resistance equals R_a, and the actual temperature. TC_R is the relative 
      temperature coefficient [1/K]. If this temperature dependency is applied 
      to multiple resistors, they are tracking over temperature.

      The 'dcvarlot' parameter holds the correlated part of the variance of the 
      value, as well as the correlated part of the variance of the temperature 
      coefficient.

      Below the definition of two resistors from one lot (lot_1).
      All resistors of this lot have a relative standard deviation 'sigma_R'.
      The standard deviation of their matching error is 'sigma_m_R'.
      The reproducible part of their temperature drift is modeled with TC_R and
      its standard deviation with sigma_TC_R. The standard deviation of
      temperature tracking error is sigma_T_tr_R

      R1 nodeP1 nodeN1 R value={R_a*(1+T_Delta*TC_R)} dcvar={sigma_m_R^2/2 + (sigma_TC_tr_R*T_Delta)^2/2} dcvarlot={lot_1}
      R2 nodeP2 nodeN2 R value={R_b*(1+T_Delta*TC_R)} dcvar={sigma_m_R^2/2 + (sigma_TC_tr_R*T_Delta)^2/2} dcvarlot={lot_1}
      .param lot_1 = {sigma_R^2 + (sigma_TC_R*T_Delta)^2}
"""
import SLiCAP as sl
import sympy as sp

def createOutput(cir):
    sl.params2html(cir)
    sl.head3html("Analysis results")
    dcVarResult = sl.doDCvar(cir, detector="V_out", pardefs="circuit")
    
    Vout = sp.simplify(dcVarResult.dcSolve[cir.depVars().index('V_out')])
    sl.text2html("DC output voltage")
    sl.eqn2html("V_out", Vout)
    
    sl.text2html("DC output voltage variance")
    sl.eqn2html("sigma_Vout^2", sp.simplify(dcVarResult.ovar))
    
    dcVarResult = sl.doDCvar(cir, detector="I_V1", pardefs="circuit")
    IV1 = sp.simplify(dcVarResult.dcSolve[cir.depVars().index('I_V1')])
    
    sl.text2html("DC current through V1")
    sl.eqn2html("I_V1", IV1)
    
    sl.text2html("Variance of DC current through V1")
    sl.eqn2html("sigma_IV1^2", sp.simplify(dcVarResult.ovar))

sl.initProject("DCVAR")

fileName = "dcMatchingTracking"
cir = sl.makeCircuit("kicad/" + fileName + "/" + fileName + ".kicad_sch", 
                     imgWidth = 1000)

sl.htmlPage("DC matching-tacking demo")
sl.head2html("Circuit diagram")
sl.img2html(fileName + ".svg", 1000)
sl.head2html("No tolerances and no temperature coefficients")

cir.defPar("TC_V", 0)          # Relative temperature coefficient of voltage source [1/K]
cir.defPar("TC_R", 0)          # Relative temperature coefficient of resistors [1/K]
cir.defPar("sigma_V", 0)       # Standard deviation of voltage source [V]
cir.defPar("sigma_R", 0)       # Relative standard deviation of resistors of lot_1 [-]
cir.defPar("sigma_m_R", 0)     # Relative standard deviation of mismatch between resistors from lot_1 [-]
cir.defPar("sigma_TC_R", 0)    # Standard deviation of relative temperature coefficient of resistors [1/K]
cir.defPar("sigma_TC_tr_R", 0) # Standard deviation of mismatch between relative temperature coefficients of resistors from lot_1 [1/K]

createOutput(cir)

###############################################################################
sl.head2html("Only DC voltage soure with standard deviation")
cir.delPar("sigma_V")
createOutput(cir)

###############################################################################
sl.head2html("Only DC voltage soure with temperature coefficient")
cir.defPar("sigma_V", 0)       # Standard deviation of voltage source [V]
cir.delPar("TC_V")
createOutput(cir)

###############################################################################
sl.head2html("Only DC voltage soure with standard deviation and temperature coefficient")
cir.delPar("sigma_V")
createOutput(cir)

###############################################################################
sl.head2html("Only (relative) standard deviation of resistor values with perfect matching")
cir.defPar("sigma_V", 0)       # Standard deviation of voltage source [V]
cir.defPar("TC_V", 0)          # Relative temperature coefficient of voltage source [1/K]
cir.delPar("sigma_R")
createOutput(cir)

###############################################################################
sl.head2html("Only (relative) standard deviation of resistor values with perfect matching and temperature tracking")
cir.delPar("TC_R")
createOutput(cir)

###############################################################################
sl.head2html("Only (relative) standard deviation of resistor values with imperfect matching and temperature tracking")
cir.delPar("sigma_m_R")
cir.delPar("sigma_TC_R")
cir.delPar("sigma_TC_tr_R")
createOutput(cir)

###############################################################################
sl.head2html("DC voltage soure with standard deviation and temperature coefficient and (relative) standard deviation of resistor values with imperfect matching and temperature tracking")
cir.delPar("TC_V")
cir.delPar("sigma_V")
cir.delPar("sigma_TC_V")
createOutput(cir)
