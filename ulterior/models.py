from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from ulterior.database import Base, db_session


class Prefix( Base ):
	__tablename__ = 'prefixes'
	id = Column( Integer, primary_key=True )
	text = Column( String( 255 ), unique=True )

	def __init__( self, text=None ):
		self.text = text

	def __repr__(self):
		return '<Prefix %r>' % ( self.text )


word_tag_table = Table(
	'word_tag_table', Base.metadata,
	Column( 'tag_id', Integer, ForeignKey( 'word_tags.id' ) ),
	Column( 'word_id', Integer, ForeignKey( 'words.id') )
)

class Tag( Base ):
	__tablename__ = 'word_tags'
	id = Column( Integer, primary_key=True )
	text = Column( String( 100 ), unique=True )

	def __init__( self, text=None ):
		self.text = text

	def __repr__( self ):
		return '<Tag %r>' % ( self.text )


class Word( Base ):
	__tablename__ = 'words'
	id = Column( Integer, primary_key=True )
	text = Column( String( 255 ), unique=True )

	tags = relationship( 'Tag', secondary='word_tag_table', backref='words' )

	def __init__( self, text=None, tags=[] ):
		self.text = text
		for tag in tags:
			t = Tag.query.filter( Tag.text == tag ).first()
			self.tags.append( t )

	def __repr__( self ):
		return '<Word %r (tags: %r)>' % ( self.text, ', '.join( [ tag.text for tag in self.tags ] ) )


class Madlib( Base ):
	__tablename__ = 'madlibs'
	id = Column( Integer, primary_key=True )
	text = Column( String( 1000 ), unique=True )

	def __init__( self, text=None ):
		self.text = text

	def __repr__( self ):
		text = self.text
		return '<Madlib %r>' % ( text )