
# SlangLens

SlangLens is a Python-based project designed to analyze any social media captions for slang words. The tool includes web scraping, text preprocessing, stopword removal, and slang detection functionalities. It leverages Python libraries like `requests`, `BeautifulSoup`, and `nltk` to extract, clean, and process textual data from posts.

## Features
1. **Web Scraping**: Fetch captions from social media posts using a provided URL.
2. **Text Preprocessing**:
   - Removes emojis, special characters, and links.
   - Converts text to lowercase for uniformity.
3. **Stopword Removal**: Removes common English stopwords for cleaner analysis.
4. **Slang Detection**: Identifies slang words in the text and provides their corresponding meanings using a custom slang dictionary.

## Prerequisites
- Python 3.6 or above
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `nltk`

Install dependencies using:
```bash
pip install requests beautifulsoup4 nltk
```

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Slangify-Analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Slangify-Analyzer
   ```
3. Install dependencies as mentioned in the Prerequisites section.
4. Download and configure NLTK resources:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage
1. Update the `post_url` variable in the script with the URL of the social media post you want to analyze.
2. Run the script:
   ```bash
   python Slangwords.py
   ```
3. The script will:
   - Fetch the post caption.
   - Preprocess the text.
   - Remove stopwords.
   - Detect slang words and print them with their meanings.

## Example Output
```text
Slang detected in caption: 'btw, omg this is mad!'
Detected slang words and their meanings:
btw: by the way
omg: oh my god
mad: angry
```

## Limitations
- This project currently works with simple HTML structures. It may not scrape captions from dynamically loaded content.
- The slang dictionary is manually defined and can be extended for better coverage.

## Future Enhancements
- Integrate with more robust scraping libraries for handling JavaScript-rendered content.
- Expand the slang dictionary with community contributions.
- Add sentiment analysis of captions.

## Contributions
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
