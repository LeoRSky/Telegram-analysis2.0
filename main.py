# from Model.TGModel import  TGModel
# from View.TGView import TGView
# from Controller.TGController import TGController
#
# class ConsoleView:
#     def __init__(self):
#         path = input("Введите путь к папке Telegram: ")
#         self.model = TGModel(path)
#         self.view = TGView()
#         self.controller = TGController(self.model, self.view)
#
#     def add(self):
#         self.controller.Add()
#
#     def showAll(self):
#         self.controller.ShowAll()
#
#     def search(self):
#         self.controller.Search()
#
#
# console = ConsoleView()
# console.add()
# console.showAll()
# console.search()

from View.TGView_gui import TGGui

gui = TGGui()
gui.run()