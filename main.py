from flask import Flask, render_template, request
from engine.forward_chain import forward_chaining
from knowledge_base import SYMPTOMS,FRAMES
import re

app = Flask(__name__)


def validate_input(input_string, pattern):
    return re.match(pattern, input_string)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward', methods=['GET', 'POST'])
def forward():
    hasil = []
    gejala_terpilih = []
    
    
    
    if request.method == 'POST':
        gejala_terpilih = request.form.getlist('gejala')
        
        for symptom in gejala_terpilih:
            if not validate_input(symptom, r'^G\d{2}$'):
                return render_template('forward.html', 
                                       gejala=SYMPTOMS, 
                                       error="Format kode gejala tidak valid")
        
        hasil = forward_chaining(gejala_terpilih)

    return render_template('forward.html', 
                           gejala=SYMPTOMS, 
                           hasil=hasil,
                           gejala_terpilih=gejala_terpilih)

if __name__ == '__main__':
    app.run(debug=True)