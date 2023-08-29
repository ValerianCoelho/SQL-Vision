def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def Create_Table_Query(table_name, column_names, data_types, constraints):
    columns = []

    for column_name, data_type, constraint in zip(column_names, data_types, constraints):
        columns.append(f'{column_name} {data_type} {constraint}')

    column_query = ', '.join(columns)
    query = f'CREATE TABLE {table_name} ({column_query});'
    return query

def Fill_Table_Query(table_name, data):
    column_names, *data = data
    query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES "

    value_rows = []
    for row in data:
        values = []
        for value in row:
            if is_float(value) or value.lower() == 'null':
                values.append(value)
            else:
                values.append(f"'{value}'")
        value_rows.append(f"({', '.join(values)})")

    query += ', '.join(value_rows) + ";"
    return query