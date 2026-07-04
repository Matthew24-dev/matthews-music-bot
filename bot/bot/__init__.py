import os
import importlib

PLUGIN_DIR = "bot/plugins"

LOADED_PLUGINS = []


def load_plugins():
    if not os.path.isdir(PLUGIN_DIR):
        print("Plugin directory not found.")
        return

    for file in os.listdir(PLUGIN_DIR):
        if file.endswith(".py") and not file.startswith("_"):
            module = f"bot.plugins.{file[:-3]}"
            try:
                importlib.import_module(module)
                LOADED_PLUGINS.append(file[:-3])
                print(f"✓ Loaded plugin: {file[:-3]}")
            except Exception as e:
                print(f"✗ Failed to load {file}: {e}")