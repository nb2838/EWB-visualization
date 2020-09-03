import os
import pytest

from mappy_all import get_layer, EWBLayer, get_map, EWBMap

def test_get_layer():
	"""
	BAD CASES
	filestring = "no_existence" (wrong filetype) - OSError: File extension or name of no_existence not supported. Use csv or excel documents
	filestring = "YellowEWB.csv" (without such file) - FileNotFoundError: [Errno 2] File b'YellowEWB.csv' does not exist: b'YellowEWB.csv'
	filestring = "testYellow.csv" (wrong naming convention) - ValueError: The file name should be <layer name>_<layer color>.csv/xlsx, 
																received filename testYellow.csv
	filestring = "Surveyees random_orange.xlsx" (wrong delimiter) -  ValueError: The filename should be <layer name>,<layer color>.csv/xlsx, 
																received filename Surveyees random_orange.xlsx

	GOOD CASES
	filestring = "Surveyees,Yellow.csv" - UserWarning: color argument of Icon should be one of: {'green', 'beige', 'red', 'blue', 'black', 
											'lightgreen', 'darkred', 'white', 'gray', 'lightblue', 'purple', 'lightred', 'orange', 'darkblue', 
											'darkpurple', 'lightgray', 'darkgreen', 'pink', 'cadetblue'}.
    icon = folium.Icon(icon=icon, color=color, prefix='fa')
    
	"""
	filestring = "./files/Surveyees random, Orange.xlsx"
	result = get_layer(filestring)
	assert type(result) == EWBLayer

def test_recenter():
	"""
	BAD CASES
	string = "allwww" (no such layer) -  OSError: ERROR: wrong string input: allwww, valid inputs are: ['Surveyees'] or 'all' or 'town

	GOD CASES
	string = "" - default "all"
	string = "town" - default hardcoded location
	string = "test" - existing layer name
	"""
	sampleMap = get_map(['./files/Surveyees random, Orange.xlsx', './files/test, Yellow.csv'])
	sampleMap.recenter("test")


"""
#test cases
def recenter:
    wrong string input
    no points on the map
    set default location to the township
    --> needs to mock the connecting functions
def get_layer:
    wrong string input
    ill-formatted excel/csv
    --> connecting functions: get_map && make_popups && EWBMap constructor
"""