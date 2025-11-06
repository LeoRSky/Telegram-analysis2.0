from pathlib import Path

class TGModel:
    def __init__(self, path):
        self.path = Path(path)
        self.types = {"pictures":[".png", ".jpg", ".jpeg", ".gif"],
                      "videos":[".mp4", ".mov", ".avi", ".mkv"],
                      "audio":[".mp3", ".wav", ".aiff"],
                      "docs":[".docs", ".docx", ".txt", ".pdf", ".ppt", ".pptx", ".rar", ".zip"]}

    def Analysis(self):
        files = {l:[] for l in self.types}

        for element in self.path.iterdir():
            if element.is_file():
                for key, value in self.types.items():
                    if element.suffix.lower() in value:
                        files[key].append(element.name)

        return files