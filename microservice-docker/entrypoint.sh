rm -rf street-situation-detection || true

# get production model
git clone https://github.com/steven-mi/street-detection.git
pytest street-detection

mkdir -p /production-model/1
cp -r /street-detection/street_detection/model/street-detection-network/* /production-model/1

tensorflow_model_server --model_base_path="/production-model" \
                        --model_name="street-detection" \
                        --rest_api_port="${REST_PORT}" \
                        --version=false