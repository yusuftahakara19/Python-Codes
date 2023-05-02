import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from scipy.spatial import distance
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


# Dosyadan verileri okuma
data = np.genfromtxt('tree.txt', delimiter=',')

# Verilerin ilk üç sütununu seçme
points = data[:, :3]

# Z koordinatı 173.49424744 ile 173.59855652 arasındaki noktaları seçme
z_filtered_points = points[(points[:, 2] > 173.49424744) & (points[:, 2] < 173.59855652)]

# PCA ile boyut indirgeme
pca = PCA(n_components=2)
reduced_points = pca.fit_transform(z_filtered_points)

# Elipsin merkezini bulma
center = np.mean(reduced_points, axis=0)

# Elipsin boyutlarını ve açısını bulma
cov_matrix = np.cov(reduced_points, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
width = 2 * np.sqrt(eigenvalues[0])
height = 2 * np.sqrt(eigenvalues[1])
angle = np.degrees(np.arctan2(*eigenvectors[:, 0][::-1]))

# Elipsi çizdirme
ellipse = Ellipse(xy=center, width=width, height=height, angle=angle, fill=False)
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.add_artist(ellipse)

# Verileri çizdirme
ax.scatter(reduced_points[:, 0], reduced_points[:, 1], s=1)

# BDH hesaplama ve çıktı alma
bdh = width
ax.set_title('BDH = {:.4f}'.format(bdh))
print("Breast Diameter Height (BDH):", bdh)

# Grafikleri gösterme
plt.show()