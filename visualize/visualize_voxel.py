import h5py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input', type=str, help="Input voxel .h5 file path.")
    parser.add_argument('output', type=str, help="Output voxel visualization.")
    args = parser.parse_args()

    with h5py.File(args.input, "r") as f:
        # Get the data
        data = f['tensor'].value

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.voxels(data)
    plt.savefig(args.output)
    plt.close()