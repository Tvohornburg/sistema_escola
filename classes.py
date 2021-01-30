
class Questao():

    def __init__(self, ni = "" , pergunta = "", resposta_certa = "", peso = 1):
        self.ni = ni
        self.pergunta = pergunta
        self.resposta_certa = resposta_certa
        self.peso = peso


        self.dic_questao = {

            "id questao": self.ni,
            "pergunta": self.pergunta,
            "resposta certa": self.resposta_certa,
            "peso questao": self.peso

        }



    def mudar_peso(self,peso_novo):
        self.peso = peso_novo


    

class Prova():
    
    def __init__(self, ni = "", questoes = []):
        
        self.ni = ni
        self.questoes = questoes
        self.peso_total = 1
        
        self.dic_prova = {

            "id questao": self.ni,
            "questoes": self.questoes,
            "peso prova": self.peso_total

        }
        

    def adicionar_questao(self,questao):                         
        if len(self.questoes) < 10:
            self.questoes.append(questao)

        else:
            return False
        
         
    def calcular_peso(self):
        peso = 0
        for i in self.questoes:           
            peso += int(i.peso)
            
            
        if peso <= 10 and peso >=1:
            self.peso_total = peso
            return peso

        else:
            return "O peso Máximo é 10"

    


            


class Aluno():

    def __init__(self, matricula = "", nome = "", media = "", provas = [], respostas = []):
        self.matricula = matricula
        self.nome = nome
        self.media = media
        self.respostas = respostas
        self.provas = provas
        self.notas_provas = []

        self.dic_aluno = {

            "matricula": self.matricula,
            "nome": self.nome,
            "media": self.media,
            "provas": self.provas,
            "respostas": self.respostas


        }
        

    def adicionar_prova(self,prova):
        self.provas.append(prova)

    def adicionar_resposta(self,resposta):
        self.respostas.append(resposta)


    def str_para_int(self):
        for i in self.provas:
            i.ni == int(i.ni)

    def calcular_media(self):
        try:
            self.media = sum(self.notas_provas)/len(self.provas)
        except:
            pass
                

    


    def Ver_questao_certo_prova(self,id_prova,id_questao):
        for i in self.provas:
            if int(i.ni) == int(id_prova):
                prova_escolhida = i    
                for x in i.questoes:                
                    if int(x.ni) == int(id_questao):
                        questao_escolhida = x
    
        for i in self.respostas:
            if int(prova_escolhida.ni) == int(id_prova) and int(questao_escolhida.ni) == int(id_questao):
                resposta_escolhida = i
        
        if str(resposta_escolhida.resposta) == str(questao_escolhida.resposta_certa):
            resposta_escolhida.mudar_status()
            self.mudar_nota(resposta_escolhida)

                        
    def mudar_nota(self,resposta):
        if resposta.status == True:            
            resposta.nota = int(resposta.peso)
            
            

    def calcular_nota_prova(self,id_prova):     
        soma = 0
        for i in self.respostas:
            if int(i.id_prova) == int(id_prova):
                soma = soma + int(i.nota)

        self.notas_provas.append(soma)
        




class Resposta():

    def __init__(self, id_prova = "", id_questao = "", resposta = "", peso = "" ,status = ""):
        self.resposta = resposta
        self.id_prova = id_prova
        self.id_questao = id_questao
        self.status = status
        self.peso = peso
        self.nota = 0
        
        self.dic_resposta = {

            "id prova": self.id_prova,
            "id questao": self.id_questao,
            "peso": self.peso,
            "resposta": self.resposta,
            "status": self.status

        }


    def mudar_status(self):
        if self.status == False:
            self.status = True
            return self.status
        

       