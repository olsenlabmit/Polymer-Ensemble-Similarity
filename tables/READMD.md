The file [SMILES_repeatunit.txt](https://github.com/olsenlabmit/Polymer-Ensemble-Similarity/blob/main/tables/SMILES_repeatunit.txt) is the tables for Repeat Units.

The function of the tables is to specify the chemistry of the repeat unit and works with the txt files of graph representation in [dataset](https://github.com/olsenlabmit/Polymer-Ensemble-Similarity/tree/main/dataset).

```
Molecule,SMILES
R0,*CC(*)c1ccccc1
R1,*CC(*)c1ccc(C(=O)OC)cc1
E1,*C(C)C(=O)OCC(C)(COC(=O)C(*)C)COC(=O)C(*)C
E2,*SC(=S)SCCCC
E3,*C(C)C(=O)OCC(COC(=O)C(*)C)(COC(=O)C(*)C)COC(=O)C(*)C
R0T,*C[C@H](C)*
R1T,*C[C@@H](C)*
```
For example, R0 represents *CC(*)c1ccccc1 and  R1 represents *CC(*)c1ccc(C(=O)OC)cc1. 


Our work is built up [GLAMOUR](https://github.com/learningmatter-mit/GLAMOUR). In [GLAMOUR](https://github.com/learningmatter-mit/GLAMOUR), bond is specified for biomacromolecules and therefore they also specify the chemistry of the bond in the file, [SMILES_bond.txt](https://github.com/olsenlabmit/Polymer-Ensemble-Similarity/blob/main/tables/SMILES_bond.txt). Our work makes use of part of code of GLAMOUR but our work do not need to specify the bond information for polymers' graph representation since we have already specified the connection point of repeat units by using the symbol  `*`. In our work, bond is used only for representing the connection between repeat unit. Also, in order to make use of code of GLAMOUR and keep compatible, we still keep [SMILES_bond.txt](https://github.com/olsenlabmit/Polymer-Ensemble-Similarity/blob/main/tables/SMILES_bond.txt). 