from flask import Flask, render_template, url_for, request
from flaskr.core.tables.graph import graph as gph, graph

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'DhlH@ndH3ltApp!2024#'

value_one = (
    {'chart': {'type': 'donut', 'height': 400}, 'title': {'text': 'Eqp. disponiveis por modelo', 'align': 'center'},
     'series': [5, 10, 186, 27], 'colors': ['#1C7FAD', '#458E66', '#EF8F2F', '#FC6D6D'],
     'labels': ['HAND HELD', 'ZEBRA TC21', 'HONEYWELL CT60', 'HONEYWELL EDA61K'],
     'plotOptions': {'pie': {'customScale': 0.8}}})

value_two = ({
    'series': [
        {
            'name': 'Equipamentos',
            'data': [17, 31, 108, 49, 34, 91, 123]
        }
    ],
    'chart': {
        'type': 'line',
        'zoom': {
            'enabled': 0
        },
        'height': 400
    },
    'dataLabels': {
        'enabled': 1
    },
    'stroke': {
        'curve': 'straight'
    },
    'title': {
        'text': 'Eqp. retirados em função do tempo (7 dias)',
        'align': 'center'
    },
    'xaxis': {
        'categories': [
            '20/9/2024', '21/9/2024', '22/9/2024', '23/9/2024', '24/9/2024',
            '25/9/2024', '26/9/2024'
        ]
    }
})

value_three = ({
    'series': [
        {
            'name': 'Equipamentos',
            'data': [3, 4, 7, 4, 2, 1, 3]
        }
    ],
    'chart': {
        'type': 'line',
        'zoom': {
            'enabled': 0
        },
        'height': 400
    },
    'dataLabels': {
        'enabled': 1
    },
    'stroke': {
        'curve': 'straight'
    },
    'title': {
        'text': 'Eqp. em manutenção em função do tempo (7 dias)',
        'align': 'center'
    },
    'xaxis': {
        'categories': [
            '20/9/2024', '21/9/2024', '22/9/2024', '23/9/2024', '24/9/2024',
            '25/9/2024', '26/9/2024'
        ]
    }
})

value_four = ({
    'series': [{
        'name': 'Equipamentos',
        'data': [1, 3, 16, 8]
    }],
    'chart': {
        'type': 'bar',
        'height': 400
    },
    'colors': ['#1C7FAD', '#458E66', '#EF8F2F', '#FC6D6D'],
    'plotOptions': {
        'bar': {
            'columnWidth': '55%',
            'distributed': 'true',
        }
    },
    'dataLabels': {
        'enabled': 1
    },
    'legend': {
        'show': 0
    },
    'title': {
        'text': 'Eqp. em manutenção em função da marca',
        'align': 'center'
    },
    'xaxis': {
        'categories': [['HAND', 'HELD'], ['ZEBRA', 'TC21'], ['HONEYWELL', 'CT60'], ['HONEYWELL', 'EDA61K']],
    },
})

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboardAdm')
def adm_dashboard():
    value_five = ({
        'series': [
            {
                'name': 'Equipamentos Retirados',
                'data': [17, 31, 108, 49, 34, 91, 123]
            },{
                'name': 'Equipamentos em Manutenção',
                'data': [3, 4, 7, 4, 2, 1, 3]
            },{
                'name': 'Equipamentos Disponíveis',
                'data': [5, 9, 7, 8, 13, 50, 17]
            }
        ],
        'chart': {
            'type': 'line',
            'zoom': {
                'enabled': 0
            },
            'height': 400
        },
        'colors': ['#1C7FAD', '#EF8F2F', '#458E66'],
        'dataLabels': {
            'enabled': 1
        },
        'stroke': {
            'curve': 'straight'
        },
        'title': {
            'text': 'Eqp. * em função do tempo (7 dias)',
            'align': 'center'
        },
        'xaxis': {
            'categories': [
                '20/9/2024', '21/9/2024', '22/9/2024', '23/9/2024', '24/9/2024',
                '25/9/2024', '26/9/2024'
            ]
        }
    })
    return render_template('pages/adm_dashboard.html', graph=[value_one, value_two, value_three, value_four, value_five])


@app.route('/equipamentos')
def adm_equipamentos():
    return render_template('pages/adm_equipamentos.html')


@app.route('/histRetirada')
def adm_hist_retirada():
    return render_template('pages/adm_hist_retirada.html', graph=[value_one, value_two])

@app.route('/eqpManutencao')
def adm_eqp_manutencao():
    return render_template('pages/adm_eqp_manutencao.html', graph=[value_three, value_four])

@app.route('/admUsuarios')
def adm_usuarios():
    return render_template('pages/adm_usuarios.html')


if __name__ == '__main__':
    app.run(debug=True)
