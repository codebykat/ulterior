from ulterior import app
from ulterior.database import db_session
from ulterior.models import Prefix, Word, Tag, Madlib

from flask import render_template, request

from sqlalchemy.sql.expression import func

from random import choice
import re

@app.route( '/' )
def madlib():
	m = Madlib.query.order_by( func.random() ).first()

	regex = re.compile( r"\{\{(.+?)\}\}" )
	blanks = regex.findall( m.text )

	return render_template( 'madlib.html', madlib=m, blanks=blanks )


# helper function for motive().  not sure if it belongs here...
def fill_in_word( match ):
	tagname = match.group( 1 )
	t = Tag.query.filter( Tag.text == tagname ).first()
	if None is t or [] == t.words:
		return tagname
	return choice( t.words ).text


@app.route( '/motive', methods=['GET', 'POST'] )
def motive():
	prefix = Prefix.query.order_by( func.random() ).first()

	if 'GET' == request.method :
		m = Madlib.query.order_by( func.random() ).first()
	else:
		m = Madlib.query.get( request.form['madlib_id'] )

	sentence = m.text

	regex = re.compile( r"\{\{(.+?)\}\}" )

	if 'GET' == request.method :
		# fill in with random words from the dictionary
		sentence = regex.sub( fill_in_word, sentence )

	else:
		# for each match, replace with next word in submitted form
		tags = regex.findall( sentence )

		i=0
		for tag in tags:
			word = request.form["madlib-blank-" + str( i )].strip()
			i += 1

			sentence = sentence.replace( "{{" + tag + "}}", word, 1 )

			# add new words to the dictionary

			# todo: lowercase -- but not proper nouns??
			w = Word.query.filter( Word.text == word ).first()
			if None is w:
				w = Word( word, [ tag ] )
				db_session.add( w )

			# add these tags if they don't exist
			t = Tag.query.filter( Tag.text == tag ).first()

			# todo: only if it doesn't exist already?
			w.tags.append( t )

		db_session.commit()

		# TODO save generated sentence for posterity - maybe only on up-vote?

	return render_template( 'motive.html', prefix=prefix, motivation=sentence )