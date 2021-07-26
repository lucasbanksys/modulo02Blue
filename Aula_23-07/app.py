# importando as funções da biblioteca flask
from flask import Flask, render_template, redirect, request

#importando funções da biblioteca flask
from flask_mail import Mail, Message
# https://myaccount.google.com/lesssecureapps (lembrar de ativar)

# instanciando o aplicativo em flask
app = Flask(__name__)

# armazenando as configurações numa variável
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'makeeeszzz@gmail.com',
    "MAIL_PASSWORD": 'Checkers333@'
}

# passando as configurações da variável mail_settings para o app (que também foi criado)
app.config.update(mail_settings)

# utilizando a função Mail no app criado
mail = Mail(app)

class Contato:
    def __init__ (self, nome, email, mensagem):
        self.nome = nome;
        self.email = email;
        self.mensagem = mensagem;

@app.route('/send', methods=['POST'])

def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )

        msg = Message(
            subject="Contato do seu portfólio",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],
            body=f"""{formContato.nome} enviou a seguinte mensagem:

            {formContato.mensagem}"""
        )
        mail.send(msg)
        return render_template("send.html", formContato = formContato)

# rota principal (toda rota precisa ter uma funcao)
@app.route('/')
def index(): 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)