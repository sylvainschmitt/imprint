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

ic = ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY").filter(ee.Filter.date('2023-07-11', '2023-09-11'))
ds = xr.open_mfdataset([ic], engine='ee', crs="EPSG:4326", scale=0.1, geometry=ee.Geometry.Rectangle([-5.5, 41.0, 10.0, 51.5]))
t2m = (
    ds["temperature_2m"]
    .sel(time="2023-08-11T12:00:00", method="nearest")
    .compute()                          # déclenche le téléchargement
    - 273.15                            # Kelvin → Celsius
)
t2m.attrs["units"] = "°C"
t2m = t2m.rio.write_crs("EPSG:4326")
t2m = t2m.rio.set_spatial_dims(x_dim="lon", y_dim="lat")
tif_path = "erafrance.tif"
t2m.transpose('lat', 'lon').to_netcdf("erafrance.nc")
