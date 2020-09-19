import h5py
import trimesh
import numpy as np
from argparse import ArgumentParser
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

def normalize(points):
    center = np.mean(points, axis= 0)
    points = points - center
    max_d = np.sqrt(np.max(points @ (points.T)))
    points = points / max_d
    return points 

def visualize(points, fig_name):
    points = np.array(points)

    points = normalize(points)
    eye = np.eye(3)
    bound_points = np.vstack((eye , eye * (-1)))
   
    x ,y ,z = points[:, 0], points[:, 1], points[:, 2]
    fig = plt.figure()
    ax = fig.add_subplot(projection= "3d")
    ax.scatter(y, x, z, s= 3, c= 'red', marker= "o")
    plt.savefig(fig_name)
    plt.close()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('input', type=str, help="Input voxel .h5 file path.")
    parser.add_argument('output', type=str, help="Output voxel visualization.")
    args = parser.parse_args()

    with open(args.input, 'r') as file:
        mesh = trimesh.load(file, file_type='off')
    points = trimesh.sample.sample_surface(mesh, 1024)[0]
    visualize(points, args.output)
