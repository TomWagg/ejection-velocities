<h1 align="center">
    Stellar ejection velocities from the binary supernova scenario:<br>A comparison across population synthesis codes
    <br>
    <a href="https://github.com/TomWagg/ejection-velocities/blob/main/paper/paper.pdf">
        <img src="https://img.shields.io/badge/read-paper-blue.svg?style=flat" alt="Read the article"/>
    </a>
    <a href='https://doi.org/10.5281/zenodo.15225730'>
        <img src='https://img.shields.io/badge/access-data-green.svg?style=flat' alt='Data' />
    </a>
    <a href="mailto:tomjwagg@gmail.com">
        <img src="https://img.shields.io/badge/contact-authors-blueviolet.svg?style=flat" alt="Email the authors"/>
    </a>
</h1>

This repository contains the code and plots for a paper comparing ejection velocities in the `COSMIC`, `COMPAS` and `binary_c` population synthesis codes.

The notebook `ejection_vels.ipynb` steps through reproducing the plots and the data is available on Zenodo [at this link](https://doi.org/10.5281/zenodo.15225730).

## Abstract

The vast majority of binary systems are disrupted at the moment of the first supernova, resulting in an unbound compact object and companion star. These ejected companion stars contribute to the observed population of runaway stars. Therefore, an understanding of their ejection velocities is essential to interpreting observations, particularly in the *Gaia* era of high-precision astronomy. We present a comparison of the predicted ejection velocities of disrupted binary companions in three different population synthesis codes: `COSMIC`, `COMPAS` and `binary_c`, which use two independent algorithms for the treatment of natal kicks. We confirm that, despite the codes producing different pre-supernova evolution from the same initial conditions, they each find the ejection velocities of secondary stars from disrupted binaries are narrowly distributed about their pre-supernova orbital velocity. We additionally include a correction to the derivation included in *Kiel & Hurley 2009* that brings it into agreement with methods from other works for determining post-supernova binary orbital parameters. During this comparison, we identified and resolved bugs in the kick prescriptions of *all three* codes we considered, highlighting how open-science practices and code comparisons are essential for addressing implementation issues.