import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load English model once (do this outside the function for efficiency)
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """
    Extract keywords from text by:
    - Tokenizing
    - Removing stopwords and punctuation
    - Keeping nouns, proper nouns, and verbs (likely skills/actions)
    """
    doc = nlp(text.lower())
    keywords = set()
    for token in doc:
        if (
            token.is_alpha  # Only letters, no numbers/punctuation
            and not token.is_stop  # Remove common stopwords
            and token.pos_ in {"NOUN", "PROPN", "VERB"}
        ):
            keywords.add(token.lemma_)  # Use lemma to normalize words

    return keywords
def count_keyword_matches(resume_text, job_keywords):
    """
    Count how many job keywords appear in the resume text.
    """
    resume_keywords = extract_keywords(resume_text)
    matched = resume_keywords.intersection(job_keywords)
    return matched, len(matched)

def match_score(resume_text, job_keywords):
    """
    Calculate the percentage of job keywords found in the resume.
    """
    matched, matched_count = count_keyword_matches(resume_text, job_keywords)
    total = len(job_keywords)
    if total == 0:
        return 0, matched  # Avoid division by zero
    score = (matched_count / total) * 100
    return score, matched
