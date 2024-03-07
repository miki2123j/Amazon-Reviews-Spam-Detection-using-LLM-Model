# Amazon-Reviews-Spam-Detection-using-LLM-Model
Description: A spam detection system for Amazon product reviews by leveraging a BERT-based pre-trained language model. The project involved three key components:

Model Architecture:
fine-tuned a bert-base-multilingual-uncased model specifically for sentiment analysis on product reviews.
Backend Implementation:
Built the backend using Flask, a lightweight Python web framework.
The Flask app serves as the interface for handling incoming review texts and forwarding them to the LLM model for sentiment analysis.
Frontend Design:
For the user interface, utilized HTML and CSS to create an intuitive and user-friendly web page.
Users can input review text, and the system provides an instant sentiment prediction based on the trained model.
Key Achievements:
Successfully fine-tuned the LLM model on an Amazon US Customer Reviews Dataset.
Achieved an accuracy of 80% on the evaluation set.
Implemented a user-friendly web interface for real-time sentiment analysis.

Limitations:
The model’s performance is optimized for Amazon reviews and products. It may not generalize well to other domains.

Dataset source:
https://www.kaggle.com/datasets/naveedhn/amazon-product-review-spam-and-non-spam
