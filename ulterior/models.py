from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from ulterior.database import Base, db_session


class Prefix(Base):
    __tablename__ = 'prefixes'
    id = Column(Integer, primary_key=True)
    text = Column(String(255))

    def __init__(self, text=None):
        self.text = text

    def __repr__(self):
        return '<Prefix %r>' % (self.text)


class WordType(Base):
    __tablename__ = 'word_types'
    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    words = relationship('Word', backref='word_type', lazy="dynamic")

    def __init__(self, description=None):
        self.description = description

    def __repr__(self):
        return '<WordType %r>' % (self.description)


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word_type_id = Column(Integer, ForeignKey('word_types.id'))

    text = Column(String(255), unique=True)

    def __init__(self, word_type, text=None):
        self.word_type = word_type
        self.text = text

    def __repr__(self):
        return '<Word %r (%r)>' % (self.text, self.word_type.description)


class MadlibWordTable(Base):
    __tablename__ = 'madlibs_to_words'
    madlib_id = Column(Integer, ForeignKey('madlibs.id'), primary_key=True)
    word_type_id = Column(Integer, ForeignKey('word_types.id'), primary_key=True)
    word_type = relationship('WordType')
    order = Column(Integer)

    def __repr__(self):
        return '<a %r at position %i>' % (self.word_type.description, self.order)


class Madlib(Base):
    __tablename__ = 'madlibs'
    id = Column(Integer, primary_key=True)
    sentence = Column(String(1000), unique=True)
    blanks = relationship('MadlibWordTable', order_by='MadlibWordTable.order')

    def __init__(self, sentence=None, blanks=[]):
        self.sentence = sentence
        i=0
        for word_type in blanks:
            wt = WordType.query.filter(WordType.description == word_type).first()
            if wt == None:
                wt = WordType(word_type)
                db_session.add(wt)
                db_session.commit()
            mwt = MadlibWordTable(order=i)
            mwt.word_type_id = wt.id
            self.blanks.append(mwt)
            i += 1

    def __repr__(self):
        sentence = self.sentence
        for wt in self.blanks:
            sentence = sentence.replace("{}", "{" + wt.word_type.description + "}", 1)
        return '<Madlib %r>' % (sentence)