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
| Conta Datadog | É necessário ter uma conta Datadog para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Gerar a chave do Datadog {#step-1-generate-datadog-key}

No Datadog, você precisará criar uma [chave de API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Para adicionar uma chave de API, acesse **Organization Settings** > **API Keys** > **New Key**.

### Etapa 2: Adicionar a chave à Braze {#step-2-add-key-to-braze}

No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e pesquise **Datadog**. Na página de parceiro do Datadog, forneça a chave de API do Datadog. Isso criará uma conexão para permitir que a Braze envie dados para o Datadog.

## Eventos da Braze {#braze-events}

Após a integração da conexão, a Braze envia os seguintes eventos para o Datadog:

- `braze.messaging.sent` - A contagem de envios

Cada um desses eventos possui metadados na forma de tags do Datadog para fornecer informações como:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (se disponível)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (se disponível)

Esses eventos e tags podem ser monitorados na página **Metrics Explorer** do Datadog. Essas métricas são registradas como [distribuições](https://docs.datadoghq.com/metrics/distributions/) no DataDog. Dada a natureza das métricas e a imprecisão das agregações e rollups do DataDog, a Braze não faz novas tentativas em caso de erros intermitentes de rede ou outros erros da API do DataDog que possam ocorrer durante a transmissão. Isso significa que essas contagens de métricas podem diferir ligeiramente das contagens vistas no dashboard da Braze e/ou por meio do Currents.

![Metrics Explorer do Datadog mostrando métricas e tags de eventos da Braze.]({% image_buster /assets/img/datadog.png %})

## Solução de problemas {#troubleshooting}

### Por que as métricas `braze.messaging.sent` não aparecem no Datadog? {#why-are-brazemessagingsent-metrics-missing-in-datadog}

Se você conectou a Braze ao Datadog, mas não vê `braze.messaging.sent` no Metrics Explorer, confirme se o **site do Datadog** selecionado na Braze corresponde à URL do site da sua organização no Datadog. Os sites disponíveis são:

- `datadoghq.com` (padrão)
- `us3.datadoghq.com`
- `us5.datadoghq.com`
- `datadoghq.eu`
- `ddog-gov.com`
- `ap1.datadoghq.com`

Uma incompatibilidade de site pode impedir que as métricas apareçam no espaço de trabalho onde você pesquisa. No dashboard da Braze, acesse **Partner Integrations** > **Technology Partners** > **Datadog** e verifique se o site corresponde ao subdomínio na URL da sua conta do Datadog.

O campo **site do Datadog** fica bloqueado após a conexão. Para alterá-lo, desconecte a integração e reconecte com o site correto.

Depois de corrigir o site, aguarde uma nova atividade de envio antes que as métricas apareçam. Os dados históricos não são preenchidos retroativamente.