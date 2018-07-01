#loads libraries
import pymssql
import pandas as pd
import pandas.io.sql as psql
import json
import xlrd
import scipy
import sklearn


#links to database
conn = pymssql.connect(server='', user='', password='', database='') 
cursor = conn.cursor()

#sets sql statement and reads the requested data into python dataframe
sql = "select distinct b.supplierID, b.name, b.DisplayName from fact.hotel a join dim.supplier b on a.supplierID = b.supplierid"
df = psql.read_sql_query(sql, conn)

conn.close()


#starts the classifier
exec(open("go.py").read())

#entered the brand name
chain = c.classify("courtyard")

#displayed the resultsin JSON form
chain

#separated the result from the JSON formatting
output = list()
for i in chain.keys():
    output.append(i)
	
output = ''.join(output)

#Displayed the cleaned results
output

C:\Users\Lawrence Reed\Documents\CreateHotelDF.py

dfs = pd.read_excel("hoteldf.xlsx", sheet_name='Sheet1', converters={'incident':int,'99InnManagementCoLtd':float, 'AccorHotels':float, 'AmanResort':float
, 'APAGroup':float, 'TheAscottLimited':float, 'BanyanTreeHoldings':float, 'Barriere':float, 'BestWesternHotels':float, 'TheDedicaAnthologyHotels':float
, 'BTGHomeinnhotelgroup':float, 'RadissonHotelGroup':float, 'ChinaLodgingGroupLimitedHuazhuHotelsGroup':float, 'ChoiceHotels':float, 'CoastHotels':float
, 'DorchesterCollection':float, 'DossenInternationalGroup':float, 'DruryHotels':float, 'DusitThaniGroup':float, 'ElegantHotelsGroup':float
, 'ExtendedStayAmericaIncFIHRegentGroup':float, 'FirstHotels':float, 'FourSeasonsHotelsandResorts':float, 'G6HospitalityLLC':float
, 'GreenTreeInnsHotelManagementGroupInc':float, 'HiltonWorldwide':float, 'HNAHospitalityGroup':float, 'HongkongandShanghaiHotels':float
, 'HoshinoResorts':float, 'HyattHotelsCorporation':float, 'InterContinentalHotelsGroupIHG':float, 'InterstateHotelResorts':float
, 'InTownSuites':float, 'JinJiangInternational':float, 'Jumeirah':float, 'Kempinski':float, 'LanghamHospitalityGroup':float, 'LoewsHotels':float
, 'LotteHotelsResorts':float, 'MagnusonHotels':float, 'MandarinOrientalHotelGroup':float, 'MarriottInternational':float
, 'MeliaHotelsInternationalSA':float, 'MillenniumCopthorneHotels':float, 'MGMResortsInternational':float, 'MinorHotels':float
, 'NHHotelGroup':float, 'TheOberoiGroup':float, 'OkuraNikkoHotelManagement':float, 'OmniHotelsResorts':float, 'PanPacificHotelsandResorts':float
, 'PrinceHotels':float, 'RedLionHotelsCorporation':float, 'RedRoofInn':float, 'RIUHotelsResorts':float, 'RosewoodHotelGroup':float
, 'ScandicHotels':float, 'ShangriLaHotelsandResorts':float, 'ShiloInns':float, 'SunmeiGroup':float, 'TajHotelsResortsandPalaces':float
, 'TokyuHotels':float, 'ToyokoInn':float, 'Travelodge':float, 'Treebo':float, 'WaltDisneyParksandResorts':float, 'WarwickHotelsandResorts':float
, 'WyndhamWorldwide':float, 'Whitbreadplc':float})


dfs = pd.read_csv("hoteldf.csv", converters={'incident':int,'99InnManagementCoLtd':float, 'AccorHotels':float, 'AmanResort':float
, 'APAGroup':float, 'TheAscottLimited':float, 'BanyanTreeHoldings':float, 'Barriere':float, 'BestWesternHotels':float, 'TheDedicaAnthologyHotels':float
, 'BTGHomeinnhotelgroup':float, 'RadissonHotelGroup':float, 'ChinaLodgingGroupLimitedHuazhuHotelsGroup':float, 'ChoiceHotels':float, 'CoastHotels':float
, 'DorchesterCollection':float, 'DossenInternationalGroup':float, 'DruryHotels':float, 'DusitThaniGroup':float, 'ElegantHotelsGroup':float
, 'ExtendedStayAmericaIncFIHRegentGroup':float, 'FirstHotels':float, 'FourSeasonsHotelsandResorts':float, 'G6HospitalityLLC':float
, 'GreenTreeInnsHotelManagementGroupInc':float, 'HiltonWorldwide':float, 'HNAHospitalityGroup':float, 'HongkongandShanghaiHotels':float
, 'HoshinoResorts':float, 'HyattHotelsCorporation':float, 'InterContinentalHotelsGroupIHG':float, 'InterstateHotelResorts':float
, 'InTownSuites':float, 'JinJiangInternational':float, 'Jumeirah':float, 'Kempinski':float, 'LanghamHospitalityGroup':float, 'LoewsHotels':float
, 'LotteHotelsResorts':float, 'MagnusonHotels':float, 'MandarinOrientalHotelGroup':float, 'MarriottInternational':float
, 'MeliaHotelsInternationalSA':float, 'MillenniumCopthorneHotels':float, 'MGMResortsInternational':float, 'MinorHotels':float
, 'NHHotelGroup':float, 'TheOberoiGroup':float, 'OkuraNikkoHotelManagement':float, 'OmniHotelsResorts':float, 'PanPacificHotelsandResorts':float
, 'PrinceHotels':float, 'RedLionHotelsCorporation':float, 'RedRoofInn':float, 'RIUHotelsResorts':float, 'RosewoodHotelGroup':float
, 'ScandicHotels':float, 'ShangriLaHotelsandResorts':float, 'ShiloInns':float, 'SunmeiGroup':float, 'TajHotelsResortsandPalaces':float
, 'TokyuHotels':float, 'ToyokoInn':float, 'Travelodge':float, 'Treebo':float, 'WaltDisneyParksandResorts':float, 'WarwickHotelsandResorts':float
, 'WyndhamWorldwide':float, 'Whitbreadplc':float})



# set input data, X are the data columns, y is the binary outcome (column 0)
X = dfs.loc[:,('99InnManagementCoLtd', 'AccorHotels', 'AmanResort', 'APAGroup', 'TheAscottLimited', 'BanyanTreeHoldings', 'Barriere', 'BestWesternHotels'
, 'TheDedicaAnthologyHotels', 'BTGHomeinnhotelgroup', 'RadissonHotelGroup', 'ChinaLodgingGroupLimitedHuazhuHotelsGroup', 'ChoiceHotels', 'CoastHotels'
, 'DorchesterCollection', 'DossenInternationalGroup', 'DruryHotels', 'DusitThaniGroup', 'ElegantHotelsGroup', 'ExtendedStayAmericaInc', 'FIHRegentGroup'
, 'FirstHotels', 'FourSeasonsHotelsandResorts', 'G6HospitalityLLC', 'GreenTreeInnsHotelManagementGroupInc', 'HiltonWorldwide', 'HNAHospitalityGroup'
, 'HongkongandShanghaiHotels', 'HoshinoResorts', 'HyattHotelsCorporation', 'InterContinentalHotelsGroupIHG', 'InterstateHotelResorts', 'InTownSuites'
, 'JinJiangInternational', 'Jumeirah', 'Kempinski', 'LanghamHospitalityGroup', 'LoewsHotels', 'LotteHotelsResorts', 'MagnusonHotels', 'MandarinOrientalHotelGroup'
, 'MarriottInternational', 'MeliaHotelsInternationalSA', 'MillenniumCopthorneHotels', 'MGMResortsInternational', 'MinorHotels', 'NHHotelGroup'
, 'TheOberoiGroup', 'OkuraNikkoHotelManagement', 'OmniHotelsResorts', 'PanPacificHotelsandResorts', 'PrinceHotels', 'RedLionHotelsCorporation'
, 'RedRoofInn', 'RIUHotelsResorts', 'RosewoodHotelGroup', 'ScandicHotels', 'ShangriLaHotelsandResorts', 'ShiloInns', 'SunmeiGroup', 'TajHotelsResortsandPalaces'
, 'TokyuHotels', 'ToyokoInn', 'Travelodge', 'Treebo', 'WaltDisneyParksandResorts', 'WarwickHotelsandResorts', 'WyndhamWorldwide', 'Whitbreadplc')].values
y = dfs.loc[:,'incident'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7, random_state=25)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.7)

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)   # this gives ValueError: Input contains NaN, infinity or a value too large for dtype('float64').

y_pred = LogReg.predict(X_test)

confusion_matrix = confusion_matrix(y_test, y_pred)

print(classification_report(y_test, y_pred))

#alternate for X
X = dfs[['99InnManagementCoLtd', 'AccorHotels', 'AmanResort', 'APAGroup', 'TheAscottLimited', 'BanyanTreeHoldings', 'Barriere', 'BestWesternHotels'
, 'TheDedicaAnthologyHotels', 'BTGHomeinnhotelgroup', 'RadissonHotelGroup', 'ChinaLodgingGroupLimitedHuazhuHotelsGroup', 'ChoiceHotels', 'CoastHotels'
, 'DorchesterCollection', 'DossenInternationalGroup', 'DruryHotels', 'DusitThaniGroup', 'ElegantHotelsGroup', 'ExtendedStayAmericaInc', 'FIHRegentGroup'
, 'FirstHotels', 'FourSeasonsHotelsandResorts', 'G6HospitalityLLC', 'GreenTreeInnsHotelManagementGroupInc', 'HiltonWorldwide', 'HNAHospitalityGroup'
, 'HongkongandShanghaiHotels', 'HoshinoResorts', 'HyattHotelsCorporation', 'InterContinentalHotelsGroupIHG', 'InterstateHotelResorts', 'InTownSuites'
, 'JinJiangInternational', 'Jumeirah', 'Kempinski', 'LanghamHospitalityGroup', 'LoewsHotels', 'LotteHotelsResorts', 'MagnusonHotels', 'MandarinOrientalHotelGroup'
, 'MarriottInternational', 'MeliaHotelsInternationalSA', 'MillenniumCopthorneHotels', 'MGMResortsInternational', 'MinorHotels', 'NHHotelGroup'
, 'TheOberoiGroup', 'OkuraNikkoHotelManagement', 'OmniHotelsResorts', 'PanPacificHotelsandResorts', 'PrinceHotels', 'RedLionHotelsCorporation'
, 'RedRoofInn', 'RIUHotelsResorts', 'RosewoodHotelGroup', 'ScandicHotels', 'ShangriLaHotelsandResorts', 'ShiloInns', 'SunmeiGroup', 'TajHotelsResortsandPalaces'
, 'TokyuHotels', 'ToyokoInn', 'Travelodge', 'Treebo', 'WaltDisneyParksandResorts', 'WarwickHotelsandResorts', 'WyndhamWorldwide', 'Whitbreadplc']].values