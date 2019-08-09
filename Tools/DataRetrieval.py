
import os
import requests
import tarfile
import zipfile
import sys

DEFAULT_DIRECTORY = 'data/raw_data'

FILETYPE_LIB = ['tgz', 'csv']
ARCHIVE_LIB = ['tgz', 'bz2', 'tar', 'zip']


class WebDataFetcher(object):
    """
    Class to fetch and handle the file-type processing to get the data ready for use
    """

    def __init__(self, file):
        if file:
            self.data_file = os.path.abspath(file)
            self.file_type = self.get_file_type_(self.data_file)
            self.data_dir = os.path.dirname(self.data_file)
        else:
            self.data_file = ''
            self.data_dir = ''
            self.file_type = '' # To keep track of the type of file. Can make disparate format specific functions and then add aggregate functions to determine type and apply accordingly

    
    def fetch(self, data_url, save_path=DEFAULT_DIRECTORY, save_name='DATA'):
        """
        Method to download data from a specified url, and save it in a specified path
        """
        # Runs get_file_type on the incoming data to confirm that it is a supported filetype.  If it is, then it will set the class attribute file_type for later reference. 
        # If it is not, then it it will exit the program.
        self.file_type = self.get_file_type_(file=data_url)

        # Create the save dir if it doesn't exist and add it to the instance attributes
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        
        self.data_dir = save_path
        
        # Code to check for type of download file and adapt file extension accordingly goes here
        file_path = os.path.join(save_path, (save_name + '.' + self.file_type))
        x = requests.get(data_url, allow_redirects=True)
        open(file_path, 'wb').write(x.content)
        self.data_file = os.path.abspath(file_path)
        print(self.data_file)
    
    def attrs(self):
        """
        See all attributes of the object and their types
        """
        for var in vars(self):
            print(var, ' ; type: ', type(vars(self)[var]), ' : ', vars(self)[var])

    def get_file_type_(self, file):
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

    
    def is_unzippable(self):
        if self.file_type in ARCHIVE_LIB:
            return True
        else:
            return False

    def convert_github_url(self, gh_url, filename):
        raw_url = gh_url.replace(old='github', new='raw.githubusercontent')
        full_url = os.path.join(raw_url, filename)
        return full_url

        
        
    def extract_all_(self):
        """
        Right now only handles tgz files, should change so that it can dynamically extra
        """
        # Setting of important variables
        data = self.data_file
        save_path = self.data_dir

        # Extract contents of file
        if zipfile.is_zipfile(data):
            f = zipfile.ZipFile(data)
            f.extractall(path = data[:-4])
            f.close()

        elif tarfile.is_tarfile(data):
            data_tgz = tarfile.open(name=data)
            data_tgz.extractall(path=save_path)
            data_tgz.close()
        
        os.remove(data)


TEST_TGZ_URL = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz'
TEST_CSV_URL = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv'
regular_url = 'https://github.com/ageron/handson-ml2/tree/master/datasets/housing'


def main():
    # fetcher = WebDataFetcher()
    # fetcher.fetch(data_url = TEST_URL)
    # print('got here')
    # fetcher.attrs()
    # print(fetcher.is_unzippable())
    # fetcher.extract_tgz_()
    fetcher = WebDataFetcher('data\\raw_data\\housing.csv')
    fetcher.attrs


if __name__ == "__main__":
    main()