from onnx_tf.backend import prepare
import onnx

onnx_model_path = 'D:\programs\AI\Deep learning\PyTorch-ONNX-TFLite-master\PyTorch-ONNX-TFLite-master\conversion\model.onnx'
tf_model_path = 'D:\programs\AI\Deep learning\PyTorch-ONNX-TFLite-master\PyTorch-ONNX-TFLite-master\conversion\model_tf'

onnx_model = onnx.load(onnx_model_path)
tf_rep = prepare(onnx_model)
tf_rep.export_graph(tf_model_path)