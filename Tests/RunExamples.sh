#!/bin/bash
declare -A test_cirs
# test_cirs is a dictionary with the directory as a key and the value as the run file
test_cirs["balancedCircuits"]="balancedCircuitsProject.py"
##test_cirs["CSstage"]="CSresnoise.py"
test_cirs["FilterDesign"]="LR4project.py"
test_cirs["myFirstRCnetwork"]="myFirstRCnetwork.py"
test_cirs["noiseFigure"]="noiseFigures.py"
mkdir allhtml
cp Template.html index.html
#This will make sure no plots are shown:
export MPLBACKEND=svg #For plotting with Matplotlib on the 'SVG' backend
for key in "${!test_cirs[@]}"; do
    cd $key
    python ${test_cirs[$key]}
    mkdir ../allhtml/$key
    mv  -v html/* ../allhtml/$key
    cd ..
    echo " <p><a href=\"./${key}/index.html\"> Link To ${key} Test</a></p>" >> index.html
done
echo "</body></html>" >> index.html
mv -v index.html allhtml/index.html
