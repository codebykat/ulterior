from ulterior.database import db_session
from ulterior.models import Prefix, Word, Tag, Madlib


prefixes = [
	"Your true passion is ",
	"Your highest goal is ",
	"Your purpose in life is ",
	"The deepest desire of your heart is ",
	"The passion that drives you is the need ",
	"Secretly, you really want ",
	"You are on a quest ",
]

tags = [
	'adjective',
	'adverb',
	'animal',
	'body part',
	'color',
	'emotion',
	'food',
	'noun',
	'number',
	'person',
	'place',
	'plural noun',
	'past-tense verb',
	'relative',
	'vehicle',
	'verb',
]

words = {
	'bees':								[ 'plural noun', 'animal', ],
	'bicycle':							[ 'noun', 'vehicle', ],
	'candies':							[ 'plural noun', 'food', ],
	'car':								[ 'noun', 'vehicle', ],
	'cat':								[ 'noun', 'animal', ],
	'cats':								[ 'plural noun', 'animal', ],
	'demon':							[ 'noun', 'animal', ],
	'dog':								[ 'noun', 'animal', ],
	'ears':								[ 'plural noun', 'body part', ],
	'eyes':								[ 'plural noun', 'body part', ],
	'face':								[ 'noun', 'body part', ],
	'hands':							[ 'plural noun', 'body part', ],
	'house':							[ 'noun', ],
	'money':							[ 'noun', ],
	'monkey':							[ 'noun', 'animal', ],
	'mouth':							[ 'noun', 'body part', ],
	'nose':								[ 'noun', 'body part', ],
	'pasturized process cheese food':	[ 'noun', 'food', ],
	'peanut butter':					[ 'noun', 'food', ],
	'sheep':							[ 'noun', 'plural noun', 'animal', ],
	'San Francisco':					[ 'noun', 'place', ],
	'Soylent':							[ 'noun', 'food', ],
	'the moon':							[ 'noun', 'place', ],
	'the world':						[ 'noun', 'place', ],
	'unicorn':							[ 'noun', 'animal', ],

	'attacked':		[ 'past-tense verb', ],
	'avenge':		[ 'verb', ],
	'devoured':		[ 'past-tense verb', ],
	'find':			[ 'verb', ],
	'kidnapped':	[ 'past-tense verb', ],
	'marry':		[ 'verb', ],
	'murdered':		[ 'past-tense verb', ],
	'raised':		[ 'past-tense verb', ],
	'rescue':		[ 'verb', ],

	'colorless':	[ 'adjective', ],
	'happy':		[ 'adjective', ],
	'ugly':			[ 'adjective', ],

	'furiously':	[ 'adverb', ],

	'David Bowie':		[ 'person', ],
	'Obama':			[ 'person', ],
	'Ichabod Crane':	[ 'person', ],
	'Ada Lovelace':		[ 'person', ],

	'red':		[ 'color', 'adjective', ],
	'green':	[ 'color', 'adjective', ],
	'blue':		[ 'color', 'adjective', ],
	'black':	[ 'color', 'adjective', ],
	'white':	[ 'color', 'adjective', ],

	'7':			[ 'number', ],
	'42':			[ 'number', ],
	'one million':	[ 'number', ],

	'mother':		[ 'relative', ],
	'father':		[ 'relative', ],
	'brother':		[ 'relative', ],
	'sister':		[ 'relative', ],

	'love':			[ 'emotion', ],
	'hate':			[ 'emotion', ],
}


madlibs = [
	"to take over {{place}}",
	"to {{verb}} your {{relative}}, who was {{past-tense verb}} by a {{animal}}",
	"to find true {{emotion}}",
	"to acquire {{place}} for strategic {{animal}} purposes",
	"to collect all the {{plural noun}} in {{place}} and stick them in your {{body part}}",
	"to steal from the {{adjective}} and give to the {{adjective}}",
	"to save up {{number}} {{plural noun}} so you can buy a really {{adjective}} {{noun}}",
]



def seed_db():
	for prefix in prefixes:
		p = Prefix( prefix )
		db_session.add( p )

	for tag in tags:
		t = Tag( tag )
		db_session.add( t )

	db_session.commit()

	for word, wordtags in words.items():
		w = Word( word, wordtags )
		db_session.add( w )

	for madlib in madlibs:
		m = Madlib( madlib )
		db_session.add( m )

	db_session.commit()