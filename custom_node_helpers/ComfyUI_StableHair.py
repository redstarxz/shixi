from custom_node_helper import CustomNodeHelper

MODELS = [
    "hair_encoder_model.bin",
    "hair_adapter_model.bin",
    "hair_controlnet_model.bin",
    "hair_bald_model.bin",
]

class  ComfyUI_StableHair(CustomNodeHelper):
    @staticmethod
    def models():
        return MODELS

    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type("LoadStableHairRemoverModel"):
            weights_to_download.extend(MODELS)

    @staticmethod
    def weights_map(base_url):
        return {
            model: {
                "url": f"{base_url}/StableHair/{model}.tar",
                "dest": "ComfyUI/models/diffusers/StableHair",
            }
            for model in MODELS
        }
