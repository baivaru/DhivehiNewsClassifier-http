
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from dhivehi_nlp.stemmer import stem
from dhivehi_nlp.tokenizer import word_tokenize
from dhivehi_nlp.stopwords import get_stopwords


class DhivehiNewsClassifier:
    def __init__(self):
        self.model_path="models/mvnews_classifier_1622907065.h5"
        self.tokenizer_path= "models/tokenizer_1622907065.pickle"
        self.stop_words = get_stopwords()
        self.model = tf.keras.models.load_model(self.model_path)
        with open(self.tokenizer_path, "rb") as f:
            self.tokenizer = pickle.load(f)

    def cleaner(self, text):
        text = "".join([i for i in text if not i.isdigit()])
        stemed_text = stem(text)
        word_tokens = word_tokenize(" ".join(stemed_text), removeNonDhivehiNumeric=True, removePunctuation=True)

        filtered_sentence = []
        for word_token in word_tokens:
            if word_token not in self.stop_words:
                filtered_sentence.append(word_token)
        text = (" ".join(filtered_sentence))
        return text

    def predict(self, text):
        categories = ["ސިޔާސީ", "ވިޔަފާރި", "ކުޅިވަރު", "ދުނިޔޭގެ ޚަބަރު", "ރިޕޯޓް"]
        cleaned_text = self.cleaner(text)
        encoded_text = self.tokenizer.texts_to_sequences([cleaned_text])
        encoded_text = sequence.pad_sequences(encoded_text, maxlen=500)
        predict_topic = self.model.predict(encoded_text)
        prediction = np.argmax(predict_topic)
        return categories[prediction]