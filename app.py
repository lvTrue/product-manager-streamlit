import streamlit as st
import json
import os

def carregar_dados():
    if os.path.exists("data.json"):
        with open("data.json", "r") as arquivo:
            return json.load(arquivo)
    return []
        
def salvar_dados(lista):
    with open("data.json", "w") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

# Importando as classes
from models import Produto
from sistema import SistemaCadastro

# Session State

if "sistema" not in st.session_state:
    st.session_state.sistema = SistemaCadastro()

sistema = st.session_state.sistema

# Interface

side_bar = st.sidebar.selectbox(
    "Selecione a opção",
    ["Cadastrar", "Lista"]
)

# Cadastrar

if side_bar == "Cadastrar":
    st.title("Cadastrar Produto")
    
    # Inputs
    
    nome = st.text_input("Nome do produto:", key="Nome_cadastro")
    preco = st.number_input("Preço:", value=0.0, min_value=0.0, step=0.01)
    quantidade = st.number_input("Quantidade:", value=0, min_value=0, step=1)

    if st.button("Cadastrar"):
        if nome:
            produto = Produto(nome, preco, quantidade)
            if sistema.add_produto(produto):
                st.success("Produtdo cadastrado com sucesso!")
            else:
                st.error("Produto já existente!")
        else:
            st.warning("Preencha todos os campos!")
    
# Lista
    
if side_bar == "Lista":
    st.title("Lista de produtos")
    
    st.subheader("Produtos:")
    
    # Colunas
    col_nome, col_preco, col_quantidade = st.columns([2, 1, 1])
    
    with col_nome:
        st.subheader("Nome")
        
        if sistema.lista_produtos:
            for prod in sistema.lista_produtos:
                st.write(f"{prod.nome}")
        
    with col_preco:
        st.subheader("Preco")
        
        if sistema.lista_produtos:
            for prod in sistema.lista_produtos:
                st.write(f"R${prod.preco}")
        
    with col_quantidade:
        st.subheader("Quantidade")
    
        if sistema.lista_produtos:
            for prod in sistema.lista_produtos:
                st.write(f"{prod.quantidade}")
                
    # Abas da lista
    aba_remover, aba_editar = st.tabs(["Remover", "Editar"])
    
    # Aba remover
    
    with aba_remover:
        st.title("Remover produto")
        
        nome = st.text_input("Nome do produto:", key="nome_remover")
        
        if st.button("Remover"):
           if sistema.remover_produto(nome):
               st.success("Produdo removido com sucesso!")
           else:
               st.error("Produto não existe!")
               
    
    # Aba editar
    with aba_editar:
        st.title("Editar produto")
        
        nome_busca = st.text_input("Nome do produto:", key="nome_busca")
        
        if st.button("Editar"):
            produto = sistema.editar_produto(nome_busca)
            
            if produto:
                st.subheader(f"Opções")
                st.success("Produto encontrado!")

                # Novos inputs
                with st.form("novo_form_editar"):
                    novo_nome = st.text_input("Nome do produto:", key="nome_editar", value=produto.nome)
                    novo_preco = st.number_input("Preço:", min_value=0.0, step=0.01, key="preco_editar", value=float(produto.preco))
                    nova_quantidade = st.number_input("Quantidade:", min_value=0, step=1, key="quantidade_editar", value=int(produto.quantidade))
                    
                    salvar = st.form_submit_button("Enviar dados")
                    
                if salvar:
                    produto.nome = novo_nome
                    produto.preco = novo_preco
                    produto.quantidade = nova_quantidade
                    st.success("Produto editado com sucesso!")
            else:
                st.error("produto não encontrado!")
                    
                
    