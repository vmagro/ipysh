import IPython
from traitlets.config.loader import Config

from pathlib import Path

from ipysh.prompt import DefaultPrompt


def ipysh():
    cfg = Config()

    cfg.TerminalInteractiveShell.confirm_exit = False

    cfg.TerminalInteractiveShell.prompts_class = DefaultPrompt

    cfg.TerminalInteractiveShell.ipython_dir = str(Path.home() / '.ipysh')
    cfg.BaseIPythonApplication.ipython_dir = str(Path.home() / '.ipysh')
    cfg.BaseIPythonApplication.copy_config_files = True
    
    cfg.InteractiveShell.show_rewritten_input = False
    cfg.InteractiveShell.autocall = 1
    cfg.InteractiveShellApp.exec_lines = [
        '%rehashx',
    ]

    IPython.start_ipython(config=cfg)
