---
nav_title: Census
article_title: Importação de coortes do Census
description: "Este artigo de referência descreve a funcionalidade de importação de coortes do Census, uma plataforma de integração de dados que permite criar dinamicamente segmentos de usuários direcionados com dados do seu data warehouse na nuvem."
page_type: partner
search_tag: Partner

---

# Importação de coortes do Census {#census-cohort-import}

> Este artigo descreve como importar coortes de usuários do [Census](https://www.getcensus.com/) para a Braze. Para saber mais sobre a integração do Census, consulte o [artigo principal sobre o Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census).

## Integração da importação de coortes {#cohort-import-integration}

### Etapa 1: Criar conexão de serviço da Braze {#step-1-create-braze-service-connection}

Para integrar o Census na plataforma Census, navegue até a guia **Connections** e selecione **New Destination** para criar uma nova conexão de serviço da Braze.

No prompt exibido, nomeie essa conexão e forneça a URL do endpoint da Braze, a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze e a chave de importação de dados. A chave de importação de dados é necessária para sincronizar coortes e pode ser encontrada na Braze acessando **Partner Integrations** > **Technology Partners** > **Census**.

![Diálogo de novo destino do Census configurado com credenciais de importação de coortes da Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Etapa 2: Criar uma sincronização do Census {#step-2-create-a-census-sync}

Para sincronizar clientes com a Braze, você deve criar uma sincronização. Aqui, você definirá onde sincronizar os dados e como deseja que os campos sejam mapeados entre as duas plataformas.

1. Navegue até a guia **Syncs** e selecione **New Sync**.<br><br>
2. No criador, selecione o modelo de dados de origem do seu data warehouse.<br><br>
3. Configure o local para onde o modelo será sincronizado. Selecione **Braze** como o destino e **User & Cohort** como o objeto a ser sincronizado.<br>![No prompt "Select a Destination", "Braze" é selecionada como a conexão, e vários objetos são listados.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecione a **Source Column** que identifica os usuários a serem adicionados a uma coorte e selecione **External User ID** como o **Identifier Type**.<br><br>
5. No menu suspenso **Cohort Name**, selecione uma coorte, crie uma coorte ou selecione uma Source Column para preencher o nome da coorte.<br><br>
6. Use o menu suspenso **When a record is removed from source data** para selecionar o que acontece com os usuários quando eles são removidos do conjunto de dados de origem, como **Do nothing** ou **Remove matching record from cohort**.<br><br>
7. Por fim, mapeie os campos de dados do Census para os campos equivalentes da Braze.<br>![Mapeamento do Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirme os detalhes e crie a sincronização.

Agora você pode executar sua sincronização!

Durante uma sincronização, todos os campos que você mapear serão primeiro sincronizados com o objeto do usuário para atualizar o que já existe na Braze. Depois disso, o usuário atualizado será adicionado à coorte especificada.

Após a sincronização, você pode criar e adicionar um Segment or segmento da Braze com um filtro de coorte do Census a futuras Campaigns e Canvas da Braze para direcionar esses usuários.

{% alert note %}
Ao usar a integração do Census com a Braze, o Census enviará apenas os deltas (dados alterados) em cada sincronização para a Braze.
{% endalert %}

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coortes não criará novos usuários na Braze.
{% endalert %}

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.