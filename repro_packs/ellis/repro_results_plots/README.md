# Reproducibility packages

This directory contains the necessary information to reproduce the figures of the paper: Reproducible Validation and Replication Studies in Nanoscale Physics, in particular the results related to Ellis et al. 2016.

To be able to reproduce these results, the user needs Python and Jupyter notebooks. 

Python libraries needed:
- `numpy` (used by author 1.15.4)
- `scipy` (used by author 1.1.0)
- `matplotlib` (used by author 3.1.0)

**Notebooks description**

* `AR_normal_vs_22deg.ipynb`: This notebook reproduce the result to extract the $E^{\parallel}_{100}$ mode for the different aspect ratios. It produces
the `AR_lower_modes.txt` file needed for the replication result of Figure S4 of Ellis et al. The original `AR_lower_modes.txt` file is under the `AR_rep_val_figs/original` directory, for comparison. This notebook also saves the output pdf figure to the directory `AR_rep_val_figs`. The sub-directory `AR_rep_val_figs/original` contains the figure that was used on the paper, and you can use for comparison as well.
* `figureS4_Ellis2016_replication_curves_AR.ipynb`: This notebook reproduce the result of the replication of Figure S4 of the supplementary material of of Ellis et al. 2016. It saves the output pdf figures to the directory `AR_rep_val_figs`. The sub-directory `AR_rep_val_figs/original` contains the figure that was used on the paper, and you can use for comparison.
* `figure2a_Ellis2016_replication.ipynb`: This notebook reproduce the result of the validation and replication of Figure 2a of Ellis et al. 2016. It saves the output pdf figures to the directory `AR_rep_val_figs`. The sub-directory `AR_rep_val_figs/original` contains the figure that was used on the paper, and you can use for comparison.


**Data-folders description**

* `results_data`: It contains the secondary data from the simulations needed to perform the plots. These data are read in the notebooks to reproduce the figures for the paper. 
* `ellis_figS4_digit`: It contains the digitized data of Figure S4 of the supplementary material of Ellis et al.2016, used on the  `figureS4_Ellis2016_replication_curves_AR.ipynb` notebook for the replication study.
* `ellis_fig2_digit`: It contains the digitized data of Figure 2a of Ellis et al.2016, used on the `figure2a_Ellis2016_replication.ipynb` notebook for validation and the replication study. 
