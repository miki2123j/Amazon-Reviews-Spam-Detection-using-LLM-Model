from transformers import BertForSequenceClassification, BertTokenizer
from flask import Flask, request, render_template
import torch

model = BertForSequenceClassification.from_pretrained("./model3")

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")


def predict_spam(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    _, preds = torch.max(outputs.logits, dim=1)
    return "Spam" if preds[0].item() == 1 else "Not Spam"


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        review = request.form["review"]
        prediction = predict_spam(review)
        return render_template("result.html", prediction=prediction)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
