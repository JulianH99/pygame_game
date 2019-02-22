from os import path, getcwd


class Path:

    paths = None

    @staticmethod
    def __cwd():
        return getcwd()

    @staticmethod
    def __paths():
        if Path.paths is None:
            cwd = Path.__cwd()
            Path.paths = {
                "assets": path.join(cwd, "assets"),
                "sprite_sheets": path.join(cwd, "assets", "sprites", "SpriteSheets"),
                "backgrounds": path.join(cwd, "assets", "sprites", "Backgrounds")
            }

        return Path.paths

    @staticmethod
    def path_to(folder: str, base_path: str):
        if folder is None or base_path is None:
            raise ValueError("Value of folder or filename cannot be None")
        return path.join(Path.__paths()[folder], base_path)
