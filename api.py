from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from transformers import DistilBertTokenizer

app = FastAPI()

# Load the TensorFlow model and tokenizer
model_path = 'Model/model.h5'
loaded_model = tf.keras.models.load_model(model_path)
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
max_length = 512
