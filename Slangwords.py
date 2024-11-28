import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Step 1: Web scraping Instagram data
def scrape_instagram_post(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract post caption
        caption = soup.find('meta', property='og:description')['content']
        return caption
    else:
        print("Failed to fetch Instagram data.")
        return ""

# Step 2: Preprocessing
def preprocess_text(text):
    # Remove emojis, special characters, and links
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

# Step 3: Stopword removal
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_text)

# Step 4: Slang dictionary
slang_dict = {
    "lol": "laugh out loud",
    "btw": "by the way",
    "omg": "oh my god",
    "mad": "angry"
    # Add more slang words and their meanings
}

# Step 5: Slang detection
def detect_slang(text):
    detected_slang = []
    tokens = word_tokenize(text)
    for token in tokens:
        if token in slang_dict:
            detected_slang.append((token, slang_dict[token]))
    return detected_slang

# Example usage:
post_url = "https://www.facebook.com/share/p/k1nfDQdJw426Ya29/?mibextid=oFDknk"
caption = scrape_instagram_post(post_url)
if caption:
    preprocessed_caption = preprocess_text(caption)
    caption_without_stopwords = remove_stopwords(preprocessed_caption)
    detected_slang = detect_slang(caption_without_stopwords)
    if detected_slang:
        print(f"Slang detected in caption: '{caption}'")
        print("Detected slang words and their meanings:")
        for word, meaning in detected_slang:
            print(f"{word}: {meaning}")
    else:
        print("No slang detected in the caption.")
else:
    print("Failed to fetch caption from the Instagram post.")