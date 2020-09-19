import numpy as np
import trimesh


if __name__ == '__main__':
    # print logged messages
    trimesh.util.attach_to_log()

    # load a mesh
    with open("./ModelNet10_scaled/chair/train/0.off", 'r') as file:
        mesh = trimesh.load(file, file_type='off')

    # get a scene object containing the mesh, this is equivalent to:
    # scene = trimesh.scene.Scene(mesh)
    scene = mesh.scene()

    # a 45 degree homogeneous rotation matrix around
    # the Y axis at the scene centroid
    rotate = trimesh.transformations.rotation_matrix(
        angle=np.radians(10.0),
        direction=[0, 1, 0],
        point=scene.centroid)

    for i in range(4):
        trimesh.constants.log.info('Saving image %d', i)

        # rotate the camera view transform
        camera_old, _geometry = scene.graph[scene.camera.name]
        camera_new = np.dot(rotate, camera_old)

        # apply the new transform
        scene.graph[scene.camera.name] = camera_new

        # saving an image requires an opengl context, so if -nw
        # is passed don't save the image
        try:
            # increment the file name
            file_name = 'render_' + str(i) + '.png'
            # save a render of the object as a png
            png = scene.save_image(resolution=[1920, 1080], visible=True)
            with open(file_name, 'wb') as f:
                f.write(png)
                f.close()

        except BaseException as E:
            print("unable to save image", str(E))