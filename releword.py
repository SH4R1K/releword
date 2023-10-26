from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
)
import pymorphy2
import re
def find_phrases(text):

    morph = pymorphy2.MorphAnalyzer(lang="ru")
    segmenter = Segmenter()

    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)

    doc = Doc(text)

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)

    massive = []
    for sent in doc.sents:
        syntax = sent.syntax
        for token in syntax.tokens:
            p = morph.parse(token.text)[0]
            if (p.normal_form == "кошка"):
                text = ""
                headId = token.id
                for token2 in syntax.tokens:
                    p = morph.parse(token2.text)[0]
                    if ((token2.head_id == headId or token2.id == headId) and (token2.rel == "amod" or p.normal_form == "кошка")):
                        text = text + f"{token2.text} "
                massive += [text.strip()]
    return massive

def get_list_sentences(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        morph = pymorphy2.MorphAnalyzer(lang="ru")
        sentences = []
        text = file.read()
        segmenter = Segmenter()
        doc = Doc(text)
        doc.segment(segmenter)
        for i in doc.sents:
            p = morph.parse(i.text)[0]
           # print(p)
            #if ("кошка" in p.normal_form):
            sentences += [re.sub(r'[^\w\s]','',  i.text.lower())]
        return sentences


