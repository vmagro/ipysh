from IPython.terminal.prompts import Prompts, Token
from IPython.core.getipython import get_ipython

import os
from pathlib import Path
from getpass import getuser
from socket import gethostname


# build a map of symlinks in ~ that we can "unresolve"
symlink_map = {}
home = Path.home()
for child in home.iterdir():
    if child.is_symlink():
        symlink_map[str(child.resolve())] = str(child)


class DefaultPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        cwd = os.getcwd()
        symlink_matches = [s for s in symlink_map.keys() if cwd.startswith(s)]
        if symlink_matches:
            prefix = max(symlink_matches, key=len)
            cwd = cwd.replace(prefix, symlink_map[prefix])
        cwd = cwd.replace(str(home), '~')
        exit_code = get_ipython().user_ns.get('_exit_code', 0)
        return [
            (Token.OutPromptNum, f'[{exit_code}] ' if exit_code else ''),
            (Token, getuser()),
            (Token, ' at '),
            (Token, gethostname()),
            (Token, ' in '),
            (Token.Keyword, cwd),
            (Token, '\n'),
            (Token.Prompt, '$ '),
        ]

    def out_prompt_tokens(self):
        return [
            (Token.OutPrompt, 'Out['),
            (Token.OutPromptNum, str(self.shell.execution_count)),
            (Token.OutPrompt, ']: '),
        ]
