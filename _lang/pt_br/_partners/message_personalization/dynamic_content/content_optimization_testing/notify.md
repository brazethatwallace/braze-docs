---
nav_title: Notify
article_title: Notify
description: "Este artigo de referência descreve a parceria entre a Braze e a Notify, uma solução de personalização omnicanal em tempo real que oferece personalização em todo o ciclo de vida do cliente."
alias:
  - /partners/notify/
  - /partners/message_personalization/dynamic_content/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/) é uma solução de software impulsionada por IA que se integra perfeitamente com ferramentas de gestão de relacionamento com o cliente para aprimorar estratégias de marketing e facilitar o engajamento em múltiplos canais.

A integração da Braze com a Notify permite que profissionais de marketing promovam efetivamente o engajamento em várias plataformas. Em vez de depender de métodos tradicionais de marketing, uma Campaign disparada por API or interface de programação do aplicativo (API) da Braze pode usar as capacidades da Notify para entregar mensagens personalizadas por meio de múltiplos canais, incluindo e-mail, SMS, notificações por push e mais.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Requisito | Descrição |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões `users.export.segment` e `campaigns.trigger.send`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Configuração de CNAME | Um subdomínio deve ser criado para o pixel de rastreamento usado no e-mail para que a Notify rastreie o engajamento do usuário com as mensagens e alimente melhor o modelo. Compartilhe a URL do subdomínio com a Notify após a criação. |
| Exportação de aceitação do banco de dados | Envie os dados de campanhas e de compras do último ano (12 meses) para a Notify. ​Essa exportação será usada para treinar o modelo preditivo da Notify. <br><br> **Campos:** <br><br> **E-mail:** Um hash SHA256 do e-mail, convertido para minúsculas e com quaisquer espaços em branco no início ou no final removidos.<br><br>**Segment or segmento or segmento:** As informações do Segment or segmento or segmento que definem o nível de atividade (ativo ou inativo).<br><br>**Subsegmento:** Qualquer outra informação relevante sobre atividades, como nível de atividade de compra.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Crie sua Campaign {#step-1-create-your-campaign}

Crie uma [Campaign disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) na Braze. Em seguida, compartilhe o `api_identifier` da Campaign com a Notify.

### Etapa 2: Crie seu Segment or segmento or segmento na Braze {#step-2-create-your-segment-in-braze}

Em seguida, crie o Segment or segmento or segmento de usuários que você deseja alcançar com a Campaign criada na [Etapa 1](#step-1-create-your-campaign). Depois, compartilhe o ID do Segment or segmento or segmento com a Notify.

### Etapa 3: Busque seu Segment or segmento or segmento {#step-3-fetch-your-segment}

A Notify então exportará os usuários no Segment or segmento or segmento vinculado à Campaign.

### Etapa 4: A Notify dispara a Campaign {#step-4-notify-triggers-the-campaign}

Usando o endpoint `/campaigns/trigger/send`, a IA da Notify dispara a Campaign da Braze criada na [Etapa 1](#step-1-create-your-campaign) para enviar aos usuários no momento em que considera haver maior probabilidade de engajamento.