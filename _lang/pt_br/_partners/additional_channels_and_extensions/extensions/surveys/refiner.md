---
nav_title: Refiner
article_title: Refiner
alias: /partners/refiner/
description: "Este artigo de referência descreve a parceria entre a Braze e a Refiner, permitindo que você envie eventos de pesquisa e dados de resposta para a Braze para disparar campanhas, segmentar usuários e atualizar perfis de usuário."
page_type: partner
search_tag: Partner

---

# Refiner

> A [Refiner](https://refiner.io) é uma plataforma de pesquisas in-app para SaaS e apps móveis. Ela permite que equipes de produto e de voz do cliente lancem pesquisas direcionadas in-app e coletem continuamente Net Promoter Score (NPS), CSAT, CES, feedback de produto e dados zero-party dos usuários.

_Essa integração é mantida pela Refiner._

## Sobre a integração {#about-the-integration}

Use a integração entre a Refiner e a Braze para enviar eventos de pesquisa e dados de resposta da Refiner para a sua conta na Braze. Use esses dados para disparar Campaigns na Braze com base em interações de pesquisa (como uma pesquisa concluída), segmentar usuários com base nas respostas e atualizar perfis de usuário na Braze com atributos derivados das respostas da pesquisa.

## Casos de uso {#use-cases}

- Segmentar usuários com base nas respostas de pesquisas, como pontuações de Net Promoter Score (NPS) ou classificações de CSAT.
- Disparar campanhas personalizadas na Braze com base nos resultados de pesquisas.
- Conduzir jornadas entre canais usando o BRAZE CANVAS ou outras ferramentas de orquestração.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta na Refiner | Uma conta na [Refiner](https://refiner.io) é necessária para usar essa integração. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões de `users.track`. Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | A URL do seu endpoint REST. O endpoint depende da [URL da Braze para a sua instância]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conecte sua conta na Braze {#step-1-connect-your-braze-account}

Na seção **Integrations** do seu projeto na Refiner, selecione **Connect Braze**. Insira sua chave da API REST da Braze e o identificador da sua instância na Braze.

### Etapa 2: Mapeie os identificadores de usuário {#step-2-map-user-identifiers}

Mapeie o identificador de usuário da Refiner para o identificador da Braze que você utiliza, como um `external_id` da Braze ou endereço de e-mail. Isso garante que os eventos sejam associados ao usuário correto na Braze.

### Etapa 3: Escolha os dados para sincronizar {#step-3-choose-data-to-sync}

- Selecione as pesquisas cujos dados você deseja sincronizar com a Braze.
- Selecione quais eventos da Refiner enviar para a Braze, como **Survey Seen**, **Survey Dismissed** e **Survey Completed**.

![Painel de configurações de integração da Refiner mostrando opções de seleção de pesquisa e mapeamento de eventos.]({% image_buster /assets/img/refiner.jpg %})

## Personalizar a Refiner {#customize-refiner}

- Escolha se os dados enviados para a Braze incluem apenas respostas de pesquisa ou campos de dados de contato adicionais.
- Escolha se os campos de dados sincronizados devem ter o prefixo `refiner_` para facilitar a identificação na sua conta na Braze.

## Usar dados de pesquisa na Braze {#use-survey-data-in-braze}

Após conectar a Braze e a Refiner, eventos de pesquisa como **Saw Survey** ou **Completed Survey** aparecem nos perfis de usuário na sua conta na Braze. Use esses eventos para disparar e personalizar mensagens na Braze, ou use os dados de resposta da pesquisa para segmentar usuários.

{% alert note %}
Você também pode enviar pesquisas da Refiner por e-mail através da Braze. Para mais detalhes, consulte a [documentação de integração da Refiner](https://refiner.io/docs/kb/integrations/braze-integration/).
{% endalert %}

## Solução de problemas {#troubleshooting}

Se você tiver problemas com a integração, consulte os seguintes recursos:

- [Guia de integração da Refiner e da Braze](https://refiner.io/docs/kb/integrations/braze-integration/)
- [Contato com o suporte da Refiner](https://refiner.io/docs/kb/getting-started/contact-support/)