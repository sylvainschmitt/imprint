# Data
Sylvain Schmitt -
Jan 7, 2026

This folder will contains the data for all analyses:

- `plots.tsv`: forest plots data extracted from INDORES dataverse
- `coords.tsv`: forest plots coordinataion extracted from INDORES
  dataverse used by the get_era script
- `hobo.tsv`: microclimate HOBO data extracted from INDORES dataverse
- `lidar.tsv`: forest lidar data extracted from INDORES dataverse
- `get_era.py`: python script to retrieve corresponding ERA5-Land data
- `era.tsv`: ERA5-Land data for the three forests
- `data.tsv`: all assembled raw data
- `decomposition.tsv`: macrolimate and microclimate decomposition with
  Fourier’s transformations
- `methor_data_onf/`: macrolimate ONF data shared by Erwan Hingant raw
  data

All analyses and files production can be found in the
[analyses](https://sylvainschmitt.github.io/imprint/).

``` r
fs::dir_tree()
```

    .
    ├── README.md
    ├── README.qmd
    ├── README.rmarkdown
    ├── coords.tsv
    ├── data.tsv
    ├── decomposition.tsv
    ├── era.tsv
    ├── get_era.py
    ├── hobo.tsv
    ├── lidar.tsv
    ├── methor_data_onf
    │   ├── MetHor2018.org
    │   ├── MetHor2018.txt
    │   ├── MetHor2019.txt
    │   ├── MetHor2020.txt
    │   ├── MetHor2021.txt
    │   ├── MetHor2022.txt
    │   └── MetHor2023.txt
    └── plots.tsv
