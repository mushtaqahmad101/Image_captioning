<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Captioning with BLIP</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #333;
        }
        code {
            background: #eee;
            padding: 5px;
            border-radius: 5px;
            font-family: monospace;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Image Captioning with BLIP</h1>
        <p>This project uses the <strong>BLIP model</strong> to generate captions for images. It is deployed using <strong>Gradio</strong> for an interactive web-based interface.</p>
        
        <h2>📥 Installation</h2>
        <p>Follow these steps to set up and run the project:</p>
        <pre><code>
git clone https://github.com/mushtaqahmad101/Image_captioning.git
cd Image_captioning
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
        </code></pre>
        
        <h2>🚀 Usage</h2>
        <p>Run the application with:</p>
        <pre><code>python gradio_app.py</code></pre>
        <p>This will launch a web-based interface where you can upload images and receive AI-generated captions.</p>
        
        <h2>🔧 Project Structure</h2>
        <pre><code>
.
├── image_caption.py      # Contains the BLIP model logic
├── gradio_app.py         # Runs the Gradio interface
├── requirements.txt      # Required dependencies
├── README.html           # Project documentation
        </code></pre>
        
        <h2>📝 How It Works</h2>
        <ol>
            <li>The project uses the <strong>BLIP model</strong> from Salesforce.</li>
            <li>A user uploads an image via the <strong>Gradio</strong> interface.</li>
            <li>The image is processed and converted into a caption using the BLIP model.</li>
            <li>The generated caption is displayed to the user.</li>
        </ol>

        <h2>📸 Example</h2>
        <p>After running the app, upload an image, and you will receive a caption like:</p>
        <pre><code>"A beautiful sunset over the mountains"</code></pre>
        
        <h2>📜 License</h2>
        <p>This project is licensed under the MIT License.</p>
    </div>
</body>
</html>
