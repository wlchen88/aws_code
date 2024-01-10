#Import packages
import earthaccess
import xarray as xr
import s3fs
import os

#Authentication with Earthdata Login
auth = earthaccess.login(strategy="netrc")
print('login success')

#os.system('aws s3 ls s3://podaac-ops-cumulus-protected/SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205/')
s3 = s3fs.S3FileSystem(anon=False)
s3.ls('podaac-ops-cumulus-public/SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205/')

# results = earthaccess.search_data(
#     short_name='SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205',
#     cloud_hosted=True,
#     bounding_box=(-105, -40, 0, 50),
#     temporal=("2022-01", "2022-02"),
#     count=10
# )
# files = earthaccess.download(results, "/home/ubuntu/SSHAlt")
