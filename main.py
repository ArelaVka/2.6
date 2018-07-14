import re
import sys
import os
import collections


def load_data(file_path):
    try:
        with open(file_path, 'r') as opened_file:
            return opened_file.read()
    except ValueError:
        return None

if __name__ == '__main__':
	return None