# coding: utf-8

# pip install pillow pywinauto
# see: https://pywinauto.readthedocs.io/en/latest/
# Caution: Use 32 bit python for UFOCapture. Otherwise, this will kill UFOCapture process.
# This should be more extensively tested.
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError, ElementAmbiguousError

try:
    app = Application().connect(title_re='UFOCapture*')
    dlg = app.window(title_re='UFOCapture*')
    print('Detect LevEdit:', dlg['Detect LevEdit'].window_text())
    dlg.maximize() ; dlg.set_focus(); im = dlg.capture_as_image()
    im.save("screenshot_ufo_capture.png")
    del im
    del dlg
    del app
except ElementNotFoundError:
    print('UFOCapture window not found')
except ElementAmbiguousError:
    print('There are several UFOCapture windows')