#Import packages
import earthaccess
import xarray as xr

#Authentication with Earthdata Login
auth = earthaccess.login(strategy="netrc")
print('Hello')
print('login success')
