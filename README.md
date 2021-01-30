# sistema_escola
Me empolgei fazendo o sistema, e acabei fazendo coisas a mais, foi meu primeiro sistema "completo", o que fazia no tecnico era geralmente partes, então foi uma experiencia nova, o sistema está bem bagunçado pois como falei é a primeira vez fazendo um sisteminha, e conforme avançando no desemvolvimento aprendia coisas novas e queria refazer algumas partes. Demorei aproximadamente 30 horas para o desemvolvimento, pois não estava satisfeito e sempre voltava para refazer algo, mas ainda não estou satisfeito, mas chegou no tempo limite.


Para o desenvolvimento do sistema utilizei a linguagem de programação python, o qual estou mais habituado, e as bibliotecas flask e json. 
para instalar python, você pode acessar o site oficial do python https://www.python.org, e para o download das bibliotecas utilizei pip, é só digitar pip install "nome_biblioteca" no terminal. 

OBS: todas as explicações começam na página inicial.

Para executar o programa basta executar o arquivo "servidor.py", e precionar e segurar ctrl e clicar em um "link" que abre no terminal depois de executar o arquivo, ele vai abrir uma pagina web no seu navegador padrão, irá aparecer uma tela com links cada um para cadastrar ou vizualizar algo, o primeiro é cadastrar questões, clique no link vai abrir outra pagina mostrando todas as questões cadastradas, se quiser cadastrar, clique no link cadastrar questões, vai abrir outra pagina com um fomulário pedindo a pergunta e a resposta, a resposta pode ser apenas "abc" ou um texto, mas para facilitar o funcionamento do cadastro das respostas dos aluno é recomendável ser apenas uma letra ou número.

Para adicionar uma questão à uma prova, deve clicar no link questões, e logo clicar em adicionar questão a prova, abrindo uma pagina com uma entrada, para digitar em qual prova quer adicionar, novamete recomendo apenas uma letra ou número, serão geradas 3 possíveis "respostas", que foi adicionada em uma prova nova ou que foi adionada ou que essa questão ja foi adionada nessa prova, para questões de teste ja existe 4 questões, onde a pergunta e resposta são iguais.

Para cadastrar um aluno é apenas clicar em Alunos, abre uma tela pedindo a matricula, se o aluno ja foi cadastrado digite a matricula dele, e vai levar para uma pagina mostrando as provas realizadas, média e um link para poder cadastrar as respostas para aquela prova, abre um formulário onde vc coloca as respostas para as questões. Para cadastrar um aluno apenas clique no link cadastrar aluno, e ele vai pedir apenas o nome dele, a matricula é gerada automaticamente de 1 a máximo definido por uma variável na lina 76 no arquivo servidor.py, nome v_controle_quantidade, para questões de testes basta diminuir essa variável.

Para visualizar uma prova ela deve ser cadastrada no link questões, mas para teste ja existe a prova 1 e prova 2, do inicio, clique no link provas, vai aparecer uma entrada, onde vc deve colocar qual prova acessar, no caso "1" e "2" ja existem, se quiser mudar o peso da questão, apenas aperte mudar peso, digite um valor válido, positivo, e o total da prova deve ser menor igual a 10. caso queira adicionar essa prova à um aluno, clique no link adicionar prova ao aluno, novamente perguntando qual aluno adicionar, digite a matricula dele, caseo não exista vai abrir uma mensagem de que ele não foi cadastrado, se sim aparece uma mensagem que foi cadastrado.

E para visualizar os alunos aprovados, basta clicar em aprovados, vai abrir uma página com todos os aprovados com a média maior ou igual a 7,0. 

OBS: Infelizmente não consegui administrar o meu trabalho, faculdade/cursos, com o desenvolvimento do programa, mas descobri o que eu quero fazer, então foi muito positivo essa experiência. Próximo projeto um jogo
