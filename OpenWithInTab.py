import sublime, sublime_plugin
import os.path
import subprocess
import os

class CopyFilePathCommand(sublime_plugin.TextCommand):
    def run(self, *args, **kwargs):
        os.system('echo|set /p=%s|clip' % text.strip())
class OpenWithNotepadPlusCommand(sublime_plugin.TextCommand):
    def run (self, edit, args=None, index=-1, group=-1, **kwargs):
        execute(self, 'notepadplus_path')

class OpenWithVimCommand(sublime_plugin.TextCommand):
    def run(self, edit, args=None, index=-1, group=-1, **kwargs):
        execute(self, 'vim_path')

def execute(self, exe_setting_name):
    settings = sublime.load_settings('OpenWithInTab.sublime-settings')
    exepath = settings.get(exe_setting_name, None)
    if exepath is None: 
        print("Missing configuration: 'notepadplus_path'.")
        self.view.set_status("OpenWithInTab", "Missing configuration: 'notepadplus_path'.")
        return
    if not os.path.exists(exepath): 
        print("'%s' not exists." % exepath)
        self.view.set_status("OpenWithInTab", "'%s' not exists." % exepath)
        return
    filepath = self.view.file_name()
    if not filepath: 
        print("Get filepath of current view fail.")
        self.view.set_status("OpenWithInTab", "Get filepath of current view fail.")
        return
    subprocess.Popen([exepath, filepath])