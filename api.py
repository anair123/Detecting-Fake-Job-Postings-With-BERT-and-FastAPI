from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import transformers
from transformers import DistilBertTokenizer

app = FastAPI()

# Load the TensorFlow model and tokenizer
model_path = 'Model/model.h5'
loaded_model = tf.keras.models.load_model(model_path,
                                          custom_objects={"TFBertModel": transformers.TFBertModel})
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
max_length = 512

# set the api to take text input
class PredictionInput(BaseModel):
    text: str


# make classification based on given text
def predict_fraudulence(text: str):
    tokenized_sentence = tokenizer.encode_plus(
        text,
        truncation=True,
        padding='max_length',
        max_length=max_length,
        return_tensors='tf'
    )
    input_ids = tokenized_sentence['input_ids']
    attention_mask = tokenized_sentence['attention_mask']
    predictions = loaded_model.predict([input_ids, attention_mask])
    predicted_label = "Fraudulent" if predictions[0][0] > 0.5 else "Not Fraudulent"
    return predicted_label

# FastAPI endpoint
@app.post("/predict")
async def predict_text(input_data: PredictionInput):
    predicted_label = predict_fraudulence(input_data.text)
    return {"prediction": predicted_label}
