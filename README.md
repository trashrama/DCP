# DCP: Dados, Processos e Comunicação 
## 1. DCP - Implementações de S.O
>  Você fará uma implementação que lê valores de uma planilha e atualiza as notas num banco de dados SQL, sendo isso dividido em dois códigos / processos que se comunicam.

> a) No primeiro código, sua aplicação deverá ler um arquivo de uma planilha de notas feito no LibreOffice Calc (formato de arquivo ODS); exemplo de planilha: 
>  | **Matrícula** | **Nome** | **Nota** |
>|---------------|----------|----------|
>| 1324          | João     | 8        |
>| 1546          | Maria    | 9        |
>| 1285          | Pedro    | 7,5      |


 > O seu programa em Python deve ler os dados dessa planilha e então comunicar o outro processo sobre esses dados. 
 > b) O segundo código / processo deverá ser um código estilo servidor que recebe a comunicação do primeiro e então atualiza num banco de dados SQLite. Essa atualização pode ser simples: para cada aluno passado, executar um comando SQL como por exemplo:
 >  **update** alunos **set** nota=8 **where** matricula=1324;
 >   Você pode usar a biblioteca de SQLite em Python.
 >    Sugestão de código: 
 >   
>     # no cliente... import xmlrpc.client
>     # no servidor... import xmlrpc.server

Essa implementação foi bem simples. Utilizei conceitos básicos de **Python**, **xmlrpc** e **SQLite**. Pra rodar, é necessário baixar alguns pacotes, você pode usar ***pip install -r requirements.txt***, ou instalar essas dependências manualmente com o *pip*, que são: **ezodf**, **lxml** e **xmlrpc**. A implementação segue o enunciado, mas há apenas uma pequena modificação do comando update, onde optei por atualizar aleatoriamente a nota *(também aleatória)* de algum aluno no Banco de Dados. Pode ser uma nota baixa, ou alta. 

*Que vontade de ser professor!*
