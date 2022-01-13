
import pandas as pd
import matplotlib.pyplot as plt

API = pd.read_csv('Data/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_3469540.csv', skiprows=4)
print(API)

APImeta = pd.read_csv(
    'Data/Metadata_Country_API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_3469540.csv')
print(APImeta)
print(APImeta.columns)

API.drop('Unnamed: 65', axis=1, inplace=True)
API.drop('Indicator Name', axis=1, inplace=True)
API.drop('Indicator Code', axis=1, inplace=True)
APImeta.drop('Unnamed: 5', axis=1, inplace=True)
APImeta.drop('TableName', axis=1, inplace=True)
APImeta.drop('SpecialNotes', axis=1, inplace=True)
print(API.columns)
print(APImeta.columns)

# drop rows with no data in the years in the API file
API.dropna(thresh=3, inplace=True)
print('cleaned shape = ' + str(API.shape))
print(API.head())
print(API.columns)

# merge the API and API metadata together
APIall = API.merge(APImeta, how='inner', on='Country Code')
print('merged shape = ' + str(APIall.shape))
print(APIall.head())
print(APIall.columns)
print(APIall['IncomeGroup'].unique())

#Create a dataframe with just the aggregate rows for income groups
APIaggincome = pd.DataFrame()

# Create a low income country dataframe
APIlowincome = APIall[APIall['IncomeGroup'] == 'Low income']
APIlowincome = APIlowincome.append(
    APIall[APIall['Country Name'] == 'Low income'])
APIaggincome = APIaggincome.append(
    APIall[APIall['Country Name'] == 'Low income'])
print('low income shape = ' + str(APIlowincome.shape))
print(APIlowincome['Country Name'])

# Create a Lower middle income country dataframe
APIlowmidincome = APIall[APIall['IncomeGroup'] == 'Lower middle income']
APIlowmidincome = APIlowmidincome.append(
    APIall[APIall['Country Name'] == 'Lower middle income'])
APIaggincome = APIaggincome.append(
    APIall[APIall['Country Name'] == 'Lower middle income'])
print('Lower middle shape = ' + str(APIlowmidincome.shape))
print(APIlowmidincome['Country Name'])

# Create a Upper middle income country dataframe
APIuppermidincome = APIall[APIall['IncomeGroup'] == 'Upper middle income']
APIuppermidincome = APIuppermidincome.append(
    APIall[APIall['Country Name'] == 'Upper middle income'])
APIaggincome = APIaggincome.append(
    APIall[APIall['Country Name'] == 'Upper middle income'])
print('Upper middle shape = ' + str(APIuppermidincome.shape))
print(APIuppermidincome['Country Name'])

# Create a High income country dataframe
APIhighincome = APIall[APIall['IncomeGroup'] == 'High income']
APIhighincome = APIhighincome.append(
    APIall[APIall['Country Name'] == 'High income'])
APIaggincome = APIaggincome.append(
    APIall[APIall['Country Name'] == 'High income'])
print('High income shape = ' + str(APIhighincome.shape))
print(APIhighincome['Country Name'])
print(APIhighincome.info())

print(APIaggincome)
print(APIaggincome.info())

# Write these tables out to csv files
APIlowincome.to_csv("Data/InflationMerged_LowIncome.csv", index=False)
APIlowmidincome.to_csv("Data/InflationMerged_LowMidIncome.csv", index=False)
APIuppermidincome.to_csv(
    "Data/InflationMerged_UpperMidIncome.csv", index=False)
APIhighincome.to_csv("Data/InflationMerged_HighIncome.csv", index=False)
APIaggincome.to_csv("Data/InflationMerged_AggregateIncome.csv", index=False)

