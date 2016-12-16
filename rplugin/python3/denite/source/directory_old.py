# -*- coding: utf-8 -*-
# FILE: directory_old.py
# AUTHOR: pocari <caffelattenonsugar at gmail.com>

from .base import Base
from os import path


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'directory_old'
        self.kind = 'directory'

    def on_init(self, context):
        self.vim.command('wviminfo | rviminfo!')

    def gather_candidates(self, context):
        recent_directories = [path.dirname(x)
                              for x in self.vim.eval('v:oldfiles')
                              if path.isdir(path.dirname(x))]
        seen = set()
        seen_add = seen.add
        return [{'word': x, 'action__path': x}
                for x in recent_directories
                if x not in seen and not seen_add(x)]
