import numpy as np
import PIL.Image
import torch

import bentoml

runner = bentoml.pytorch.get("mnist_model:latest").to_runner()
runner.init_local()

img = PIL.Image.open("samples/0.png")
np_img = np.array(img)
tensor_img = torch.from_numpy(np_img).float()
tensor_img = tensor_img.unsqueeze(0).unsqueeze(0)
tensor_img = torch.nn.functional.interpolate(tensor_img, size=28, mode='bicubic', align_corners=False)

result = runner.predict.run(tensor_img)  # => tensor(0)
print(result)