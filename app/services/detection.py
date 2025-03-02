from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Ensure deterministic results
DetectorFactory.seed = 0

def detect_language(text: str):
    """
    Detects the language of a given text.
    """
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"
