from custom_node_helper import CustomNodeHelper

class ComfyUI_PMRF(CustomNodeHelper):

    @staticmethod
    def add_weights(weights_to_download, node):
        if node.is_type("PMRF"):
            from weights_downloader import WeightsDownloader
            weights_downloader = WeightsDownloader()
            weights_downloader.download_if_not_exists(
                "model.safetensors",
                "https://huggingface.co/redstarxz/comfyw/resolve/main/PMRF.tar",
                "ComfyUI/models/pmrf/",
            )

