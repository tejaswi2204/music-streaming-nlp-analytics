# 🎵 Product Analytics and User Feedback Analysis of Music Streaming Platforms using NLP

> MCA Final Year Project | KL Education Foundation  
> Department of Computer Science and Applications  
> \*\*Student:\*\* S. Lakshmi Tejaswi (2401600069)  
> \*\*Guide:\*\* Mr. L Nageswar Rao, Asst. Professor M.Tech (PhD)

\---

## 📌 Overview

This project analyzes user behavior, satisfaction, and feedback for popular music streaming platforms — **Spotify**, **YouTube Music**, **JioSaavn**, **Gaana**, and **Wynk Music** — using **Natural Language Processing (NLP)** and **Data Analytics** techniques.

It combines structured **survey data** (17-question Google Form) and unstructured **Google Play Store review data** to identify user pain points, sentiment trends, and factors influencing premium subscription adoption. Final insights are presented through interactive **Power BI dashboards**.

\---

## 🎯 Objectives

* Collect and preprocess user feedback from surveys and Google Play Store
* Detect review language using `langdetect` and filter for meaningful English reviews
* Generate semantic embeddings using **Sentence-BERT (all-MiniLM-L6-v2)**
* Perform **KMeans clustering** (k=5) to identify hidden patterns in reviews
* Apply **VADER sentiment analysis** to classify opinions (Positive / Negative / Neutral)
* Map reviews into 7 business topic categories based on keyword rules
* Process and engineer features from structured survey data for dashboard-ready output
* Visualize insights via interactive **Power BI dashboards**

\---

## 🧠 Key Features

|Feature|Description|
|-|-|
|Web Scraping|Collect 200 reviews per app (1000 total) from Google Play Store using `google-play-scraper`|
|Language Detection|Filter non-English and short reviews using `langdetect`|
|NLP Preprocessing|Lowercasing, URL removal, special character stripping, whitespace normalization|
|Sentiment Analysis|VADER-based classification with contrastive clause refinement (`but` / `however`)|
|Semantic Embeddings|Sentence-BERT (`all-MiniLM-L6-v2`) for contextual review representation|
|Clustering|KMeans (k=5) on sentence embeddings to group similar reviews|
|Topic Labeling|Keyword-based mapping into 7 business issue categories|
|Survey Processing|18-column survey cleaning with ordinal encoding, binary flags, and engagement scoring|
|Visualization|Power BI dashboards (Overview, NLP Insights, Survey Insights)|

\---

## 🛠️ Tech Stack

|Layer|Tools / Libraries|
|-|-|
|Language|Python 3.13|
|Data Processing|Pandas, NumPy|
|NLP \& Embeddings|NLTK (VADER), `sentence-transformers` (`all-MiniLM-L6-v2`)|
|Machine Learning|Scikit-learn (KMeans, cosine similarity)|
|Language Detection|`langdetect`|
|Visualization|Power BI|
|Data Collection|Google Forms (survey), `google-play-scraper` (reviews)|
|Development|Jupyter Notebook / Anaconda|

\---

## 📁 Project Structure

```
Analysis on Music streaming platforms/
│
├── Data/
│   ├── raw\_data/
│   │   ├── music\_app\_reviews.csv        # Raw scraped app reviews (1000 rows, 5 apps)
│   │   └── raw\_form\_data.csv            # Raw Google Forms survey data (17 questions)
│   └── processed\_data/
│       ├── final\_output.csv             # Reviews with cluster, topic, and sentiment labels
│       ├── summary\_output.csv           # Aggregated topic × sentiment counts
│       └── survey\_data\_cleaned\_new.csv  # Cleaned \& feature-engineered survey data
│
├── Notebooks/
│   ├── App\_reviews.ipynb                # Google Play scraping (all 5 apps)
│   ├── Data\_preprocessing.ipynb         # Survey data cleaning \& feature engineering
│   └── Model.ipynb                      # Embeddings, clustering, sentiment, topic labeling
│
├── Dashboards/
│   └── MusicStreamingAnalytics.pbix     # Power BI dashboard file
│
├── reports/
│   └── Documentation(2401600069).docx   # Full project documentation
│
├── survey\_data.pdf                      # Original survey form (PDF export)
├── requirements.txt                     # Python dependencies
├── gitignore                            # Files to exclude from Git
└── README.md                            # Project overview (this file)
```

\---

## ⚙️ Setup \& Installation

### 1\. Clone the Repository

```bash
git clone https://github.com/<your-username>/music-streaming-platforms-nlp.git
cd music-streaming-platforms-nlp
```

### 2\. Install Dependencies

```bash
pip install -r requirements.txt
pip install langdetect sentence-transformers
```

### 3\. Download NLTK Data

```python
import nltk
nltk.download('vader\_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')
```

### 4\. Run the Notebooks (in order)

Open Jupyter Notebook and run in this sequence:

|Step|Notebook|Description|
|-|-|-|
|1|`App\_reviews.ipynb`|Scrape 200 reviews per app from Google Play|
|2|`Data\_preprocessing.ipynb`|Clean and engineer features from survey CSV|
|3|`Model.ipynb`|Run embeddings → clustering → sentiment → topic labeling|

\---

## 🗂️ Topic Categories

Reviews are classified into 7 business-meaningful categories using keyword rules:

|Topic|Trigger Keywords|
|-|-|
|Ads Issues|`ads`|
|Premium Issues|`premium`, `subscription`|
|Performance Issues|`crash`, `lag`, `slow`|
|Content/Search Issues|`search`, `not available`, `missing`|
|Recommendation Issues|`recommend`, `suggest`, `discover`|
|User Experience|`easy`, `interface`, `experience`, `freedom`|
|Regional Feedback|Reviews containing Hindi/Devanagari script|
|General Feedback|All others|

\---

## 🔍 Cluster Insights (from KMeans, k=5)

|Cluster|Theme|
|-|-|
|0|Frustration — missing songs, useless without premium|
|1|Music discovery — playlist recommendations, variety|
|2|Ads — too many interruptions, download restrictions|
|3|Regional / Hindi feedback — pricing complaints, search failures|
|4|General praise — good app, good song library|

\---

## 📊 Survey Data

The Google Forms survey captured **17 questions** across 18 structured columns including:

* Demographics: Age group
* Behavior: Daily listening hours, skip frequency, device used, video watching
* App preferences: Current app, reasons for choice, free vs. premium
* Satisfaction: Overall score, recommendation quality, premium price rating
* Pain points: Biggest frustration, desired changes
* Churn signals: Switched before, reasons for switching, future switch intent

**Engineered features** created during preprocessing: `listening\_hours\_ord`, `skip\_frequency\_ord`, `premium\_user`, `watches\_video`, `switched\_before`, `switch\_risk`, `satisfaction\_tier`, `engagement\_score`, `premium\_price\_worth\_it\_score`

\---

## 📊 Dashboard

The Power BI dashboard (`dashboard/MusicStreamingAnalytics.pbix`) contains three report pages:

* **Overview** — High-level KPIs: total users, satisfaction score, premium adoption, churn risk
* **NLP Insights** — Sentiment distribution, topic breakdown, app-wise cluster comparison
* **Survey Insights** — User behavior, switching intent, feature preferences, engagement scores

> Open the `.pbix` file using \[Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/).

\---

## 📈 Results

* Scraped **1,000 reviews** across 5 platforms (200 per app)
* Identified **5 review clusters** using Sentence-BERT embeddings + KMeans
* Classified reviews into **7 topic categories** using keyword-based rules
* Detected **Hindi/regional reviews** automatically using Unicode range detection
* Key pain points: excessive ads, high premium pricing, missing songs, poor recommendations
* Survey data revealed strong correlation between low satisfaction scores and high switching intent

\---

## 🚀 Future Enhancements

* Replace VADER with **RoBERTa** for deeper contextual sentiment analysis
* Add **real-time review monitoring** via Play Store streaming
* Build a **churn prediction model** using behavioral signals from survey data
* Add **multilingual sentiment support** for regional-language reviews (Hindi, Telugu, etc.)
* Deploy as a **web application** with automated reporting

\---

## 📦 Dependencies Note

The following packages are used but not listed in `requirements.txt` — add them manually:

```
langdetect
sentence-transformers
```

\---

## 📚 References

* Hutto \& Gilbert (2014) — VADER Sentiment Analysis
* Reimers \& Gurevych (2019) — Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks
* Pang \& Lee (2008) — Opinion Mining and Sentiment Analysis
* Pedregosa et al. (2011) — Scikit-learn
* Bird, Klein \& Loper (2009) — NLTK

\---

## 👩‍💻 Author

**S. Lakshmi Tejaswi**  
Roll No: 2401600069  
Master of Computer Applications  
Department of Computer Science and Applications  
KL Education Foundation, Vaddeswaram, Andhra Pradesh

\---

## 📄 License

This project is submitted for academic purposes at KL University. All rights reserved.

