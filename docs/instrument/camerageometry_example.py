from ctapipe.instrument import CameraGeometry
from matplotlib import pyplot as plt

plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
geom = CameraGeometry.from_name("HESS", 1)
plt.imshow(geom.neighbor_matrix)
plt.title('Pixel Neighbor Matrix')

plt.subplot(1, 2, 2)
plt.scatter(geom.pix_x, geom.pix_y)
plt.title('Pixel Positions')

plt.show()
