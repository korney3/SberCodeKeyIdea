def extract_keywords(text):
    from rutermextract import TermExtractor
    term_extractor = TermExtractor()
    return [term.normalized for term in term_extractor(text)]
