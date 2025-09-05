!pip install tf2onnx


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import tf2onnx


# Load dataset
df = pd.read_csv("/content/squat_exercise_cleaned.csv")

# Drop unnecessary columns
df_cleaned = df.drop(columns=["Timestamp", "Subject_ID"])


# Encode labels
label_encoder = LabelEncoder()
squat_type_encoder = LabelEncoder()

df_cleaned['Label'] = label_encoder.fit_transform(df_cleaned['Label'])
df_cleaned['Squat_Type'] = squat_type_encoder.fit_transform(df_cleaned['Squat_Type'])


# Optional: Feedback map
squat_feedback_map = df[['Squat_Type', 'Feedback_Message']].drop_duplicates().set_index('Squat_Type')['Feedback_Message'].to_dict()
df_cleaned['Feedback_Message'] = df['Squat_Type'].map(squat_feedback_map)


# Feature and target split
X = df_cleaned.drop(columns=['Label', 'Squat_Type', 'Feedback_Message'])
y = df_cleaned['Label']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Time-aware split (80%-20%)
split_index = int(len(X_scaled) * 0.8)
X_train, X_test = X_scaled[:split_index], X_scaled[split_index:]
y_train, y_test = y[:split_index], y[split_index:]


# MLP model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

model.fit(X_train, y_train, validation_split=0.2, epochs=50, batch_size=16, callbacks=[early_stop], verbose=1)


# Predict and evaluate
y_pred = (model.predict(X_test) > 0.5).astype(int)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


loss, accuracy = model.evaluate(X_test, y_test)
print(f"\n Model Test Accuracy: {accuracy*100:.2f}%\n")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
labels = ['Incorrect', 'Correct']
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()


import tf2onnx
import tensorflow as tf

# إعداد input_signature
input_signature = [tf.TensorSpec([None, X_train.shape[1]], tf.float32, name="input")]

# لف الموديل داخل tf.function
@tf.function(input_signature=input_signature)
def model_func(x):
    return model(x)

# التحويل إلى ONNX
onnx_model, _ = tf2onnx.convert.from_function(
    model_func,
    input_signature=input_signature,
    opset=13,
    output_path="squat_mlp_model.onnx"
)

print("✅ ONNX model saved as 'squat_mlp_model.onnx'")



