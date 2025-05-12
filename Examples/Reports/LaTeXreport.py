#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 14:51:28 2025

@author: anton
"""
import SLiCAP as sl
import sympy as sp

sl.initProject("LATEX formatter") # Initialize the SLiCAP project
ltx = sl.formatter("latex")       # Initialize a LaTeX formatter

# Create a circuit object
cir = sl.makeCircuit("kicad/myPassiveNetwork/myPassiveNetwork.kicad_sch")

ltx.netlist("myPassiveNetwork.cir").save("netlist")

ltx.elementData(cir, label="tab-expanded", 
                caption="Expanded netlist").save("expanded")

ltx.parDefs(cir, label="tab-pardefs", 
            caption="Circuit parameter definitions").save("pardefs")

ltx.params(cir, label="tab-params", 
           caption="Undefined parameters").save("params")

# Obtain the MNA matrix equation of this network
matrixResult = sl.doMatrix(cir)
Iv = matrixResult.Iv
Dv = matrixResult.Dv
M  = matrixResult.M

# Save the matrix equation as LaTeX snippet
ltx.matrixEqn(Iv, M, Dv, label="eq-matrices").save("matrices")

# Evaluate the transfer of the network
transfer = sl.doLaplace(cir).laplace

# Save the transfer as a LaTeX displayed equation
ltx.eqn("V_out/V_in", transfer, label="eq-H1").save("H1")

# Save the transfer as a LaTeX inline expression
ltx.expr(transfer).save("H2")

# Save the transfer as a LaTeX inline equation
ltx.eqnInline("V_out/V_in", transfer).save("H3")

# Use the dictTable method to display a dictionary as a table
mydct = cir.parDefs
head = ["Name", "Value"]
ltx.dictTable(mydct, head, label='tab-mydct', 
              caption='Circuit parameters using the dictTable format ' +
              'and modified alternate row color.', 
              color="mygray").save('mydct')

# Coefficients of the transfer:
# Define a transfer function:
H_s = sl.doLaplace(cir).laplace
# Assign the gain, the normalized numerator coefficients and the 
# normalized denominator coefficients to the variable 'coeffs'
coeffs = sl.coeffsTransfer(H_s)
# Generate a LaTeX snippet of the coefficient table with the 
# LaTeX formatter 'ltx':
ltx.coeffsTransfer(coeffs, label="tab-coeffs", 
                   caption="Numerator and denominator coefficients of " +
                   "$H(s)$, $b_i$ and $a_i$, respectively").save("coeffs")

# Plot the magnitude plot
result = sl.doLaplace(cir, pardefs="circuit", numeric=True)
sl.plotSweep("dBmag", "dB magnitude plot of the transfer", result, 0.01,
             100, 500, sweepScale="M", funcType="dBmag")

dcVarResults = sl.doDCvar(cir)
ltx.dcvarContribs(dcVarResults, label="tab-dcvar", 
                  caption="dcvar analysis results").save("dcvar")

noiseResults = sl.doNoise(cir, pardefs="circuit")
ltx.noiseContribs(noiseResults, label="tab-noise", caption="Noise contributions").save("noise")

polesResult = sl.doPoles(cir, pardefs="circuit")
zerosResult = sl.doZeros(cir, pardefs="circuit")
pzResult    = sl.doPZ(cir, pardefs="circuit")
symZeros    = sl.doZeros(cir)

ltx.pz(polesResult, label="tab-poles", caption="Poles of the transfer").save("poles")
ltx.pz(zerosResult, label="tab-zeros", caption="Zeros of the transfer").save("zeros")
ltx.pz(pzResult, label="tab-pz", caption="Poles and zeros of the transfer").save("pz")
ltx.pz(symZeros, label="tab-symzeros", caption="Symbolic zeros of the transfer").save("symzeros")
ltx.expr(pzResult.DCvalue).save("dcValue")

f = ltx.file("../cir/myPassiveNetwork.cir", language="ltspice").save("f")

specs = []
f_min = 10
f_max = 10e6
v_n   = sl.rmsNoise(noiseResults, 'onoise', 10, 1e6)
specs.append(sl.specItem("f_min", "Lower limit noise bandwidth", f_min, 
                         units="Hz", specType="performance"))
specs.append(sl.specItem("f_max", "Upper limit noise bandwidth", f_max, 
                         units="Hz", specType="performance"))
specs.append(sl.specItem("v_n", "RMS output noise over noise bandwidth", 
                         v_n, units="V", specType="design"))
sl.specs2csv(specs, "specs.csv")
ltx.specs(specs, specType="performance", label="tab-performance", 
          caption="Performance specifications").save("performance")
ltx.specs(specs, specType="design", label="tab-design", 
          caption="Design specifications").save("design")

step_dict = {}
step_dict["method"] = "array"
step_dict["params"] = ["C_b", "R_ell"]
step_dict["values"] = [["100p", "250p", "500p"], [150, 100, 50]]
# Plot the magnitude plot
result = sl.doLaplace(cir, pardefs="circuit", numeric=True, stepdict=step_dict)
sl.plotSweep("dBmagStepped", "dB magnitude plot of the transfer", result, 0.01,
             100, 500, sweepScale="M", funcType="dBmag")
ltx.stepArray(step_dict["params"], step_dict["values"], label="tab-stepdict", caption="Step array").save("stepdict")
