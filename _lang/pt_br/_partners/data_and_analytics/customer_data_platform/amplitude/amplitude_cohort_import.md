---
nav_title: Amplitude
article_title: Importação de coorte do Amplitude
description: "Este artigo de referência descreve a funcionalidade de importação de coorte do Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
search_tag: Partner
---

# Importação de coorte do Amplitude {#amplitude-cohort-import}

> Este artigo aborda como importar coortes de usuários do [Amplitude](https://amplitude.com/) para a Braze. Para saber mais sobre a integração do Amplitude e suas outras funcionalidades, consulte o artigo principal do [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Integração de importação de dados {#data-import-integration}

Qualquer integração que você configurar será contabilizada no volume de pontos de dados da sua conta.

### Etapa 1: Obtenha a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Amplitude**. Lá, você encontrará o endpoint REST e poderá gerar sua chave de importação de dados da Braze.

Após a geração, você pode criar uma nova chave ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard do Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Etapa 2: Configurar a integração da Braze no Amplitude {#step-2-set-up-the-braze-integration-in-amplitude}

No Amplitude, navegue até **Sources & Destinations** > **[nome do projeto]** > **Destinations** > **Braze**. No prompt exibido, forneça a chave de importação de dados e o endpoint REST da Braze e clique em **Save**.

![]({% image_buster /assets/img/amplitude.png %})

### Etapa 3: Exportar uma coorte do Amplitude para a Braze {#step-3-export-an-amplitude-cohort-to-braze}

Primeiro, para exportar usuários do Amplitude para a Braze, crie uma [coorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) de usuários que deseja exportar. Em seguida, para capturar usuários identificados e anônimos, configure duas sincronizações para essa coorte com as seguintes propriedades de mapeamento de identificadores:
- ID do usuário (ID externo)
- ID do dispositivo

Você pode configurar várias conexões com a Braze na sua conta do Amplitude. Isso permite configurar uma conexão para sincronizar IDs de usuário para usuários conhecidos e outra para sincronizar IDs de dispositivo para usuários anônimos.

Depois de criar uma coorte, clique em **Sync to...** para exportar esses usuários para a Braze.

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

#### Definição da cadência de sincronização {#defining-sync-cadence}

As sincronizações de coorte podem ser definidas como uma sincronização única, programadas diariamente ou a cada hora, ou até mesmo em tempo real, com atualizações a cada minuto.

Qualquer integração configurada registrará pontos de dados. Se você tiver alguma dúvida sobre as nuances dos pontos de dados da Braze, seu gerente de conta da Braze poderá respondê-las.

### Etapa 4: Segmentar usuários na Braze {#step-4-segment-users-in-braze}

Na Braze, para criar um segmento desses usuários, navegue até **Segments** em **Engagement**, nomeie seu segmento e selecione **Amplitude Cohorts** como filtro. Em seguida, use a opção "includes" e escolha a coorte que você criou no Amplitude.

![No criador de segmentos da Braze, o filtro "amplitude_cohorts" está definido como "includes_value" e "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

Depois de salvar, você pode referenciar esse segmento durante a criação de um Canvas ou de uma Campaign na etapa de direcionamento de usuários.

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.