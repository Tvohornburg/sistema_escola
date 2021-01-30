from flask import Flask, render_template, request
from classes import Questao as Q, Prova as P, Aluno as A, Resposta as R
import funcoes as F

 

app = Flask(__name__)


questoes = [ 
    Q(1,1,1,4),
    Q(2,2,2,6),
    Q(3,3,3,5),
    Q(4,4,4,5)

]




provas = [
    P(1,[questoes[0],questoes[1]]),
    P(2,[questoes[2],questoes[3]])
]


alunos = [

]


respostas = [

]


               
# INICIO
@app.route("/")
def inicio():
    return render_template('inicio.html')


# APROVADOS
@app.route("/aprovados")
def mostrar_aprovados():
    alunos_aprovados= []
    for i in alunos:
        if float(i.media) >= 7.0:
            alunos_aprovados.append(i)
    
    if not alunos_aprovados:
        return render_template("mensagem.html", mensagem = "Nenhum alunos aprovado")
    
    return render_template("listar_aprovados.html", alunos = alunos_aprovados)

# ALUNO    

@app.route("/aluno")
def mostrar_aluno():
    return render_template('aluno.html')

@app.route("/form_cadastrar_aluno")
def mostrar_form_aluno():
    matricula = F.gerar_id(alunos)
    return render_template('form_cadastrar_aluno.html', matricula = matricula)


@app.route("/cadastrar_aluno")
def cadastrar_aluno():
    matricula = request.args.get("matricula")
    nome = request.args.get("nome")

    aluno_escolhido = 0

    v_controle_quantidade = 100
    if int(matricula) >= v_controle_quantidade:
        return render_template("mensagem.html", mensagem = "O máximo de alunos é 100")


    for i in range(0,len(alunos)):
        if str(alunos[i].matricula) == str(matricula):
            aluno_escolhido = 1

    if aluno_escolhido == 0:
        aluno_novo = A(matricula,nome,0,[],[])
        alunos.append(aluno_novo)

        return render_template("mensagem.html", mensagem = "Aluno Cadastrado")




@app.route("/verificar_qual_aluno")
def verificar_aluno():
    matricula = request.args.get("matricula")
    
    for i in alunos:
        for x in i.provas:
            x.calcular_peso()

        if int(i.matricula) == int(matricula):
            aluno_escolhido = i
            aluno_escolhido.calcular_media()
            
            return render_template("listar_aluno.html", aluno = aluno_escolhido)
        
        
    return render_template("mensagem.html", mensagem = "Aluno não encontrado")


     
        
# provas aluno

@app.route("/adicionar_prova_aluno")
def mostrar_form_prova():
    id_prova = request.args.get("id_prova")    
    return render_template("form_prova_aluno.html", id_prova = id_prova)

@app.route("/salvar_prova_aluno")
def salvar_prova_aluno():
    id_prova = request.args.get("id_prova")
    matricula = request.args.get("matricula")

    prova_escolhida = 0
    aluno_escolhido = 0

    for i in provas:
        if int(i.ni) == int(id_prova):
            prova_escolhida = i
            
            
    for i in alunos:           
        if int(i.matricula) == int(matricula):
            aluno_escolhido = i
            

    if aluno_escolhido != 0:
        aluno_escolhido.adicionar_prova(prova_escolhida)

        
        return render_template("mensagem.html", mensagem = "adicionado com sucesso")
    else:
        return render_template("mensagem.html", mensagem = "Aluno não cadastrado")



#Respostas Aluno 

@app.route("/adicionar_resposta_aluno")
def adicionar_resposta_aluno():
    id_prova = request.args.get("id_prova")
    matricula = request.args.get("matricula")
       
    prova_escolhida = 0

    for i in provas:
        
        if int(id_prova) == int(i.ni):
            prova_escolhida = i                 

    if prova_escolhida != 0:
        return render_template("resposta.html", matricula = matricula, prova = prova_escolhida)
    
    else:
        return render_template("mensagem.html", mensagem = "Não foi possivel achar a prova")



@app.route("/salvar_resposta_aluno")
def salvar_resposta_aluno():
    id_prova = request.args.get("id_prova")
    matricula = request.args.get("matricula")

    prova_escolhida = 0

    for i in provas:
        if int(id_prova) == int(i.ni):
            prova_escolhida = i 
    
    for i in prova_escolhida.questoes:
        resposta = request.args.get("resposta"+str(i.ni))
        if resposta != None:           
            for x in alunos:           
                if int(x.matricula) == int(matricula):
                    aluno_escolhido = x
                    resposta_nova = R(id_prova,i.ni,resposta,i.peso,False)
                    x.adicionar_resposta(resposta_nova)               
                    x.Ver_questao_certo_prova(prova_escolhida.ni,i.ni)
                    
               
    aluno_escolhido.calcular_nota_prova(prova_escolhida.ni)    

    return render_template("mensagem.html", mensagem = "Resposta cadastrada")




# QUESTÕES

@app.route("/questoes")
def listar_questoes():
    return render_template('questoes.html', lista_questoes = questoes)



@app.route("/cadastrar_questoes")
def mostrar_formulario_questoes():
    return render_template('cadastrar_questoes.html')



@app.route("/salvar_questoes")
def cadastrar_questoes():
    id_questao = F.gerar_id(questoes)
    pergunta = request.args.get("pergunta")
    resposta = request.args.get("resposta")

    questao_nova = Q(id_questao,pergunta,resposta,)
    questoes.append(questao_nova)

    return render_template("mensagem.html", mensagem = "Questão Salva")



# PROVA

@app.route("/adicionar_na_prova")
def adicionar_questao_prova():
    id_questao = request.args.get("id_questao")

    for i in questoes:
        if str(i.ni) == str(id_questao):
            questao_escolhida = i

    return render_template("adicionar_na_prova.html", pergunta = questao_escolhida.pergunta, ni = questao_escolhida.ni)



@app.route("/salvar_na_prova")
def salvar_questao_prova():
    id_prova = request.args.get("id_prova")    
    id_questao = request.args.get("id_questao")

    prova_escolhida = 0
    questao_escolhida = 0

    for i in questoes:
        if str(i.ni) == str(id_questao):
            questao_escolhida = i

    for i in range(0,len(provas)):
        if str(provas[i].ni) == str(id_prova):
            prova_escolhida =provas[i]
    

    if prova_escolhida == 0:                 
        prova_nova = P(id_prova,questoes=[questao_escolhida])        
        provas.append(prova_nova)       
        return render_template("mensagem.html", mensagem = "questão adicionada em uma prova nova")

    
    
    for x in prova_escolhida.questoes:       
        if str(x.ni) == str(id_questao):                   
            return render_template("mensagem.html", mensagem = "Questao ja foi adicionada")

        
    
    prova_escolhida.adicionar_questao(questao_escolhida)   
    return render_template("mensagem.html", mensagem = "Questao adicionada")

        

@app.route("/provas")
def mostra_provas():
    return render_template("provas.html")



@app.route("/verificar_qual_prova")
def ver_provas():
    id_prova = request.args.get("id_prova")
    prova_escolhida = 0
    for i in range(0,len(provas)):
        if str(provas[i].ni) == str(id_prova):
            prova_escolhida = provas[i]

    if prova_escolhida == 0:
        return render_template("mensagem.html", mensagem = "Prova Não Encontrada")

    
    peso_total = prova_escolhida.calcular_peso()
    
    return render_template("listar_provas.html", id_prova = id_prova, prova = prova_escolhida, peso_total = peso_total)



@app.route("/form_mudar_peso")
def mostra_form_peso():
    id_questao = request.args.get("id_questao")
    id_prova = request.args.get("id_prova")
    return render_template("form_mudar_peso.html",id_questao = id_questao,id_prova = id_prova)



@app.route("/mudar_peso")
def mudar_peso():
    id_prova = request.args.get("id_prova")
    id_questao = request.args.get("id_questao")
    novo_peso = int(request.args.get("peso"))
        
    prova_escolhida = 0
    for i in range(0,len(provas)):
        if str(provas[i].ni) == str(id_prova):
            prova_escolhida = provas[i]       
    
    if prova_escolhida != 0:
        for i in prova_escolhida.questoes:
            if str(i.ni) == str(id_questao):
                peso_antigo = int(i.peso)
                i.mudar_peso(novo_peso)
                if prova_escolhida.calcular_peso() == "O peso Máximo é 10":
                    i.mudar_peso(peso_antigo)
                    return render_template("mensagem.html", mensagem = "Peso é positivo e o máximo da prova é 10")  

                return render_template("mensagem.html", mensagem = "Peso mudado")
          



app.run(debug=True)