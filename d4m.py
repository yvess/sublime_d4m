import sublime_plugin
import sublime
import subprocess
import os
import sys
import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)


__version__ = '0.1.0'
__authors__ = ['"Yves Serrano" <y@yas.ch>']


def plugin_loaded():
    pass


class D4mNfsTouchListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        settings = view.settings()
        plugin_settings = sublime.load_settings('d4m.sublime-settings')
        extensions, paths = (
            settings.get(
                'file_extensions',
                plugin_settings.get('file_extensions', [])
            ),
            settings.get(
                'watch_paths',
                plugin_settings.get('watch_paths', [os.getenv("HOME")])
            ),
        )
        fname = view.file_name()
        if not self.is_valid_fname(fname, paths, extensions):
            return
        if self.has_d4m_screen():
            cmd = '''screen -S d4m -p 0 -X stuff "touch %s
"'''
            subprocess.check_call(cmd % fname, shell=True)

    def is_valid_fname(self, fname, paths, extensions):
        valid_path = False
        for path in paths:
            if fname.startswith(path):
                valid_path = True
                break
        valid_ext = True
        if extensions:
            valid_ext = fname.split(".")[-1] in extensions
        return all([valid_path, valid_ext])

    def has_d4m_screen(self):
        exit_code = subprocess.check_call('screen -ls|grep -q d4m', shell=True)
        return True if exit_code == 0 else False
