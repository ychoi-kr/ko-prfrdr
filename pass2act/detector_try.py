
#!/usr/bin/env python

import os, requests, re, csv
import pandas as pd
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser

java_path = "usr/bin/java"
os.environ['JAVAHOME'] = java_path
current_dir = os.path.dirname(os.path.abspath(__file__))

stanford_parser_dir = current_dir + '/stanford_NLP/stanford-parser-full-2015-04-20'
eng_model_path = stanford_parser_dir + "/edu/stanford/nlp/models/lexparser/englishRNN.ser.gz"
my_path_to_models_jar = stanford_parser_dir + "/stanford-parser-3.5.2-models.jar"
my_path_to_jar = stanford_parser_dir + "/stanford-parser.jar"

parser = StanfordParser(model_path = eng_model_path, path_to_models_jar = my_path_to_models_jar, path_to_jar = my_path_to_jar)
dependency_parser = StanfordDependencyParser(path_to_jar = my_path_to_jar, path_to_models_jar = my_path_to_models_jar)


def save_csv_file(this_text_data, database_location):
    with open(database_location , 'w', newline='', encoding='utf-8') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter = ',')
        for n in range(0, len(this_text_data)):
            csvWriter.writerow(this_text_data[n])

def parse_sentence(sentence):
    print (sentence)
    result = dependency_parser.raw_parse(sentence)
    dep = result.__next__()
    parsed_result = list(dep.triples())
    print (parsed_result)
    auxpass = False
    nsubjpass = False
    nsubj = False

    if "nsubj" in str(parsed_result):
       nsubj = True

    if "nsubjpass" in str(parsed_result):
       nsubjpass = True

    if "auxpass" in str(parsed_result):
        auxpass = True

    words_in_sentence = word_tokenize(sentence)
    sentence_length_in_words = len(words_in_sentence)
    longest_word = max(words_in_sentence, key=len)
    longest_word_length = len(longest_word)
    return [sentence,nsubj,nsubjpass,auxpass,sentence_length_in_words,longest_word,longest_word_length]

def extract_sentences(page_content):
    this_text_data = []
    this_text_data.append(['sentence','nsubj','nsubjpass','auxpass','sentence_length_in_words','longest_word','longest_word_length'])
    sentences_to_parse = sent_tokenize(page_content)
    for sentence in sentences_to_parse:
        new_data_row = parse_sentence(sentence)
        this_text_data.append(new_data_row)
    return this_text_data


def get_text_from_dir(location):
    with open(location, 'r') as local_file:
        file_content = local_file.read()
        return file_content

def run_prog(dictionary_array):
    print(dictionary_array)
    for dictionary in dictionary_array:
        print ('Processing ' +  dictionary['location'] )
        text = get_text_from_dir(dictionary['location'])
        sentences_data = extract_sentences(text)

        save_csv_file(sentences_data,'PA_output' + dictionary['results'])


