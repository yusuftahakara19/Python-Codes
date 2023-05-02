import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from scipy.spatial import distance
import matplotlib.pyplot as plt


# Dosyadan verileri okuma
data = np.genfromtxt('tree.txt', delimiter=',')

# Verilerin ilk üç sütununu seçme
points = data[:, :3]

# Z koordinatı 173.49424744 ile 173.59855652 arasındaki noktaları seçme
z_filtered_points = points[(points[:, 2] > 173.49424744) & (points[:, 2] < 173.59855652)]

# PCA ile boyut indirgeme
pca = PCA(n_components=2)
reduced_points = pca.fit_transform(z_filtered_points)

# Dairenin merkezini bulma
center = np.mean(reduced_points, axis=0)

# Dairenin yarıçapını bulma
radius = np.max(distance.cdist(reduced_points, [center]))

# Çemberi çizdirme
circle = plt.Circle(center, radius, fill=False)
fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect('equal')
ax.add_artist(circle)

# Verileri çizdirme
ax.scatter(reduced_points[:, 0], reduced_points[:, 1], s=1)

# BDH hesaplama ve çıktı alma
bdh = radius * 2
print("Breast Diameter Height (BDH):", bdh)

# Grafikleri gösterme
ax.set_xlim(center[0]-1.1*radius, center[0]+1.1*radius)
ax.set_ylim(center[1]-1.1*radius, center[1]+1.1*radius)
plt.show()