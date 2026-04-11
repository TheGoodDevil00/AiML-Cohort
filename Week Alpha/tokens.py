import sentencepiece as spm

# Train a model from raw text
spm.SentencePieceTrainer.train('--input=data.txt --model_prefix=m --vocab_size=1000')

# Load the model
sp = spm.SentencePieceProcessor()
sp.load('m.model')

# Encode and decode
print(sp.encode_as_pieces('Hello world'))
print(sp.decode_pieces([' Hello', ' world']))
