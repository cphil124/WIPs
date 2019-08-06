
import os
import requests
import tarfile
import sys

DEFAULT_DIRECTORY = 'data/raw_data'

FILETYPE_LIB = ['tgz', 'csv']


class WebDataFetcher(object):
    """
    Class to fetch and handle the file-type processing to get the data ready for use
    """

    def __init__(self):
        self.data_dir = ''
        self.data_file = ''
        self.file_type = '' # To keep track of the type of file. Can make disparate format specific functions and then add aggregate functions to determine type and apply accordingly

    
    def fetch(self, data_url, save_path=DEFAULT_DIRECTORY, save_name='DATA'):
        """
        Method to download data from a specified url, and save it in a specified path
        """
        # Runs get_file_type on the incoming data to confirm that it is a supported filetype.  If it is, then it will set the class attribute file_type for later reference. 
        # If it is not, then it it will exit the program.
        self.file_type = self.get_file_type(file=data_url)

        # Create the save dir if it doesn't exist and add it to the instance attributes
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        
        self.data_dir = save_path
        
        # get_file_type(
        # Code to check for type of download file and adapt file extension accordingly goes here
        file_path = os.path.join(save_path, (save_name + '.' + self.file_type))
        x = requests.get(data_url, allow_redirects=True)
        open(file_path, 'wb').write(x.content)
        self.data_file = os.path.abspath(file_path)
        # self.
        print(self.data_file)
    
    def attrs(self):
        """
        See all attributes of the object and their types
        """
        for var in vars(self):
            print(var, ' ; type: ', type(vars(self)[var]), ' : ', vars(self)[var])

    def get_file_type(self, file):
        if file:
            data = file
        else:
            data = self.data_file

        extension = data[-6:].split('.')[1]

        if extension in FILETYPE_LIB:
            return extension
        else:
            print('This filetype handling not supported at present')
            sys.exit(1)


        
        
    def extract_tgz_(self):
        """
        Right now only handles tgz files, should change so that it can dynamically extra
        """
        # if self.file_type is tgz
        tgz_path = self.data_file
        save_path = self.data_dir
        data_tgz = tarfile.open(tgz_path)
        data_tgz.extractall(path=save_path)
        data_tgz.close()
        os.remove(tgz_path)


TEST_URL = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz'



fetcher = WebDataFetcher()
# fetcher.fetch(data_url = TEST_URL)
x = fetcher.get_file_type(file='target.tgz')
print(x)