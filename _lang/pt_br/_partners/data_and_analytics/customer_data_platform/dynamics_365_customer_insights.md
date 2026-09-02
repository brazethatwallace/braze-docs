---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Este artigo de referência descreve a parceria entre a Braze e o Dynamics 365 Customer Insights, uma CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente líder no mercado, que permite exportar segmentos de clientes para a Braze para usar em Campaigns ou Canvas."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights

> O [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) é uma plataforma empresarial de dados de cliente líder que oferece experiências personalizadas aos clientes com uma visão de 360 graus.

_Essa integração é mantida pelo Dynamics 365 Customer Insights._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Dynamics 365 Customer Insights permite que você exporte segmentos de clientes para a Braze para usar em Campaigns ou Canvas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Dynamics 365 Customer Insights | É necessário ter uma conta [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) para usar a parceria. Você precisará de acesso como administrador para visualizar e editar conexões dentro da sua conta do Dynamics 365 Customer Insights para acessar os plugins necessários. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | É necessária uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões `users.track` e `users.export.segment`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Identificadores de perfil correspondentes | Os perfis de clientes unificados nos segmentos exportados contêm um campo que representa um endereço de e-mail e um `external_id` da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Configurar a conexão com a Braze {#step-1-set-up-braze-connection}

No Customer Insights, navegue até **Admin > Connections**. Em seguida, selecione **Add connections** e escolha **Braze** para configurar a conexão.

1. Dê à sua conexão um nome reconhecível no campo **Display name**.
2. Escolha quem pode usar esta conexão. Se você deixar este campo em branco, o padrão será Administradores. Para saber mais, consulte [Permitir que os colaboradores usem uma conexão para exportações](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Forneça sua chave de API or interface de programação do aplicativo (API) da Braze e o endpoint REST or transferir estado representacional no formato `rest.iad-03.braze.com`.
4. Selecione **I agree** para confirmar a conformidade com os dados e a privacidade.
5. Selecione **Connect** para iniciar a conexão com a Braze.
6. Selecione **Add yourself as export user** e forneça suas credenciais do Customer Insights.
7. Selecione **Save** para concluir a conexão.

### Etapa 2: Criar um Segment na Braze {#step-2-create-a-braze-segment}

1. Na Braze, acesse **Audience** > **Segments**.
2. Crie um Segment or segmento dos usuários que deseja que a Microsoft atualize por meio do Dynamics 365 Customer Insights.
3. Capture o **identificador de API or interface de programação do aplicativo (API)** do Segment or segmento.

### Etapa 3: Configurar uma exportação {#step-3-configure-an-export}

Você pode configurar esta exportação se tiver acesso a uma conexão deste tipo. Para saber mais, consulte [Visão geral das exportações](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. No Customer Insights, acesse **Data > Exports**. Para criar uma nova exportação, selecione **Add destination**.
2. No campo **Connection for export**, selecione uma conexão para a seção Braze. Se esse nome de seção não aparecer, isso significa que não há conexões desse tipo disponíveis para você.
3. Forneça o identificador de API or interface de programação do aplicativo (API) do Segment or segmento na Braze.
4. Na seção **Data matching**, no campo **Email**, selecione o campo que representa o endereço de e-mail de um cliente. Em seguida, no campo **Braze Customer ID**, selecione o campo que representa o ID do cliente na Braze. Você também pode selecionar um campo adicional e opcional para correspondência de dados.
  a. Se você mapear o `external_id` na Braze para o campo de ID do cliente da Braze no Customer Insights, os registros existentes serão atualizados na Braze durante a exportação.
  b. Se você mapear um campo de ID diferente que não represente o `external_id` de um registro na Braze, ou um campo vazio, novos registros serão criados na Braze durante a exportação.
5. Por fim, selecione os segmentos que deseja exportar e selecione **Save**.

Observe que salvar uma exportação não a executa imediatamente. Esta exportação será executada com cada [atualização programada](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). Você também pode [exportar dados sob demanda](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand).


### Usando essa integração {#using-this-integration}

Depois que seus segmentos forem exportados com sucesso para a Braze, você poderá encontrá-los como atributos personalizados nos perfis de usuário. O atributo personalizado será nomeado com o identificador de API or interface de programação do aplicativo (API) do Segment or segmento da Braze que foi inserido durante a configuração da conexão de exportação. Por exemplo, `"Segment_API_Identifier": "0000-0000-0000"`

Para criar um Segment or segmento desses usuários na Braze, navegue até **Segments**, crie um novo Segment or segmento e selecione **Custom Attributes** como seu filtro. A partir daqui, você pode escolher o atributo personalizado sincronizado do Dynamics 365. Depois que o Segment or segmento for criado, você pode selecioná-lo como um filtro de público ao criar uma Campaign ou Canvas.

{% alert note %}
Para saber mais sobre essa integração, visite o [artigo de integração](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) com a Braze criado pela Microsoft.
{% endalert %}