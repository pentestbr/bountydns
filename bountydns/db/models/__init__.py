from os import walk
from os.path import join
from importlib import import_module
from bountydns.core.utils import db_dir, snake_to_title

models = []

models_dir = db_dir("models")
for directory_name, sub_directories, files in walk(models_dir):
    for f in sorted(files):
        if not f.startswith("__") and not f.startswith("base"):
            base_name = f.split(".")[0]
            class_name = snake_to_title(base_name)
            module_path = f"bountydns.db.models.{base_name}"
            module = import_module(module_path, class_name)
            model = getattr(module, class_name)
            if model not in models:
                models.append(model)
