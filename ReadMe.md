# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using Python, Machine Learning, and Natural Language Processing (NLP). The system analyzes movie metadata — genres, keywords, cast, crew, and plot overview — to recommend the top 5 most similar movies for any given title.

---

## 🚀 How It Works

1. **Data Loading** — Loads two TMDB datasets (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) and merges them on movie title.
2. **Feature Extraction** — Extracts genres, keywords, top 3 cast members, and director from raw JSON-like string columns using Python's `ast` module.
3. **Text Preprocessing** — Combines all features into a single `tags` column, removes spaces from multi-word names, converts to lowercase.
4. **Stemming** — Applies Porter Stemmer (NLTK) to reduce words to their root form for better matching.
5. **Vectorization** — Converts the `tags` text into numerical vectors using `CountVectorizer` with a vocabulary of 5000 features and English stopword removal.
6. **Similarity Calculation** — Computes Cosine Similarity between all movie vectors to find the closest matches.
7. **Recommendation** — Returns the top 5 most similar movies for any input title.
8. **Model Saving** — Exports the processed dataframe and similarity matrix as `.pkl` files using `pickle` for reuse.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas & NumPy | Data loading, merging, and manipulation |
| ast | Parsing JSON-like string columns |
| NLTK (PorterStemmer) | Text stemming / NLP preprocessing |
| Scikit-learn (CountVectorizer) | Text vectorization |
| Scikit-learn (Cosine Similarity) | Movie similarity calculation |
| Matplotlib & Seaborn | Data visualization |
| Pickle | Saving model artifacts |

---

## 📁 Project Structure

```
movie-recommendation-system/
│
├── dataset/
│   ├── tmdb_5000_movies.csv       → Movie details (genres, keywords, overview)
│   └── tmdb_5000_credits.csv      → Cast and crew information
│
├── movie_recomending_system.ipynb → Main Jupyter Notebook (full pipeline)
├── movie_list.pkl                 → Processed movie dataframe (pickled)
├── similarity.pkl                 → Cosine similarity matrix (pickled)
└── README.md                      → Project documentation
```└── download_links.txt  → Google Drive download link for similarity.pkl

---s

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn nltk matplotlib seaborn
   ```

3. **Download NLTK data** (if not already installed)
   ```python
   import nltk
   nltk.download('punkt')
   ```

4. **Place the datasets** inside a `dataset/` folder

5. **Run the notebook**
   ```bash
   jupyter notebook movie_recomending_system.ipynb
   ```

6. **Get recommendations**
   ```python
   print(recommend('Avatar'))
   # Output: ['Guardians of the Galaxy', 'Aliens', ...]
   ```

---

## 📊 Dataset

- **Source:** [TMDB 5000 Movie Dataset — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Size:** 4,800+ movies
- **Features used:** genres, keywords, overview, cast (top 3), crew (director)

---

## 💡 Key Concepts Used

- **Content-Based Filtering** — Recommends movies similar to the one you input based on content features, not user ratings.
- **Bag of Words (CountVectorizer)** — Converts text into word frequency vectors.
- **Cosine Similarity** — Measures the angle between two vectors to determine how similar two movies are.
- **Porter Stemming** — Reduces words like "running", "runs", "ran" to their base form "run" for better matching.

---

## 🙋‍♂️ Author

**Sidharth Gupta**  
BCA Student | Data Science Enthusiast  
[LinkedIn](https://linkedin.com/in/your-profile) · [GitHub](https://github.com/your-username)