---
nav_title: Peak
article_title: Peak
description: "Este artigo de referência descreve a parceria entre a Braze e a Peak, uma plataforma de inteligência de decisão, que permite que você pegue a probabilidade de churn prevista e os atributos com base nos comportamentos e interações dos clientes, e os importe para a Braze para usar na segmentação e direcionamento de clientes."
alias: /partners/peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://peak.ai/), uma plataforma de inteligência de decisão, é um sistema de ponta a ponta onde a inteligência de decisão é a aplicação comercial de IA para melhorar a tomada de decisões empresariais, aumentando a receita e os lucros.

_Essa integração é mantida pela Peak._

## Sobre a integração {#about-the-integration}

A parceria entre a Braze e a Peak permite que você pegue a probabilidade de churn prevista e os atributos com base nos comportamentos e interações dos clientes, e os importe para a Braze para usar na segmentação e direcionamento de clientes.

## Pré-requisitos {#prerequisites}

Como ponto de partida, um tenant da Peak deve hospedar a integração entre a Peak e a Braze. Isso é tradicionalmente criado durante a integração dos clientes da Peak. Além disso, uma solução de inteligência de decisão é necessária no início, pois gera os resultados orientados por IA que serão integrados à Braze depois.

| Requisito | Descrição |
| ----------- | ----------- |
| Tenant da Peak | Uma instância da plataforma Peak, conhecida como tenant, é necessária para hospedar e orquestrar a integração. |
| Solução de inteligência de decisão | A integração entre a Peak e a Braze é baseada em resultados orientados por IA e, portanto, requer uma solução implantada pela Peak ou pelo cliente em seu tenant. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A solução de inteligência do cliente da Peak utiliza um modelo para prever uma série de atributos futuros com base nos comportamentos e interações dos clientes. Esses atributos são armazenados na Peak e podem ser usados para gerar segmentação preditiva, incluindo a probabilidade de churn do cliente. A atualização desses atributos preditivos será baseada em uma cadência configurável (diária ou semanal).

### Etapa 1: Executar modelo e extrair clientes {#step-1-run-model-and-extract-customers}

A integração é disparada a partir da execução do modelo de IA e do recálculo dos atributos preditivos do cliente. Essas saídas de IA são armazenadas na Peak, inclusive quando um atributo é atualizado com um novo status ou valor.

Com base em quando os atributos foram atualizados, uma seleção é realizada para coletar todos os clientes com atributos preditivos atualizados desde a última sincronização entre a Peak e a Braze.

### Etapa 2: Atualizar a Braze {#step-2-update-braze}

Com os clientes atualizados e os atributos associados, a Peak enviará esses dados para a Braze usando o [endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), com o cabeçalho [em massa]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates).

Após o recebimento de códigos de status bem-sucedidos da API, a Peak registrará a sincronização bem-sucedida entre a Peak e a Braze.

### Etapa 3: Usando esta integração {#step-3-using-this-integration}

Depois que a sincronização entre a Peak e a Braze for bem-sucedida, os usuários atualizados agora incluem os novos atributos. Use esses atributos em Campaigns e Canvas para direcionar usuários e personalizar mensagens.