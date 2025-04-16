from flask import Flask, render_template, jsonify # type: ignore
import random

app = Flask(__name__)

# Lista di parole per generare il contenuto
soggetti = [
    # Santi principali
    "Dio", "Madonna", "Gesù", "San Pietro", "San Paolo", "San Giuseppe", "Sant'Antonio",
    "San Francesco", "Santa Rita", "San Gennaro", "Santa Maria", "San Giovanni",
    "San Giacomo", "Santa Lucia", "San Michele", "Sant'Anna", "San Martino",
    "Santa Chiara", "San Benedetto", "San Lorenzo", "Santa Teresa", "San Nicola",
    "San Marco", "Santa Caterina", "San Domenico", "San Giovanni Battista", "San Rocco",
    # Santi moderni
    "San Pio da Pietrelcina", "San Giovanni Paolo II", "Santa Teresa di Calcutta", 
    "San Josemaría Escrivá", "Santa Gianna Beretta Molla", "San Massimiliano Kolbe",
    # Santi dottori della Chiesa
    "Sant'Agostino", "San Tommaso d'Aquino", "San Bonaventura", "Sant'Alfonso",
    "San Bernardo", "Santa Caterina da Siena", "San Giovanni della Croce",
    # Santi patroni
    "San Cristoforo", "San Biagio", "Santa Barbara", "Santa Lucia", "San Vito",
    "Sant'Agnese", "San Sebastiano", "Santa Cecilia", "San Giorgio", "Sant'Andrea",
    # Arcangeli
    "San Michele Arcangelo", "San Gabriele Arcangelo", "San Raffaele Arcangelo",
    # Altri santi popolari
    "San Filippo Neri", "San Camillo de Lellis", "Santa Rita da Cascia", 
    "San Giovanni Bosco", "Santa Bernadette", "Santa Gemma Galgani"
]

azioni = [
    # Insulti animali
    "porco", "cane", "maiale", "serpente", "verme", "ratto", "scimmia", "asino",
    "sciacallo", "iena", "avvoltoio", "corvo", "bestia", "scarafaggio", "lumaca",
    # Insulti caratteriali
    "infame", "traditore", "vigliacco", "codardo", "meschino", "subdolo", "perfido",
    "inetto", "idiota", "imbecille", "cretino", "sciocco", "fesso", "scemo",
    "maledetto", "dannato", "sciagurato", "bastardo", "viscido", "schifoso",
    # Insulti fisici
    "puzzolente", "fetido", "lurido", "sporco", "marcio", "putrido", "sudicio",
    "lercio", "bavoso", "moccioso", "caccoloso", "rognoso", "lebbroso",
    # Insulti comportamentali
    "ladro", "bugiardo", "imbroglione", "parassita", "sanguisuga", "profittatore",
    "approfittatore", "opportunista", "scroccone", "fannullone", "perdigiorno"
    # Insulti vegetali
    "erbaccia", "rovo", "cactus", "fungo", "muschio", "felce", "carciofo",
    "cavolo", "broccolo", "radice", "fungo velenoso", "erba cattiva",
    "finocchio", "carota", "cipolla", "aglio", "peperone", "zucchina",
]    

aggettivi_opzionali = [
    # Aggettivi negativi
    "puzzolente", "maledetto", "dannato", "schifoso", "lurido", "infame", 
    "viscido", "fetido", "marcio", "putrido", "sporco", "bastardo", "traditore",
    "vigliacco", "codardo", "perfido", "miserabile", "ripugnante", "disgustoso",
    "nauseabondo", "stomachevole", "repellente", "rivoltante", "ignobile",
    # Aggettivi di disprezzo
    "insignificante", "spregevole", "deprecabile", "esecrabile", "abominevole",
    "detestabile", "odioso", "ributtante", "riprovevole", "squallido", "immondo",
    # Aggettivi di derisione
    "ridicolo", "patetico", "pietoso", "misero", "meschino", "mediocre", "insulso",
    "insignificante", "incapace", "inetto", "incompetente", "fallito"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/generate')
def generate():
    soggetto = random.choice(soggetti)
    azione = random.choice(azioni)
    
    # Aumentiamo la probabilità di aggettivi extra al 40%
    if random.random() < 0.4:
        aggettivo_extra = random.choice(aggettivi_opzionali)
        risultato = f"{soggetto} {azione} {aggettivo_extra}"
    else:
        risultato = f"{soggetto} {azione}"
    
    return jsonify({"result": risultato})

@app.route('/why-this')
def why_this():
    return render_template('why-this.html')

if __name__ == '__main__':
    app.run(debug=True)