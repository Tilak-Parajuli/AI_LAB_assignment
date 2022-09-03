# Import required libraries
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser

# Example text
sample_text = "John hit he dog"

# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))

#Extract all parts of speech from any text
chunker = RegexpParser("""
					NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases
					P: {<IN>}			 #To extract Prepositions
					V: {<V.*>}			 #To extract Verbs
					PP: {

<p> <NP>}		 #To extract Prepositional Phrases
					VP: {<V> <NP|PP>*}	 #To extract Verb Phrases
					""")

# Print all parts of speech in above sentence
output = chunker.parse(tagged)
print("After Extracting\n", output)

# To draw the parse tree
output.draw()