---
nav_title: Amplitude
article_title: Importação de coorte do Amplitude
description: "Este artigo de referência descreve a funcionalidade de importação de coorte do Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
search_tag: Partner
---

# Importação de coorte do Amplitude {#amplitude-cohort-import}

> Este artigo aborda como importar coortes de usuários do [Amplitude](https://amplitude.com/) para a Braze. Para saber mais sobre a integração do Amplitude e suas outras funcionalidades, consulte o artigo principal do [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences).

## Integração de importação de dados {#data-import-integration}

Qualquer integração que você configurar contará para o volume de pontos de dados da sua conta.

### Etapa 1: Obter a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}

Na Braze, navegue até **Partner Integrations** > **Technology Partners** e selecione **Amplitude**. Lá, você encontrará o endpoint REST or transferir estado representacional e poderá gerar sua chave de importação de dados da Braze.

Após gerar a chave, você pode criar uma nova ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da Amplitude.<br><br>![Página da parceira de tecnologia Amplitude na Braze mostrando a chave de importação de dados e o endpoint.]({% image_buster /assets/img/amplitude3.png %})

### Etapa 2: Configurar a integração com a Braze na Amplitude {#step-2-set-up-the-braze-integration-in-amplitude}

Na Amplitude, navegue até **Sources & Destinations** > **[nome do projeto]** > **Destinations** > **Braze**. No prompt que aparecer, forneça a chave de importação de dados da Braze e o endpoint REST or transferir estado representacional, e clique em **Save**.

![Configurações de destino da Amplitude para sincronização de coorte com a Braze com credenciais preenchidas.]({% image_buster /assets/img/amplitude.png %})

### Etapa 3: Exportar uma coorte da Amplitude para a Braze {#step-3-export-an-amplitude-cohort-to-braze}

Primeiro, para exportar usuários da Amplitude para a Braze, crie uma [coorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) de usuários que você deseja exportar. Em seguida, para capturar usuários identificados e anônimos, configure duas sincronizações para essa coorte com estas propriedades de mapeamento de identificador:
- User ID (ID externo)
- Device ID

Você pode configurar múltiplas conexões com a Braze na sua conta da Amplitude. Isso permite que você configure uma conexão para sincronizar user IDs de usuários conhecidos e outra para sincronizar device IDs de usuários anônimos.

Depois de criar uma coorte, clique em **Sync to...** para exportar esses usuários para a Braze.

{% alert important %}
Somente usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

#### Definindo a cadência de sincronização {#defining-sync-cadence}

As sincronizações de coorte podem ser configuradas como sincronização única, agendadas diariamente ou por hora, ou até em tempo real, com atualização a cada minuto.

Qualquer integração que você configurar registrará pontos de dados. Se você tiver dúvidas sobre as particularidades dos pontos de dados da Braze, seu gerente de conta da Braze pode respondê-las.

### Etapa 4: Segmentar usuários na Braze {#step-4-segment-users-in-braze}

Na Braze, para criar um Segment or segmento desses usuários, navegue até **Segments** em **Engagement**, nomeie seu Segment or segmento e selecione **Amplitude Cohorts** como filtro. Em seguida, use a opção "includes" e escolha a coorte que você criou na Amplitude.

![No criador de segmentos da Braze, o filtro "amplitude_cohorts" está definido como "includes_value" e "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

Após salvar, você pode referenciar esse Segment or segmento durante a criação de Canvas ou Campaign na etapa de direcionamento de usuários.

## Correspondência de usuários {#user-matching}

Usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.

## Perguntas frequentes {#faq}

### Posso obter uma lista de coortes do Amplitude? {#can-i-pull-a-list-of-amplitude-cohorts}

A Braze não oferece uma API or interface de programação do aplicativo (API) para exportar um catálogo com todas as definições de coortes do Amplitude. Você pode visualizar e usar coortes nos seguintes locais:

1. **No Amplitude:** visualize e gerencie coortes no dashboard do Amplitude antes de sincronizá-las com a Braze.
2. **Na Braze:** após a sincronização de uma coorte, direcione usuários com o filtro de Segment or segmento **Amplitude Cohorts**. O filtro lista as coortes sincronizadas pelo nome enviado pelo Amplitude.

Para erros de sincronização de coortes, confirme o alinhamento de IDs de usuário e as chaves de API or interface de programação do aplicativo (API) no Amplitude primeiro. Consulte ["We do not have enough data yet for this filter" ao sincronizar uma coorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort).