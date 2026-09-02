---
nav_title: Extensão de encaminhamento de eventos
article_title: Adobe
description: "Este artigo de referência aborda a extensão de encaminhamento de eventos da Braze que permite aproveitar os dados capturados na Adobe Experience Platform Edge Network e enviá-los para a Braze na forma de eventos do lado do servidor."
page_type: partner
page_order: 2
search_tag: Partner
---

# Extensão de encaminhamento de eventos da API or interface de programação do aplicativo (API) Track Events {#track-events-api-event-forwarding-extension}

> A extensão de [encaminhamento de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) da API or interface de programação do aplicativo (API) Track Events da Braze permite aproveitar os dados capturados na Adobe Experience Platform Edge Network e enviá-los para a Braze na forma de eventos do lado do servidor usando a API or interface de programação do aplicativo (API) [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Este documento aborda os casos de uso da extensão, como instalá-la em suas bibliotecas de encaminhamento de eventos e como empregar seus recursos em uma [regra](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de encaminhamento de eventos.

{% alert note %}
O uso do encaminhamento de eventos da Adobe pode aumentar o uso de pontos de dados da Braze. Para saber mais, consulte a documentação da Braze sobre [pontos de dados]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#billable-data-points).
{% endalert %}

## Casos de uso {#use-cases}

Essa extensão deve usar dados da Edge Network na Braze para aproveitar seus recursos de análise de dados e direcionamento de clientes.

Por exemplo, considere uma organização de varejo com presença multicanal (website e dispositivos móveis) que captura dados transacionais ou conversacionais como dados de eventos de seu website e plataformas móveis.

Usando várias regras de [tag](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en), esses dados são enviados para a Edge Network em tempo real. A partir daí, a extensão de encaminhamento de eventos da Braze envia automaticamente os eventos relevantes para a Braze pelo lado do servidor.

## Limites de frequência {#rate-limits}

| API or interface de programação do aplicativo (API) | Limites de frequência |
| --- | --- |
| User Track | 50.000 solicitações por minuto.<br><br>Consulte a [documentação da API or interface de programação do aplicativo (API) User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) para mais detalhes.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de frequência" }

## Integração {#integration}

### Etapa 1: Reúna os detalhes de configuração necessários {#step-1-gather-required-configuration-details}

Para conectar o Edge Network à Braze, os seguintes itens são necessários:

| Tipo de chave | Descrição |
| --- | --- |
| Instância da Braze | Sua instância da Braze pode ser obtida com seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#endpoints). |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com todas as permissões. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1: Reúna os detalhes de configuração necessários" }

### Etapa 2: Crie um segredo {#step-2-create-a-secret}

Crie um novo [segredo de encaminhamento de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) e defina o valor como sua [chave de API or interface de programação do aplicativo (API) da Braze](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Isso será usado para autenticar a conexão com sua conta, mantendo o valor seguro.

### Etapa 3: Instale e configure a extensão Braze {#step-3-install-and-configure-the-braze-extension}

1. Para instalar a extensão, [crie uma propriedade de encaminhamento de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) ou escolha uma propriedade existente para editar.
2. Em seguida, selecione **Extensions** na navegação à esquerda. Na guia **Catalog**, selecione **Install** no cartão da extensão Braze.
3. Na próxima tela, insira sua instância REST or transferir estado representacional e chave de API or interface de programação do aplicativo (API) e selecione **Save** quando terminar.

### Etapa 4: Crie uma regra de envio de evento {#step-4-create-a-send-event-rule}

Após instalar a extensão, crie uma nova [regra](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de encaminhamento de eventos e configure suas condições conforme desejado. Ao configurar as ações para a regra, selecione a extensão **Braze** e, em seguida, selecione **Send Event** para o tipo de ação.

![Ação de regra de encaminhamento de eventos da Adobe configurada para usar Braze Send Event.]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Identificação do usuário %}

| Entrada | Descrição |
| --- | --- |
| ID de usuário externo | Um UUID ou GUID longo, aleatório e bem distribuído. Se você escolher um método diferente para nomear seus IDs de usuário, eles também devem ser longos, aleatórios e bem distribuídos. Saiba mais sobre a [convenção de nomenclatura de ID de usuário sugerida]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| ID de usuário Braze | Identificador de usuário da Braze. |
| Alias de usuário | Um alias serve como um identificador de usuário único alternativo. Use aliases para identificar usuários em dimensões diferentes do seu ID de usuário principal.<br><br>O objeto de alias de usuário consiste em duas partes: um `alias_name` para o identificador em si e um `alias_label` indicando o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Crie uma regra de envio de evento" }

{% alert note %}
Para vincular o evento a um usuário, você deve preencher o campo `External User ID`, o campo `Braze User Identifier` ou a seção `User Alias`.
{% endalert %}

{% endtab %}
{% tab Dados do evento %}

| Entrada | Descrição | Obrigatório |
| --- | --- | --- |
| Nome do evento | Nome do evento. | Sim |
| Hora do evento | Data e hora como string no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sim |
| Identificador do app | O identificador do app ou `app_id` é um parâmetro que associa a atividade a um app específico no seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. | Não |
| Propriedades do evento | Um objeto JSON contendo propriedades personalizadas do evento. | Não |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Crie uma regra de envio de evento" }

{% alert note %}
A ação **Braze Send Event** requer apenas que um **Event Name** e um **Event Time** sejam especificados, mas você deve incluir o máximo de informações possível no campo de propriedades personalizadas. Consulte o [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object) para mais detalhes.
{% endalert %}

{% endtab %}
{% tab Atributo de usuário %}

Os atributos de usuário podem ser um objeto JSON contendo campos que criarão ou atualizarão um atributo com o nome e valor fornecidos no perfil de usuário especificado. As seguintes propriedades são suportadas:

| Atributo de usuário | Descrição |
| --- | --- |
| Nome | Nome do usuário. |
| Sobrenome | Sobrenome do usuário. |
| Telefone | Número de telefone do usuário. |
| E-mail | Endereço de e-mail do usuário. |
| Gênero | Uma das seguintes strings: "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer). |
| Cidade | A cidade do usuário. |
| País | O país do usuário como string no formato [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | O idioma do usuário como string no formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Data de nascimento | A data de nascimento do usuário como string no formato "YYYY-MM-DD" (por exemplo, 1980-12-21). |
| Fuso horário | Nome do fuso horário do banco de dados [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, 'America/New_York' ou 'Eastern Time (US & Canada)'). |
| Facebook | Um hash contendo qualquer um dos seguintes: `id` (string), `likes` (array de strings), `num_friends` (inteiro). |
| Twitter | Hash contendo qualquer um dos seguintes: id (inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (inteiro), `friends_count` (inteiro), `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Crie uma regra de envio de evento" }

{% alert note %}
Todos os atributos adicionados na configuração serão enviados cada vez que o evento for enviado à Braze, independentemente de o valor do atributo ter sido alterado. Ao configurar atributos de usuário, certifique-se de saber como isso afetará seu uso de pontos de dados.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Crie uma regra de envio de evento de compra {#step-5-create-a-send-purchase-event-rule}

Após instalar a extensão, crie uma nova [regra](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de encaminhamento de eventos e configure suas condições conforme desejado. Ao configurar as ações para a regra, selecione a extensão **Braze** e, em seguida, selecione **Send Purchase Event** para o tipo de ação.

![Ação de regra de encaminhamento de eventos da Adobe configurada para usar Braze Send Purchase Event.]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Identificação do usuário %}

| Entrada | Descrição |
| --- | --- |
| ID de usuário externo | Um UUID ou GUID longo, aleatório e bem distribuído. Se você escolher um método diferente para nomear seus IDs de usuário, eles também devem ser longos, aleatórios e bem distribuídos. Saiba mais sobre a [convenção de nomenclatura de ID de usuário sugerida]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web#naming-best-practices). |
| ID de usuário Braze | Identificador de usuário da Braze. |
| Alias de usuário | Um alias serve como um identificador de usuário único alternativo. Use aliases para identificar usuários em dimensões diferentes do seu ID de usuário principal.<br><br>O objeto de alias de usuário consiste em duas partes: um `alias_name` para o identificador em si e um `alias_label` indicando o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 5: Crie uma regra de envio de evento de compra" }

{% alert note %}
Para vincular o evento a um usuário, você deve preencher o campo `External User ID`, o campo `Braze User Identifier` ou a seção `User Alias`.
{% endalert %}

{% endtab %}
{% tab Dados de compra %}

| Entrada | Descrição | Obrigatório |
| --- | --- | --- |
| ID do produto | Identificador da compra. (por exemplo, nome do produto ou categoria do produto) | Sim |
| Hora da compra | Data e hora como string no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sim |
| Moeda | Moeda como string no formato de código alfabético de moeda [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Sim |
| Preço | O preço do objeto. | Sim |
| Quantidade | A quantidade comprada. Se não for fornecida, o valor padrão será 1. O valor máximo deve ser inferior a 100. | Não |
| Identificador do app | O identificador do app ou `app_id` é um parâmetro que associa a atividade a um app específico no seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. | Não |
| Propriedades de compra | Um objeto JSON contendo propriedades personalizadas da compra. | Não |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Crie uma regra de envio de evento de compra" }

{% alert note %}
A ação **Send Purchase Event** requer apenas que `Product ID`, `Purchase Time`, `Currency` e `Price` sejam especificados, mas você deve incluir o máximo de informações possível no campo de propriedades de compra. Consulte o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) para mais detalhes.
{% endalert %}

{% endtab %}
{% tab Atributos de usuário %}

Você pode escolher se deseja enviar atributos com cada evento na visualização de configuração.

Os atributos de usuário podem ser um objeto JSON contendo campos que criarão ou atualizarão um atributo com o nome e valor fornecidos no perfil de usuário especificado. As seguintes propriedades são suportadas:

| Atributo de usuário | Descrição |
| --- | --- |
| Nome | Nome do usuário. |
| Sobrenome | Sobrenome do usuário. |
| Telefone | Número de telefone do usuário. |
| E-mail | Endereço de e-mail do usuário. |
| Gênero | Uma das seguintes strings: "M", "F", "O" (outro), "N" (não aplicável), "P" (prefere não dizer). |
| Cidade | A cidade do usuário. |
| País | O país do usuário como string no formato [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | O idioma do usuário como string no formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Data de nascimento | A data de nascimento do usuário como string no formato "YYYY-MM-DD" (por exemplo, 1980-12-21). |
| Fuso horário | Nome do fuso horário do banco de dados [IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, 'America/New_York' ou 'Eastern Time (US & Canada)'). |
| Facebook | Um hash contendo qualquer um dos seguintes: `id` (string), `likes` (array de strings), `num_friends` (inteiro). |
| Twitter | Hash contendo qualquer um dos seguintes: id (inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (inteiro), `friends_count` (inteiro), `statuses_count` (inteiro). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 5: Crie uma regra de envio de evento de compra" }

{% alert note %}
Todos os atributos adicionados na configuração serão enviados cada vez que o evento for enviado à Braze, independentemente de o valor do atributo ter sido alterado. Ao configurar atributos de usuário, certifique-se de saber como isso afetará seu uso de pontos de dados.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 6: Valide os dados na Braze {#step-6-validate-data-within-braze}

Se a coleta de eventos e a integração com a Adobe Experience Platform foram bem-sucedidas, você verá os eventos no console da Braze ao [visualizar perfis de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Especificamente, os novos dados de eventos enviados à Braze são refletidos na seção **Purchases** ou **Custom Events** da [guia de visão geral]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#overview-tab) de um usuário específico.