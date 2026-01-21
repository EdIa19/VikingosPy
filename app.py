from flask import Flask, render_template, jsonify

app = Flask(__name__)

SALSA_OPCIONES = ["Verde", "Roja", "Sin salsa"]
VERDURA_OPCIONES = ["Cilantro", "Cebolla", "Cilantro y cebolla", "Sin verdura"]

MENU_VIKINGO = {

    # ---------------- TACOS ----------------
    "Tacos": [
        {
            "n": "Taco sencillo",
            "descripcion": "Taco tradicional con tortilla de maíz",
            "p": 20,
            "opciones_carne": ["Pastor", "Suadero", "Longaniza", "Bistec"],
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Taco con queso",
            "descripcion": "Taco con queso gratinado",
            "p": 40,
            "opciones_carne": ["Pastor", "Suadero", "Longaniza", "Bistec"],
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Taco de tripa",
            "descripcion": "Tripa bien dorada",
            "p": 27,
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Taco de cabeza",
            "descripcion": "Cabeza suave y bien sazonada",
            "p": 25,
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        }
    ],

    # ---------------- TORTAS ----------------
    "Tortas": [
        {
            "n": "Torta sencilla",
            "descripcion": "Bolillo crujiente con carne a elegir",
            "p": 80,
            "opciones_carne": ["Pastor", "Longaniza", "Suadero", "Bistec"],
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Torta con queso",
            "descripcion": "Torta con queso derretido",
            "p": 90,
            "opciones_carne": ["Pastor", "Longaniza", "Suadero", "Bistec"],
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Torta Vikinga",
            "descripcion": "Pastor, bistec, pollo, frijol y verduras",
            "p": 110,
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        }
    ],

    # ---------------- QUESOS ----------------
    "Quesos": [
        {
            "n": "Quesadilla",
            "descripcion": "Tortilla con queso fundido",
            "p": 60,
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Gringa",
            "descripcion": "Tortilla de harina con queso y carne",
            "p": 110,
            "opciones_carne": ["Pastor", "Bistec", "Suadero"],
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        },
        {
            "n": "Costra de queso",
            "descripcion": "Queso dorado con carne a elegir",
            "p": 120,
            "opciones_carne": ["Pastor", "Bistec", "Chorizo"],
            "salsa": SALSA_OPCIONES,
            "verdura": VERDURA_OPCIONES
        }
    ],

    # ---------------- HAMBURGUESAS ----------------
    "Hamburguesas": [
        {
            "n": "Hamburguesa tradicional",
            "descripcion": "Jamón, tocino, queso Oaxaca y aderezos",
            "p": 90
        },
        {
            "n": "Hamburguesa hawaiana",
            "descripcion": "Jamón, tocino, piña y queso",
            "p": 100
        }
    ],

    # ---------------- ENTRADAS ----------------
    "Entradas": [
        {
            "n": "Frijoles charros",
            "descripcion": "Frijoles tradicionales estilo charro",
            "p": 40,
            "variantes": ["Sencillos", "Con queso", "Con chorizo", "Combinados"]
        },
        {
            "n": "Orden de papas",
            "descripcion": "Papas a la francesa",
            "p": 60
        },
        {
            "n": "Orden de alitas",
            "descripcion": "Alitas doradas",
            "p": 75
        }
    ],

    # ---------------- BEBIDAS ----------------
    "Bebidas": [
        {
            "n": "Refresco",
            "p": 28,
            "opciones": ["Coca-Cola", "Sidral", "Jarritos", "Manzanita"]
        },
        {
            "n": "Agua fresca 1L", # Nombre clave para el mensaje automático
        "descripcion": "Pregunta por los sabores del día",
        "p": 25
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/menu')
def get_menu():
    return jsonify(MENU_VIKINGO)

if __name__ == '__main__':
    app.run(debug=True)
