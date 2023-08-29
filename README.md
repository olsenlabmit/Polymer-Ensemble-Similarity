# Calculating Pairwise Similarity of Polymer Ensembles via Earth Mover’s Distance


This repository supports the following manuscript, which has been submitted for peer-review.

Jiale Shi, Dylan J. Walsh, Nathan J. Rebello, Weizhong Zou, Michael E. Deagen, Katharina A. Fransen, Xian Gao,  Debra J. Audus, Bradley D. Olsen (2023), "Calculating Pairwise Similarity of Polymer Ensembles via Earth Mover’s Distance", ACS Polymer Au, submitted.

In this work, we proposed the [earth mover’s distance (EMD)](https://en.wikipedia.org/wiki/Earth_mover%27s_distance) method to quantitatively calculate the pairwise similarity score for polymer ensembles.

The repository is intended for the following use cases:

- Illustrate the EMD method for polymer ensemble calculation in the manuscript
- Allow for full reproducibility of the results in the manuscript


### Using the codebase
To use the code with an Anaconda environment, follow the installation procedure here - 
```
conda create -n polymer_ensemble python=3.9
conda activate polymer_ensemble
conda install pytorch -c pytorch
conda install -c conda-forge matplotlib
conda install -c rdkit rdkit
conda install -c dglteam dgl
conda install -c anaconda scikit-learn
conda install -c anaconda networkx
conda install seaborn
conda install -c conda-forge svglib
conda install -c conda-forge umap-learn
conda install -c conda-forge grakel
conda install -c conda-forge pyomo
conda install -c conda-forge coincbc
```

## Contact

Jiale Shi, PhD  

Postdoctoral Associate  

Department of Chemical Engineering 

Massachusetts Institute of Technology (MIT) 

Email: jialeshi@mit.edu  

GithubID: shijiale0609  
 

## How to cite

If you use the code, please cite our repository since our manuscript is currently in review:

Jiale Shi, Dylan Walsh, Nathan J. Rebello, Weizhong Zou, Michael E. Deagen, Katharina A. Fransen, Xian Gao,  Debra J. Audus, Bradley D. Olsen (2023), "Calculating Pairwise Similarity of Polymer Ensembles via Earth Mover’s Distance", https://github.com/olsenlabmit/Polymer-Ensemble-Similarity.
