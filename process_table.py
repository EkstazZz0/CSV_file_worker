from config import where_operators

def convert_table_to_type(table = list[dict]):
    row_types = []
    for key in table[0].keys():
        try:
            int(table[0].get(key))
            row_types.append(int)
        except ValueError:
            try:
                float(table[0].get(key))
                row_types.append(float)
            except ValueError:
                row_types.append(str)
    
    for table_index, row in enumerate(table):
        for key_index, key in enumerate(row.keys()):
            table[table_index][key] = row_types[key_index](table[table_index][key])
    
    return table


def filter_table(table = list[dict], where: str | None = None):

    if where:
        column, value = next((where.split(op) for op in where_operators if op in where))

        match where:
            case where if ">" in where:
                if type(table[0].get(column)) is str:
                    raise ValueError("Unsupported operator > for filtering string column")
                
                table = [row for row in table if row.get(column) > type(row.get(column))(value)]
            case where if "<" in where:
                if type(table[0].get(column)) is str:
                    raise ValueError("Unsupported operator < for filtering string column")
                
                table = [row for row in table if row.get(column) < type(row.get(column))(value)]
            case where if "=" in where:
                table = [row for row in table if type(row.get(column))(value) == row.get(column)]
    
    return table


def get_aggregation(table = list[dict], aggregate: str | None = None):
    if not aggregate:
        return table
    
    column_name, operator = aggregate.split("=")
    
    if type(table[0].get(column_name)) is str:
        raise ValueError(f"aggregation for string columns, like {column_name} is not supported. Use columns with int or float types")

    values = [row.get(column_name) for row in table]

    match operator:
        case "min":
            return [{operator: min(values)}]
        case "max":
            return [{operator: max(values)}]
        case "avg":
            return [{operator: sum(values) / len(values)}]