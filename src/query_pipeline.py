import argparse
from inference_api import query_response

class Pipeline:
    def __init__(self, query='', response=''):
        self.query, self.path = self.parse_arguments()
        self.response = response

    def generate_response(self):
        return query_response(self.query)

    
    def parse_arguments(self):

        parser = argparse.ArgumentParser(description ='Process user query and generate response.')
        parser.add_argument('--query', 
                            type = str, 
                            help ='The query to be answered',
                            default = None)

        parser.add_argument('--path', 
                            type = str, 
                            help ='The file path to the query in audio form',
                            default=None)

        args = parser.parse_args()
        query = args.query
        path = args.path
        #print(query)

        return query, path