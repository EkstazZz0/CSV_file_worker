from argparse import ArgumentParser, Namespace
import os
from config import where_operators, aggregate_operators

def validate_arguments(parser: ArgumentParser):
    args = parser.parse_args()

    if not (os.path.exists(args.file) and os.path.isfile(args.file) and args.file.lower().endswith("csv")):
        parser.error("Invalid file path. It could be a path for a folder or a non-csv file")
    
    if args.where and not any(op in args.where for op in where_operators):
        parser.error("Unavailable operator for where, you should use >, < or =.\nExample: 'column<value'")
    
    if args.aggregate and not any(args.aggregate.endswith(op) for op in aggregate_operators) and not ("=" in args.aggregate):
        parser.error("Unavailable operator for aggregate. It supports only min, max and avg.\nExample: 'column=min'")


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--where", required=False)
    parser.add_argument("--aggregate", required=False)

    validate_arguments(parser=parser)

    return parser.parse_args()