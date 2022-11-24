# RF_CTCF_BP
Random Forest CTCF Binding Predictor


This projact contaisn the code required to replicate the Manuscritp by Villaman et al. "Prediction of CTCF binding and the role of histone marks on the spatial organization of chromatin"


alberto.martin@uss.cl

code and data is organized in folders as follows:

  - GM.zip HL.zip K.zip SK.zip: files with all required data to generate input for all 4 cell lines only for chromosome 4
  - CTCF.fimo.sortedBed: bed file with FIMO determined CTCF binding sites
  - matrixmaker.py: python3 script that takes as input files in each of the GM HL K SK folders and CTCF.fimo.sortedBed to generate input files for the RF predictor
  - shortex.zip: matrix files for chromosome 4
  - RF CTCF chr4 short example.ipynb Jupyter Notebook with all code required to test and train all models employed in the manuscript


Be sure hardcoded paths are changed
