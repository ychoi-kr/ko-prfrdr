import unittest
import glob
import sys
from collections import Counter

from proofread import *

import yaml


import_KoNLPy()

class TestsContainer(unittest.TestCase):
    longMessage = True

def make_test_function(name, line):
    def test(self):
        warnings_counter = Counter()
        if re.match(r'\w+_TC\d', name):
            corrections, warnings_counter = check(rules, line, None, False, warnings_counter)
            #print(corrections)
            self.assertGreater(len(corrections), 0, name)
        elif re.match(r'\w+_FC\d', name):
            corrections, warnings_counter = check(rules, line, None, False, warnings_counter)
            #print(corrections)
            self.assertEqual(len(corrections), 0, name)
        else:
            sys.exit("Something's wrong with test cases!")
    return test


if __name__ == '__main__':
    rules = loadrules(' '.join(glob.glob('*.json')))
    for filename in glob.glob('test/*.yaml'):
        with open(filename, 'r') as stream:
            try:
                parsed_yaml = yaml.safe_load(stream)
                caseid = re.search(r'test/(\w+).yaml', filename)[1]
                true_cases = parsed_yaml['true cases']
                if true_cases:
                    for i, case in enumerate(true_cases):
                        name = caseid +'_TC' + str(i)
                        test_func = make_test_function(name, case)
                        setattr(TestsContainer, f'test_{name}', test_func)
   
                false_cases = parsed_yaml['false cases']
                if false_cases:
                    for i, case in enumerate(false_cases):
                        name = caseid +'_FC' + str(i)
                        test_func = make_test_function(name, case)
                        setattr(TestsContainer, f'test_{name}', test_func)

            except yaml.YAMLError as e:
                print(e)
        
    unittest.main()

