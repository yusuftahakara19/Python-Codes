import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from scipy.stats import ttest_rel
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Excel dosyasını oku
<<<<<<< HEAD:AI/Regression_Analysis/regression_analysis.py
df = pd.read_excel('dataset.xlsx')
=======
df = pd.read_excel('database.xlsx')
>>>>>>> b6d782d91abd94c7c84746e5e1c7d88a1cb722e8:AI/Height_Estimation_With_Machine_Learning/Height_Estimation_With_Machine_Learning.py

# LabelEncoder nesnesini oluştur
label_encoder = LabelEncoder()

# Verilerin türünü dönüştür
# Veri kümesindeki kategorik verilerin sayısal formata dönüştürülmesi 
for column in df.columns:
    df[column] = df[column].astype(str)
    df[column] = label_encoder.fit_transform(df[column])

# Anket verilerini ayrıştır
X = df.drop('Boy', axis=1)
y = df['Boy']

# Tahminleyicileri tanımla
linear_reg = LinearRegression()
decision_tree_reg = DecisionTreeRegressor()
random_forest_reg = RandomForestRegressor()
svr = SVR()
knn_reg = KNeighborsRegressor()

# Tahminleyici listesi
regressors = [linear_reg, decision_tree_reg, random_forest_reg, svr, knn_reg]

# Tahminleyici başarılarını değerlendir
# 5 farklı tahminleyici ile 10 katlı çapraz geçerleme sonuçları elde edilmesi
for regressor in regressors:
    scores = cross_val_score(regressor, X, y, cv=10)
    mean_score = scores.mean()
    std_score = scores.std()
    print(f"Tahminleyici: {regressor.__class__.__name__}")
    print(f"Ortalama Başarı: {mean_score}")
    print(f"Standart Sapma: {std_score}")
    print()

# Özellik önemlilik analizi
feature_importances = random_forest_reg.fit(X, y).feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
importance_df = importance_df.sort_values('Importance', ascending=False)
print("Özellik Önemlilikleri:")
print(importance_df)

# Özellik dönüşümü (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("PCA ile Dönüştürülmüş Veriler:")
print(X_pca)

# Veri normalizasyonu (Min-Max ölçeklendirme)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print("Min-Max Ölçeklendirilmiş Veriler:")
print(X_scaled)

# Tahminleyici performanslarını karşılaştırma (t-test)
scores_linear_reg = cross_val_score(linear_reg, X, y, cv=10)
scores_decision_tree_reg = cross_val_score(decision_tree_reg, X, y, cv=10)
scores_random_forest_reg = cross_val_score(random_forest_reg, X, y, cv=10)
scores_svr = cross_val_score(svr, X, y, cv=10)
scores_knn_reg = cross_val_score(knn_reg, X, y, cv=10)

mean_score_linear_reg = scores_linear_reg.mean()
mean_score_decision_tree_reg = scores_decision_tree_reg.mean()
mean_score_random_forest_reg = scores_random_forest_reg.mean()
mean_score_svr = scores_svr.mean()
mean_score_knn_reg = scores_knn_reg.mean()

_, p_value_linear_decision_tree = ttest_rel(scores_linear_reg, scores_decision_tree_reg)
_, p_value_linear_random_forest = ttest_rel(scores_linear_reg, scores_random_forest_reg)
_, p_value_linear_svr = ttest_rel(scores_linear_reg, scores_svr)
_, p_value_linear_knn = ttest_rel(scores_linear_reg, scores_knn_reg)

print("Tahminleyici Performansları:")
print(f"Linear Regression vs Decision Tree: p-value={p_value_linear_decision_tree}")
print(f"Linear Regression vs Random Forest: p-value={p_value_linear_random_forest}")
print(f"Linear Regression vs SVR: p-value={p_value_linear_svr}")
print(f"Linear Regression vs KNN: p-value={p_value_linear_knn}")

# Tahminleyici başarıları grafiği
plt.bar(['Linear Regression', 'Decision Tree', 'Random Forest', 'SVR', 'KNN'],
        [mean_score_linear_reg, mean_score_decision_tree_reg, mean_score_random_forest_reg, mean_score_svr, mean_score_knn_reg])
plt.xlabel('Tahminleyici')
plt.ylabel('Başarı')
plt.title('Tahminleyici Başarıları')
plt.show()

# Özellik önemlilikleri grafiği
plt.bar(importance_df['Feature'], importance_df['Importance'])
plt.xlabel('Özellik')
plt.ylabel('Önemlilik')
plt.title('Özellik Önemlilikleri')
plt.xticks(rotation=90)
plt.show()
