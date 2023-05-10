from st_pages import Page,  Section, show_pages, add_indentation

add_indentation()
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages([
        Page("pages/title.py", "Home"),
        Page("pages/introduction_trends.py", "Introduction and Trends"),
        Page("pages/objectives_methodology_scopes.py", "Objectives, Methodology, and Scopes and Limitations"),
        Page("pages/data_extraction_eda_ml.py", "Data Extraction, EDA and Machine Learning"),
        Page("pages/recommender_engine.py", "Recommender Engine"),
        Page("pages/conclusion.py", "Conclusion"),
        Page("pages/final_thoughts.py", "Final Thoughts")
    ]
)

