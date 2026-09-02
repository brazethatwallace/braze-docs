---
nav_title: Caso de uso da coleção
article_title: Caso de uso da coleção
page_order: 3
page_type: reference
description: "Este artigo de referência cobre um caso de uso de coleta de dados de usuários sobre como um app de viagem por aplicativo pode decidir quais dados de usuários coletar."

---

# Caso de uso da coleção {#collection-use-case}

> Este artigo aborda um caso de uso de coleta de dados de usuários sobre como um app de viagem por aplicativo pode decidir quais dados de usuários coletar.

Vamos supor que um táxi ou app de viagem por aplicativo, chamado StyleRyde, queira decidir quais dados de usuários coletar. As seguintes perguntas e o processo de brainstorming são um ótimo modelo para suas equipes de marketing e desenvolvimento seguirem. Até o final deste exercício, ambas as equipes devem ter uma compreensão sólida sobre quais eventos e atributos personalizados fazem sentido coletar para ajudar a alcançar seu objetivo.

## Pergunta do caso 1: Qual é o objetivo? {#case-question-1-what-is-the-goal}

O objetivo da StyleRyde é simples: eles querem que os usuários chamem corridas de táxi pelo app.

## Pergunta do caso 2: Quais são as etapas para alcançar esse objetivo após a instalação do app? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. A StyleRyde precisa que os usuários iniciem o processo de registro e preencham suas informações pessoais.
2. A StyleRyde precisa que os usuários concluam e verifiquem o processo de registro inserindo no app um código recebido por SMS.
3. A StyleRyde precisa que os usuários tentem chamar um táxi.
4. A StyleRyde precisa estar disponível quando os usuários chamarem um táxi.

Essas ações podem então ser marcadas como os seguintes eventos personalizados:

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

Após implementar os eventos, a StyleRyde pode executar Campaigns que incluem o seguinte:

1. Enviar mensagens para usuários que iniciaram o registro (Began Registration), mas não concluíram o registro (Completed Registration) dentro de um determinado período.
2. Enviar mensagens de parabéns para usuários que concluíram o registro (Completed Registration).
3. Enviar pedidos de desculpas e crédito promocional para usuários que tiveram chamadas de táxi malsucedidas (Unsuccessful Taxi Hails) que não foram seguidas por uma chamada de táxi bem-sucedida (Successful Taxi Hail) dentro de um determinado período.
4. Enviar promoções para usuários frequentes com muitas chamadas de táxi bem-sucedidas (Successful Taxi Hails) para agradecer pela fidelidade.

## Pergunta do caso 3: Que outras informações do usuário poderíamos coletar e usar para orientar nossas mensagens? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- Os usuários têm algum crédito promocional?
- Qual é a avaliação média que os usuários dão aos seus motoristas?
- Códigos de promoção exclusivos para os usuários?

Essas características podem então ser marcadas como os seguintes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Avaliação média do motorista (tipo inteiro)
- Código de promoção exclusivo (tipo string)

Esses atributos permitem que você envie Campaigns para os usuários, como:

1. Lembrar usuários que não usaram o app nos últimos sete dias e que têm crédito promocional em suas contas para voltar ao app e usar o crédito.
2. Usar nossos modelos de mensagem e [recursos de personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para inserir o atributo de código de promoção exclusivo nas mensagens direcionadas aos usuários.

{% alert important %}
A Braze bloqueia perfis de usuário ("usuários fictícios") com mais de 5.000.000 de sessões, mais de 20.000 nomes distintos de eventos personalizados ou mais de 20.000 nomes distintos de produtos em compras, pois geralmente são resultado de uma integração incorreta. Depois que um perfil é bloqueado, a Braze para de ingerir todos os dados de entrada desse perfil, tanto dos SDKs quanto da REST or transferir estado representacional API or interface de programação do aplicativo (API). Se você perceber que isso aconteceu com um usuário legítimo, entre em contato com o gerente da sua conta Braze.
{% endalert %}