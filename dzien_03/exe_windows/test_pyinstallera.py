from nicegui import ui


# for Linux to work with native=True
import multiprocessing
multiprocessing.set_start_method("spawn", force=True)
###

ui.label('test pyinstallera!')
ui.run(native=True, show=False, reload=False, title="PyInstaller Test")