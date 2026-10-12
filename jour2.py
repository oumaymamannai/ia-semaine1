from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. Données : X = mesures des fleurs, y = espèce (0, 1 ou 2)
X, y = load_iris(return_X_y=True)

# 2. On met 20 % des données de côté pour le test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 3. ENTRAÎNEMENT : le modèle apprend sur les données d'entraînement
model = KNeighborsClassifier(n_neighbors=100)
model.fit(X_train, y_train)

# 4. INFÉRENCE : prédiction sur une fleur jamais vue
print("Prédiction :", model.predict(X_test[:1]))
print("Vraie espèce :", y_test[:1])

# 5. ÉVALUATION : proportion de bonnes réponses sur tout le test
print("Score :", model.score(X_test, y_test))

#n_neighbors=100,et observe la chute du score puisque il voit trop de voisins 100 voisins et donc il se trompe plus souvent. 
#test_size=0.5	Moins de données pour apprendre : le score peut baisser
#si je gardes random_state=42, il choisit toujours les mêmes fleurs pour le train et le test a consition que les autres donnes de test split soient les memes et si je change 5 ou 10, il choisit d'autres
# fleurs pour le train et le test, donc le score peut changer et si je garde le meme nbre le decoupage ne se fait pas forcement avec les memes fleurs 