import os

import glob
import json
import requests

import numpy as np

from PIL import Image

print("GET REQUESTS ---------------------------------")
json_response = requests.get("http://localhost:8888/v1/models/street-detection/metadata")
print(json_response.text)

print("POST REQUESTS ---------------------------------")
img_pattern = os.path.join(os.getcwd(), "evaluation-images", "*")
for img_path in glob.glob(img_pattern):
    # load data
    img = np.array(Image.open(img_path))
    img = img / 255
    img = np.expand_dims(img, axis=0)
    # create request
    data = json.dumps({"instances": img.tolist()})
    headers = {"content-type": "application/json"}
    # send request
    json_response = requests.post('http://localhost:8888/v1/models/street-detection:predict',
                                  data=data,
                                  headers=headers)
    # print result
    predictions = json.loads(json_response.text)['predictions']
    print("{} was predicted as {}".format(img_path, np.argmax(predictions[0])))
