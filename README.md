# Calculating Pairwise Similarity of Polymer Ensembles via Earth Mover’s Distance


This repository supports the following manuscript, which has been submitted for peer-review.

Jiale Shi, Dylan J. Walsh, Weizhong Zou, Nathan J. Rebello, Michael E. Deagen, Katharina A. Fransen, Xian Gao,  Debra J. Audus, Bradley D. Olsen (2023), "Calculating Pairwise Similarity of Polymer Ensembles via Earth Mover’s Distance", ACS Polymer Au, submitted.

In this work, we proposed the [earth mover’s distance (EMD)](https://en.wikipedia.org/wiki/Earth_mover%27s_distance) method to quantitatively calculate the pairwise similarity score for polymer ensembles. The distance ($d_{i,j}$) between one polymer molecule $p_i$ and another polymer molecule $q_j$ is calculated through graph edit distance. This part of the code builds on [GLAMOUR](https://github.com/learningmatter-mit/GLAMOUR).

The repository is intended for the following use cases:

- Illustrate the EMD method for polymer ensemble similarity calculation in the manuscript
- Allow for full reproducibility of the results in the manuscript


## Running the code

### Running notebooks in Google Colab

If you are interested in running one or more notebooks in [Google Colab](https://colab.research.google.com/), first, click on the relevant links below.

* [Example1_Two_Component_Polymer_Ensemble](./notebook/Example1_Two_Component_Polymer_Ensemble_Colab.ipynb)
* [Example2_First_order_Markov_Copolymer_Ensemble_onehot](./notebook/Example2_First_order_Markov_Copolymer_Ensemble_onehot_Colab.ipynb)
* [Example2_First_order_Markov_Copolymer_Ensemble_fp](./notebook/Example2_First_order_Markov_Copolymer_Ensemble_fp_Colab.ipynb)
* [Example3_Nonlinear_Star_Polymer_Ensemble](./notebook/Example3_Nonlinear_Star_Polymer_Ensemble_Colab.ipynb)
* [Example4_Polymer_Ensembles_Represented_by_Experimental_Molecular_Mass_Distributions](./notebook/Example4_Polymer_Ensembles_Represented_by_Experimental_Molecular_Mass_Distributions_Colab.ipynb)


Then, click on the Colab badge <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" width="75" height="15"/> in the notebook.

It will open a Colab notebook. Then, you can run the notebook as normal. All the required libraries and functions are present in the Colab notebook. 
If you cannot successfully open the Colab badge, download the notebook and upload it to Google Colab.


## Contact

Jiale Shi, PhD  

Postdoctoral Associate  

Department of Chemical Engineering 

Massachusetts Institute of Technology (MIT) 

Email: jialeshi@mit.edu  

GithubID: shijiale0609  
 

## How to cite

If you use the code, please cite our repository since our manuscript is currently in review:

Jiale Shi, Dylan J. Walsh, Weizhong Zou, Nathan J. Rebello, Michael E. Deagen, Katharina A. Fransen, Xian Gao,  Debra J. Audus, Bradley D. Olsen (2023), "Calculating Pairwise Similarity of Polymer Ensembles via Earth Mover’s Distance", https://github.com/olsenlabmit/Polymer-Ensemble-Similarity.
