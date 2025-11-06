class TGView:
    def UserPath(self):
        return input("Введите путь для сохранения: ")

    def OutputResult(self, files, path):
        print(f"\n{"Результат анализа файлов": ^37}")

        for key, lst in files.items():
            print(f"{key.capitalize()}:{len(lst)} файлов")
        print(f"\nФайли сохранены в: {path}")