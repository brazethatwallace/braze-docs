---
nav_title: Okendo
article_title: Okendo
description: "Aprenda como integrar a Okendo com a Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) é uma plataforma unificada de marketing de clientes que fornece ferramentas para cultivar a defesa da marca, escalar o boca a boca e maximizar o lifetime value para mobilizar seus clientes rumo a um crescimento mais rápido e eficiente.

*Esta integração é mantida pela Okendo.*

## Sobre a integração {#about-the-integration}

A integração da Braze com a Okendo funciona em vários produtos na plataforma da Okendo, incluindo Avaliações, Fidelidade, Indicações, Pesquisas e Questionários. A Okendo envia eventos personalizados e atributos de usuário para a Braze, que podem ser usados para personalizar e disparar mensagens.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|------------------------|-----------------------------------------------------------------------------|
| Conta Okendo | Uma conta Okendo é necessária para aproveitar esta parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint depende da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Configurar o conector Braze na Okendo {#step-1-set-up-braze-connector-in-okendo}

1. Na Okendo, acesse **Settings** > **Integrations** > **Email & SMS** > **Braze**.
2. Adicione o endpoint da API or interface de programação do aplicativo (API) e a chave de API or interface de programação do aplicativo (API) nas configurações de **Integration**.

### Etapa 2: Configure seu identificador {#step-2-configure-your-identifier}

O campo `external_id` é usado para identificar o usuário associado a cada evento. Ative **Use Shopify Customer ID for Braze user identification** para associar o campo com IDs de clientes Shopify. Caso contrário, desative para associá-lo ao endereço de e-mail de cada usuário.

## Sincronizando eventos e atributos da Okendo para a Braze {#syncing-okendo-events-and-attributes-to-braze}

### Eventos personalizados {#custom-events}

{% alert note %}
Para dados de eventos de exemplo, consulte a [documentação da Okendo](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c).
{% endalert %}

#### Eventos de avaliação {#review-events}

- Okendo Review Created
- Okendo Review Request

#### Eventos de indicação {#referral-events}

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### Eventos de fidelidade {#loyalty-events}

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### Evento de pesquisa {#survey-event}

- Submitted Okendo Survey

#### Evento de quiz {#quiz-event}

- Submitted Okendo Quiz

### Atributos personalizados {#custom-attributes}

A Okendo envia dados do perfil do usuário como atributos personalizados na Braze, que podem ser usados para criar segmentos de público. Os exemplos incluem:

- Perguntas de perfil feitas em pesquisas e durante o envio de uma avaliação, como idade, aniversário, tipo de pele e cor do cabelo
- Métricas de avaliação como *Classificação média da avaliação* e *Sentimento médio da avaliação*
- Métricas de fidelidade, como *Saldo de pontos* e *Nível VIP*
- Métricas de indicações, como o *Número de indicações bem-sucedidas* e *Receita total de indicações*
- Pontuação Net Promoter Score (NPS) coletada de uma pesquisa

## Usando a Braze com produtos Okendo {#using-braze-with-okendo-products}

Dependendo do produto Okendo, você deve completar etapas adicionais para usar a Braze e a Okendo juntas. Consulte os seguintes artigos para mais detalhes:

- [Integrando Avaliações com a Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integrando Fidelidade com a Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integrando Indicações com a Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integrando Pesquisas com a Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integrando Questionários com a Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Para assistência na configuração da integração, entre em contato com a equipe de suporte da Okendo.
{% endalert %}