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

## Pergunta 1: Qual é o objetivo? {#case-question-1-what-is-the-goal}

O objetivo do StyleRyde é simples: eles querem que os usuários chamem corridas de táxi pelo app.

## Pergunta 2: Quais são as etapas para alcançar esse objetivo após a instalação do app? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. O StyleRyde precisa que os usuários comecem o processo de registro e preencham suas informações pessoais.
2. O StyleRyde precisa que os usuários completem e verifiquem o processo de registro inserindo um código no app que recebem por SMS.
3. O StyleRyde precisa que os usuários tentem chamar um táxi.
4. O StyleRyde precisa estar disponível quando os usuários chamam um táxi.

Essas ações poderiam então ser marcadas como os seguintes eventos personalizados:

- Início do registro
- Registro concluído
- Chamadas de táxi bem-sucedidas
- Chamadas de táxi malsucedidas

Após implementar os eventos, o StyleRyde pode executar campanhas incluindo o seguinte:

1. Enviar mensagens aos usuários que iniciaram o registro, mas não o concluíram dentro de um determinado período.
2. Enviar mensagens de parabéns aos usuários que concluíram o registro.
3. Enviar desculpas e crédito promocional aos usuários que tiveram chamadas de táxi malsucedidas, que não foram seguidas por uma chamada de táxi bem-sucedida dentro de um determinado período.
4. Enviar promoções aos usuários avançados com muitas chamadas de táxi bem-sucedidas para agradecê-los pela fidelidade.

## Pergunta 3: Que outras informações do usuário poderíamos coletar e usar para orientar nosso envio de mensagens? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- Os usuários têm algum crédito promocional?
- A avaliação média que os usuários dão aos seus motoristas?
- Códigos de promoção exclusivos para usuários?

Essas características poderiam então ser marcadas como os seguintes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Classificação média do motorista (tipo inteiro)
- Código de promoção exclusivo (tipo string)

Esses atributos permitem que você envie campanhas para usuários, como:

1. Lembrar os usuários que não usaram o app nos últimos sete dias e têm crédito promocional em sua conta para retornar ao app e usar o crédito.
2. Usar nossos modelos de mensagens e [recursos de personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) para arrastar o atributo de código de promoção exclusivo para o envio de mensagens direcionadas aos usuários.

{% alert important %}
A Braze vai banir ou bloquear usuários ("usuários fictícios") com mais de 5.000.000 de sessões e não vai mais ingerir seus eventos de SDK, porque geralmente são resultado de uma integração incorreta. Se você descobrir que isso aconteceu com um usuário legítimo, fale com seu gerente de conta da Braze.
{% endalert %}