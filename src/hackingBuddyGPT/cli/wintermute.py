import argparse
import sys
from dotenv import load_dotenv
import os
from hackingBuddyGPT.usecases.base import use_cases


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(required=True)
    for name, use_case in use_cases.items():
        subb = subparser.add_parser(
            name=use_case.name,
            help=use_case.description
        )
        use_case.build_parser(subb)
    x= sys.argv[1:]
    parsed = parser.parse_args(x)
    instance = parsed.use_case(parsed)
    instance.init()
    instance.run()


if __name__ == "__main__":
    main()
