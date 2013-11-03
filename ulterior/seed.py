from ulterior.database import db_session
from ulterior.models import Prefix, Word, Tag, Madlib


prefixes = [
	"Your true passion is to ",
	"Your highest goal is to ",
	"Your purpose in life is to ",
	"The deepest desire of your heart is to ",
	"The passion that drives you is the need to ",
	"Secretly, you really want to ",
	"You are on a quest to ",
	"More than anything, you want to ",
	"Most of all, you want to",
	"You will not rest until you ",
	"You are training day and night to ",
	"Ever since you were a child, you knew it was your destiny to ",
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
	'past-tense verb',
	'person',
	'place',
	'plural noun',
	'profession',
	'relative',
	'vehicle',
	'verb',
]

words = {
	'bee':								[ 'noun', 'animal', ],
	'bees':								[ 'plural noun' ],
	'bicycle':							[ 'noun', 'vehicle', ],
	'candies':							[ 'plural noun', 'food', ],
	'car':								[ 'noun', 'vehicle', ],
	'cat':								[ 'noun', 'animal', ],
	'cats':								[ 'plural noun', ],
	'demon':							[ 'noun', 'animal', ],
	'dog':								[ 'noun', 'animal', ],
	'duck':								[ 'noun', 'animal', ],
	'ears':								[ 'plural noun', 'body part', ],
	'elbow':							[ 'noun', 'body part', ],
	'eyes':								[ 'plural noun', 'body part', ],
	'face':								[ 'noun', 'body part', ],
	'hands':							[ 'plural noun', 'body part', ],
	'house':							[ 'noun', ],
	'Manhattan':						[ 'noun', 'place', ],
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
	'seduce':		[ 'verb', ],

	'colorless':	[ 'adjective', ],
	'famous':		[ 'adjective', ],
	'happy':		[ 'adjective', ],
	'mad':			[ 'adjective', ],
	'powerful':		[ 'adjective', ],
	'popular':		[ 'adjective', ],
	'rich':			[ 'adjective', ],
	'silly':		[ 'adjective', ],
	'ugly':			[ 'adjective', ],

	'furiously':	[ 'adverb', ],

	'David Bowie':			[ 'person', ],
	'Obama':				[ 'person', ],
	'Ichabod Crane':		[ 'person', ],
	'Ada Lovelace':			[ 'person', ],
	'Miley Cyrus':			[ 'person', ],
	'Katy Perry':			[ 'person', ],
	'The Queen of England':	[ 'person', ],
	'Isaac Asimov':			[ 'person', ],

	'red':		[ 'color', 'adjective', ],
	'green':	[ 'color', 'adjective', ],
	'blue':		[ 'color', 'adjective', ],
	'black':	[ 'color', 'adjective', ],
	'white':	[ 'color', 'adjective', ],

	'7':			[ 'number', ],
	'42':			[ 'number', ],
	'one million':	[ 'number', ],

	'your mother':		[ 'relative', 'person', ],
	'your father':		[ 'relative', 'person', ],
	'your brother':		[ 'relative', 'person', ],
	'your sister':		[ 'relative', 'person', ],
	'your step-mother':	[ 'relative', 'person', ],
	'your step-father': [ 'relative', 'person', ],

	'love':			[ 'emotion', ],
	'hate':			[ 'emotion', ],
	'happiness':	[ 'emotion', ],
	'sadness':		[ 'emotion', ],

	'doctor':				[ 'profession', ],
	'computer programmer':	[ 'profession', ],
	'fireman':				[ 'profession', ],
	'scientist':			[ 'profession', ],
}


madlibs = [
	"take over {{place}} with your army of {{adjective}} {{plural noun}}",
	"{{verb}} {{person}}, who was {{past-tense verb}} by a {{animal}}",
	"find true {{emotion}}",
	"acquire {{place}} for strategic {{animal}} purposes",
	"collect all the {{plural noun}} in {{place}} and stick them in your {{body part}}",
	"steal from the {{adjective}} and give to the {{adjective}}",
	"save {{number}} {{plural noun}} so you can buy a really {{adjective}} {{noun}}",
	"become {{adjective}} and {{adjective}}",
	"win the {{emotion}} of a {{adjective}} {{profession}}",
	"become the most {{adjective}} {{profession}} in {{place}}",
	"become more {{adjective}} than {{person}}",
	"learn the answer to the ultimate question of {{noun}}, {{place}} and {{noun}}",
	"find a cure for {{relative}}, who has come down with a {{adjective}} illness",
	"{{verb}} the {{adjective}} {{profession}} who {{past-tense verb}} {{person}}",
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