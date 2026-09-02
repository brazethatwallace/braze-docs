---
nav_title: Importação de coorte Hightouch
article_title: Importação de coorte Hightouch
description: "Este artigo de referência descreve a funcionalidade de importação de coorte da Hightouch, uma plataforma para sincronizar os dados de seus clientes do seu data warehouse com ferramentas de negócios."
page_type: partner
search_tag: Partner

---
# Importação de coorte Hightouch {#hightouch-cohort-import}

> Este artigo descreve como importar coortes de usuários do [Hightouch](https://hightouch.io) para a Braze para que você possa enviar campanhas direcionadas com base em dados que podem existir apenas no seu data warehouse. Para saber mais sobre a integração com a Hightouch e suas outras funcionalidades, consulte o [artigo principal sobre a Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch).

## Integração de importação de dados {#data-import-integration}

### Etapa 1: Obter a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}
Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Hightouch**.

Aqui você encontrará o endpoint REST e poderá gerar sua chave de importação de dados da Braze. Depois que a chave for gerada, você pode criar uma nova ou invalidar uma existente.<br><br>![Página da parceira de tecnologia Hightouch na Braze mostrando o endpoint REST e os controles da chave de importação de dados.]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"}

### Etapa 2: Adicionar coortes da Braze como destino no Hightouch {#step-2-add-braze-cohorts-as-a-destination-in-hightouch}
Navegue até a página **Destination** no seu espaço de trabalho Hightouch, procure por **Braze Cohorts** e clique em **Continue**. Em seguida, insira seu endpoint REST e a chave de importação de dados e clique em **Continue**.<br><br>![Configuração de destino no Hightouch para Braze Cohorts com campos de credencial.]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Etapa 3: Sincronizar um modelo (ou público) com Braze Cohorts {#step-3-sync-a-model-or-audience-into-braze-cohorts}
No Hightouch, usando o [modelo](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) ou [público](https://hightouch.io/docs/audiences/usage/) que você criou, crie uma nova sincronização. Em seguida, selecione o destino Braze Cohorts que você criou na etapa anterior. Por fim, na configuração de destino de Braze Cohorts, selecione o identificador que deseja usar para correspondência e decida se quer que o Hightouch crie uma nova coorte na Braze ou atualize uma já existente.<br><br>![Configuração de sincronização de Braze Cohorts no Hightouch com identificador de correspondência e opções de coorte.]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

### Etapa 4: Criar um Segment or segmento na Braze a partir do público personalizado do Hightouch {#step-4-create-a-braze-segment-from-the-hightouch-custom-audience}
Na Braze, navegue até **Segments**, crie um novo segmento e selecione **Hightouch Cohorts** como seu filtro. A partir daí, você pode escolher qual coorte do Hightouch deseja incluir. Depois que o segmento de coorte do Hightouch for criado, você poderá selecioná-lo como filtro de público ao criar uma Campaign ou um Canvas.<br><br>![Criador de segmentos na Braze usando o filtro Hightouch Cohorts.]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Usando essa integração {#using-this-integration}
Para usar seu segmento do Hightouch, crie uma Campaign ou um Canvas na Braze e selecione o segmento como seu público-alvo.<br><br>![Etapa de direcionamento de público na Braze com um segmento baseado no Hightouch selecionado.]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Correspondência de usuários {#user-matching}

Usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.