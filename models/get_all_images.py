import glob
from typing import List
import os

class GetAllImages:
    """
    Get all images from a given path
    :input: path: str
    :output: all_images: List[str]
    """
    def __init__(self, path: str) -> None:
        self.path = path
        self.all_images = []
        extensions = ['*.jpg', '*.png', '*.jpeg']
        for ext in extensions:
            self.all_images.extend(glob.glob(os.path.join(self.path, ext)))
        
    def get_images(self) -> List[str]:
        return self.all_images