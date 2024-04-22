import flet as ft
from glob import glob
import os 
from pathlib import Path
from models.get_all_images import GetAllImages
from models.clip_model import ClipModel

class ImageSearchControl(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.model = None
        self.image_object = None
        self.all_image = None
        self.folder_path_input = None
        self.images = None

    def build(self):
        # Input field for folder path
        self.folder_path_input = ft.TextField(label="Enter Folder Path", expand=True)
        # Input field for image search
        self.search_input = ft.TextField(label="Enter Image you want to search for" , expand=True)
        # Display images
        self.images = ft.Row(expand=1, wrap=False, scroll="always")

        # Layout adjustment
        return ft.Column(
            width=800,
            controls=[
                ft.Row(
                    controls=[
                        self.folder_path_input,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.handle_add_folder),
                    ],
                ),
                ft.Row(
                    controls=[
                        self.search_input,
                        ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=self.handle_search),
                    ],
                ),
                ft.Row(
                    controls=[
                        self.images,
                    ],
                ),          
            ], 
        )

    def handle_add_folder(self, event):
        folder_path = self.folder_path_input.value
        print(folder_path)  
        if folder_path:
            self.image_object = GetAllImages(folder_path)
            self.all_image = self.image_object.get_images()
            self.model = ClipModel(self.all_image)
            self.update()

    def handle_search(self, event):
        search_term = self.search_input.value
        if search_term and self.model:
            search_results = self.model.search_image(search_term)
            print(search_results)
            self.update_images_display(images_to_display=search_results)
            self.update()

    def update_images_display(self, images_to_display=None):
        self.images.controls.clear()
        for i in images_to_display:
            self.images.controls.append(
                ft.Image(
                    src=i['path'],
                    width=300,             
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                )
            )
        self.update()

def main(page: ft.Page):
    page.title = "Images Search"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.add(ImageSearchControl())

ft.app(target=main)
