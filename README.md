(( 🦁 VENTURE GOTCHI ))





📌 Sobre o Projeto:

 O VentureGotchi é uma plataforma web gamificada desenvolvida como projeto educacional, com foco no aprendizado prático de programação e back-end, utilizando o framework Django.

 O sistema propõe a evolução profissional do usuário por meio de um avatar virtual (Gotchi), que progride conforme o cumprimento de metas, missões e trilhas de aprendizado. O projeto foi construído por alunos iniciantes, tendo como principal objetivo consolidar os conhecimentos adquiridos em sala de aula.

Este repositório representa uma prova de conceito e uma amostra prática do aprendizado, respeitando o tempo, o escopo e o prazo definidos para a entrega.


👥 Autores do Projeto Integrador:

*Lussandro de Andrade Farias
GitHub: https://github.com/Lussandrorj2

*Miguel Gonçalves Viana
GitHub: https://github.com/VianaMiguel

*Renan Silveira Marquet
GitHub: https://github.com/Renan-Marquet


🎯 Objetivo:

° Aplicar na prática os conceitos aprendidos em programação web

° Desenvolver uma aplicação funcional em Django

° Trabalhar conceitos de back-end como models, views, templates e rotas

° Utilizar gamificação como forma de engajamento

° Demonstrar organização de projeto, versionamento e integração de apps


🧠 Conceito da Plataforma:

Na plataforma VentureGotchi:

° Cada usuário possui um avatar (Gotchi)

° O avatar evolui conforme o usuário avança em missões e metas

° O progresso é representado por níveis, XP e conquistas

° O sistema estimula constância, disciplina e evolução profissional


🛠️ Tecnologias Utilizadas:

° Python 3

° Django

° HTML5

° CSS3

° SQLite 

° Django Admin


🗂️ Estrutura do Projeto:

O projeto foi organizado em múltiplos apps para melhor separação de responsabilidades:

accounts – autenticação, usuários e perfis

gotchi – avatar, nível e sistema de XP

missions – missões diárias e semanais

achievements – conquistas e progresso

core / main – páginas principais e dashboard

Todos os apps estão integrados ao Django Admin, permitindo gerenciamento interno dos dados.


✅ Funcionalidades Implementadas:

° Estrutura base do projeto em Django

° Sistema de usuários

° Dashboard inicial

° Avatar Gotchi com nível e barra de progresso

° Sistema de missões

° Conquistas básicas em XP

° Integração de arquivos estáticos (CSS)

° Organização do projeto para futuras expansões
++ -------------------------------------------------- ++
▶️ Como Rodar o Projeto Localmente:

Siga os passos abaixo para executar o projeto em sua máquina:

1️⃣ Entrar na pasta do projeto
cd Projeto_VentureGotchi

2️⃣ Criar o ambiente virtual
python -m venv venv

3️⃣ Ativar o ambiente virtual (Windows)
venv\Scripts\activate

4️⃣ Instalar as dependências
pip install -r requirements.txt

5️⃣ Atualizar o pip (opcional, mas recomendado)
python.exe -m pip install --upgrade pip

6️⃣ Criar as migrações
python manage.py makemigrations

7️⃣ Aplicar as migrações
python manage.py migrate

8️⃣ Executar o servidor
python manage.py runserver

Após isso, acesse no navegador:

http://127.0.0.1:8000/  ou   http://127.0.0.1:8000/admin (Criando um Superusuário)

▶️ Para acesso ao admin, no terminal, dentro da pasta raiz do projeto, execute o comando:

python manage.py createsuperuser

++ -------------------------------------------------- ++
🧪 Testes Realizados:

Durante o desenvolvimento do VentureGotchi, foram realizados testes manuais e verificações funcionais com o objetivo de validar o correto funcionamento das principais funcionalidades da aplicação, garantindo estabilidade e coerência com o escopo proposto.

Por se tratar de um projeto educacional em fase inicial, os testes foram conduzidos de forma prática e incremental ao longo do desenvolvimento.

-- ++ 🔹 Testes Funcionais (Manuais):

Foram executados testes de fluxo para validar a interação entre os principais módulos do sistema, incluindo:

° Cadastro de usuário e autenticação (login/logout);

° Acesso ao dashboard após autenticação;

° Visualização do avatar Gotchi;

° Execução de missões;

° Ganho de XP após conclusão de atividades;

° Atualização do nível e da barra de progresso;

° Registro e exibição da página de conquistas básicas.

Esses testes garantiram que o fluxo principal do usuário ocorresse de forma contínua e sem falhas críticas.

-- ++ 🔹 Testes de Integração:

Foram validadas integrações entre diferentes partes do sistema, assegurando a consistência dos dados:

° Cadastro → Login → Acesso ao dashboard;

° Missão → Geração de XP → Evolução do avatar;

° Integração entre models, views e templates;

° Comunicação correta entre os apps do projeto (accounts, gotchi, missions e achievements).

-- ++ 🔹 Testes de Performance Básicos:

Embora não tenham sido utilizados frameworks específicos de benchmark, foram realizadas verificações práticas relacionadas a desempenho, tais como:

° Carregamento adequado do dashboard;

° Renderização fluida das páginas;

° Animações leves e responsivas;

° Consultas ao banco de dados compatíveis com o escopo do projeto.

++ -------------------------------------------------- ++ 
**📚 Considerações Finais:**
++ -------------------------------------------------- ++ 


 O projeto VentureGotchi foi desenvolvido como um trabalho de caráter acadêmico e formativo, aproximando-se da proposta de um Projeto Integrador, ao integrar conceitos teóricos e práticos estudados ao longo da formação.

 A construção da aplicação permitiu aos alunos vivenciar todas as etapas fundamentais do desenvolvimento de software, incluindo planejamento, organização da estrutura do projeto, implementação em back-end, integração entre componentes e testes funcionais básicos. Além disso, possibilitou o contato direto com boas práticas de programação, versionamento de código e utilização de frameworks amplamente utilizados no mercado.

 Mesmo se tratando de um projeto desenvolvido por iniciantes na área de programação e back-end, o VentureGotchi cumpre seu papel como prova de conceito, demonstrando a capacidade da equipe em aplicar os conhecimentos adquiridos de forma estruturada e coerente, respeitando o escopo, o prazo e os objetivos definidos.

 Dessa forma, o projeto estabelece uma base sólida para futuras evoluções, podendo ser expandido e aprimorado em trabalhos posteriores, inclusive como continuação ou aprofundamento em um projeto formal.