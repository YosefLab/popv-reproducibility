import scanpy as sc
from cuml.ensemble import RandomForestClassifier as cuRF
import numpy as np

print('new')
adata = sc.read(f'annotation/pretrained_models_cuml/prepared_data.h5ad')
adata.obs['_labels_annotation'] = np.arange(adata.n_obs)
adata.obs['_labels_annotation'] = adata.obs['_labels_annotation'].astype('category')
train_idx = adata.obs_names[:300]
train_x = adata[train_idx].X.todense()
train_y = adata.obs.loc[train_idx, '_labels_annotation'].cat.codes.to_numpy()
try:
    rf = cuRF(n_bins=128, bootstrap=False, verbose=True)
    rf.fit(train_x, train_y)
except:
    print('failed')
print('finished')
