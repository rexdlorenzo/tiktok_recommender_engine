from st_pages import Page,  Section, show_pages, add_indentation

add_indentation()
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages([
        Page("pages/title.py", "Home"),
        Page("pages/introduction.py", "Introduction"),
        Page("pages/methodology.py", "Methodology"),
        Page("pages/dataset.py", "Dataset"),
        Page("pages/results.py", "Results"),
        Page("pages/recommender_engine.py", "Recommender Engine")
    ]
)

