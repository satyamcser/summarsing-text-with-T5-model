import os
import datasets
import transformers
from datasets import load_dataset
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import streamlit as st

# Function to load dataset
def load_xsum_dataset():
    # Specify an absolute path for the cache directory
    cache_dir = '/main/data/'

    # Create the cache directory if it doesn't exist
    os.makedirs(cache_dir, exist_ok=True)

    # Loading the dataset
    xsum_dataset = load_dataset(
        "xsum",
        version="1.2.0",
        cache_dir=cache_dir
    )

    return xsum_dataset

# Function to summarize text
def summarize_text(input_text):
    summarizer = pipeline(
        task="summarization",
        model="t5-small",
        min_length=40,
        max_length=60,
        truncation=True,
        model_kwargs={"cache_dir": '/main/'},
    )

    # Generate the summary
    summary = summarizer(input_text, max_length=300, min_length=60, do_sample=False)[0]['summary_text']

    bullet_points = summary.split(". ")

    return bullet_points, summary

# Main Streamlit app
def main():
    st.title("Text Summarization By LLMs | Satyam")

    # Load XSum dataset
    xsum_dataset = load_xsum_dataset()

    # Display a sample of the loaded dataset
    st.write(xsum_dataset["train"].select(range(10)).to_pandas())

    # User input
    input_text = st.text_area("Enter the text you want to summarize:", height=200)

    # Summarize button
    if st.button("Summarize"):
        if input_text:
            # Generate the summary
            bullet_points, summary = summarize_text(input_text)

            # Display the summary as bullet points
            st.subheader("Summary:")
            for point in bullet_points:
                st.write(f"- {point}")
            st.write("Full Summary:", summary)
        else:
            st.warning("Please enter text to summarize.")

if __name__ == "__main__":
    main()
