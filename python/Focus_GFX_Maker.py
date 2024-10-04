#Original code By Wendell08, modified for a Focus GFX implementer by Krumtum

import tkinter as tk
from tkinter import filedialog, Text
import shutil
import os
import re
import sys

get_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

print(get_path)

focus_gfx = os.path.join(get_path, r"interface\goals.gfx")
focus_shine = os.path.join(get_path, r"interface\goals_shine.gfx")

class App(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.select_image_file = ""
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.run_script = tk.Button(self)
		self.run_script["text"] = "Run Program"
		self.run_script["command"] = self.run_app
		self.run_script.pack(side="top")

		self.select_image_button = tk.Button(self)
		self.select_image_button["text"] = "Select Focus Image\n(.dds)"
		self.select_image_button["command"] = self.select_image_path
		self.select_image_button.pack(side="top")

		self.image_image = tk.Label(self)
		self.image_image["text"] = f"\nCurrent Image File:\n{self.select_image_file}\n"
		self.image_image["wraplength"] = 260
		self.image_image.pack(side="top")

	def select_image_path(self):
		self.select_image_file = filedialog.askopenfilename(initialdir=os.path.join(get_path,r"gfx\interface\goals"))
		self.image_image["text"] = f"\nCurrent Image File:\n{os.path.split(self.select_image_file)[1]}\n"

	def run_app(self):
		_, focus_image = os.path.split(self.select_image_file)
		focus_name,a = focus_image.split(".")

		try:
			shutil.copy(self.select_image_file, os.path.join(get_path, r"gfx\interface\goals"))
		except:
			print("Image file already in Folder")
			pass
		#--------------------

		with open(focus_gfx) as inp:
			line_list = inp.readlines()
            # insert at second last line of file
			line_list.insert(len(line_list)-1, f'''	spriteType = {{
		name = "{focus_name}"
		texturefile = "gfx/interface/goals/{focus_image}"
	}}

''')

			with open(focus_gfx, "w") as out:
				for line_to_write in line_list:
					out.write(line_to_write)


		#--------------------

		with open(focus_shine) as inp:
			line_list = inp.readlines()
            # insert at second last line of file
			line_list.insert(len(line_list)-1, f'''	SpriteType = {{
		name = "{focus_name}_shine"
		texturefile = "gfx/interface/goals/{focus_image}"
		effectFile = "gfx/FX/buttonstate.lua"
		animation = {{
			animationmaskfile = "gfx/interface/goals/{focus_image}"
			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
			animationrotation = -90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = {{ x = 0.0 y = 0.0 }}
			animationtexturescale = {{ x = 1.0 y = 1.0 }}
		}}
		animation = {{
			animationmaskfile = "gfx/interface/goals/{focus_image}"
			animationtexturefile = "gfx/interface/goals/shine_overlay.tga"
			animationrotation = 90.0
			animationlooping = no
			animationtime = 0.75
			animationdelay = 0
			animationblendmode = "add"
			animationtype = "scrolling"
			animationrotationoffset = {{ x = 0.0 y = 0.0 }}
			animationtexturescale = {{ x = 1.0 y = 1.0 }}
		}}
		legacy_lazy_load = no
	}}

''')

			with open(focus_shine, "w") as out:
				for line_to_write in line_list:
					out.write(line_to_write)

		#--------------------
		print("Finished %s GFX Implementation", focus_name)


root = tk.Tk()
root.geometry("300x640")
root.title("Focus GFX Implementer")
app = App(master=root)
app.mainloop()
