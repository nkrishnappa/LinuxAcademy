"""
Question: Create a Python function that takes a text file as input and 
returns the number of words contained in the text file.
"""
import argparse

def wordCount(file):
    with open(file, "r") as f:
        contents = f.read()
        return len(contents.split())

parser = argparse.ArgumentParser()
# parser.add_argument('file')
parser.add_argument(
    '-f', '--file'
)
args = parser.parse_args() 
print(wordCount(args.file))

"""
Explanation:

The script consists of opening the file in read mode,
loading the text into a string using read  and 
then splitting and counting the number of words.
"""