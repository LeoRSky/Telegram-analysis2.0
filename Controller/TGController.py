from pathkib import path
from Model.TGModel import TGModel
from Views.TGView import TGView

class TGController:
    def __init__(self,model, view):
        self.model = model
        self.view = view
        self.files = {}

    def Add(self):
        print(f'\nАнализ папки Telegram')
        self.files = self.model.Analysis()
        print('Анализ завершен.')
        return self.files

    def ShowAll(self):
        if not self.files:
            print('Сначала Add')
            return

        path = self.view.UserPath()
        Path(path).mkdir(parents=True, exist_ok=True)

        for key, lst in self.files.items():
            with open(Path(path) / f'{key}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(lst))

        self.view.OutputResult(self.files, path)
        return path