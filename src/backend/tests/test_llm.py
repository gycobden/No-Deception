from src.backend.llm_integration.llm_query import queryLLM_to_JSON

def test_good_categorized_text():
    article_analysis, relevant_articles = queryLLM_to_JSON(
        "We become immune to (or protected from) a disease when" +
        "our bodies create specific antibodies to fight that disease. " +
        " Vaccines contain ingredients that help your body build this immunity."
    )
    assert article_analysis == {
        "sentences": [],
        "category": "good"
    }

def test_bad_categorized_text():
    article_analysis, relevant_articles = queryLLM_to_JSON(
        "Vaccines give you cancer."
    )
    assert article_analysis == {
        "sentences": ["Vaccines give you cancer."],
        "category": "bad"
    }

# def test_no_info_categorized_text():
#     article_analysis, relevant_articles = queryLLM_to_JSON(
#         "A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects."
#     )
#     assert article_analysis == {
#         "sentences": [],
#         "category": "couldn't find relevant documents"
#     }