from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,

    Doc
)
import pymorphy2
morph = pymorphy2.MorphAnalyzer(lang="ru")
segmenter = Segmenter()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

text = "Красная кошка Маруся приехала в бот и улетела на крюке кошке в стратосферу. Ботинки с кошками плотно зацепились за скалу."
doc = Doc(text)

doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)

sent = doc.sents[0]
syntax = sent.syntax
#print(syntax.tokens[1])
massive = []
for token in syntax.tokens:
    p = morph.parse(token.text)[0]
    if (p.normal_form == "кошка"):
        text = ""
        headId = token.id
        for token2 in syntax.tokens:
            if (token2.head_id == headId or token2.id == headId):
                text = text + f"{token2.text} "
        massive = massive + [text.strip()]
        '''print("-------")
        print(text)
        print("-------")'''
print(massive)
#sent.syntax.print()
#print(doc.spans[0])
'''tokens = segmenter.tokenize(text)
for token in tokens:
    p = morph.parse(token.text)[0]
    print(token)
    print(p)
    print('-----')
    if (p.normal_form == "кошка"):
        print(1)'''