# %%
import pandas as pd
import numpy as np
from glob import glob
import os

# %%
write_sql = open('create_tables_from_csv.pgsql', 'w')