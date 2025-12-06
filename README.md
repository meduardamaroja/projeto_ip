# 🎮 WikiGames — Aplicação Flask com Integração à IA Gemini

Este projeto é uma aplicação web desenvolvida em **Python + Flask**, criada como parte da disciplina de *Introdução à Programação* na UNIESP.  
O site funciona como uma plataforma informativa sobre jogos cooperativos e inclui uma **integração completa com IA generativa (Google Gemini)**, permitindo que o usuário faça perguntas e receba recomendações em tempo real.

---

## 🚀 Funcionalidades Principais

### 🔹 Catálogo de Jogos Cooperativos
- Página inicial apresentando o projeto.
- Listagem de jogos com filtros dinâmicos (Aventura, Narrativa, Co-op, Ação).
- Cards com imagem, descrição, categorias e link para detalhes.
- Páginas individuais com informações completas sobre:
  - **It Takes Two**
  - **Split Fiction**
  - **A Way Out**

---

## 🔹 Integração com IA (Gemini)

O site possui um chatbot funcional integrado ao modelo **gemini-2.5-flash**.

### Recursos implementados:
- Respostas em tempo real via API.
- System prompt especializado em jogos cooperativos.
- Sugestões de perguntas rápidas.
- Tratamento de erros avançado (API Key inválida, vazamento ou não configurada).
- Registros detalhados via `logging`.

Exemplo da chamada ao modelo:

```python
resultado = client.models.generate_content(
    model=modelo,
    contents=pergunta,
    config=genai.types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)
resposta = resultado.text

## 🧠 Aprendizados Técnicos

Durante o desenvolvimento, foram explorados conceitos como:

- Roteamento e views no Flask  
- Templates modulares com Jinja2  
- Integração com APIs externas  
- Configuração e proteção de variáveis de ambiente  
- Tratamento robusto de exceções  
- Comunicação entre front-end e back-end  
- Boas práticas de organização em aplicações web  

---

## 🔧 Tecnologias Utilizadas

- **Python 3**  
- **Flask**  
- **Jinja2**  
- **Google Gemini (google-genai)**  
- **HTML5 / CSS3**  
- **Bootstrap 5**  
- **dotenv**  
- **Logging**  

---

## 👨‍💻 Equipe de Desenvolvimento

- **Gabriel Mendonça** — integração com API Gemini, testes e ajustes finais  
- **Jayne Chaves** — front-end e conteúdo  
- **Maria Eduarda Maroja** — back-end e estruturação das rotas  

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos —  
**Introdução à Programação | Sistemas para Internet | UNIESP.**
