#Import packages
import earthaccess
import xarray as xr

#Authentication with Earthdata Login
auth = earthaccess.login(strategy="netrc")
print('login success')

results = earthaccess.search_data(
    short_name='SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205',
    cloud_hosted=True,
    bounding_box=(-105, -40, 0, 50),
    temporal=("2023-01", "2023-02"),
    count=10
)
files = earthaccess.download(results, "/home/ubuntu/SSHAlt")
