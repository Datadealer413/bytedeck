from .base import *
try:
    # this file will only exists on the production server
    from .production_hackerspace import *
except:
    print("***** NO PRODUCTION SETTINGS FOUND         *******")
    print("***** IMPORTING LOCAL DEVELOPMENT SETTINGS *******")
