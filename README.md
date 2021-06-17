# CMSC6950_Project

##Argopy

Argo is a real-time global ocean in situ observing system.The ocean is a key component of the Earth climate system.  It thus needs a con-tinuous real-time monitoring to help scientists better understand its dynamicand predict its evolution.  All around the world, oceanographers have managedto join their efforts and set up a Global Ocean Observing System among whichArgo is a key component.<br />

**The following packages must be INSTALLED:**


 1. Argopy -           pip install argopy
 2. Pandas -           pip install pandas
 3. Numpy -            pip install numpy
 4. Matplotlib -       pip install matplotlib
 5. Make -             sudo apt-get install build-essential
 6. LaTexmk-           apt-get install latexmk

**Reporducing the Workflow**

 With the index.py file and the Report.tex file the workflow acn be reproduced using a MakeFile.
 1. Run make almost_clean, to remove the temporary files created by the Latexmk.
 2. Run make clean, to remove the report.pdf file and its dependencies.
 3. Run the make command o reproduce the workflow.
