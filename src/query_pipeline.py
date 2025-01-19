import argparse

parser = argparse.ArgumentParser(description ='Process user query and generate response.')
parser.add_argument('--query', 
                    type = str, 
                    help ='The query to be answered',
                    default = None)

parser.add_argument('--path', 
                    type = str, 
                    help ='The file path to the query in audio form')

args = parser.parse_args()

query = args.query
print(query)