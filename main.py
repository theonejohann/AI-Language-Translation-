# Importing the pipeline function from the transformers library
from transformers import pipeline
# Creating a Text2TextGenerationPipeline for language translation
pipe = pipeline(task='text2text-generation', model='facebook/m2m100_418M')
# Converting 
print(pipe("This is a computer.", forced_bos_token_id=pipe.tokenizer.get_lang_id(lang='de')))