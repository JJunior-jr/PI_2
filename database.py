from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import enum

# Carregar variáveis do arquivo .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Configuração do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Enum para o perfil de usuário
class PerfilEnum(enum.Enum):
    administrador = "administrador"
    usuario = "usuario"

# Enum para status do equipamento
class StatusEnum(enum.Enum):
    disponivel = "disponivel"
    indisponivel = "indisponivel"

# Definir o modelo Usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    telefone = db.Column(db.String(20))
    senha = db.Column(db.String(255), nullable=False)
    perfil = db.Column(db.Enum(PerfilEnum), nullable=False)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Definir o modelo Equipamento
class Equipamento(db.Model):
    __tablename__ = 'equipamento'
    equipamento_id = db.Column(db.Integer, primary_key=True, index=True)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    wifi_ip_address = db.Column(db.String(15), nullable=False)
    coldre = db.Column(db.Boolean, default=False)
    alca = db.Column(db.Boolean, default=False)
    touch = db.Column(db.Boolean, default=False)
    som = db.Column(db.Boolean, default=False)
    vibracao = db.Column(db.Boolean, default=False)
    gatilho = db.Column(db.Boolean, default=False)
    laser = db.Column(db.Boolean, default=False)
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.disponivel)
    observacao = db.Column(db.String)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    atualizado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Definir o modelo Responsavel
class Responsavel(db.Model):
    __tablename__ = 'responsavel'
    responsavel_id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Definir o modelo Manutencao
class Manutencao(db.Model):
    __tablename__ = 'manutencao'
    manutencao_id = db.Column(db.Integer, primary_key=True, index=True)
    equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamento.equipamento_id'))
    data_saida = db.Column(db.Date, nullable=False)
    data_retorno = db.Column(db.Date)
    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.responsavel_id'))
    descricao = db.Column(db.String)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Definir o modelo Emprestimo
class Emprestimo(db.Model):
    __tablename__ = 'emprestimo'
    emprestimo_id = db.Column(db.Integer, primary_key=True, index=True)
    equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamento.equipamento_id'))
    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.responsavel_id'))
    data_saida = db.Column(db.Date, nullable=False)
    data_retorno = db.Column(db.Date)
    status_retorno = db.Column(db.String(20), default='pendente')
    observacao = db.Column(db.String)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Definir o modelo HistoricoMovimentacao
class HistoricoMovimentacao(db.Model):
    __tablename__ = 'historico_movimentacao'
    movimentacao_id = db.Column(db.Integer, primary_key=True, index=True)
    equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamento.equipamento_id'))
    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.responsavel_id'))
    data_retirada = db.Column(db.Date, nullable=False)
    data_devolucao = db.Column(db.Date)
    observacao = db.Column(db.String)
    status = db.Column(db.String(20), default='em uso')
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()
