import json
import os
import re

def save_json(filepath, data):
    """Save dictionary or list data to a JSON file, creating dirs if needed."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving to {filepath}: {e}")

def load_json(filepath):
    """Load dictionary or list data from a JSON file. Returns None if not found."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading from {filepath}: {e}")
        return None

def normalize_text(text):
    """Normalize text: lowercase, strip, remove extra spaces, unify line endings."""
    if not isinstance(text, str):
        return ""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()

def mood_from_text(text):
    """
    Improved mood detection from text using keyword scanning.
    Returns: 'happy', 'sad', 'angry', 'anxious', 'calm', 'excited', 'tired', or 'neutral'
    """
    if not isinstance(text, str) or not text.strip():
        return 'neutral'

    # Expanded keyword lists
    mood_keywords = {
        'happy':    ['happy', 'joy', 'great', 'good', 'awesome', 'fantastic', 'delighted', 'pleased', 'cheerful', 'content'],
        'sad':      ['sad', 'bad', 'depressed', 'unhappy', 'down', 'upset', 'cry', 'tearful', 'miserable'],
        'angry':    ['angry', 'mad', 'furious', 'irritated', 'annoyed', 'frustrated'],
        'anxious':  ['anxious', 'worried', 'nervous', 'tense', 'stressed', 'afraid', 'scared', 'panic'],
        'calm':     ['calm', 'relaxed', 'peaceful', 'chill', 'serene', 'at ease'],
        'excited':  ['excited', 'eager', 'thrilled', 'enthusiastic', 'pumped'],
        'tired':    ['tired', 'sleepy', 'exhausted', 'fatigued', 'worn out', 'drained'],
    }

    text_lower = text.lower()
    for mood, keywords in mood_keywords.items():
        for word in keywords:
            if re.search(r'\b' + re.escape(word) + r'\b', text_lower):
                return mood
    return 'neutral'