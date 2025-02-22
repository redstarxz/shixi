from custom_node_helper import CustomNodeHelper

MODELS = [
    "landmark.onnx",
    "models/buffalo_l",
]
class ComfyUI_FaceShaper(CustomNodeHelper):

    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type("FaceShaperCropper"):
            weights_to_download.extend(MODELS)


