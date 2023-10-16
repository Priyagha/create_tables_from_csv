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

for file in files:
    print(file)
    df = pd.read_csv(file)
    table_name = file.split('\\')[1].split('.')[0].upper()
    table_str = f"CREATE TABLE {table_name} ("
    for columns in df.columns:
        obj_type = df[columns].dtype
        obj_max = df[columns].apply(lambda x: len(str(x))).max()

        if obj_type == object:
            if columns in ['START', 'STOP', 'DATE'] or 'DATE' in columns:
                table_str += f' {columns} DATE,'

            elif obj_max == 36:
                table_str += f' {columns} UUID,'

            else:
                table_str += f' {columns} VARCHAR({obj_max}),'

        elif obj_type == int:
            table_str += f' {columns} BIGINT,'
        
        elif obj_type == float:
            table_str += f' {columns} REAL,'

    table_str = table_str[:-1]
    table_str += ');\n'

    csv_path = os.path.join(pwd, file.split('\\')[1]).replace('\\','/')
    csv_str = f"COPY {table_name} FROM '{csv_path}' DELIMITER ',' CSV HEADER;\n\n"
    print('\t',table_str)
    print('\t', csv_str)

    write_sql.write(table_str)
    write_sql.write(csv_str)


write_sql.close()