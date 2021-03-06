from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer

training_data = load_data('nlu.md')
pipeline = [{"name": "nlp_spacy"},
            {"name": "tokenizer_spacy"},
            {"name": "intent_featurizer_spacy"},
            {"name": "intent_classifier_sklearn"}]
trainer = Trainer(RasaNLUModelConfig({"pipeline": pipeline}))
interpreter = trainer.train(training_data)
model_directory = trainer.persist('./projects/default/')
