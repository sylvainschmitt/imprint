# Fourier
Sylvain Schmitt
Sep 8, 2026

<div>

[![](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

</div>

The general idea is to test the development of
[`microclimr`](https://github.com/sylvainschmitt/microclimr) by
reproducing analyses of the IMRPINT project on the forest microclimate
from the Mormal, Blois and Aigoual forests.

## Usage

**fourier** analyses rely on the quarto documents `index.qmd`,
`supplementary_note.qmd` and `cover_letter.qmd` that can be run with R
and associated environment defined with [renv](#0).

## Project

**fourier** includes:

- Manuscript and analyse of the data with associated documentation and
  figures:
  - Manuscript: `index.qmd` and associated html
  - Supplementary note: `supplementary_note.qmd` and associated html
    Cover letter: `cover_letter.qmd` and associated html
- All data in `data/`
- All figures in `figs/`
- R environment definition with
  [renv](https://rstudio.github.io/renv/articles/renv.html) in `renv/`
  and `renv/lock`
- R files (`.Rbuildignore` , `.Rdata` , `.Rprofile` , `.Rhistory`)
- Git and GitHub files (`.gitignore`)
- Project documentation (`README.qmd` , `README.md` , `NEWS.md` ,
  `LICENSE`)

## Poeple

- Sylvain Schmitt CIRAD
- Erwan Hingant University of Picardie Jules Verne
- Jonathan Lenoir CNRS
