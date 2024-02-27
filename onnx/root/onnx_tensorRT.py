#0. Setup: code for tensorRT optimization

# install script
# pip install --upgrade --index-url https://pypi.ngc.nvidia.com nvidia-tensorrt
#

# optional script
# pip install pycuda onnx scikit-image
#


# torchvision: 
# pip install torchvision

#1. Model format: onnx.

# backbone link:
# wget https://s3.amazonaws.com/download.onnx/models/opset_8/resnet50.tar.gz -O resnet50.tar.gz

# un-tar:
# tar xzf resnet50.tar.gz

# or:
# wget https://github.com/onnx/models/blob/main/validated/vision/classification/resnet/model/resnet50-v1-7.onnx

#2. Batch size: 
# default is 32. 
import numpy as np
BATCH_SIZE=32

#3. Precision:
# TensorRT supports TF32, FP32, FP16, and INT8 precisions.
# use FP32.

PRECISION = np.float32

dummy_input_batch = np.zeros((BATCH_SIZE, 224, 224, 3), dtype=PRECISION)

#4. Tensor RT path: ONNX conversion path
# convert models from ONNX to a TensorRT engine.
# use trtexec - a command line tool 

# trtexec --onnx=resnet50/model.onnx --saveEngine=resnet_engine_intro.trt  --explicitBatch

# trtexec notes:
# model path:  --onnx=resnet50/model.onnx  
# save engine: --saveEngine=resnet_engine_intro.trt
# fixed batch size: --explicitBatch

#5. Runtime:

# 2 types: a standalone runtime which has C++ and Python bindings
#     and: a native integration into TensorFlow.

# use: a simplified wrapper (ONNXClassifierWrapper) which calls the standalone runtime.  

# from onnx_helper import ONNXClassifierWrapper
# trt_model = ONNXClassifierWrapper("resnet_engine_intro.trt", [BATCH_SIZE, 1000], target_dtype = PREC

# Warm up: dummy batch
# trt_model.predict(dummy_input_batch)[0][:10] # softmax probability predictions for the first 10 cla

# use %%timeit: measure performance
# %%timeit
# trt_model.predict(dummy_input_batch)[0][:10]



