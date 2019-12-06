import csv
import datetime
from hdx.data.dataset import Dataset
from hdx.hdx_configuration import Configuration
import shutil
import glob
import os, sys

def get_new_date(urlend, docname):
    # Gets specific url for indicated category
    Configuration.create(hdx_site='prod', user_agent='A_Quick_Example', hdx_read_only=True)
    dataset = Dataset.read_from_hdx(urlend)
    datasets = Dataset.search_in_hdx(docname, rows=10)
    resources = Dataset.get_all_resources(datasets)
    # Creates variable for most updated version of dataset date
    y = dataset.get_dataset_date()
    # Gets year, month, and day of dataset
    year1 = y[:4]
    month1 = y[5:7]
    day1 = y[8:10]
    # Organizes dataset date into datetime format
    global d2
    d2 = datetime.datetime(int(year1),int(month1),int(day1))

# Gets original date from csv and converts to datetime format
def getd1(csv1):
    a = []; i=0; b='';
    csvReader = csv.reader(open(csv1, 'r'), delimiter='|');
    for row in csvReader:
        a.append(row)
    print(a)
    for i in range(0, len(a)):
        a.append(i)
    print(a)
    newvar = a[i]
    newstr = str(newvar).strip('[]')
    x = newstr.replace("'", "")
    year,month,day = x.split('-')
    global d1
    d1 = datetime.datetime(int(year),int(month),int(day))

# Compares older date to newer date
def compare_dates(csvname,urlend,filename,docname,keyword):
    dataset = Dataset.read_from_hdx(urlend)
    datasets = Dataset.search_in_hdx(docname, rows=10)
    resources = Dataset.get_all_resources(datasets)
    if d2 > d1:
        url, path = resources[0].download('/Users/katherinenewcomb/Desktop/TestingRepo')
        print('Resource URL %s downloaded to %s' % (url, path))
        f= open('/Users/katherinenewcomb/Desktop/TestingRepo/{}'.format(csvname),"w+")
        f.write(dataset.get_dataset_date())
        shutil.move('/Users/katherinenewcomb/Desktop/TestingRepo/{}'.format(filename),'/Users/katherinenewcomb/Desktop/TestingRepo/ArchiveData/{}'.format(filename))
        os.rename('/Users/katherinenewcomb/Desktop/TestingRepo/{}'.format(filename),'/Users/katherinenewcomb/Desktop/TestingRepo/ArchiveData/{}'.format(filename))
        newfile = glob.glob('/Users/katherinenewcomb/Desktop/TestingRepo/*{}*'.format(keyword))
        print(newfile)
    else:
        newfile = "No new file"
        print(newfile)
        print('System Update Complete')
    return newfile

# Each function below tests individual category for updated data
def choos_func(function1):
    if function1 == 'get_poverty_update':
        def get_poverty_update():
            getd1('povertydate.csv')
            get_new_date('philippines-poverty-statistics','190710')
            compare_dates('povertydate.csv', 'philippines-poverty-statistics','190710_poverty-statistics.xlsx.XLSX','190710','poverty')
        get_poverty_update()
    elif function1 == 'get_popage_update':
        def get_popage_update():
            getd1('popdate.csv')
            get_new_date('philippines-pre-disaster-indicators','180814')
            compare_dates('popdate.csv','philippines-pre-disaster-indicators','180814_Philippines Population Admin 1 to 3_2015_vertical.xlsx.XLSX','180814','pre-disaster')
        get_popage_update()
    elif function1 == 'get_housing_update':
        def get_housing_update():
            getd1('housingdate.csv')
            get_new_date('philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9','PHL_haima_houses')
            compare_dates('housingdate.csv','philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9','PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv.CSV','PHL_haima_houses','house')
        get_housing_update()
    elif function1 == 'get_employment_update':
        def get_employment_update():
            getd1('employmentdate.csv')
            get_new_date('philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0','employment')
            compare_dates('employmentdate.csv','philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0', 'Work and employment.csv.CSV','employment','employment')
        get_employment_update()
    elif function1 == 'get_dependency_update':
        def get_dependency_update():
            getd1('dependencydate.csv')
            get_new_date('world-bank-indicators-for-philippines','Age dependency')
            compare_dates('dependencydate.csv','world-bank-indicators-for-philippines', 'Old_age_dependency_ratio.xlsx.XLSX','Age dependency','dependency')
        get_dependency_update()
    else:
        print('Failed')
