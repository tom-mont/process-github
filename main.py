import logging
from requests_sse import EventSource
import json
from pprint import pformat

def main():
    logging.info("START")

    with EventSource(
            "http://github-firehose.libraries.io/events",
            timeout=30
    ) as event_source:
        for event in event_source:
            value = json.loads(event.data) ## turns into python dictionary
            key = value['id'] ## note the dictionary notation1
            logging.info("Got: %s", pformat(value)) ## turns back into a string with neat indentation

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
