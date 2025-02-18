from custom_node_helper import CustomNodeHelper

class ComfyUI_RMBG2(CustomNodeHelper):

    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type("LayerMask: LoadBiRefNetModelV2"):
            if node.input("version") != "RMBG-2.0":
                return
            from weights_downloader import WeightsDownloader
            weights_downloader = WeightsDownloader()
            weights_downloader.download_if_not_exists(
                "model.safetensors",
                "https://huggingface.co/redstarxz/comfyw/resolve/main/RMBG2.tar",
                "ComfyUI/models/BiRefNet/RMBG2.0/",
            )

