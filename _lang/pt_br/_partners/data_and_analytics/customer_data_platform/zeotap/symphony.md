---
nav_title: Zeotap Symphony
description: "Este artigo de referência descreve a parceria entre a Braze e a Zeotap, uma plataforma de dados do cliente de última geração que fornece resolução de identidade, insights e enriquecimento."
page_type: partner
search_tag: Partner
page_order: 2
---

# Zeotap Symphony

A integração entre a Braze e o Zeotap Symphony permite que você crie orquestrações em tempo real e execute campanhas de e-mail e notificações por push.

- Envie nomes e sobrenomes pelo Zeotap, com base nos quais os usuários podem enviar e-mails personalizados pela Braze.
- Envie eventos personalizados ou um evento de compra em tempo real por meio do Zeotap, com base nos quais os usuários podem criar gatilhos de Campaign na Braze para direcionar seus clientes.

{% alert note %}
Para criar campanhas de marketing por e-mail, integre os e-mails brutos ao Zeotap mapeando-os para `Email Raw` no Zeotap Catalogue.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Nome do cliente | Esse é o nome do cliente da sua conta Braze. Você pode encontrá-lo navegando até o console da Braze. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância | Sua instância da Braze pode ser obtida com seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Esta seção contém informações sobre os dois métodos de integração com a Braze:

### Método 1 {#method-1}
Neste método, você deve executar as seguintes tarefas:
1. Integrar o SDK da Braze ao seu site ou app.
2. Integrar a Braze com o Zeotap pela Symphony.

- `User traits` devem ser mapeados para os respectivos campos da Braze na guia **Data To Send**. Se você mapear os atributos `Event` e `Purchase`, isso levará à duplicação de eventos na Braze.
- Mapeie `External ID` para `User ID` configurado durante a configuração do SDK da Braze.

Quando a integração for configurada com sucesso, você poderá criar campanhas de e-mail e notificações por push com base em atributos personalizados enviados à Braze por meio do Symphony.

### Método 2 {#method-2}
Neste método, você pode integrar a Braze ao Zeotap pela Symphony.

- Esse método não oferece suporte aos recursos da interface do usuário da Braze, como envio de mensagens no app, Content Cards ou notificações por push.
- O Zeotap recomenda mapear o `hashed email` disponível no Zeotap Catalogue para o `External ID`.

Quando a integração for configurada com sucesso, você só poderá criar campanhas de e-mail com base em atributos personalizados enviados à Braze por meio do Symphony.

## Fluxo de dados para a Braze e identificadores suportados {#data-flow-to-braze-and-supported-identifiers}

Os dados fluirão do Zeotap para a Braze usando o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Os pontos a seguir resumem o fluxo de dados:

1. O Zeotap envia atributos de perfil de usuário, atributos personalizados, eventos personalizados e campos de compra.
2. Você mapeia todos os campos relevantes do Zeotap Catalogue para os campos da Braze na guia **Data To Send**.
3. Em seguida, é feito o upload dos dados para a Braze.

Você pode encontrar detalhes sobre os diferentes atributos na seção [Data To Send](#data-to-send-tab).

## Configuração do destino {#destination-setup}

Após aplicar filtros ou adicionar uma condição para seus usuários no Symphony, é possível ativá-los na Braze em **Send to Destinations**. Uma nova janela é aberta, onde você pode configurar seu destino. Você pode usar um destino existente na lista de **Available Destinations** ou criar um novo.

### Adicionar novo destino {#add-new-destination}
Execute as etapas a seguir para adicionar um novo destino:
1. Selecione **Add New Destination**.
2. Procure por **Braze**.
3. Adicione o **Client Name**, a **API Key** e a **Instance** e salve o destino.

O destino é criado e disponibilizado em **Available Destinations**.

### Adicionar entradas em nível de fluxo de trabalho {#add-workflow-level-inputs}
Depois de criar um destino, você deve adicionar entradas no nível do fluxo de trabalho, conforme descrito nesta seção.
1. Escolha o destino na lista de destinos disponíveis usando o recurso de pesquisa.
2. Os campos **Client Name**, **API Key** e **Instance** são preenchidos automaticamente com base no valor que você inseriu ao criar o destino.
3. Digite o **Audience Name** que você deseja criar para esse nó de fluxo de trabalho. Isso é enviado como um **atributo personalizado** para a Braze.
4. Complete o mapeamento de Catálogo para destinos na guia **Data To Send**. Você pode encontrar detalhes sobre como realizar o mapeamento nesta seção.

### Guia Data To Send {#data-to-send-tab}
A guia **Data To Send** permite mapear os campos do Zeotap Catalogue para os campos da Braze que podem ser enviados à Braze. O mapeamento pode ser feito de uma das seguintes maneiras:
- **Mapeamento estático** — Há determinados campos que o Zeotap mapeia automaticamente para os campos relevantes da Braze, como e-mail, telefone, nome, sobrenome e assim por diante.<br>
- **Seleção suspensa** — Mapeie os campos relevantes ingeridos no Zeotap para os campos da Braze fornecidos no menu suspenso.<br>![Várias características de usuário definidas no Zeotap, como idioma, cidade, aniversário e outras.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Entrada de dados personalizados** — Adicione dados personalizados mapeados ao campo relevante do Zeotap e envie para a Braze.<br>![Selecionando "loyalty_points" como a característica do usuário no Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Atributos suportados {#supported-attributes}
Você pode encontrar detalhes de todos os campos da Braze nesta seção.

| Campo da Braze | Tipo de mapeamento | Descrição |
| --- | --- | --- |
| ID externo | Seleção suspensa | Este é o `User ID` persistente definido pela Braze para rastrear usuários em dispositivos e plataformas. Recomendamos que você mapeie `User ID` para `External ID`; caso contrário, o Zeotap poderá enviar e-mail como um alias de usuário.<br><br>O Zeotap recomenda mapear o `hashed email` disponível no Zeotap Catalogue para o `External ID`. |
| E-mail | Mapeamento estático | É mapeado para `Email Raw` no Zeotap Catalogue. |
| Telefone | Mapeamento estático | É mapeado para `Mobile Raw` no Zeotap Catalogue.<br><br>• A Braze aceita números de telefone no formato `E.164`. O Zeotap não realiza nenhuma transformação. Portanto, é necessário que você faça a ingestão dos números de telefone no formato prescrito. Para saber mais, consulte [Números de telefone do usuário]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers). |
| Nome | Mapeamento estático | É mapeado para `First Name` no Zeotap Catalogue. |
| Sobrenome | Mapeamento estático | É mapeado para `Last Name` no Zeotap Catalogue. |
| Gênero | Mapeamento estático | É mapeado para `Gender` no Zeotap Catalogue. |
| Nome do evento personalizado | Mapeamento estático | É mapeado para `Event Name` no Zeotap Catalogue.<br><br>Tanto o nome do evento personalizado quanto o registro de data e hora do evento personalizado devem ser mapeados para capturar eventos personalizados na Braze. O evento personalizado não poderá ser processado se um deles não estiver mapeado. Para saber mais, consulte o [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Registro de data e hora do evento personalizado | Mapeamento estático | É mapeado para o `Event Timestamp` no Zeotap Catalogue.<br><br>Tanto o nome do evento personalizado quanto o registro de data e hora do evento personalizado devem ser mapeados para capturar eventos personalizados na Braze. O evento personalizado não poderá ser processado se um deles não estiver mapeado. Para saber mais, consulte o [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Inscrição de e-mail | Seleção suspensa | Faça a integração de um campo `Email Marketing Preference` e mapeie para ele.<br><br>O Zeotap envia os três valores a seguir:<br>• `opted_in` — indica que o usuário se registrou explicitamente para a preferência de marketing por e-mail<br>• `unsubscribed` — indica que o usuário optou explicitamente por não receber mensagens de e-mail<br>• `subscribed` — indica que o usuário nem aceitou nem recusou |
| Inscrição de push | Seleção suspensa | Faça a integração de um campo `Push Marketing Preference` e mapeie para ele.<br><br>O Zeotap envia os três valores a seguir:<br>• `opted_in` — indica que o usuário se registrou explicitamente para a preferência de marketing por push<br>• `unsubscribed` — indica que o usuário optou explicitamente por não receber mensagens de push<br>• `subscribed` — indica que o usuário nem aceitou nem recusou |
| Ativar o rastreamento de aberturas de e-mail | Seleção suspensa | Mapeie o campo relevante `Marketing Preference`.<br><br>Quando definido como true, ativa um pixel de rastreamento de abertura a ser adicionado a todos os futuros e-mails enviados a esse usuário. |
| Ativar o rastreamento de cliques de e-mail | Seleção suspensa | Mapeie o campo relevante `Marketing Preference`.<br><br>Quando definido como true, ativa o rastreamento de cliques para todos os links em todos os futuros e-mails enviados a esse usuário. |
| ID do produto | Seleção suspensa | • Identificador de uma ação de compra `(Product Name/Product Category)`. Para mais detalhes, consulte o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object).<br>• Faça a integração do atributo relevante no Zeotap Catalogue e mapeie para ele.<br><br>`Product ID`, `Currency` e `Price` devem ser mapeados obrigatoriamente para capturar eventos de compra na Braze. O evento de compra não poderá ser realizado se algum dos três for esquecido. Para saber mais, consulte o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-object). |
| Moeda | Seleção suspensa | • Atributo de moeda para a ação de compra.<br>• O formato suportado é `ISO 4217 Alphabetic Currency Code`.<br>• Faça a integração de dados de moeda corretamente formatados no Zeotap Catalogue e mapeie para ele.<br><br>`Product ID`, `Currency` e `Price` devem ser mapeados obrigatoriamente para capturar eventos de compra na Braze. O evento de compra não poderá ser realizado se algum dos três for esquecido. |
| Preço | Seleção suspensa | • Atributo de preço para a ação de compra.<br>• Faça a integração do atributo relevante no Zeotap Catalogue e mapeie para ele.<br><br>`Product ID`, `Currency` e `Price` devem ser mapeados obrigatoriamente para capturar eventos de compra na Braze. O evento de compra não poderá ser realizado se algum dos três for esquecido. |
| Quantidade | Seleção suspensa | • Atributo de quantidade para a ação de compra.<br>• Faça a integração do atributo relevante no Zeotap Catalogue e mapeie para ele. |
| País | Seleção suspensa | Mapeie para o campo `Country` do Catalogue que você está integrando. |
| Cidade | Seleção suspensa | Mapeie para o campo `City` do Catalogue que você está integrando. |
| Idioma | Seleção suspensa | • O formato aceito é o padrão `ISO-639-1` (por exemplo, en).<br>• Faça a integração do idioma formatado corretamente e mapeie para ele. |
| Data de nascimento | Seleção suspensa | Mapeie para o campo `Date of Birth` que você está integrando. |
| Atributo personalizado | Entrada de dados personalizados | Mapeie qualquer atributo de usuário para uma entrada de dados personalizada, que é então enviada à Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos suportados" }

## Visualização de dados no console da Braze {#viewing-data-on-braze-console}

Depois que você mapear os atributos relevantes a serem enviados e publicados no fluxo de trabalho, os eventos começarão a fluir para a Braze com base nos critérios definidos. É possível pesquisar por ID de e-mail ou ID externo no console da Braze.

![Visualização do perfil de usuário na Braze mostrando atributos e eventos recebidos do Zeotap.]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Vários atributos estão em diferentes seções do dashboard de usuário na Braze.
- A guia **Profile** contém os atributos do usuário.
- A guia **Custom Attributes** contém os atributos personalizados definidos pelo usuário.
- A guia **Custom Events** contém os eventos personalizados definidos pelo usuário.
- A guia **Purchases** contém as compras feitas pelo usuário durante um período de tempo.

## Criação de campanhas {#campaign-creation}

Os usuários podem criar campanhas na Braze e ativar usuários em tempo real ou com base no horário programado. As campanhas podem ser disparadas com base nas ações realizadas pelo usuário (evento personalizado, compra) ou nos atributos do usuário.