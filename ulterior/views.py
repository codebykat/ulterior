from ulterior import app
from ulterior.models import Prefix, Madlib, WordType, Word

from flask import render_template, request

from random import randint, choice

@app.route('/', methods=['GET', 'POST'])
def motive():

	if(request.method == 'POST'):
		rand = randint(1, Prefix.query.count())
		prefix = Prefix.query.get(rand)

		m = Madlib.query.get(request.form['madlib_id'])

		sentence = m.sentence

		blanks = m.blanks
		i=0

		for blank in m.blanks:
		# for word in request.form.getlist("madlib_blank[]"):
			submitted_val = request.form["madlib-blank-"+str(blank.word_type.id)]
			# TODO add new words to the dictionary
			# wt = blanks[i]
			# i += 1

			# todo: lowercase
			# word_in_dictionary = Word.query.filter(Word.word_type == wt).filter(Word.text == word)
			# if word_in_dictionary is None:
			# 	Word(word_type, word)
				# TODO save to database

			sentence = sentence.replace('{}', submitted_val, 1)
		# for blank in m.blanks:
		# 	if(blank.words.all() == []):
		# 		word = "(nothing found)"
		# 	else:
		# 		word = choice(blank.words.all()).text
		# 	sentence = sentence.replace('{}', word, 1)

		# TODO save generated sentence for posterity - maybe only on up-vote?

		return render_template('motive.html', prefix=prefix, motivation=sentence)

	# implicit else - GET request displays a madlib form
	rand = randint(1, Madlib.query.count())	
	m = Madlib.query.get(rand)

	return render_template('madlib.html', madlib=m)