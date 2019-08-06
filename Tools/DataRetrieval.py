
import os
import requests
import tarfile

DEFAULT_DIRECTORY = 'data/raw_data'


class WebDataFetcher(object):
    """
    Class to fetch and handle the file-type processing to get the data ready for use
    """

    def __init__(self, data_dir = DEFAULT_DIRECTORY):
        self.data_dir = DEFAULT_DIRECTORY
        self.data_file = ''
        self.file_type = '' # To keep track of the type of file. Can make disparate format specific functions and then add aggregate functions to determine type and apply accordingly

    
    def fetch(self, data_url, save_path=DEFAULT_DIRECTORY, save_name='DATA'):
        """
        Method to download data from a specified url, and save it in a specified path
        """
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        
        # Code to check for type of download file and adapt file extension accordingly goes here
        tgz_path = os.path.join(save_path, (save_name + '.tgz'))
        x = requests.get(data_url, allow_redirects=True)
        open(tgz_path, 'wb').write(x.content)
        self.data_file = os.path.abspath(tgz_path)
        print(self.data_file)
    
    def attrs(self):
        for var in vars(self):
            print(var, ' ; type: ', type(vars(self)[var]), ' : ', vars(self)[var])

    def get_file_type(self):
        print(self.data_file[-6:])
        
        
    def extract_tgz_(self):
        data_tgz = self.data_file
        data_tgz = tarfile.open(tgz_path)
        data_tgz.extractall(path=save_path)
        data_tgz.close()
        os.remove(tgz_path)


TEST_URL = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz'



fetcher = WebDataFetcher()
fetcher.fetch(data_url = TEST_URL)
get_file_type()