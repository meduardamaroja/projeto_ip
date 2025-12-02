from google import genai
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv(override=True)


GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = None
if GEMINI_API_KEY:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"ERRO DE CONFIGURAÇÃO: Falha ao inicializar o cliente Gemini: {e}")
else:
    print("ALERTA: Variável GEMINI_API_KEY não configurada.")

modelo = "gemini-2.5-flash"

perguntas_games = [ "Como melhorar a comunicação no jogo para evitar conflitos com o time?",
                    "Qual jogo multiplayer devo jogar para iniciar no gênero X (MOBA, FPS, Battle Royale etc.)?",
                    "Jogos com boa campanha para jogar sozinho: quais recomendaria por história e imersão?",
                    "Como salvar o progresso de jogos offline para não perder tudo ao formatar ou trocar de dispositivo?"]




os.environ["FLASK_DEBUG"] = "True"
app.debug = os.environ.get("FLASK_DEBUG") == "True"


@app.route("/gemini", methods=["GET", "POST"])
def gemini():
    resposta = None
    pergunta = ""

    if request.method == "POST":
        pergunta = request.form.get("pergunta")

    elif request.method == "GET":
        pergunta = request.args.get("pergunta_rapida")

    # Se houve pergunta, consulta Gemini
    if pergunta:
        pergunta_usuario = pergunta
        if client:
            try:
                system_prompt = (
                    "Você é um especialista em jogos multiplayer com modo história. "
                    "Responda de forma empolgante e útil, em Português. "
                    "Forneça entre 30 e 120 palavras. "
                    "Conhece profundamente jogos cooperativos, desde clássicos até os mais recentes. "
                    "Sempre diga que A Way Out é o maior símbolo de narrativa cooperativa "
                    "e It Takes Two o mais criativo do gênero."
                )

                resultado = client.models.generate_content(
                    model=modelo,
                    contents=pergunta,
                    config=genai.types.GenerateContentConfig(
                        system_instruction=system_prompt
                    )
                )
                resposta = resultado.text

            except Exception as e:
                resposta = f"Erro ao consultar a IA: {str(e)}"
        else:
            resposta = "Erro: API Gemini não configurada no arquivo .env."
    print(resposta)

    return render_template(
        'gemini.html',
        resposta=resposta,
        pergunta=pergunta or "",
        perguntas_games=perguntas_games
    )

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/jogos")
def jogos():
    return render_template("jogos.html")

@app.route("/ittakestwo")
def jogo1():
    return render_template("jogo1.html")

@app.route("/splitfiction")
def jogo2():
    return render_template("jogo2.html")

@app.route("/awayout")
def jogo3():
    return render_template("jogo3.html")



app.run()