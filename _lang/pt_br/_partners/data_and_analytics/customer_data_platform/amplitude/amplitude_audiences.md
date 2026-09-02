---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Este artigo de referência descreve a parceria entre a Braze e a Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude}

> A [Amplitude](https://amplitude.com/) é uma plataforma de análise de dados e business intelligence de produtos.

A integração bidirecional entre a Braze e a Amplitude permite a [importação de coortes da Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import), características de usuários e eventos para a Braze, bem como a criação de segmentos que podem direcionar os usuários em futuras campanhas ou Canvas. Você também pode aproveitar o Braze Currents para [exportar seus eventos da Braze para a Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents#data-export-integration) para realizar análises mais profundas de seus dados de produto e marketing.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Amplitude | É necessário ter uma [conta da Amplitude](https://amplitude.com/) para usar essa parceria. |
| Currents | Para exportar dados de volta para a Amplitude, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Escolha uma integração {#choose-an-integration}

A Amplitude e a Braze oferecem dois métodos de integração diferentes. Leia a documentação a seguir para decidir quais métodos atenderão às suas necessidades:

- Braze Event Streaming: uma integração que permite encaminhar dados brutos de eventos da Amplitude diretamente para a Braze.
- [Importação de coorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import): uma integração que permite encaminhar coortes da Amplitude para a Braze.

## Braze Event Streaming

### Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com todas as permissões.<br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [A URL do seu endpoint REST or transferir estado representacional][1]. Seu endpoint dependerá da URL da Braze para sua instância. |
| Identificador do app Braze | O identificador do app que receberá eventos da Amplitude. Ele pode ser encontrado em **Dashboard da Braze > Console de desenvolvedor > Configurações**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

### Configuração da Amplitude {#amplitude-setup}

1. Na Amplitude, navegue até **Data Destinations** e procure "Braze - Event Stream".
2. Digite um nome de sincronização e clique em **Create Sync**.
3. Clique em **Edit** e forneça seu endpoint REST or transferir estado representacional da Braze, sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional e o identificador do app Braze.
4. Use o filtro de eventos de envio para selecionar os eventos a serem enviados. Você pode enviar todos os eventos, mas a Amplitude recomenda escolher os mais importantes.
5. Quando terminar, ative o destino e salve.

Consulte [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/) para saber mais sobre essa integração.

## Sincronizar características e cálculos do usuário {#sync-user-traits-and-computations}

Use públicos para enviar propriedades e cálculos do usuário para a Braze como atributos personalizados. Você poderá sincronizar as propriedades do usuário ou as propriedades computadas dos usuários que estiveram ativos nos últimos 90 dias.

Quando a propriedade de um usuário ou um cálculo for atualizado, a Amplitude atualizará um atributo personalizado na Braze com o mesmo nome da propriedade ou do cálculo do usuário.

As sincronizações de características e cálculos do usuário criarão novos usuários para identificadores de usuário que ainda não existem na Braze. Os cálculos e as características do usuário só podem ser sincronizados usando identificadores de usuário. Um identificador de usuário pode ser qualquer um dos seguintes:
- ID externo
- ID da Braze
- Alias de usuário
- Endereço de e-mail

Consulte a documentação da Amplitude para saber mais sobre a [sincronização de propriedades, recomendações e coortes com destinos de terceiros](https://help.amplitude.com/hc/en-us/articles/360060055531).

### Como sincronizar as propriedades e os cálculos do usuário {#how-to-sync-user-properties-and-computations}

Nos públicos da Amplitude, selecione **Syncs > Create Sync**.

![Página de sincronizações do Amplitude Audiences com a opção Create Sync selecionada.]({% image_buster /assets/img/amplitude11.png %})

Em seguida, escolha sincronizar uma propriedade, um cálculo, uma coorte ou uma recomendação de usuário.

{% tabs %}
{% tab Syncing user property %}

Selecione **User Property** e, em seguida, a propriedade do usuário que deseja sincronizar.

![Etapa de configuração de sincronização da Amplitude selecionando uma propriedade de usuário para sincronizar.]({% image_buster /assets/img/amplitude7.png %})

Em seguida, selecione um destino para sincronizar a propriedade do usuário.

![Seletor de destino da Amplitude para sincronizar propriedades com a Braze.]({% image_buster /assets/img/amplitude8.png %})

Por fim, defina a frequência de sua sincronização.

![Defina sua cadência como uma sincronização única ou uma sincronização programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Syncing computation %}

Selecione **Computation** e, em seguida, o cálculo que deseja sincronizar.

![Etapa de configuração de sincronização da Amplitude selecionando um cálculo para sincronizar.]({% image_buster /assets/img/amplitude10.png %})

Em seguida, selecione um destino para sincronizar seu cálculo.

![Seletor de destino da Amplitude para sincronizar cálculos com a Braze.]({% image_buster /assets/img/amplitude8.png %})

Por fim, defina a frequência de sua sincronização.

![Defina sua cadência como uma sincronização única ou uma sincronização programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Solução de problemas {#troubleshooting}

### "We do not have enough data yet for this filter" ao sincronizar uma coorte {#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort}

Se você receber esse erro ao [importar uma coorte da Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import) para a Braze, tente o seguinte:

1. **Confirme o alinhamento do ID do usuário.** O User ID na Amplitude (não o Amplitude ID) deve corresponder exatamente ao External User ID na Braze (não o Braze ou BSON ID). Por exemplo, o User ID `12345` na Amplitude deve corresponder ao External User ID `12345` na Braze.
2. **Regenere sua chave de API or interface de programação do aplicativo (API) da Braze.** No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** > **Amplitude** e selecione **Generate New Key**. Em seguida, tente novamente a sincronização da coorte da Amplitude usando a nova chave de API or interface de programação do aplicativo (API).
3. **Confirme que a coorte foi sincronizada na Amplitude.** Entre em contato com o [suporte da Amplitude](https://help.amplitude.com/) para confirmar que a coorte foi sincronizada com sucesso no lado da Amplitude antes de investigar mais na Braze.

## Endpoints da API or interface de programação do aplicativo (API) do perfil de usuário da Amplitude {#amplitude-user-profile-api-endpoints}

Para verificar alguns dos endpoints comuns da API or interface de programação do aplicativo (API) da Amplitude que podem ser usados com Conteúdo conectado, consulte nossa [documentação específica da API or interface de programação do aplicativo (API) da Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api).