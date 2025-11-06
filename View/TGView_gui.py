import tkinter as tk
from Model.TGModel import TGModel
from Controller.TGController import TGController

class TGGui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Telegram Analyzer")
        self.window.geometry("450x350")
        self.window.resizable(False, False)

        # Поле для пути
        tk.Label(self.window, text="Путь к папке Telegram:").pack(pady=5)
        self.path_entry = tk.Entry(self.window, width=50)
        self.path_entry.pack()

        # Кнопки
        tk.Button(self.window, text="Анализировать", command=self.analyze).pack(pady=5)
        tk.Button(self.window, text="Показать результат", command=self.show_result).pack(pady=5)
        tk.Button(self.window, text="Сохранить всё", command=self.save_all).pack(pady=5)

        # Поле вывода
        self.output = tk.Text(self.window, width=55, height=12, state="disabled")
        self.output.pack(pady=10)

        self.controller = None
        self.files = None

    def analyze(self):
        path = self.path_entry.get().strip()
        if not path:
            self.show_text("Ошибка: введите путь к папке Telegram.\n")
            return

        model = TGModel(path)
        self.controller = TGController(model, None)
        self.files = self.controller.Add()
        self.show_text("Анализ завершён успешно.\n")

    def show_result(self):
        if not self.files:
            self.show_text("Сначала выполните анализ.\n")
            return

        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        for key, lst in self.files.items():
            self.output.insert(tk.END, f"{key.capitalize()}: {len(lst)} файлов\n")
        self.output.config(state="disabled")

    def save_all(self):
        if not self.files:
            self.show_text("Сначала выполните анализ.\n")
            return

        save_path = self.path_entry.get().strip()
        self.controller.ShowAll()
        self.show_text(f"Результаты сохранены в: {save_path}\n")

    def show_text(self, text):
        self.output.config(state="normal")
        self.output.insert(tk.END, text)
        self.output.config(state="disabled")

    def run(self):
        self.window.mainloop()