import argparse
from inference_api import query_response


class Pipeline:
    def __init__(self, query="", path=""):
        self.query, self.path = query, path

    def generate_response(self):
        return query_response(self.query)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Process user query and generate response."
    )
    parser.add_argument(
        "--query", type=str, help="The query to be answered", default=None
    )

    parser.add_argument(
        "--path",
        type=str,
        help="The file path to the query in audio form",
        default=None,
    )

    args = parser.parse_args()
    return args.query, args.path


if __name__ == "__main__":
    query, path = parse_arguments()
    pipeline = Pipeline(query, path)
    response = pipeline.generate_response()
    print("Response:", response)
