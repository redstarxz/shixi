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
        elif (appname == "portrays"):
            MODELS=[
                "flux1-redux-dev.safetensors",
                "detection_Resnet50_Final.pth",
                "clip_l.safetensors",
                "landmark.onnx",
                "sigclip_vision_patch14_384.safetensors",
                "parsing_parsenet.pth",
                "models/buffalo_l",
                "flux1-fill-dev.safetensors",
                "codeformer.pth",
                "ae.safetensors",
                "t5xxl_fp8_e4m3fn.safetensors"
            ]
            for model in MODELS:
                kwargs["weights_downloader"].download_weights(
                    model
                )
        elif (appname == "hairfit"):
            MODELS=[
                "flux1-redux-dev.safetensors",
                "detection_Resnet50_Final.pth",
                "clip_l.safetensors",
                "landmark.onnx",
                "sigclip_vision_patch14_384.safetensors",
                "parsing_parsenet.pth",
                "models/buffalo_l",
                "flux1-fill-dev.safetensors",
                "codeformer.pth",
                "ae.safetensors",
                "t5xxl_fp8_e4m3fn.safetensors"
            ]
            for model in MODELS:
                kwargs["weights_downloader"].download_weights(
                    model
                )
