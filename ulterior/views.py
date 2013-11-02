from ulterior import app
from ulterior.models import Prefix, Madlib, WordType, Word

from flask import render_template, request

from random import randint, choice

@app.route('/')
def madlib():
	rand = randint(1, Madlib.query.count())	
	m = Madlib.query.get(rand)

	return render_template('madlib.html', madlib=m)


@app.route('/motive', methods=['GET', 'POST'])
def motive():
	rand = randint(1, Prefix.query.count())
	prefix = Prefix.query.get(rand)

	if(request.method == 'GET'):
		rand = randint(1, Madlib.query.count())	
		m = Madlib.query.get(rand)
	else:
		m = Madlib.query.get(request.form['madlib_id'])

	sentence = m.sentence

	# i=0

	for blank in m.blanks:
		if(request.method == 'GET'):
			if(blank.word_type.words.all() == []):
				word = "(nothing found)"
			else:
				word = choice(blank.word_type.words.all()).text
		else:
			word = request.form["madlib-blank-"+str(blank.word_type.id)]
			# TODO add new words to the dictionary
			# wt = blanks[i]
			# i += 1

			# todo: lowercase
			# word_in_dictionary = Word.query.filter(Word.word_type == wt).filter(Word.text == word)
			# if word_in_dictionary is None:
			# 	Word(word_type, word)
			# TODO save to database

		sentence = sentence.replace('{}', word, 1)


	# TODO save generated sentence for posterity - maybe only on up-vote?

	return render_template('motive.html', prefix=prefix, motivation=sentence)