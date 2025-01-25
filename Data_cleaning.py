import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

DataFrame = pd.read_csv(r'D:\Virtual_Environment\Assignment\Task\Companies_Dataset.csv')

# Data Cleaning
# Removing all duplicates from the Dataframe.
DataFrame = DataFrame.drop_duplicates()

# Data Standarization.
DataFrame['Website'] = DataFrame['Website'].str.strip('https://')
DataFrame['LinkedIn URL'] = DataFrame['LinkedIn URL'].str.strip('https://')

# Updating No. of Employees in Dataframe
EmployeesValue = [15000,3100,1000,1041,1200,991,581,1301,696,350,110,275,342,294,319,235,191,503,250,169,124]
DataFrame['No. of Employees'] = EmployeesValue

# Adding the new column in Dataframe( Valuation in Million ($)).
Valuation = [5930,5600,2000,121,870,1000,387,945,356,300,122,50,3500,73.5,104,267,66,58.4,1.5,12.6,9]
DataFrame['Valuation in Million ($)'] = Valuation

# Updating the Size of the Firms based on their Valuation.
DataFrame['Firm Size'] = DataFrame['Valuation in Million ($)'].apply(
                         lambda x : 'Small' if x < 100
                                    else 'Medium' if x < 1000
                                    else 'Large'
)

# Updating Industries.
CompanyName = ['Rubrik', 'FarEye', 'Exotel', 'Locus', 'Flock', 'Pando', 'Skit', 'Hotelogix']
IndustryType = ['Cyber and Data security', 'Logistic', 'Telicommunication','Logistic','Telicommunication',
                'Logistic','Telicommunication','Hospitality']
DataFrame.loc[DataFrame['Company Name'].isin(CompanyName), 'Industry/Sector'] = IndustryType

# Changing Data type of the Dataframe.
DataFrame = DataFrame.astype({
    'Company Name':'string',
    'Website':'string',
    'Industry/Sector':'string',
    'Headquarters Location':'string',
    'Decision Maker(s) Name':'string',
    'Title/Role':'string',
    'LinkedIn URL':'string',
    'Contact Email':'string',
    'Firm Size':'string',
    'No. of Employees':'int',
    'Hiring in 2023':'string',
    'Hiring in 2024':'string',
    'Valuation in Million ($)':'float'})

# Column Rename.
DataFrame = DataFrame.rename(columns = {'Industry/Sector':'Industry',
                                        'Headquarters Location':'Location',
                                        'Decision Maker(s) Name':'Decision Maker',
                                        'Title/Role':'Title'
                                       })

# Saving the file into CSV.
UpdatedFile= DataFrame.to_csv('UpdatedFile.csv')

print(DataFrame)
