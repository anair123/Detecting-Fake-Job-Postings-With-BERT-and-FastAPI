import transformers
from transformers import DistilBertTokenizer
import transformers
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model
import warnings

warnings.filterwarnings(action='ignore')

model_path = 'Model/model.h5'

# Load the model from the downloaded temporary file
loaded_model = tf.keras.models.load_model(model_path,  
                                          custom_objects={"TFBertModel": transformers.TFBertModel})


# Load the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

max_length=512

input_sentence = """
Scammers use instant messaging services, like Telegram or WhatsApp, to communicate and conduct fake job interviewers with job seekers. Although convenient, it is rare to actually secure a job or conduct a job interview with a legitimate company through a social media or chat platform. If you are approached through chat, be sure to request that they give you a call, and do your research before interviewing to see if the results yield any red flags.

"""

def predict(text):
    tokenized_sentence = tokenizer.encode_plus(text, 
                                                truncation=True, 
                                                padding='max_length', 
                                                max_length=max_length, 
                                                return_tensors='tf')

    # Extract input IDs and attention masks from the tokenized sentence
    input_ids = tokenized_sentence['input_ids']
    attention_mask = tokenized_sentence['attention_mask']

    # Make predictions
    predictions = loaded_model.predict([input_ids, attention_mask])

    # Assuming a binary classification task with sigmoid activation
    predicted_label = "Fraudulent" if predictions[0][0] > 0.5 else "Not Fraudulent"  # Adjust threshold as needed

    print(predicted_label)
    return predicted_label

predict(text=input_sentence)