from nicegui import ui

# for Linux to work with native=True
import multiprocessing
multiprocessing.set_start_method("spawn", force=True)
###

ui.label('Hello NiceGUI!')
ui.run(native=True)