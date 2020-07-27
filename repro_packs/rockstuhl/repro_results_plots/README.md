# Reproducibility packages

This directory contains the necessary information to reproduce the figures of the paper: Reproducible Validation and Replication Studies in Nanoscale Physics

To be able to reproduce these results, the user needs Python and Jupyter notebooks. 

Python libraries needed:
- `numpy` (used by author 1.15.4)
- `scipy` (used by author 1.1.0)
- `matplotlib` (used by author 3.1.0)

**Notebooks description**

* `19K_vs_15K_cube535nm.ipynb`: This notebook reproduce the result of the grid independence study, and saves the output pdf figure to the directory `grid_indep_fig`. The sub-directory `grid_indep_fig/original` contains the figure that was used on the paper, and you can use for comparison.
* `extend_third_dir_comparison.ipynb`: This notebook reproduce the results for the consequence of extending the third direction, results of the effeect of roundness on the meshes. It saves the output pdf figures to the directory `extend_third_dir_fig14`. The sub-directory `extend_third_dir_fig14/original` contains the figure that was used on the paper, and you can use for comparison.
*  `figure_14ab_replication.ipynb`: This notebook reproduce the result of the replication of Figure 14 of Rockstuhl et al. 2005. It saves the output pdf figures to the directory `replication_fig14`. The sub-directory `replication_fig14/original` contains the figure that was used on the paper, and you can use for comparison.

**Data-folders description**

* `results_data`: It contains the secondary data from the simulations needed to perform the plots. These data are read in the notebooks to reproduce the figures for the paper. 
* `figure_14_rocksthul_digitized`: It contains the digitized data of Figure 14 of Rockstuhl et al.2005, used on the `figure_14ab_replication.ipynb` notebook for the replication study. 

