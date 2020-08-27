import os

import pytest

import ewb_mappy.validation as v
import ewb_mappy.read as r

CURRENT_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
GOOD_FILE_PATH = os.path.join(CURRENT_FILE_PATH, 'test_files/good_tables')
BAD_FILE_PATH = os.path.join(CURRENT_FILE_PATH, 'test_files/bad_tables')


class TestFileReading:
    def test_determine_extension_excel_files(self):
        excel_files = ['test.xlsm','test/home.xls', 'home/me_caat/test.xls']
        for filename in excel_files:
            assert r.determine_extension(filename) == r.EXCEL_EXTENSION

    def test_determine_extension_csv_files(self):
        long_name = '/Users/nicolasvelezbeltran/Documents/Columbia/ghana/EWB-visualization/'
        long_name += 'tests/test_files/bad_tables/bad_latitude_format.csv'
        csv_files = ['test.csv', 'test/home/ewb.csv', long_name]
        
        for filename in csv_files:
            assert r.determine_extension(filename) == r.CSV_EXTENSION


class TestDataValidation:
    
    def test_invalid_raise_error(self):
        """Test that verifies invalid files raise an error"""
        bad_files = os.listdir(BAD_FILE_PATH)
        bad_files = [os.path.join(BAD_FILE_PATH, filename) for filename in bad_files]
        for filename in bad_files:
            with pytest.raises(ValueError):
                test_map = r.get_map(filename)

        

        
        
