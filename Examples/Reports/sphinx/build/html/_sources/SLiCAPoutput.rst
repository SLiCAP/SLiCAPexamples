=============
SLiCAP output
=============

In the next sections we will describe SLiCAP functions that generate data that can directly be imported in ReStructuredText files.

makeCircuit()
=============

If KiCad or Lepton-EDA is used as schematic capture program, `makeCircuit()` creates drawing size images in `.svg` and `.pdf` format in the images folder (see section :ref:`Project file locations`).

.. literalinclude:: ../../RSTreport.py
    :lines: 13-16
    :linenos:
    :lineno-start: 13

The RST code to include the schematic circuit diagram of `cir` and a reference to it is: 

.. literalinclude:: SLiCAPoutput.rst
    :lines: 26-34
    :linenos:
    :lineno-start: 27

**This renders as:**

:numref:`fig-myPassiveNetwork` shows the simple RC circuit.

.. _fig-myPassiveNetwork:
.. Figure:: ../../img/myPassiveNetwork.svg
    :width: 800px
    :align: center
    :alt: Passive network
    
    Passive network

The netlist file that is created with `makeCircuit()` can be displayed in the Sphinx document using:

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 85
    :lineno-start: 85

**This will render as follows:**

.. literalinclude:: ../../cir/myPassiveNetwork.cir

plot(), plotSweep(), and plotPZ()
=================================

:numref:`fig-dBmag` shows the `dBmag` plot of the source-to-load transfer of the circuit.

.. _fig-dBmag:

.. Figure:: ../../img/dBmag.svg
    :width: 600px
    :align: center
    :alt: dB magnitude plot of the source-detector transfer

    dB magnitude plot of the source-detector transfer

The SLiCAP code for creating this plot is:

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 66-69
    :lineno-start: 66

The RST source for including it is:

.. literalinclude:: SLiCAPoutput.rst
    :linenos:
    :lines: 52-59
    :lineno-start: 59

