# 3D-multiview
Utility scripts to generate 3D multi-representation datasets. These scripts convert mesh data (`.off` files) into multiview images or voxels.

## Download Datasets
Simple run

```
./download.sh
```

in each scripts folder. The dataset will be downloaded to that folder.

## Mesh to Voxels
To convert mesh to voxels, I used [`mesh-voxelixation`](https://github.com/davidstutz/mesh-voxelization). For building `mesh-voxelization`, checkout the original repo. After building, move the binary in `mesh-voxelization/bin/voxelize` to `/usr/bin`.
   
To convert dataset from mesh representation to voxels, in each scripts folder run

```
scale.sh
voxelize.sh
```
A scaled mesh dataset `[dataset name]_scaled` and a voxel dataset `[dataset_name]_voxelized` will be created in the scripts folder.
