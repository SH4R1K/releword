def find_phrases(text):
    from natasha import (
        Segmenter,
        NewsEmbedding,
        NewsMorphTagger,
        NewsSyntaxParser,
        Doc
    )
    import pymorphy2

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
                    if (token2.head_id == headId or token2.id == headId):
                        text = text + f"{token2.text} "
                massive = massive + [text.strip()]
    return massive

