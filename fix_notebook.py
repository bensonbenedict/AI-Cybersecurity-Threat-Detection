import nbformat

with open('train.ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'code':
        if "if df[column].dtype == 'object':" in cell.source:
            cell.source = cell.source.replace("if df[column].dtype == 'object':", "if df[column].dtype in ['object', 'str', 'string'] or str(df[column].dtype) in ['string', 'str', 'object']:")

with open('train.ipynb', 'w') as f:
    nbformat.write(nb, f)
