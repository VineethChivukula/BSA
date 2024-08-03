import os
import re
from graphviz import Digraph

def list_sql_files(directory):
    """List all SQL files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.sql')]

def parse_sql_file(filepath):
    """Parse the SQL file to extract schema information and relationships."""
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Simple regex to extract table name and columns
    tables = re.findall(r'CREATE TABLE (\w+) \((.*?)\);', content, re.S)
    schema_info = []
    relationships = []
    
    for table, columns in tables:
        columns = [col.strip() for col in columns.split(',')]
        for col in columns:
            col_name = col.split()[0]
            col_type = ' '.join(col.split()[1:])
            schema_info.append((table, col_name, col_type))
            
            # Detect foreign key relationships
            fk_match = re.match(r'FOREIGN KEY \((\w+)\) REFERENCES (\w+)\((\w+)\)', col)
            if fk_match:
                fk_column, ref_table, ref_column = fk_match.groups()
                relationships.append((table, fk_column, ref_table, ref_column))
    
    return schema_info, relationships

def generate_erd(directory):
    """Generate an ERD for the SQL files in the given directory."""
    sql_files = list_sql_files(directory)
    all_schema_info = []
    all_relationships = []
    
    for sql_file in sql_files:
        filepath = os.path.join(directory, sql_file)
        schema_info, relationships = parse_sql_file(filepath)
        all_schema_info.extend(schema_info)
        all_relationships.extend(relationships)
    
    # Create a graph
    dot = Digraph(comment='ERD')
    
    # Add tables and columns
    tables = {}
    for table, col_name, col_type in all_schema_info:
        if table not in tables:
            tables[table] = []
        tables[table].append(f'{col_name}: {col_type}')
    
    for table, columns in tables.items():
        dot.node(table, label=f'{table}\n' + '\n'.join(columns), shape='box')
    
    # Add relationships
    for table, fk_column, ref_table, ref_column in all_relationships:
        dot.edge(f'{table}:{fk_column}', f'{ref_table}:{ref_column}', label=f'{fk_column} -> {ref_column}')
    
    # Save and render the graph
    dot.render('erd', format='png', cleanup=True)
    print("ERD generated and saved as 'erd.png'")

# Directory containing SQL migration files
migrations_directory = 'migrations'

# Generate ERD
generate_erd(migrations_directory)