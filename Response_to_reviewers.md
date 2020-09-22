# Response to reviewers

## Reviewer 1 comments

This is a nicely written report that provides an important demonstration of high-quality V&V and R&R. The effort of the group to provide all materials and act as a positive example for the computational community is commendable. The report also benefits from a deep and informative background section; a positive aspect and a good fit for a journal such as Phil. Transactions A.  

Minor comments:

- [x]  Pg 2 line 26 – trecode should be treecode
- [x]  Pg 2 line 36 – mode should be modes
- [x]  Pg 8 line 39 – there is repetition of ‘a a’
- [x]  Pg 9, and elsewhere, when discussing the features of the figures, in the case of Pg 9 it is figure 4, it would be useful to be more descriptive, for instance “One can see that the second peak in the E||b plot at 10.6 um is not present for the green curve”
- [x]  In the Figure 4 caption it would be useful to briefly explain the legend terms: trimesh, uniform and uni + round.
- [x]  Pg 12 line 27 – change “per Angstrom-squared” to use the Angstrom symbol and rewrite?
- [x] Pg 19 line 19 – given he relationship


**Changes**

Commit: [c5095c3](https://github.com/barbagroup/pygbe_validation_paper/commit/c5095c31761e7092858b21a43a16d39aadbd0912)

- In abstract:
trecode -> treecode
position of some mode -> position of some modes 
- In results:
a a -> a 
- In discussion:
given he -> given the

Commit: [b060520](https://github.com/barbagroup/pygbe_validation_paper/pull/4/commits/b0605200ac6928998e75a2a9667889e69c81639d),
commit [50d7357](https://github.com/barbagroup/pygbe_validation_paper/commit/50d73572fa65f8823dfed09342a490ee55ed284e)
- Explain legends in caption

Commit [bf14a0a](https://github.com/barbagroup/pygbe_validation_paper/commit/bf14a0ae0122e371ea6180c230b5196ee329aef8) - better explain Fig. 4

Commit: [6f5dec](https://github.com/barbagroup/pygbe_validation_paper/pull/4/commits/6f5decbc6a101b8c38c6e83b0b772b7e0f648b17)
- Use Angstrom symbol

## Reviwer 2 comments

It was a pleasure to review the manuscript “Reproducible Validation and Replication Studies in Nanoscale Physics” by Clementi and Barba. This paper presents validation and replication studies in area of nanostructure responses to electromagnetic waves. The authors use their previously developed open-source software PyGBe to replicate results from previous publications. The authors make their reproducibility packages openly accessible, including the computational software, input files, execution scripts, analysis code, data and figures. This is essential for open science and for the feasibility of replication study. The manuscript addresses the important topic of reproducibility and replication. Its well-written background section makes the paper not only of interest to this specific field, but also to a general audience. I recommend to publish the manuscript after some minor revisions:

Although the main purpose of the paper is replication, the other closely related topics should also be addressed. This includes:

- [x] Although the authors released their reproducibility packages, they don’t show the reproducibility of their calculations: can consistent results be generated when the calculations are repeated, how sensitive the results are to the input data, etc.
- [x]  What are the uncertainties of the calculations? Can error bars be added to the results as displayed in the figures and tables?

- [x] In the “replication of results from Rockstuhl, et al., 2005”, it appears that the main reason for the differences is the 2D and 3D representation between the previous and current studies. The authors show the impact of the y dimensions to the calculated results, but only use two lengths. Are there any limitations to to stop the authors to lengthen y larger than 2688 nm? Will some peaks disappear if the y dimension approaches to infinity?


Typos:
- [x] Page 5, line 30: PyGBE --> PyGBe
- [x] Page 18, line 18, “… he relationship …” --> “ … the relationship …”


**Response**

Running the execution scripts with the same input file on the same machine will produce the same results with bit-by-bit reproducibility. If running on a different machine, the results could show a difference due to floating-point error. We did confirm this. In fact, we have manually triggered correctness tests on the software that we run each time a change is applied in the code, which compares to previously generated results; we set these tests to pass when the difference in the results match to 10^{-10}.

The uncertainties in the calculations are: model uncertainties (quasi static approximation), spatial discretization errors (quantified via grid-convergence analysis in a previous paper that we cite in the manuscript), algebraic errors (from the iterative linear solver, set via exit tolerance), tree code approximation (quantifiable and controllable via expansion order and tree level). Additionally, the experimentally obtained value of the dielectric constant of the material is also subject to uncertainties (unknown to us). Since none of these sources of uncertainty is of statistical nature, error bars are not appropriate.

**Changes**

Added: "We did not explore larger values of $y$ because of the limitations imposed by the quasistatic limit model."

## Additional changes

After submission of the manuscript, and having posted the preprint on ArXiv, we received email communication from Prof. Carsten Rockstuhl, noting some refinements we could make to a couple of passages. We have documented this correspondence and the changes we made to the paper in [Issue 3](https://github.com/barbagroup/pygbe_validation_paper/issues/3) within our manuscript repository.
 
See history of commits, including:

- Commit [94279c6](https://github.com/barbagroup/pygbe_validation_paper/commit/94279c66d6654eebe2da4163689ac5d88ecd130a)
- Commit: [89b23f9](https://github.com/barbagroup/pygbe_validation_paper/commit/89b23f94f972d2c2bff5c1a899c407386de1ae48)

We added a note in the acknowledgements for this correspondence with Rockstuhl.