## 🤖 AI Vision Agent – Security Made Human -  *_Em progresso_*

> Um Agente de Segurança Inteligente baseado em IA e Visão Computacional que age como um colega atencioso — ajudando colaboradores a manterem bons hábitos de segurança sem punição, apenas pequenos empurrões gentis.

---
##  *_Em progresso_*  
Para concluir esse projeto, é necessário realizar algumas partes separadas e depois juntar tudo.
* Criar o conceito do projeito:  Concluído  
Essa parte é a "idéia" de como a IA vai interagir com os users, receber e enviar respostas. Temos a escolha de um app/programa com interface gráfica local ou cloud, porém vamos utilizar cloud. Isso significa que o programa ficara hospedado no HuggingFace mas tem a opção de ser baixado e utilizado localmente, sendo de escolha do user se a IA vai utilizar internet ou não.
* Escolha do modelo de IA:  
  O modelo escolhido durante o desenvolvimento pode mudar, pelo simples motivo de que alguns modelos oferecem melhor suporte para o trabalho designado.
  Enquanto alguns modelos são treinados com uma variação gigantesca de imagens, esse programa não precisa de tantas imagens, pois já definido o ambiente e os objetos a serem detectados.
* Objetos que serão detectáveis:   
Para tornar as coisas simples, esses são os objetos que a IA detectará: Crachá, celular, notebook, computador, bolsas, sacolas, papel, caneta, lápis, dispositivos eletrônicos. A lista de dispositivos eletrônicos pode ser pequena ou ugrande mas para esse projeto teste, apenas uma pequena quantidade de dispositivos eletrônicos será utilizada para reconhecimento e ainda está em definição quais.
* E depois?  
  Após a identificação, é gerado um registro com hora, data e identificação da câmera que filmou.
  É necessário revisar os registros por humanos, pois toda IA pode aluucinar e registrar informações incorretas.
* Interface:
  Duas interfaces, uma para o funcionário do departamento de câmeras e outra interface para os funcionários operacionais.
  Os registros serão enviados apenas para o user responsável pelas câmeras.

## Progresso do projeto  
* A interface para o user responsável já está feita, porém ainda faltam os logs e um modelo ajustado para detectar os crachás.
Foram utilizados modelos existentes de primeira parte porém criei um modelo do zero para não incluir imagens que não serão utilizadas nesse cenários (animais, gravata, veículos) reduzir o processamemto de imagens e tornar o programa mais leve, evitando o processamento de imagens desnecessárias.

## O que falta?
* Criar a interface do user oepracional
* Refinar novamente uma IA com a lista de correta de objetos
* Upar a versão amigável para os funcionários operacionais (isso é fácil, qualquer IA pode te dar um prompt para esse "agente" ou assistente). Não fiz ainda pois a interface do user precisa estar em concordância com a interface do user responsável.
* Seu patriocinio: Com sua ajuda consigo terminar mais rápido esse projeto e forcecer mais informações de forma privada sobre como implementar o projeto na sua empresa.
  

## 📌 Sobre o Projeto - *_Em progresso_*

A maioria dos incidentes de segurança começa com um “ops”, não com más intenções.  
Ferramentas tradicionais de compliance costumam ser intrusivas e punitivas, focadas em punir erros em vez de preveni-los.

Por isso, estou construindo uma abordagem diferente:  
👉 um **Agente de Segurança baseado em IA** que detecta situações de risco e ajuda discretamente — antes que virem incidentes.

---

### ✨ Funcionalidades (Protótipo)

Atualmente, o agente:
- 🔍 Detecta objetos básicos como **laptops**, **janelas**, **portas**
- 📷 Analisa imagens recebidas e retorna elementos visíveis
- 🧠 Estruturado para escalar para:
  - Desfoque automático de documentos sensíveis
  - Bloqueio de tela via notificação discreta
  - Alertas privados no Slack/Teams

---

### 🎯 Resultados Esperados

- 🤖 **92% das situações resolvidas automaticamente**
- 🎯 **100% de aprovação em auditorias em 6 meses**
- 💡 **70% menos treinamentos repetitivos**

---

### 🔄 Exemplo de Fluxo de Trabalho

1. **Laptop deixado aberto na sala de café**  
   → Tela bloqueada automaticamente + mensagem no Slack:  
   _"Já fechei pra você! 🔒"_

2. **Documento sensível à mostra**  
   → Desfoque inteligente + notificação por email:  
   _"Guarde esse arquivo no Gabinete A!"_

3. **Visitante em área restrita**  
   → Notificação silenciosa para segurança:  
   _"Precisa de ajuda com esse acesso?"_

---

### 🚀 Como Testar

Você pode testar uma versão visual do agente no Hugging Face:

👉 [Security AI Agent Vision](https://huggingface.co/spaces/ThiSecur/security-ai-agent)  
* Em breve, disponibilizo o repositório completo no GitHub para rodar localmente e integrar com sistemas corporativos.  
* Essas duas versões ainda não estão com versão "gentle" e estão sem Supervised fine-tuning (SFT)   
* Em breve posto os resultados   
* Estou aceitando colaboração no projeto ou patrocionio, contatos abaixo  

---

### 🤝 Quer Conversar?

Me chama se você:  
🔹 É líder de equipe cansado de compliance chata   
🔹 É recrutador buscando talentos em **IA + segurança centrada no ser humano**   
🔹 Ou simplesmente ama tecnologia que **respeita as pessoas**  

📧 Contato:  
💼 LinkedIn: https://www.linkedin.com/in/thiago-cequeira-99202239/  
🧑‍💻 GitHub: https://github.com/ThiagoMaria-SecurityIT/  
🤗 Hugging Face: https://huggingface.co/ThiSecur
