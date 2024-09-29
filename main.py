import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

## Load de data
melbourne_file_path = './input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

# Limpieza de data
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# Cargar pesos del modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

print(type(X_test))

# convert dataframe to dictionary

X_test_dict = X_test.to_dict(orient='records')

print(X_test_dict[0])



# grid search



# regressor_args = {'bootstrap': True, 'ccp_alpha': 0.0, 'criterion': 'squared_error', 'max_depth': None, 'max_features': 'sqrt', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'monotonic_cst': None, 'n_estimators': 100, 'n_jobs': None, 'oob_score': False, 'random_state': None, 'verbose': 0, 'warm_start': False}
# new_pipeline = Pipeline([
#     ('scaler', StandardScaler()),  # Paso de preprocesamiento
#     ('regr', RandomForestRegressor(**regressor_args))  # Usar los mejores parámetros
# ])

# new_pipeline.fit(X_train, y_train)

# # Test
# y_pred = new_pipeline.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print("Error cuadrático medio en el conjunto de prueba:", mse)

# joblib.dump(new_pipeline, 'model.joblib')
# print("Modelo Guardado")