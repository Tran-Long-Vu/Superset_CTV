### Formulate a simple linear regression with onnx.

## 1. version check
from onnx import __version__, IR_VERSION
from onnx.defs import onnx_opset_version
print(f"onnx.__version__={__version__!r}, opset={onnx_opset_version()}, IR_VERSION={IR_VERSION}")

#import libs
from onnx import TensorProto
from onnx.helper import (
    make_model, make_node, make_graph,
    make_tensor_value_info)
from onnx.checker import check_model
from onnx import load

# input 
X = make_tensor_value_info('X', TensorProto.FLOAT, [None, None])
A = make_tensor_value_info('A', TensorProto.FLOAT, [None, None])
B = make_tensor_value_info('B', TensorProto.FLOAT, [None, None])

# outputs
Y = make_tensor_value_info("Y",TensorProto.FLOAT, [None,None])

#nodes
node1 = make_node("MatMul" , ["X", "A"], ["XA"] )
node2 = make_node("Add", ["XA", "B"], ["Y"])

#graph
graph = make_graph([node1, node2],'lr', [X,A,B], [Y])

#model
onnx_model = make_model(graph)

#check model
check_model = make_model(graph)


## 2.1. serialization (save to dir)
with open("linear_regression.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())


# load from dir
with open("linear_regression.onnx", "rb") as f:
    onnx_model = load(f)

# display
#print(onnx_model)
print(" loaded above onnx from dir \n")


## 2.2 Protobuf when size > 2gb: Using numpy array
import numpy
from onnx.numpy_helper import from_array
print("serializing numpy to protobuf:")

#convert to numpy
numpy_tensor = numpy.array([0,1,4,5,3],dtype=numpy.float32)
print(type(numpy_tensor))

#convert to onnx.numpy
onnx_tensor = from_array(numpy_tensor)
print(type(onnx_tensor))

#serialize to str
serialized_tensor = onnx_tensor.SerializeToString()
print(type(serialized_tensor))

#save as protobuf
with open("saved_tensor.pb", "wb") as f:
    f.write(serialized_tensor)
print("saved serialized into protobuf \n")

# de serialize:
print("de serializing from protobuf file: \n")
from onnx import TensorProto
from onnx.numpy_helper import to_array

#open protobuf
with open("saved_tensor.pb", "rb") as f:
    serialized_tensor = f.read()
print(type(serialized_tensor))

# parse from string: de serialize
onnx_tensor = TensorProto()
onnx_tensor.ParseFromString(serialized_tensor)
print(type(onnx_tensor))

# convert to numpy array:
numpy_tensor = to_array(onnx_tensor)
print(numpy_tensor)

print("de serializing from protobuf file: complete \n")










