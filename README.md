# Text Summarization Using Large Language Models (LLMs) with Hugging Face and Streamlit by Satyam

## Check App: https://t5modelsummary.streamlit.app/

## Overview
This repository provides an implementation of a text summarization application using Large Language Models (LLMs) with Hugging Face and Streamlit. The code demonstrates how to leverage Hugging Face's pre-trained models, specifically the T5 model, for text summarization. The application is built using Streamlit, allowing users to input text and obtain summarized output.

## Requirements
Make sure you have the following dependencies installed:
```bash
pip install streamlit
pip install sacremoses==0.0.53
pip install datasets
pip install transformers
pip install torch torchvision torchaudio

## Dataset

The code uses the XSum dataset, which comprises a collection of BBC articles and summaries. The dataset is loaded using the Hugging Face datasets library.

## Running the Application

1. Clone the repository:

git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Execute the Streamlit application:

streamlit run test.py

3. Access the application in your web browser. Streamlit will provide a local URL (usually http://localhost:8501) where you can interact with the text summarization interface.

## Notes:

Ensure that you have the required packages and dependencies installed.

Adjust the cache directory paths in the code based on your system's file structure.

The application uses the T5-small model; you can experiment with other pre-trained models provided by Hugging Face.





