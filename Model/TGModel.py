from pathlib import Path

class TGModel:
    def __init__(self, path):
        self.path = Path(path)
        self.types = {"pictures":[".png", ".jpg", ".jpeg", ".gif"],
                      "videos":[".mp4", ".mov", ".avi", ".mkv"],
                      "audio":[".mp3", ".wav", ".aiff"],
                      "docs":[".docs", ".docx", ".txt", ".pdf", ".ppt", ".pptx", ".rar", ".zip"]}


