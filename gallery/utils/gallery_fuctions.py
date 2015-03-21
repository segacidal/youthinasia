__author__ = 'clint'

import os

def create_folder(foldername):
    #print os.path.join(os.path.dirname(__file__), '..', foldername)
    os.mkdir(os.path.join(os.path.dirname(__file__), '..', foldername))


if __name__ == '__main__':
    #create_folder('test-thing')
    pass