class TGView:
    def UserPath(self):
        return input("Введите путь для сохранения: ")

    def OutputResult(self, files, path):
        title="Результат анализа файлов"
        print(f"\n{title:^37}")

        for key, lst in files.items():
            print(f"{key.capitalize()}:{len(lst)} файлов")
        print(f"\nФайли сохранены в: {path}")