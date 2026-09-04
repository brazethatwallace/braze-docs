---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Este artigo de referência descreve a parceria entre a Braze e a Jacquard Dynamic Optimisation, que utiliza Braze Currents e Conteúdo conectado para coletar informações de rastreamento de cliques dos seus assinantes por meio de webhooks. Em seguida, a Jacquard vincula esses eventos às suas variantes de linguagem para otimização da linguagem em tempo real."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> A [Jacquard](https://www.jacquard.com/) reúne inteligência artificial, linguística computacional e um espírito de centralização no cliente para ajudar a implementar a linguagem da marca, em escala, em canais personalizados de acordo com a voz da sua marca.

A Dynamic Optimisation, alimentada pela Jacquard X, utiliza Braze Currents e Conteúdo conectado para coletar informações de rastreamento de cliques dos seus assinantes por meio de webhooks. Em seguida, a Jacquard vincula esses eventos às suas variantes de linguagem para otimização da linguagem em tempo real.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Jacquard | É necessário ter uma [conta Jacquard](https://www.jacquard.com/) para aproveitar essa parceria. |
| Token do servidor de conexão da Jacquard | Uma longa string de caracteres que servirá como senha da sua Campaign na Braze para acessar sua linguagem Jacquard.<br><br>Você pode solicitá-lo ao seu CSM da Jacquard, caso ainda não o tenha recebido. |
| Currents | Para exportar dados para o Currents, é necessário que o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) esteja configurado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Solicitar credenciais do Jacquard Amazon S3 {#step-1-request-jacquard-amazon-s3-credentials}

Você precisará que a Jacquard configure um bucket S3 dedicado da Amazon para receber seus eventos de rastreamento de cliques da Braze. Entre em contato com seu CSM da Jacquard para iniciar esse processo. Quando o bucket for criado, você receberá credenciais exclusivas para criar seu Current.

### Etapa 2: Criar um Current {#step-2-create-current}

1. Na Braze, selecione **Currents > Create New Current > Amazon S3 Data Export**.
2. Em seguida, dê um nome ao seu Current e insira um e-mail de contato.
3. Adicione seu ID da chave de acesso do Jacquard AWS e a chave de acesso secreta na caixa de credenciais. Depois, adicione "phrasee-braze-currents-exports" como o nome do bucket S3 da AWS.
4. Por fim, adicione a pasta do bucket S3 da AWS que você recebeu do CSM da Jacquard. Provavelmente será o nome da sua empresa.
5. Em **General Settings**, marque a caixa "Include events from anonymous users" e, em **Manage Engagement Events**, marque "Email Click".
6. Quando terminar, selecione **Launch Current**.

### Etapa 3: Solicitar a remoção de informações de identificação pessoal (IPI) {#step-3-request-to-remove-personally-identifiable-information-pii}

Em seguida, entre em contato com a equipe da sua conta na Braze para garantir que nenhuma informação pessoal identificável seja transmitida para a Jacquard.

Por padrão, o Current incluirá determinados atributos de IPI, como e-mail e endereço. A Jacquard não pode e não receberá IPI, portanto, é fundamental que você solicite à equipe da sua conta na Braze que desative essa opção para todos os dados de eventos transmitidos à Jacquard.

### Etapa 4: Snippets de código do Jacquard X {#step-4-jacquard-x-code-snippets}

Entre em contato com a equipe da sua conta na Jacquard para obter os trechos de código necessários.

Esses trechos usam [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) e, depois de inseridos nos seus e-mails, puxarão dinamicamente a linguagem e um pixel de rastreamento para que a Jacquard possa otimizar sua linguagem em tempo real usando a Jacquard X.