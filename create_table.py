# %%
import pandas as pd
import numpy as np
from glob import glob
import os

# %%
write_sql = open('create_tables_from_csv.pgsql', 'w')

# sorting the list of file paths returned by glob() 
files = sorted(glob('./*.csv'))

# getting the current working directory
pwd = os.getcwd()