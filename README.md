# Split Text into Sentences using DeepL's Private API

This Python code snippet demonstrates how to split a given raw text into sentences using DeepL's private API. It utilizes reverse engineering techniques to access DeepL's advanced natural language processing (NLP) features.

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/devtonic-net/NLPSplitSentencesDeepLAPI.git

2. Navigate to the project directory:

    ```bash
    cd NLPSplitSentencesDeepLAPI

3. Create a new virtual environment:

    ```bash
    python3 -m venv venv

4. Activate the virtual environment:

    For Windows:

    ```bash
    venv\Scripts\activate

    For Unix or Linux:

    ```bash
    source venv/bin/activate

## Usage

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

2. Create a text file called `my_text.txt`. This file should contain the text you need to split into sentences.
3. Import the necessary modules in your Python script:

    ```python3
    import requests
    import json

4. In `main.py`, Call the `split_sentences()` function, passing the raw text as the argument:

    ```python3
    text = get_text("my_text.txt")
    sentences = split_sentences(text)

    for index, sentence in enumerate(sentences, start=1):
        print(f"{index}. {sentence}")

This will split the raw text into sentences using DeepL's private API and print them with their respective indices.
