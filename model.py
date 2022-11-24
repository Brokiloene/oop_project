import random
import re

from transformers import GPT2LMHeadModel, GPT2Tokenizer


class RecipeModel:
    def __init__(self, max_length=150, repetition_penalty=10.0, top_p=0.8):
        self.__tokenizer: GPT2Tokenizer = GPT2Tokenizer.from_pretrained("model_data")
        self.__tokenizer.padding_side = "left"
        self.__tokenizer.pad_token = self.__tokenizer.eos_token
        self.__model: GPT2LMHeadModel = GPT2LMHeadModel.from_pretrained("model_data")
        self.__max_length = max_length
        self.__repetition_penalty = repetition_penalty
        self.__top_k = random.randint(10, 200)
        self.__top_p = top_p
        self.__temperature = random.uniform(1.0, 2.0)

    def generate_text(self, prompt):
        encoding = self.__tokenizer(prompt, padding=False, return_tensors="pt", )
        generated_ids = self.__model.generate(**encoding, max_length=self.__max_length, do_sample=True,
                                              repetition_penalty=self.__repetition_penalty,
                                              top_k=self.__top_k,
                                              top_p=self.__top_p, temperature=self.__temperature)
        generated_texts = self.__tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        return generated_texts[0]
    
    
def preparation(text):
    text = text.replace('\xa0—', ' ').replace('\n', ' ')
    text = re.sub('[a-zA-z<>/="&%]', '', text)
    text = text[(text.find('ание: ') + 7):]
    text = text[: (text.find('Рецепт') - 1)].upper() + '\n' + text[(text.find('Рецепт')):]
    text = text.replace('..', 'twodots').replace('...', 'threedots').replace('. ', '.').replace('.', '. ') \
        .replace('! ', '!').replace('!', '! ').replace('? ', '?').replace('?', '? ').replace('  ', ' ') \
        .replace(' :', ':').replace('twodots', '..').replace('threedots', '...')
    return text
