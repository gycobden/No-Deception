from flask import Flask, request, jsonify
from flask_cors import CORS  # Enables cross-origin requests
from llm_integration.llm_query import queryLLM_to_JSON

app = Flask(__name__)
CORS(app)  # Allows all origins; you can restrict this if needed

@app.route('/backend/endpoint', methods=['POST'])
def process_code():
    data = request.get_json()

    qreturn = queryLLM_to_JSON(data)

    if not data or 'code' not in data:
        return jsonify({'error': 'No code provided'}), 400

    code = data['code']
    
    # Example processing: count lines and return
    #processed_result = f"Received {len(code.splitlines())} lines of code:\n\n{code}"

    return jsonify({'highlight': qreturn.highlight_sentences, 'truthy': "Quality of info: " + qreturn.category, 'article': qreturn[1]})

if __name__ == '__main__':
    app.run(debug=True)
