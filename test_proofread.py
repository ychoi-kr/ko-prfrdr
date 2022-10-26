import unittest
import glob
import sys

from proofread import *

import yaml


import_KoNLPy()

class TestsContainer(unittest.TestCase):
    longMessage = True

def make_test_function(name, line):
    def test(self):
        if re.match(r'\w+_TC\d', name):
            corrections = check(rules, line, show_all_lines=False)
            #print(corrections)
            self.assertGreater(len(corrections), 0, name)
        elif re.match(r'\w+_FC\d', name):
            corrections = check(rules, line, show_all_lines=False)
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

