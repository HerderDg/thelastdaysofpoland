# Turbocoder 2137 for creating superevents in Hearts of Iron IV mod "Pride and Fall" by Herder

import tkinter as tk
from tkinter import filedialog, messagebox
import os


MOD_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

MUSIC_ASSET = os.path.join(MOD_ROOT, "music", "SUPEREVENTS", "super_music.asset")
MUSIC_TXT = os.path.join(MOD_ROOT, "music", "SUPEREVENTS", "super_music.txt")
SUPEREVENT_GFX = os.path.join(MOD_ROOT, "interface", "PaF_superevents.gfx")
SUPEREVENT_GUI = os.path.join(MOD_ROOT, "interface", "PaF_superevents.gui")
SCRIPTED_GUI = os.path.join(MOD_ROOT, "common", "scripted_guis", "PaF_super_events.txt")

REQUIRED_FILES = [MUSIC_ASSET, MUSIC_TXT, SUPEREVENT_GFX, SUPEREVENT_GUI, SCRIPTED_GUI]


def extract_id(path):
    return os.path.splitext(os.path.basename(path))[0] if path else ""

def file_contains(path, text):
    if not os.path.exists(path): return False
    with open(path, "r", encoding="utf-8") as f:
        return text in f.read()

def insert_into_block(path, block_keyword, content, marker, indent="    "):
    if not os.path.exists(path) or file_contains(path, marker): return
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_idx = -1
    for i, line in enumerate(lines):
        if block_keyword in line:
            start_idx = i
            break
    if start_idx == -1: return

    brace_count = 0
    end_idx = -1
    for i in range(start_idx, len(lines)):
        brace_count += lines[i].count('{')
        brace_count -= lines[i].count('}')
        if brace_count == 0:
            end_idx = i
            break
    
    if end_idx != -1:
        lines.insert(end_idx, f"{indent}{content}\n")
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)

def insert_in_effects_section(path, keyword, content, marker, forbidden_content=None):
    if not os.path.exists(path) or file_contains(path, marker): return
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_effects_block = False
    inserted = False
    
    for i, line in enumerate(lines):
        if "effects = {" in line:
            in_effects_block = True
            continue
        
        if in_effects_block and keyword in line:
            if forbidden_content and forbidden_content in line:
                continue
            
            lines.insert(i, f"        {content}\n")
            inserted = True
            break

    if inserted:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)


def insert_before_button(path, content, marker):
    if not os.path.exists(path) or file_contains(path, marker): return
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    inserted = False
    for i, line in enumerate(lines):
        if "buttonType =" in line:
            lines.insert(i, f"        {content}\n")
            inserted = True
            break

    if inserted:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)


class SupereventApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=10, pady=10)
        self.music_file = ""
        self.image_file = ""
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="PaF Superevent Turbocoder 2137", font=("Arial", 11, "bold")).pack()
        tk.Button(self, text="1. Wybierz plik dźwiękowy .ogg", command=self.select_music).pack(fill="x", pady=2)
        self.music_label = tk.Label(self, text="---")
        self.music_label.pack()
        tk.Button(self, text="2. Wybierz plik graficzny .dds", command=self.select_image).pack(fill="x", pady=2)
        self.image_label = tk.Label(self, text="---")
        self.image_label.pack()
        tk.Button(self, text="ZAPIERDALAJ", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=self.generate).pack(fill="x", pady=10)

    def select_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("OGG", "*.ogg")])
        self.music_label.config(text=os.path.basename(self.music_file) if self.music_file else "---")

    def select_image(self):
        self.image_file = filedialog.askopenfilename(filetypes=[("DDS", "*.dds")])
        self.image_label.config(text=os.path.basename(self.image_file) if self.image_file else "---")

    def generate(self):
        if not self.music_file or not self.image_file:
            messagebox.showerror("Błąd", "Wybierz oba pliki!")
            return
        
        base_id = extract_id(self.music_file)
        img = os.path.basename(self.image_file)

        insert_into_block(SUPEREVENT_GFX, "spriteTypes = {", 
                          f'spriteType = {{ name = "GFX_{base_id}" texturefile = "gfx/superevent/{img}" legacy_lazy_load = no }}', 
                          f'GFX_{base_id}')

        gui_content = f'iconType = {{ name = "{base_id}_image" spriteType = "GFX_{base_id}" position = {{ x = 0 y = 0 }} alwaystransparent = yes }}'
        insert_before_button(SUPEREVENT_GUI, gui_content, f'name = "{base_id}_image"')

        insert_in_effects_section(SCRIPTED_GUI, "has_global_flag", f"has_global_flag = {base_id}_visible", f"has_global_flag = {base_id}_visible", forbidden_content="Super_Event_Visible")
        insert_in_effects_section(SCRIPTED_GUI, "clr_global_flag", f"clr_global_flag = {base_id}_visible", f"clr_global_flag = {base_id}_visible", forbidden_content="Super_Event_Visible")

        trig_block = f'{base_id}_image_visible = {{ has_global_flag = {base_id}_visible }}'
        insert_into_block(SCRIPTED_GUI, "triggers = {", trig_block, f'{base_id}_image_visible', indent="        ")

        if not file_contains(MUSIC_ASSET, f'name = "{base_id}"'):
            with open(MUSIC_ASSET, "a", encoding="utf-8") as f:
                f.write(f'\nmusic = {{ name = "{base_id}" file = "{base_id}.ogg" volume = 1 }}')

        if not file_contains(MUSIC_TXT, f'song = "{base_id}"'):
            with open(MUSIC_TXT, "a", encoding="utf-8") as f:
                f.write(f'\nmusic = {{ song = "{base_id}" chance = {{ base = -1000 }} }}')
        
        messagebox.showinfo("Sukces", f"Superevent wkodowany, jeszcze tylko wywołaj go w kodzie, ID: {base_id}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Turbocoder 2137")
    root.geometry("400x350")
    app = SupereventApp(root)
    root.mainloop()