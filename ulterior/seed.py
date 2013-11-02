from ulterior.database import db_session
from ulterior.models import Prefix, Word, WordType, Madlib


prefixes = [
	"Your true passion is ",
	"Your highest goal is ",
	"Your purpose in life is ",
	"The deepest desire of your heart is ",
	"The passion that drives you is the need ",
	"Secretly, you really want ",
	"You are on a quest "
]

words = {
	"food": [
		"Soylent",
		"peanut butter",
		"pasturized process cheese food"
	],
	"body part": [
		"ears",
		"eyes",
		"nose",
		"face",
		"mouth",
		"hands"
	],
	"noun": [
		"money"
	],
	"animal": [
		"dog",
		"cat",
		"monkey",
		"sheep",
		"unicorn",
		"demon"
	],
	"verb": [
		"avenge",
		"find",
		"marry"
	],
	"past-tense verb": [
		"murdered",
		"attacked",
		"devoured",
		"raised",
		"kidnapped"
	],
	"adjective": [
		"colorless",
		"happy",
		"ugly"
	],
	"adverb": [
		"furiously"
	],
	"place": [
		"the world",
		"the moon",
		"San Francisco"
	],
	"person": [
		"David Bowie",
		"Obama",
		"Ichabod Crane",
		"Ada Lovelace"
	],
	"color": [
		"red",
		"green",
		"blue",
		"black",
		"white"
	],
	"number": [
		"7",
		"42",
		"one million"
	],
	"relative": [
		"mother",
		"father",
		"brother",
		"sister"
	],
	"emotion": [
		"love",
		"hate"
	]
}


madlibs = [
	[ "to take over {}", [ "place" ] ],
	[ "to {} your {}, who was {} by a {}", [ "verb", "relative", "past-tense verb", "animal" ] ],
	[ "to find true {}", [ "emotion" ] ],
	[ "to acquire {} for strategic {} purposes", ["place", "animal"]],
	[ "to collect all the {} in {} and stick it in your {}", ["noun", "place", "body part"]]
]



def seed_db():
	for prefix in prefixes:
		p = Prefix(prefix)
		db_session.add(p)
		db_session.commit()

	for word_type, word_examples in words.items():
		wt = WordType(word_type)
		db_session.add(wt)
		db_session.commit()

		wt = WordType.query.filter(WordType.description == word_type).first()

		for example in word_examples:
			w = Word(wt, example)
			db_session.add(w)

	for madlib in madlibs:
		m = Madlib(madlib[0], madlib[1])
		db_session.add(m)

	db_session.commit()