import sys; sys.dont_write_bytecode = True # prevent creation __pycache__ folder
from flask import Flask, request, jsonify
from flask_cors import CORS  # Enables cross-origin requests
from llm_integration.llm_query import queryLLM_to_JSON

app = Flask(__name__)
CORS(app)  # Allows all origins; you can restrict this if needed

@app.route('/backend/endpoint', methods=['POST'])
def process_code():
    data = request.get_json()

    if not data or 'code' not in data:
        return jsonify({'error': 'No code provided'}), 400

    user_text = data['code']
    article_analysis, relevant_articles = queryLLM_to_JSON(user_text)

    # After getting article_analysis from queryLLM_to_JSON
    highlights = [a.get('sentence', '') for a in article_analysis]
    categories = [a.get('category', 'unknown') for a in article_analysis]

    return jsonify({
        'highlights': highlights,
        'truthy': ["Quality of info: " + cat for cat in categories],
        'article': relevant_articles
    })

if __name__ == '__main__':
    app.run(debug=True)