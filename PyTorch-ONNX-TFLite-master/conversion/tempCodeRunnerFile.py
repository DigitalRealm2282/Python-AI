import tensorflow as tf

saved_model_dir = 'D:\programs\AI\Deep learning\PyTorch-ONNX-TFLite-master\PyTorch-ONNX-TFLite-master\conversion\model_tf'
tflite_model_path = 'D:\programs\AI\Deep learning\PyTorch-ONNX-TFLite-master\PyTorch-ONNX-TFLite-master\conversion\model.tflite'

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Save the model
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)