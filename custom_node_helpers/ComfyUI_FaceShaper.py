from custom_node_helper import CustomNodeHelper

class ComfyUI_FaceShaper(CustomNodeHelper):

    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type("FaceShaperCropper"):
            from weights_downloader import WeightsDownloader
            weights_downloader = WeightsDownloader()
            weights_downloader.download_if_not_exists(
                "landmark_model.onnx",
                "https://huggingface.co/redstarxz/comfyw/resolve/main/landmark_model.onnx",
                "ComfyUI/models/liveportrait/",
            )

