import clip
import torch 
import numpy as np
import os
import glob
from pathlib import Path
from typing import List
from PIL import Image
import chromadb
from chromadb import Settings
class ClipModel:
    """
    This class is used to search images using CLIP model and store the image features in ChromaDB
    :input: images: List[str]
    :output: None
    """
    def __init__(self , images : List[str]) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)
        self.images = images
        self.image_features = []
        self.image_names = []
        self.chroma_client = chromadb.PersistentClient("image_search.db" , settings=Settings(allow_reset=True))
        self.chroma_client.reset()
        self.create_vector_database()
        self.add_image_to_database()

    def create_vector_database(self):
        self.image_collection = self.chroma_client.create_collection("image" , metadata={"hnsw:space": "cosine"})

    def add_image_to_database(self):
        ids_index = 0 # Initialize ids_index to 0
        for i in self.images:
            image = self.preprocess(Image.open(i)).unsqueeze(0).to(self.device)
            with torch.no_grad():
                image_features = self.model.encode_image(image).cpu().numpy().tolist()
            ids_index += 1
            self.image_collection.add(ids=str(ids_index), embeddings=image_features, metadatas={"path": i, "name": os.path.basename(i)})

    def search_image(self , search_text : str):
        text = clip.tokenize(search_text).to(self.device)
        with torch.no_grad():
            text_features = self.model.encode_text(text).cpu().numpy()

        search_result = self.image_collection.query(text_features.tolist(), n_results=2)
        return search_result['metadatas'][0]
