from flask import Flask, request, jsonify
from flask_cors import CORS
from functions.scrapers import find_linkedin, simple_prompt, short_company_inf

app = Flask(__name__)
CORS(app)

@app.route('/process-formulas', methods=['POST'])
def process_formulas():
    data = request.get_json()
    results = []
    
    for formula in data['formulas']:
        result = {
            'sheet': formula['sheet'],
            'position': formula['position'],
            'value': process_formula(
                formula['formula'], 
                formula['args']
            )
        }
        results.append(result)
    
    return jsonify({'results': results})

def process_formula(name, args):
    try:
        if name == 'CUSTOM_FORMULA1':
            return find_linkedin(args[0], args[1])
        elif name == 'CUSTOM_FORMULA2':
            return short_company_inf(args[0])
        elif name == 'CUSTOM_FORMULA3':
            return simple_prompt(args[0])
        else:
            return 'Unknown formula'
    except Exception as e:
        return f'Error: {str(e)}'

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
