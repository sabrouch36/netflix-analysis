🎬 Netflix Content Analysis Project

Python • SQL • Power BI

📌 Project Overview

This project analyzes Netflix’s content catalog using Python (pandas), SQLite (SQL), and Power BI to answer key business and strategic questions related to:

Content types (Movies vs TV Shows)

Growth of content over time

Geographic contribution

Content rating distribution

Movie duration trends

Future content growth outlook (Forecast)

The project simulates a real-world data analyst workflow:
Data Cleaning → Database Design → SQL Analysis → Visualization → Strategic Insights

🗂️ Project Structure
netflix-analysis/
│
├── data/
│   ├── raw/        # Original Netflix dataset
│   ├── prepared/   # Cleaned dataset (CSV)
│   └── dw/         # SQLite database (netflix.db)
│
├── notebooks/
│   └── 01_data_audit.ipynb   # Data cleaning + SQL analysis
│
├── outputs/        # Analysis outputs
├── sql/            # SQL scripts
├── README.md
└── pyproject.toml

🧹 Data Preparation (Completed)

Data cleaning and feature engineering were performed using pandas:

Converted date_added to datetime format

Extracted year_added from date_added

Standardized missing values (director, country)

Extracted numeric values from duration

Split duration into:

movie_duration_min

tv_seasons

Verified data types and removed inconsistencies

✅ Final cleaned dataset saved as:
data/prepared/netflix_clean.csv

🗄️ Database Creation (Completed)

Created SQLite database: data/dw/netflix.db

Loaded cleaned data into table: netflix_titles

Verified successful insertion (8,790 rows)

📊 SQL Business Analysis
🎬 Content Type Distribution

How many Movies and TV Shows are available on Netflix?

Type	Total Titles
Movie	6,126
TV Show	2,664

Insight:
Netflix’s catalog is heavily dominated by movies, although TV Shows represent a strategically important segment.

📅 Content Growth Over Time

How has Netflix content grown year by year?

Findings:

Slow growth before 2015

Rapid expansion starting in 2016

Peak growth between 2018–2020

Slight decline after 2020

Insight:
Netflix experienced an explosive growth phase following 2016, driven by aggressive content investment.

🌍 Country Contribution

Top content-producing countries:

Country	Titles
United States	3,240
India	1,057
United Kingdom	638
Pakistan	421
Unknown	287

Insight:

The U.S. is the primary content contributor

India plays a major secondary role

A notable number of titles lack country attribution

⭐ Content Ratings Analysis

Most common ratings:

TV-MA

TV-14

TV-PG

R

PG-13

Simplified Rating Groups:

Kids

Family

Teen

Mature

Unrated / Other

Insight:
Mature-rated content dominates Netflix’s catalog, indicating a strong focus on adult audiences.

⏱️ Movie Duration Analysis

Average movie duration: ~99.6 minutes

Trend (2017–2021):

Slight decrease around 2019–2020

Minor rebound in 2021

Insight:
Recent Netflix movies tend to be slightly shorter, though the trend remains relatively stable overall.

🧠 Key Analytical Takeaways

Movies significantly outnumber TV Shows

Content production accelerated rapidly after 2016

Mature content is the dominant rating group

The U.S. and India are major production hubs

Movie durations remain within standard cinematic ranges

📊 Data Visualization (Python)

Visualizations were created using Matplotlib:

Movies vs TV Shows
→ Movies clearly dominate the catalog.

Titles Added Per Year
→ Sharp growth after 2015.

Top 10 Countries
→ U.S. leads by a wide margin.

Content Ratings Distribution
→ Mature content is most prevalent.

Movie Duration Histogram
→ Most movies fall between 80–120 minutes.

📊 Power BI Dashboard Project
🎯 Objectives

Analyze content growth over time

Compare Movies vs TV Shows

Simplify ratings for clarity

Identify peak growth periods

Apply forecasting techniques

Deliver executive-level insights

## 📄 Power BI Dashboard (PDF)

A static export of the Power BI dashboard is available for quick review:

➡️ [Download Netflix Power BI Dashboard (PDF)](powerbi/screenshots/netflix_dashboard.pdf)

This PDF provides a snapshot of:
- Key KPIs
- Content growth trends
- Rating distribution
- Country contribution
- Forecast insights


📈 Dashboard Components
🔹 KPIs

Total Titles

Movies Count

TV Shows Count

Average Movies Added Per Year

Average TV Shows Added Per Year

Best Year for Content Growth

🔹 Visuals

Content Growth Over Time (Line Chart)

Movies vs TV Shows Share (Donut Chart)

Rating Group Distribution

Top Countries by Content Volume

3-Year Forecast Projection

🔮 Forecast & Strategic Insight

Using Power BI’s built-in forecasting:

Key Observations:

Strong expansion between 2017–2020

Peak year: 2019

Recent years indicate growth stabilization

🧠 Executive Forecast Insight

Netflix experienced rapid content expansion between 2017 and 2020, reaching a peak in 2019.
Forecast trends suggest a transition toward selective, quality-driven content investments rather than volume-based growth.

⭐ Final Business Questions — Answers
❓ What patterns do you observe in Netflix content growth?

Netflix transitioned from slow early growth to rapid expansion after 2015, peaking around 2019, followed by stabilization indicating market maturity.

❓ What types of content dominate the platform?

Movies dominate by volume, while TV Shows represent a strategic focus for long-term engagement and retention.

❓ How has Netflix’s content strategy changed over time?

Netflix shifted from licensing to aggressive content expansion, then moved toward a more selective, quality-focused strategy after 2020.

❓ What insights could guide future content investments?

Prioritize high-performing content categories

Invest selectively in TV Shows

Expand internationally with quality control

Balance mature and teen-oriented content

⭐ Final Insight Question

What trends can be identified over time, and how do content type, rating, and country contribute?

Answer:
Netflix evolved from gradual growth to rapid expansion, peaking in 2019. Movies remain dominant in volume, TV Shows drive engagement, mature and teen content lead production, and the U.S. remains the primary contributor with increasing international diversification.

🛠 Tools Used

Python (pandas)

SQLite (SQL)

Power BI Desktop

DAX

Forecast Analytics

✅ Project Outcome

This project delivers a complete analytical workflow combining data engineering, business analysis, and predictive insights, suitable for academic evaluation, professional portfolios, and executive decision support.

👤 Author

Sabri Hamdaoui
MBA – Data Analytics