import argparse
from inference_api import query_response
from transformers import pipeline
from extract_data import return_data


class Pipeline:
    def __init__(self, query="", path=""):
        self.query, self.path = query, path
        self.context = return_data()
        print(self.context)
        # self.summary = self.summarize_articles(self.context)

    def generate_response(self):
        return query_response(self.query)

    def summarize_articles(self, articles_text, max_length=300, min_length=100):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(
            articles_text, max_length=max_length, min_length=min_length, do_sample=False
        )
        return summary[0]["summary_text"]


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
