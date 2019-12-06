from hdx.hdx_configuration import Configuration
from hdx.data.dataset import Dataset

def get_resources(url_end, csv_filename, docname,keyword):
    Configuration.create(hdx_site='prod', user_agent='A_Quick_Example', hdx_read_only=True)
    # Gets web url
    dataset = Dataset.read_from_hdx(url_end)
    # Writes Dataset Date in dependencydate csv
    f= open('/Users/katherinenewcomb/Desktop/TestingRepo/{}'.format(csv_filename),"w+")
    f.write(dataset.get_dataset_date())
    # Searches for specific file on web url
    datasets = Dataset.search_in_hdx(docname, rows=10)
    # Grabs resources from file
    global resources
    resources = Dataset.get_all_resources(datasets)
    # Only uncomment if you want to download file!!
    url, path = resources[0].download('/Users/katherinenewcomb/Desktop/TestingRepo/censusfiles')
    print('Resource URL %s downloaded to %s' % (url, path))


# Have to run each separately for code to work

# Poverty
get_resources('philippines-poverty-statistics','povertydate.csv','190710','poverty')

# Population + Age
# get_resources('philippines-pre-disaster-indicators', 'popdate.csv', '180814')

# Housing
# get_resources('philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9','housingdate.csv','PHL_haima_houses')

# Employment - Downloads wrong file (11/21/19)
# get_resources('philippines-other-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0','employment_NSCB.xls','employment')

# Dependency - Downloads wrong file (11/21/19)
# get_resources('world-bank-indicators-for-philippines','dependencydate.csv','all_indicators_phl')
