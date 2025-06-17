import csv
from tabulate import tabulate

from get_args import parse_arguments
from process_table import convert_table_to_type, filter_table, get_aggregation


def process_csv_file(file_path: str, where: str | None = None, aggregate: str | None = None):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        table = csv.DictReader(csvfile)
        table = [row for row in table]
        table = convert_table_to_type(table=table)
        table = filter_table(table=table, where=where)
        table = get_aggregation(table=table, aggregate=aggregate)
    
    return table


if __name__ == '__main__':
    args = parse_arguments()
    print(tabulate(process_csv_file(file_path=args.file, where=args.where, aggregate=args.aggregate), headers="keys", tablefmt="grid"))
