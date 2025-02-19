from custom_node_helper import CustomNodeHelper

MODELS = [
    "groundingdino_swint_ogc.pth",
]


class ComfyUI_SegAnyV2(CustomNodeHelper):
    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type_in(["LayerMask: SegmentAnythingUltra V2"]):
            weights_to_download.extend(MODELS)
