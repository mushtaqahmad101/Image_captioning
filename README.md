
    <title>Flask Image Captioning - README</title>
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
        <h1>Flask Image Captioning</h1>
        <p>This project provides an image captioning system using the BLIP model, deployed via Gradio.</p>
        
        <h2>Installation</h2>
        <p>Follow these steps to set up the project on your local machine:</p>
        <pre><code>git clone https://github.com/mushtaqahmad101/Image_captioning.git
cd Image_captioning
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt</code></pre>
        
        <h2>Usage</h2>
        <p>Run the Gradio app with:</p>
        <pre><code>python gradio_app.py</code></pre>
        <p>This will launch a web-based interface where you can upload images and receive captions.</p>
        
        <h2>Project Structure</h2>
        <pre><code>.<br>
├── captioning.py     <br>  # Contains the BLIP image captioning logic
├── gradio_app.py       <br># Launches the Gradio interface
├── requirements.txt   <br> # Required dependencies
├── README.html         <br># Project documentation</code></pre>
        
        <h2>License</h2>
        <p>MIT License</p>
    </div>
</body>
</html>
