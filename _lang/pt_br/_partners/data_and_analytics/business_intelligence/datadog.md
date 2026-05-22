---
nav_title: Datadog
article_title: Datadog
description: "Este artigo de referência descreve a parceria entre a Braze e o Datadog, um serviço de observabilidade para aplicativos em escala de nuvem, que fornece monitoramento de servidores, bancos de dados, ferramentas e serviços por meio de uma plataforma de análise de dados baseada em SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> O [Datadog](https://www.datadoghq.com/) é um serviço de observabilidade para aplicativos em escala de nuvem, que fornece monitoramento de servidores, bancos de dados, ferramentas e serviços por meio de uma plataforma de análise de dados baseada em SaaS.

A integração entre a Braze e o Datadog permite que os clientes coletem dados da Braze no Datadog e criem alertas sobre os dados enviados. Por exemplo, você pode configurar um monitor e um alerta caso sua Campaign de newsletter semanal envie um volume anormalmente baixo de mensagens, ou caso uma etapa do Canvas que normalmente envia apenas algumas mensagens por dia comece a enviar milhares.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta do Datadog | É necessário ter uma conta do Datadog para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Gerar a chave do Datadog {#step-1-generate-datadog-key}

No Datadog, você precisará criar uma [chave de API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Para adicionar uma chave de API, navegue até **Organization Settings** > **API Keys** > **New Key**.

### Etapa 2: Adicionar a chave à Braze {#step-2-add-key-to-braze}

No dashboard da Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e pesquise **Datadog**. Na página de parceiro do Datadog, forneça a chave de API do Datadog. Isso criará uma conexão para permitir que a Braze envie dados para o Datadog.

## Eventos da Braze {#braze-events}

Depois que a conexão for integrada, a Braze enviará os seguintes eventos ao Datadog:

- `braze.messaging.sent` — A contagem de envios

Cada um desses eventos terá metadados na forma de tags do Datadog para fornecer informações como:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (se disponível)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (se disponível)

Esses eventos e tags podem ser monitorados na página **Metrics Explorer** do Datadog. Essas métricas são registradas como [distribuições](https://docs.datadoghq.com/metrics/distributions/) no Datadog. Dada a natureza das métricas e a imprecisão das agregações e rollups do Datadog, a Braze não tenta novamente em caso de erros de rede intermitentes ou outros erros da API do Datadog que possam ocorrer durante a transmissão. Isso significa que essas contagens de métricas podem diferir ligeiramente das contagens exibidas no dashboard da Braze e/ou no Currents.

![Página do Metrics Explorer no Datadog exibindo métricas da Braze]({% image_buster /assets/img/datadog.png %})