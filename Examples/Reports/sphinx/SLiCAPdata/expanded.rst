.. _tab-expanded:
.. csv-table:: Expanded netlist
    :header: "ID", "Nodes", "Refs", "Model", "Param", "Symbolic", "Numeric"
    :widths: auto

    "C1", "0 out ", "", "C", "value", :math:`C_{\mathrm{a}}`, :math:`2.5 \cdot 10^{-8}`
    "", "", "", "", "vinit", :math:`0`, :math:`0`
    "C2", "out 1 ", "", "C", "value", :math:`C_{\mathrm{b}}`, :math:`2.5 \cdot 10^{-10}`
    "", "", "", "", "vinit", :math:`0`, :math:`0`
    "L1", "1 out ", "", "L", "value", :math:`L`, :math:`1.0 \cdot 10^{-6}`
    "", "", "", "", "iinit", :math:`0`, :math:`0`
    "R1", "1 in ", "", "R", "value", :math:`R_{\mathrm{s}}`, :math:`150`
    "", "", "", "", "noisetemp", :math:`T`, :math:`300`
    "", "", "", "", "noiseflow", :math:`0`, :math:`0`
    "", "", "", "", "dcvar", :math:`\sigma_{\mathrm{R1}}^{2}`, :math:`0.0004`
    "", "", "", "", "dcvarlot", :math:`0`, :math:`0`
    "R2", "out 0 ", "", "R", "value", :math:`R_{\ell}`, :math:`50`
    "", "", "", "", "noisetemp", :math:`T`, :math:`300`
    "", "", "", "", "noiseflow", :math:`0`, :math:`0`
    "", "", "", "", "dcvar", :math:`\sigma_{\mathrm{R2}}^{2}`, :math:`0.0001`
    "", "", "", "", "dcvarlot", :math:`0`, :math:`0`
    "V1", "in 0 ", "", "V", "value", :math:`\frac{1}{s}`, :math:`\frac{1}{s}`
    "", "", "", "", "noise", :math:`S_{\mathrm{v}}`, :math:`4.0 \cdot 10^{-18}`
    "", "", "", "", "dc", :math:`V_{\mathrm{DC}}`, :math:`5`
    "", "", "", "", "dcvar", :math:`V_{\mathrm{DC}}^{2} \sigma_{\mathrm{V}}^{2}`, :math:`0.0625`

