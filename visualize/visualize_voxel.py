import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

filename = "ModelNet10_voxelized/bed/train/0.h5"

with h5py.File(filename, "r") as f:
    # Get the data
    data = f['tensor'].value

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.voxels(data)
plt.savefig('test.png')
plt.close()