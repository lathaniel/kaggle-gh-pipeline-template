# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: kaggle-cms
#     language: python
#     name: kaggle-cms
# ---

# # Initial Setup
#
# I often prefer to run my notebooks outside of Kaggle.  
#
# As a result, I specify at the top whether I am running the notebook locally or on Kaggle

# + vscode={"languageId": "python"}
localEnv = True
kaggleDataDir = './kaggle-data' if localEnv == True \
    else '/kaggle/input/CMS-Covid-19-Nursing-Homes-dataset'
# -

# # Import packages

# + vscode={"languageId": "python"}
import pandas as pd

# + vscode={"languageId": "python"}
# Verify we can read dataset
df = pd.read_csv(f'{kaggleDataDir}/COVID_19_Nursing_Home_Data_09_25_2022.csv')
# -

# ## Initial data exploration
#

# + vscode={"languageId": "python"}
# Remove unsubmitted data
df = df.loc[df['Submitted Data']=='Y']

# + vscode={"languageId": "python"}
# Occupancy percentage (all locations)
print('Occupancy Percentage: {}%'.format(
    round(
        df['Total Number of Occupied Beds'].sum() / 
            df['Number of All Beds'].sum(),
        4
    )* 100
)) 
