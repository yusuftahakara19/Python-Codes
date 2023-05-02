import numpy as np
from sklearn.decomposition import PCA
from scipy.spatial import distance
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

# Dosyadan verileri okuma
data = np.genfromtxt('tree.txt', delimiter=',')

# Verilerin ilk üç sütununu seçme
points = data[:, :3]

# Z koordinatı 173.49424744 ile 173.59855652 arasındaki noktaları seçme
z_filtered_points = points[(points[:, 2] > 173.49424744) & (points[:, 2] < 173.59855652)]

# PCA ile boyut indirgeme
pca = PCA(n_components=2)
reduced_points = pca.fit_transform(z_filtered_points)

# Elipsin merkezini ve boyutlarını bulma
center = np.mean(reduced_points, axis=0)
cov_matrix = np.cov(reduced_points, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
big_radius = np.max(np.sqrt(eigenvalues))
small_radius = np.min(np.sqrt(eigenvalues))
angle = np.degrees(np.arctan2(*eigenvectors[:, 0][::-1]))

# Elipsi çizdirme
ellipse = Ellipse(xy=center, width=2*big_radius, height=2*small_radius, angle=angle, fill=False)
fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect('equal')
ax.add_artist(ellipse)

# Verileri çizdirme
ax.scatter(reduced_points[:, 0], reduced_points[:, 1], s=1)

# BDH hesaplama ve çıktı alma
bdh_ellipse = 2*big_radius
ax.set_title('BDH (Elips) = {:.4f}'.format(bdh_ellipse))
print("Breast Diameter Height (BDH - Elips):", bdh_ellipse)

# Çemberin merkezini ve yarıçapını bulma
radius_circle = big_radius
circle = Circle(xy=center, radius=radius_circle, fill=False)
ax.add_artist(circle)

# BDH hesaplama ve çıktı alma
bdh_circle = 2*radius_circle
print("Breast Diameter Height (BDH - Çember):", bdh_circle)

# Grafikleri gösterme
ax.set_xlim(center[0]-1.1*big_radius, center[0]+1.1*big_radius)
ax.set_ylim(center[1]-1.1*big_radius, center[1]+1.1*big_radius)
plt.show()