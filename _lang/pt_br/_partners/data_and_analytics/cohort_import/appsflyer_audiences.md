---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "Este artigo de referência descreve a parceria entre a Braze e o AppsFlyer Audiences, um recurso da plataforma AppsFlyer que permite criar e conectar segmentos de público com eficiência a redes de parceiros."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> Este artigo descreve como importar coortes de usuários da AppsFlyer para a Braze usando a integração do [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/). Para saber mais sobre a integração da AppsFlyer e suas outras funcionalidades, como atribuição móvel, consulte o [artigo principal da AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer/).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da AppsFlyer | É necessário ter uma conta da AppsFlyer para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK or kit de desenvolvimento de software da AppsFlyer | Além do SDK or kit de desenvolvimento de software da Braze obrigatório, você deve instalar o [SDK or kit de desenvolvimento de software da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração de importação de dados {#data-import-integration}

### Etapa 1: Configurar o SDK or kit de desenvolvimento de software da AppsFlyer {#step-1-configure-the-appsflyer-sdk}

Para usar essa integração, você deve passar o ID externo da Braze do usuário para a AppsFlyer usando a função `setPartnerData()` do SDK or kit de desenvolvimento de software da AppsFlyer:

#### Android
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Etapa 2: Obter a chave de importação de dados da Braze {#step-2-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **AppsFlyer**.

Aqui, você pode encontrar o endpoint REST e gerar sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar uma nova ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da AppsFlyer.<br><br>![A caixa "Importação de dados usando importação de coortes" na página de tecnologia da AppsFlyer. Nessa caixa, são exibidos a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### Etapa 3: Configurar uma conexão da Braze no AppsFlyer Audiences {#step-3-configure-a-braze-connection-in-appsflyer-audiences}

1. No [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections), acesse a guia **Connections** e clique em **Add partner connection**.
2. Selecione Braze como parceiro e dê um nome à conexão.
3. Forneça a chave de importação de dados e o endpoint REST or transferir estado representacional da Braze.
4. Salve a conexão, e ela estará disponível para ser vinculada a qualquer público novo ou existente.

![A página de configuração de conexão de parceiro da plataforma AppsFlyer Audiences. A parte inferior da imagem mostra que a caixa de ID externo da Braze está marcada.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### Etapa 4: Usar coortes do AppsFlyer Audiences na Braze {#step-4-using-appsflyer-audiences-cohorts-in-braze}

Após o upload de um público da AppsFlyer para a Braze, você pode usá-lo como filtro ao definir segmentos na Braze, selecionando o filtro **AppsFlyer Cohorts**.

![Filtro de atributos do usuário "AppsFlyer Cohorts" selecionado.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.