# mamba env create -f get_era_ee.yml 
# mamba activate get-era-ee
# python get_era_ee.py > log_ee.txt

import ee
import xarray as xr
import pandas as pd

coords = pd.read_csv("coords.tsv", sep="\t")
ee.Initialize(project="ee-sylvainmschmitt", opt_url='https://earthengine-highvolume.googleapis.com')
pts = ee.Geometry.MultiPoint(coords[["lon", "lat"]].values.tolist())
ic = ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY").filter(ee.Filter.date('2020-01-01', '2023-12-31'))
ds = xr.open_mfdataset([ic], engine='ee', projection=ic.first().select(0).projection(), geometry=pts, fast_time_slicing=True)
ds['tas'] = ds['temperature_2m'] - 273.15
ds = ds[['tas']]
ds = ds.sel(lon = xr.DataArray(coords.lon), 
            lat = xr.DataArray(coords.lat),
            method='nearest')
ds_df = ds.to_dataframe()
ds_df.to_csv("era.tsv", sep="\t", index=True)
