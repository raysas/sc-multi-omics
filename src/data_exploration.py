import scanpy as sc

data=sc.datasets.pbmc3k()
print(f'AnnData type: {type(data)}')

print(data)
print(f'AnnData dict: {data.__dict__}')

print(f'num of cells: {data.n_obs}')
print(f'num of genes: {data.n_vars}')
print(f'ann data shape: {data.shape}')

# -- first preprocessings:
print(f'filtering cells with less than 500 genes')
sc.pp.filter_cells(data, min_genes=500)
print(f'    num of cells after filtering: {data.n_obs}')
print(f'    num of genes after filtering: {data.n_vars}')

print(f'filtering genes expressed in less than 3 cells')
sc.pp.filter_genes(data, min_cells=3)
print(f'    num of cells after filtering: {data.n_obs}')
print(f'    num of genes after filtering: {data.n_vars}')

# -- plots
# print(f'plotting the number of genes per cell')
# sc.pl.violin(data, ['n_genes'], jitter=0.4, multi_panel=True)
# print(f'plotting the number of counts per cell')
# sc.pl.violin(data, ['n_cells'], jitter=0.4, multi_panel=True)

print(f'plotting the percentage of mitochondrial genes per cell')
data.var['mt'] = data.var_names.str.startswith('MT-')

# sc.pp.calculate_qc_metrics(data, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True) # -- imp to have pct_counts_mt in the obs
# sc.pl.violin(data, ['pct_counts_mt'], jitter=0.4, multi_panel=True)

print(data.var)
print(data.obs)

# -- from __dict__ can see that _obs and _var are private attributes, but can access them via .obs and .var
#    setters ensure the data in correct format (that of obs and var should be pandas dataframes)

# -- the real data is in data.X, scipy spare matrix
print(f'raw data type: {type(data.X)}')
# -- its shape is the same as data.shape