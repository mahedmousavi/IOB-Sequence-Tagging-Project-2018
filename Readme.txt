First, Run the transtioncreator.py in order to obtain a txt file of transtions.
then use these commands to create the transducer from the txt file

ngramsymbols uniPosTagger.txt > lx.lex #to make a lexicon file
fstcompile --isymbols=lx.lex --osymbols=lx.lex uniPosTagger.txt > uniPosTagger.fst #to get the FST

then use these command to train the language model

farcompilestrings --symbols=lx.lex --unknown_symbol='<unk>' pos.txt > pos.far
ngramcount --order=4 --require_symbols=false pos.far > pos.cnt
ngrammake --method=kneser_ney pos.cnt > pos.lm
 
then run the evaluation.py to compose the sentence & FST & language model and obtain result.
the result is the outcome. and the prediction is a file to pass to conlleval.pl



codes:
baselinecreator.py
evaluation.py
distributionfinder.py # is a dirty way of obtaining the distribution of words or tags, etc.
transtioncreator.py 