from ulterior import app
from ulterior.database import db_session
from ulterior.models import Prefix, Word, Tag, Madlib

from flask import render_template, request

from random import randint, choice
import re

@app.route( '/' )
def madlib():
	rand = randint( 1, Madlib.query.count() )	
	m = Madlib.query.get( rand )

	regex = re.compile( r"\{\{(.+?)\}\}" )
	blanks = regex.findall( m.text )

	return render_template( 'madlib.html', madlib=m, blanks=blanks )


def fill_in_word( match ):
	tagname = match.group( 1 )
	t = Tag.query.filter( Tag.text == tagname ).first()
	if None == t or [] == t.words:
		return tagname
	return choice( t.words ).text


@app.route( '/motive', methods=['GET', 'POST'] )
def motive():
	rand = randint( 1, Prefix.query.count() )
	prefix = Prefix.query.get( rand )

	if 'GET' == request.method :
		rand = randint( 1, Madlib.query.count() )	
		m = Madlib.query.get( rand )
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
			if None == w:
				w = Word( word, [ tag ] )
				db_session.add( w )

			# add these tags if they don't exist
			t = Tag.query.filter( Tag.text == tag ).first()
			if None == t:
				t = Tag( tag )
				db_session.add( t )

			# todo: only if it doesn't exist already?
			w.tags.append( t )

		db_session.commit()

		# TODO save generated sentence for posterity - maybe only on up-vote?

	return render_template( 'motive.html', prefix=prefix, motivation=sentence )