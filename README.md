# Image Search Application

This is an application that allows you to search for images using deep learning techniques.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-search.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    If you encounter an error regarding the installation of the `clip` package, you can download it from the following link:

    ```bash
    pip install git+https://github.com/openai/CLIP.git
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Enter the path to your folder, press the "add" button, and wait one minute. This is because our model will need some time to create the embedding for each image and save it in a vector database.

3. Use the search bar to enter your query and click the "Search" button.

4. The application will display a list of images related to your query.
