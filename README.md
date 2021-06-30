# CMSC6950_Project

## Argopy

Argo is a real-time global ocean observing system.The Ocean makes up more than 70 percent of the earth’s surface, and Argopyprovides a global system for monitoring ocean behaviours.  Scientists study thebehaviour of the Ocean for many reasons, including but not limited to;
1.  Ocean behaviour helps scientists understand global weather conditions.
2.  The Ocean supports different forms of life that need preserving;  drasticchanges in parameters like Temperature or Pressure will impact these lifeforms.
3.  Global Warming.

Argo consists of about 4000 autonomous floats, measuring parameters like Tem-perature, Pressure and Salinity.  This historical data is available to the public.<br />

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
