from custom_node_helper import CustomNodeHelper

MODELS = [
    "detection_Resnet50_Final.pth",
    "parsing_parsenet.pth",
]


class ComfyUI_FaceRestore(CustomNodeHelper):
    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type_in(["ReActorRestoreFace"]):
            weights_to_download.extend(MODELS)
