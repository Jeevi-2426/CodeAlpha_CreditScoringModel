import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
df = pd.read_csv("dataset/german_credit_data.csv")

# Remove unnecessary column
df.drop("Unnamed: 0", axis=1, inplace=True)

# Fill missing values
df["Saving accounts"] = df["Saving accounts"].fillna("Unknown")
df["Checking account"] = df["Checking account"].fillna("Unknown")

# Create Credit Risk Target
df["Risk"] = np.where(
    (df["Credit amount"] > 5000) &
    (df["Duration"] > 24),
    1,
    0
)

# Encode text columns
le = LabelEncoder()

for col in df.select_dtypes(include=['object']).columns:
    df[col] = le.fit_transform(df[col])

# Features and Target
X = df.drop("Risk", axis=1)
y = df["Risk"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

# Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
import matplotlib.pyplot as plt
import seaborn as sns

# Confusion Matrix Visualization
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()
import matplotlib.pyplot as plt
import seaborn as sns

# Confusion Matrix Graph
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# Feature Importance Graph
feature_importance = model.feature_importances_

plt.figure(figsize=(10,5))
plt.bar(X.columns, feature_importance)

plt.xticks(rotation=45)
plt.title("Feature Importance")

plt.tight_layout()
plt.show()