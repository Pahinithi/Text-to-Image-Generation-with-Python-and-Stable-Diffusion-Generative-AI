# Text-to-Image Generator


## Overview

The **Text-to-Image Generator** application allows users to generate AI-driven images based on text prompts. Utilizing FastAPI for the backend and the Stable Diffusion model for image generation, this project provides a user-friendly web interface for creating custom images. It also supports **negative prompts**, which allow users to specify elements they want to exclude from the generated image.

This project is perfect for exploring AI art generation and image synthesis, leveraging state-of-the-art machine learning models.

## Features

- **Text-to-Image Generation**: Create high-quality images from text prompts using Stable Diffusion.
- **Negative Prompt Support**: Specify elements to avoid in generated images.
- **FastAPI Integration**: Lightweight, efficient backend with FastAPI.
- **Bootstrap-based UI**: Simple, responsive interface for a seamless user experience.
- **Dynamic Image Rendering**: View generated images immediately after submission.

## Demo

You can try a live demo here: [Live Demo Link](https://drive.google.com/file/d/1J9ii61RDtmDEg7qt-e4YrV17q-oKq8EW/view?usp=sharing)  


### Screenshots

<img width="1728" alt="Screenshot 2024-09-07 at 01 34 17" src="https://github.com/user-attachments/assets/d5727197-6e52-4b16-91cb-6dc36740ba21">


<img width="1728" alt="Screenshot 2024-09-07 at 01 33 57" src="https://github.com/user-attachments/assets/ed3400a3-faa3-498a-a61a-944288833605">


## How It Works

1. **Enter a Prompt**: The user inputs a description of the image they want to generate (e.g., "A vibrant sunset over the city skyline").
2. **Optional Negative Prompt**: Specify any elements to avoid (e.g., "Avoid including water or cars").
3. **Generate Image**: The user clicks the **Generate Image** button, and an AI-generated image is displayed.
4. **Download/Save**: The generated image is saved on the server and can be accessed from the results.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Jinja2 templates, HTML5, CSS3, Bootstrap
- **AI Model**: Stable Diffusion (via Hugging Face’s Diffusers Library)
- **Deployment**: Uvicorn (FastAPI server)
- **Libraries**:
  - `torch`: For PyTorch models
  - `diffusers`: To handle the image generation process
  - `pillow`: For image manipulation and saving

## Installation

To run this project locally, follow these steps:

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- Git

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Pahinithi/Text-to-Image-Generation-with-Python-and-Stable-Diffusion-Generative-AI
   cd text-to-image-generator
   ```

2. **Set up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   uvicorn main:app --reload
   ```

   The app should now be running on [http://localhost:8000](http://localhost:8000).

### Directory Structure

```
text-to-image-generator/
│
├── static/
│   └── styles.css               # CSS for styling the application
├── templates/
│   └── index.html               # Main HTML page for the web interface
├── __pycache__/                 # Cache directory
├── generate.py                  # Logic for generating images using the AI model
├── main.py                      # FastAPI routes and application logic
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation (this file)
```

## Usage

1. **Access the Application**: Open your browser and navigate to `http://localhost:8000`.
2. **Input a Text Prompt**: In the input field, type the description of the image you'd like to generate.
3. **Negative Prompt (Optional)**: You can specify objects or elements to avoid in the image.
4. **Generate the Image**: Press **Generate Image** and wait for the result to be displayed.
5. **View/Save the Image**: The generated image will appear on the page, and you can download or use it as needed.

## Code Explanation

### `main.py`

- Sets up the FastAPI application and serves the HTML frontend.
- Handles POST requests for generating images, passing the user's prompt and optional negative prompt to the image generation logic.

### `generate.py`

- Contains the code for loading and running the Stable Diffusion model via Hugging Face’s Diffusers library.
- Generates an image based on the user's input and saves it to the `static` folder for display on the frontend.

### `index.html`

- The main user interface where users can input prompts and view the generated images.
- Styled using basic CSS with a responsive layout for better user experience.

## Example Prompts

1. **Positive Prompt**: "A vibrant sunset over the mountains."
2. **Negative Prompt**: "Avoid including clouds."
   - *Generated Image*: A scenic sunset with clear skies over mountainous terrain.

3. **Positive Prompt**: "A futuristic city skyline with flying cars."
4. **Negative Prompt**: "Avoid including water or boats."
   - *Generated Image*: A futuristic city without water elements.

## Future Improvements

- **Multilingual Support**: Add support for text prompts in multiple languages.
- **Cloud Deployment**: Deploy the app on cloud platforms like AWS or Heroku.
- **Image Quality Customization**: Allow users to choose resolution and aspect ratio.
- **Multiple Image Generation**: Add support for generating multiple images simultaneously.

## Issues and Troubleshooting

If you encounter any issues while running the project, here are a few things to check:

1. **Dependency Errors**: Make sure all dependencies in `requirements.txt` are installed.
2. **Model Loading Issues**: Ensure you have internet access to download the Stable Diffusion model on the first run.
3. **Image Not Displaying**: Check if the generated images are correctly saved in the `static/` folder.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Open a pull request

## License

This project is licensed under the MIT License. 

## Acknowledgments

- **Hugging Face Diffusers**: For the Stable Diffusion model and pipeline.
- **FastAPI**: For the simple and powerful web framework.
- **Bootstrap**: For easy and responsive frontend design.
- 
  
