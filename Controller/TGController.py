from pathkib import path
from Model.TGModel import TGModel

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