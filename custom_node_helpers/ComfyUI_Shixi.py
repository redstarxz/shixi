from custom_node_helper import CustomNodeHelper


class ComfyUI_Shixi(CustomNodeHelper):
    @staticmethod
    def app_prepare(**kwargs):
        appname = kwargs["appname"]
        if (appname == "weblend"):
            MODELS=[
                "models/antelopev2",
                "instantid-ip-adapter.bin",
                "segm/person_yolov8m-seg.pt",
                "landmark.onnx",
                "models/buffalo_l",
                "detection_Resnet50_Final.pth",
                "instantid-controlnet.safetensors",
                "bbox/hand_yolov8s.pt",
                "jibMixRealisticXL_v10Lightning46Step.safetensors",
                "add-detail-xl.safetensors",
                "bbox/face_yolov8m.pt",
                "sam_vit_l_0b3195.pth",
                "parsing_parsenet.pth",
                "codeformer.pth"
            ]
            for model in MODELS:
                kwargs["weights_downloader"].download_weights(
                    model
                )

