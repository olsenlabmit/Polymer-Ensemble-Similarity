How to generate txt files for polymer chain graph representation.

Take Example1 Ensemble P for example,

<img src="https://drive.google.com/uc?export=view&id=1b0wnyachSnJKj1pSajL5GT0erMGUwx3p"  width="50%">

where blue sphere is R0, red sphere is R1.

Therefore, [the txt files](https://github.com/olsenlabmit/Polymer-Ensemble-Similarity/blob/main/dataset/Example1/Ensemble_P/p1_graph.txt) for polymer chain graph representation of $p_1$ is

```
SMILES
R0
R1
cc_bond


MONOMERS
1 R0
2 R1
3 R0
4 R1
5 R0
6 R1
7 R0
8 R1
9 R0


BONDS
1 2 cc_bond
2 3 cc_bond
3 4 cc_bond
4 5 cc_bond
5 6 cc_bond
6 7 cc_bond
7 8 cc_bond
8 9 cc_bond
```

* In the **SMILES**, there are three types of components `R0`, `R1` and `cc_bond`. The details of the chemistry of `R0`, `R1` is shown in [tables](https://github.com/olsenlabmit/Polymer-Ensemble-Similarity/blob/main/tables/SMILES_repeatunit.txt). As for `cc_bond`, in the original work [GLAMOUR](https://github.com/learningmatter-mit/GLAMOUR), bond is specified for biomacromolecules. Our work makes use of part of code of GLAMOUR but our work do not need to specify the bond information for polymers' graph representation since we have already specified the connection point of repeat units by using the symbol  `*`. In our work, `cc_bond` is used only for representing the connection between repeat unit.
Also, in order to make use of the GLAMOUR code and maintain compatibility, we still keep this data format. 

* In the **MONOMERS**, since $p_1$ has 9 nodes, 9 nodes are presented with the specific repeat units.

* In the **BONDS**, the connections of these 9 nodes are presented based on $p_1$'s topological information.

