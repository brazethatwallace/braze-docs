---
nav_title: actionable.me
article_title: actionable.me
description: "Este artigo de referência descreve a parceria entre a Braze e a actionable.me, uma solução proprietária de software e processos, que permite aproveitar ao máximo seu investimento na Braze imediatamente."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), construído pela equipe da Massive Rocket, uma agência de dados e CRM, é uma abordagem padronizada e automatizada para executar programas de CRM, fornecendo ferramentas e processos projetados para levar os clientes da Braze a obter valor de forma rápida, consistente e previsível.

_Esta integração é mantida pela actionable.me._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a actionable.me permite implantar um serviço para monitorar seu progresso na utilização da Braze. Por meio de uma combinação de ferramentas e processos, eles irão rapidamente avaliar o desempenho do seu CRM, identificar novas oportunidades e fornecer recomendações sobre como melhorar seus resultados.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta actionable.me | Uma conta actionable.me é necessária para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões listadas na próxima seção.<br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar a Braze e a actionable.me, a plataforma actionable.me deve ser configurada, e é preciso criar uma chave de API da Braze na Braze e configurá-la no dashboard da actionable.me.

### Etapa 1: Crie sua chave de API da Braze {#step-1-create-your-braze-api-key}

Na Braze, navegue para **Configurações** > **Chaves de API**. Selecione **Criar nova chave de API** e confirme se as seguintes permissões foram adicionadas:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Etapa 2: Forneça informações para a equipe actionable.me {#step-2-provide-information-to-the-actionableme-team}

Para completar a integração, você deve fornecer sua chave da API REST e a [URL do endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) para sua equipe de operações actionable.me. A actionable.me então estabelecerá a conexão e entrará em contato com você após a configuração estar completa para começar a compartilhar insights.

![A página "adicionar plataforma" da actionable.me que a equipe de operações da actionable.me configurará.]({% image_buster /assets/img/actionableme/image2.png %})

## Solução de problemas {#troubleshooting}

Entre em contato com a equipe da actionable.me ou da Massive Rocket para obter mais ajuda: [info@massiverocket.com](mailto:info@massiverocket.com)