=================
Formatter methods
=================

.. include:: ../SLiCAPdata/substitutions.rst

The ReStructuredText formatter in SLiCAP generates *RST* snippets that can be imported in *RST* documents using the `.. include:: <file name>` role or the variable substitution role `|<variable name>|`. The `RST` formatter needs to be initialized. An example of the initialization of this formatter is shown below (see line 11).

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 1-11
    :lineno-start: 1
    
In this script, variables for inline substitution are saved in the file `substitutions.rst` in the rst-snippet directory (see ref:`Project file locations`).

This file is included where ever needed. In `this <../../../sphinx/source/FormatterOutput.rst>`_ document:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 5
    :lineno-start: 5

In the following sections we will discuss the rst formatter methods.

coeffsTransfer()
================

**coeffsTransfer(Coeffs, label="", caption="", position=0)**

This method is used to display the numerator and denominator coefficients of a rational function in the form of a table.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 54-65
    :lineno-start: 54

Let :math:`H(s)=` |H2|

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 50-52
    :lineno-start: 50
    
**This renders as:**

:numref:`tab-coeffs` shows the numerator and denominator coefficients of the Laplace variable :math:`s` of :math:`H(s)`.

.. include:: ../SLiCAPdata/coeffs.rst

dcvarContribs()
===============

**dcvarContribs(resultObject, label="", caption="", position=0)**

The individual contributions of independent DC error sources to the detector-referred and source-referred dc variance can be exported in the form of a table.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 72-74
    :lineno-start: 72

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 77-79
    :lineno-start: 77
    
**This renders as:**

The result is shown in :numref:`tab-dcvar`

.. include:: ../SLiCAPdata/dcvar.rst

dictTable()
===========

**dictTable(dct, head=None, label="", caption="", position=0)**

This method displays the key-value pairs of a dictionary in the form of a table.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 48-52
    :lineno-start: 48

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 104-106
    :lineno-start: 104
    
**This renders as:**

The result is shown in :numref:`tab-mydct`.  

.. include:: ../SLiCAPdata/mydct.rst

elementData()
=============

**elementData(circuitObject, label="", caption="", position=0)**

This method displays the expanded netlist of a circuit object in the form of a table.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 18,19
    :lineno-start: 18

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 131-133
    :lineno-start: 131
    
**This renders as:**

:numref:`tab-expanded` shows the result.

.. include:: ../SLiCAPdata/expanded.rst

eqn()
=====

**eqn(LHS, RHS, units="", label="", multiline=False, position=0)**

The formatter method `eqn()` creates an RST snippet of a displayed and numbered equation.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 39,40
    :lineno-start: 39

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 158-160
    :lineno-start: 158
    
**This renders as:**

The transfer function is shown in :eq:`eq-H1`.

.. include:: ../SLiCAPdata/H1.rst

If `multiline=True` SLiCAP breaks the equation in parts of a sum or a product.

eqnInline()
===========

**eqnInline(LHS, RHS, units="", name="")**

The method `eqnInline()` produces an RST snippet for an inline equation.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 45,46
    :lineno-start: 45

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 187
    :lineno-start: 187

**This renders as:**

You can write :eq:`eq-H1` inline as: |H3|

expr()
======

**expr(expr, units="", name="")**

The method `expr()` creates an RST snippet of an inline expression.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 42,43
    :lineno-start: 42

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 212
    :lineno-start: 212

**This renders as:**

The transfer can be written as: |H2|

file()
======

**file(fileName, lineRange=None, firstNumber=None, position=0)**

The method `file()` generates an RST snippet for displaying a code file.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 91
    :lineno-start: 91

Please notice the file path relative to the RST document.

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 239
    :lineno-start: 239

**This renders as:**

.. include:: ../SLiCAPdata/f.rst

matrixEqn()
===========

**matrixEqn(Iv, M, Dv, label="", position=0)**

The method `matrixEqn()` generates an RST snippet for a displayed matrix equation. `Iv`, `M`, and `Dv` must be Sympy matrices, representing the vector with independent variables, the transfer matrix, and the vector with dependent variables, respectively.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 27-34
    :lineno-start: 27

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 264-266
    :lineno-start: 264

**This renders as:**

The matrix equation of the network is given in :eq:`eq-matrices`.

.. include:: ../SLiCAPdata/matrices.rst

netlist()
=========

**netlist(netlistFile, lineRange=None, firstNumber=None, position=0)**

This method creates a `.. include::` statement for a SLiCAP netlist file.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 16
    :lineno-start: 16

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 291
    :lineno-start: 291

**This renders as:**

.. include:: ../SLiCAPdata/netlist.rst

noiseContribs()
===============

**noiseContribs(resultObject, label="", caption="", position=0")**

The method `noiseContribs()` creates a table with noise sources and their contributions to the source-referred noise and the detector-referred noise.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 76-78
    :lineno-start: 76

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 316
    :lineno-start: 318

**This renders as:**

The noise contributions are listed in :numref:`tab-noise`.

.. include:: ../SLiCAPdata/noise.rst

params()
========

**params(circuitObject, label="", caption="", position=0)**

This method creates a single-column table with names of undefined parameters.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 24-25
    :lineno-start: 24

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 343
    :lineno-start: 345

This renders as:

Undefined parameters are given in :numref:`tab-params`.

.. include:: ../SLiCAPdata/params}

parDefs()
=========

**parDefs(circuitObject, label="", caption="", position=0)**

This method creates a single-column table with circuit parameter definitions.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 21-22
    :lineno-start: 21

**RST code:**

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 370-372
    :lineno-start: 370
    
**This renders as:**

Parameter definitions are given in numref:`tab-pardefs`.

.. include:: ../SLiCAPdata/pardefs.rst

pz()
====

**pz(resultObject, label="", append2caption="", position=0)**

This method creates RST table snippets for results of pole-zero analysis results.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 76-78
    :lineno-start: 76

**RST code** for the poles table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 397-399
    :lineno-start: 397

**This renders as:**

The numeric poles are listed in :numref:`tab-poles`.

.. include:: ../SLiCAPdata/poles.rst

**RST code** for the symbolic zeros table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 410-412
    :lineno-start: 410

**This renders as:**

The symbolic zeros are listed in :numref:`tab-symzeros`.

.. include:: ../SLiCAPdata/symzeros.rst

**RST code** for the numeric zeros table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 425
    :lineno-start: 27

**This renders as:**

The numeric zeros are listed in :numref:`tab-zeros`.

.. include:: ../SLiCAPdata/zeros.rst

**RST** code for the numeric poles-zeros table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 436-438
    :lineno-start: 436

**This renders as:**

The poles and zeros are listed in :numref:`tab-pz`.

.. include:: ../SLiCAPdata/pz.rst

The DC value of the transfer equals: |dcValue|

specs()
=======

**specs(specs, specType, label="", caption="", position=0)**

This method exprots an RST snippet for a specification tabel.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 93-101
    :lineno-start: 93

**RST code** for the performance specifications table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 465-467
    :lineno-start: 465

**This renders as:**

The performance specifications are listed in :numref:`tab-performance`.

.. include:: ../SLiCAPdata/performance.rst

**RST code** for the design specifications table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 478-480
    :lineno-start: 478

**This renders as:**

The design specifications are listed in :numref:`tab-design`.

.. include:: ../SLiCAPdata/design.rst

stepArray()
===========

**stepArray(stepVars, stepArray, label="", caption="", position=0)**

This method exports an RST table snippet with step-data for array-type stepping.

**SLiCAP code:**

.. literalinclude:: ../../RSTreport.py
    :linenos:
    :lines: 103-112
    :lineno-start: 103

**RST code** for the step array table:

.. literalinclude:: FormatterOutput.rst
    :linenos:
    :lines: 513-515
    :lineno-start: 513

.. _fig-dBmagStepped:
.. Figure:: ../../img/dBmagStepped.svg
    :width: 600px
    :align: center
    :alt: dB magnitude plot of the source-to-load transfer
    
    dB magnitude plot of the source-to-load transfer

**This renders as:**

The step values that apply to :numref:`fig-dBmagStepped` are shown in :numref:`tab-stepdict`.

.. include:: ../SLiCAPdata/stepdict.rst

