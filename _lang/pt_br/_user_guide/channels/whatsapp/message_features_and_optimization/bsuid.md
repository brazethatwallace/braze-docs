---
nav_title: Nomes de usuário e BSUID
article_title: Nomes de usuário e IDs de usuário com escopo de negócio do WhatsApp
page_order: 7
description: "Saiba como os nomes de usuário do WhatsApp e os IDs de usuário com escopo de negócio (BSUIDs) afetam a identificação de usuários, o envio de mensagens e o tratamento de dados na Braze."
page_type: reference
alias: "/whatsapp_usernames/"
channel:
  - WhatsApp
hidden: true
noindex: true
---

# Nomes de usuário e IDs de usuário com escopo de negócio do WhatsApp {#whatsapp-usernames-and-business-scoped-user-ids}

> Em junho de 2026, o WhatsApp planeja introduzir nomes de usuário: um recurso opcional de privacidade que oculta os números de telefone dos usuários ao enviar mensagens para empresas. A Braze está totalmente preparada para lidar com essa mudança; para a maioria dos clientes, nada nas suas Campaigns ou Canvas precisa mudar.

{% alert important %}
Os nomes de usuário do WhatsApp e os IDs de usuário com escopo de negócio (BSUIDs) devem ser lançados em junho de 2026, com as atualizações da Braze programadas para acompanhar esse lançamento. As atualizações da Braze descritas neste artigo **ainda não** foram lançadas.
{% endalert %}

Quando os usuários do WhatsApp adotam um nome de usuário, seu número de telefone deixa de ser compartilhado automaticamente com as empresas para as quais enviam mensagens. Em vez disso, o WhatsApp fornece às empresas um ID de usuário com escopo de negócio (BSUID), um identificador único específico para cada par de portfólio de negócios e usuário.

A Braze lidará com os BSUIDs automaticamente. Os usuários que adotarem um nome de usuário continuarão aparecendo no seu espaço de trabalho da Braze, recebendo mensagens, acionando Canvas e gerando eventos. Alguns clientes podem precisar [se preparar para a mudança](#how-to-prepare-for-the-change).

## ID de usuário com escopo de negócio (BSUID) {#business-scoped-user-id-bsuid}

Um BSUID é um identificador único e persistente que o WhatsApp atribui para representar um usuário dentro do seu portfólio de negócios específico. Pense nele como um número de telefone alternativo para usuários que optam por manter seu número de telefone privado.

Os BSUIDs têm três características principais:

| Característica | Descrição |
| ----- | ----- |
| Único | Dois usuários não compartilham o mesmo BSUID dentro do seu portfólio de negócios. |
| Com escopo de negócio | O mesmo usuário terá um BSUID diferente com cada empresa para a qual envia mensagens. Os BSUIDs não podem ser compartilhados ou comparados entre portfólios de negócios diferentes. |
| Disponível em webhooks | Os BSUIDs são incluídos em todas as mesmas cargas úteis de webhook que atualmente contêm o número de telefone do usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ID de usuário com escopo de negócio (BSUID)" }

## Mudanças nos tipos de usuário do WhatsApp {#changes-to-whatsapp-user-types}

Após o lançamento dos nomes de usuário do WhatsApp, haverá dois tipos de usuários do WhatsApp:

| Tipo de usuário | Identificação no WhatsApp | O que a Braze recebe |
| ----- | ----- | ----- |
| Usuários sem nome de usuário | Número de telefone (sem alteração) | Número de telefone (sem alteração) |
| Usuários com nome de usuário | Nome de usuário (exibido), BSUID (backend) | BSUID, número de telefone para usuários que já têm uma conversa existente com sua empresa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mudanças nos tipos de usuário do WhatsApp" }

A principal diferença é que um usuário que adota um nome de usuário compartilha seu número de telefone com sua empresa apenas se você já teve uma conversa anterior com ele ou se ele aparece no seu Catálogo de Contatos do WhatsApp.

## Como a Braze lida com BSUIDs {#how-braze-will-handle-bsuids}

A Braze armazenará os BSUIDs como um [alias de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) com o rótulo `whats_app_bsuid` no perfil de usuário. Isso significa que usuários somente com BSUID terão perfis de usuário completos na Braze e poderão entrar em Canvas, receber mensagens, gerar eventos e ser atualizados pela API or interface de programação do aplicativo (API).

### Enviar mensagens {#send-messages}

Quando a Braze envia uma mensagem pelo WhatsApp, ela usa o número de telefone, se houver um disponível. Se o usuário tiver apenas um BSUID (como um usuário que envia a primeira mensagem para você após adotar um nome de usuário), a Braze enviará usando o BSUID. Nenhuma alteração nos seus modelos de mensagem, Campaigns ou etapas do Canvas é necessária.

### Mensagens recebidas e disparadores de Canvas {#inbound-messages-and-canvas-triggers}

Quando um usuário com nome de usuário envia uma mensagem recebida pelo WhatsApp, a Braze irá:

1. Buscar o usuário pelo BSUID ou número de telefone (o que estiver disponível no webhook).
2. Se nenhum usuário correspondente for encontrado, criar um novo perfil de usuário anônimo com o BSUID armazenado como alias de usuário.
3. Disparar qualquer Canvas ou Campaign configurado para iniciar com uma mensagem recebida pelo WhatsApp.

### Perfil de usuário {#user-profile}

Você poderá ver o BSUID de um usuário no perfil de usuário da Braze, na seção do WhatsApp.

![Perfil de usuário com uma seção do WhatsApp que contém o ID de usuário com escopo de negócio.]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### Grupos de inscrições {#subscription-groups}

O gerenciamento de grupos de inscrições funcionará da mesma forma para usuários com BSUID e para qualquer usuário identificado por um alias de usuário. Você pode atualizar o status de inscrição de usuários com BSUID por meio de:

- O [endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) usando `user_alias`
- A etapa [User Update]({{site.baseurl}}/user_update) do Canvas (funciona automaticamente)
- Upload de CSV

{% alert note %}
O [endpoint subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) não oferecerá suporte a [`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object). Use o [endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar o status de inscrição de usuários somente com BSUID.
{% endalert %}

### Currents e dados de eventos {#currents-and-event-data}

Todos os eventos do WhatsApp no Currents (envio, entrega, leitura, falha, recebimento, interrupção, nova tentativa) incluirão um campo de BSUID. Para usuários que possuem tanto um número de telefone quanto um BSUID, ambos os campos serão incluídos. Para usuários que possuem apenas um BSUID, somente o campo de BSUID será incluído (o campo de número de telefone ficará vazio).

## Como se preparar para a mudança {#how-to-prepare-for-the-change}

Para a maioria dos clientes, nenhuma ação é necessária. A Braze lidará automaticamente com o roteamento de BSUID, a criação de usuários e o rastreamento de eventos. No entanto, recomendamos [ativar o Catálogo de Contatos do WhatsApp](#enable-whatsapp-contact-book) e [vincular portfólios de negócios](#link-business-portfolios-if-you-use-multiple-wabas) se você usa múltiplas Contas do WhatsApp Business (WABAs).

### Ativar o Catálogo de Contatos do WhatsApp {#enable-whatsapp-contact-book}

O Catálogo de Contatos é um recurso da Meta que registra números de telefone de usuários com os quais você já conversou. Quando um usuário adota um nome de usuário, o número de telefone dele permanece visível para a sua empresa se ele aparecer no seu Catálogo de Contatos. Isso significa que a Braze pode continuar identificando usuários pelo número de telefone mesmo depois que eles ativaram um nome de usuário.

Para ativar o Catálogo de Contatos:

1. Acessar **Meta Business Suite** > **Configurações de negócios** > **Informações do negócio**.
2. Confirme que o recurso Catálogo de Contatos está ativado.

{% alert tip %}
O recurso Catálogo de Contatos está ativado por padrão, mas recomendamos confirmar isso nas configurações do Meta Business. Se o Catálogo de Contatos estiver desativado, os usuários que adotarem nomes de usuário aparecerão como novos usuários somente com BSUID, mesmo que você já tenha enviado mensagens a eles anteriormente.
{% endalert %}

### Vincular portfólios de negócios se você usa múltiplas WABAs {#link-business-portfolios-if-you-use-multiple-wabas}

Os BSUIDs são vinculados a um único portfólio de negócios. Se a sua organização gerencia WABAs de múltiplos portfólios de negócios dentro do mesmo espaço de trabalho da Braze, o mesmo usuário terá um BSUID diferente para cada portfólio. Isso pode resultar em perfis de usuário duplicados na Braze.

Para evitar isso, entre em contato com o seu ponto de contato na Meta para verificar se a sua empresa é elegível para vincular portfólios. Consulte [Vincular portfólios de negócios e BSUIDs principais](#link-business-portfolios-and-parent-bsuids) para mais detalhes.

Se todas as suas WABAs estiverem dentro do mesmo portfólio de negócios, nenhuma ação é necessária.

## Vincular portfólios de negócios e BSUIDs principais {#link-business-portfolios-and-parent-bsuids}

Se sua organização opera múltiplas contas do WhatsApp Business (WABAs) em diferentes portfólios de negócios, você pode pedir ao seu ponto de contato na Meta para verificar se sua empresa é elegível para vincular esses portfólios. A elegibilidade é determinada pela Meta e está disponível para empresas gerenciadas.

### Comportamento de portfólios vinculados {#linked-portfolio-behavior}

Quando seus portfólios de negócios estão vinculados, o WhatsApp incluirá um BSUID principal em todos os webhooks de mensagem junto com o BSUID regular. O BSUID principal será atribuído a uma nova propriedade `parent_user_id` na carga útil do webhook.

Os BSUIDs principais têm as mesmas propriedades dos BSUIDs regulares, mas serão compartilhados entre todos os números de telefone comerciais dentro do seu conjunto de portfólios vinculados. Isso significa que o mesmo usuário terá um único identificador consistente, independentemente da WABA para a qual ele envia mensagens, evitando o risco de perfis de usuário duplicados.

Um BSUID principal inclui `ENT` entre o código do país e o identificador alfanumérico. Por exemplo:

```
US.ENT.11815799212886844830
```

Um BSUID regular não inclui `ENT`.

### Como a Braze usa os BSUIDs principais {#how-braze-uses-parent-bsuids}

Quando um webhook contém tanto um BSUID regular quanto um BSUID principal, a Braze usará o BSUID principal como identificador primário. Isso permite que um usuário que envia mensagens por meio de múltiplas WABAs nos seus portfólios vinculados seja consistentemente associado ao mesmo perfil de usuário na Braze.

Se nenhum BSUID principal estiver presente (por exemplo, porque seus portfólios não estão vinculados ou o usuário está enviando mensagens para uma WABA não vinculada), a Braze usará o BSUID regular. Os BSUIDs regulares continuarão a funcionar normalmente em todos os casos.

{% alert note %}
A Meta gerencia o processo de vinculação de portfólios de negócios. Para começar, entre em contato com seu ponto de contato na Meta. Você ainda poderá enviar mensagens aos usuários usando o BSUID regular, mesmo que seus portfólios estejam vinculados; os BSUIDs principais são complementares, não substitutos.
{% endalert %}

| Cenário | Identificador usado pela Braze |
| ----- | ----- |
| Portfólio de negócios único | BSUID regular |
| Múltiplos portfólios vinculados | BSUID principal (preferencial). Se nenhum BSUID principal existir, usa o BSUID regular |
| Múltiplos portfólios não vinculados | BSUID regular (pode resultar em perfis de usuário duplicados por portfólio) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Como a Braze usa os BSUIDs principais" }

## Perguntas frequentes {#frequently-asked-questions}

### Minhas Campaigns e Canvas existentes vão parar de funcionar quando os nomes de usuário do WhatsApp forem lançados? {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

Não. Campaigns e Canvas existentes continuarão funcionando. Usuários que não adotarem um nome de usuário não serão afetados de forma alguma. Para usuários que adotarem um nome de usuário e já tiverem um histórico de conversa com sua empresa, a Braze continua usando o número de telefone como identificador principal.

### O que acontece com um usuário que adota um nome de usuário, mas já enviou mensagens para minha empresa? {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

Se o seu Catálogo de Contatos do WhatsApp estiver ativado e você tiver uma conversa anterior com o usuário (ou tiver enviado uma mensagem para ele) nos últimos 30 dias, o número de telefone dele continuará aparecendo nas cargas úteis do webhook junto com o BSUID. A Braze fará a correspondência com o perfil de usuário existente. Nenhum perfil duplicado será criado.

### E se um usuário adotar um nome de usuário e não tiver nenhuma conversa anterior com minha empresa? {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

A Braze receberá o BSUID do usuário no webhook de entrada e fará a correspondência com um perfil de usuário existente (se você já tiver armazenado o BSUID dele) ou criará um novo perfil de usuário anônimo com o BSUID armazenado como alias de usuário. Esse usuário poderá então entrar em Canvas, receber mensagens de saída e ser identificado ou mesclado com outros perfis usando as ferramentas padrão de resolução de identidade da Braze.

### Posso segmentar usuários com BSUID em Segments? {#can-i-target-bsuid-users-in-segments}

Usuários com BSUID são perfis de usuário completos na Braze, então você pode Segment or segmentoá-los por meio de filtros de público padrão (como "recebeu uma mensagem do WhatsApp" ou associação a grupo de inscrições). No entanto, a segmentação especificamente por valores de BSUID (como "BSUID existe" ou "BSUID igual a X") não é suportada.

### Como funciona a precificação do WhatsApp para usuários com BSUID? {#how-does-whatsapp-pricing-work-for-bsuid-users}

A precificação de conversas do WhatsApp é determinada pelo país do usuário. Para usuários identificados por número de telefone, a Meta determina o país a partir do código de país do número. Para usuários identificados por BSUID, o país é codificado diretamente no próprio BSUID; por exemplo, um BSUID que começa com `US` representa um usuário nos Estados Unidos.

Isso significa que o comportamento de precificação é consistente independentemente de o usuário ser identificado por número de telefone ou BSUID. O país usado para calcular as taxas de conversa é determinado pelo identificador que a Meta fornece, e a Braze repassa essa informação sem modificação. Você não precisa fazer nada diferente, mas esteja ciente de que, ao enviar mensagens para usuários somente com BSUID, a precificação baseada em país da Meta é baseada no país codificado no BSUID do usuário, e não em um número de telefone.

### Como faço referência a um usuário com BSUID em chamadas de API or interface de programação do aplicativo (API)? {#how-do-i-reference-a-bsuid-user-in-api-calls}

Use o parâmetro `user_alias` com `alias_label: "whats_app_bsuid"` e `alias_name` definido como o valor do BSUID do usuário. Por exemplo:

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

Isso funciona com `users/track`, `users/identify`, upload de CSV e a etapa do canva de atualização de usuário.

### Meus pipelines de dados do Currents vão parar de funcionar? {#will-my-currents-data-pipelines-break}

Os eventos do Currents para WhatsApp incluem um campo `bsuid` junto com o campo de número de telefone existente. Para usuários que possuem apenas um BSUID, o campo de número de telefone estará vazio. Se seus pipelines downstream tiverem requisitos rígidos para o campo de número de telefone, confirme que eles conseguem lidar com um valor nulo ou vazio.

### Tenho vários WABAs em diferentes portfólios de negócios. O mesmo usuário aparecerá como dois perfis diferentes na Braze? {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

Sem portfólios vinculados, sim. O mesmo usuário do WhatsApp terá um BSUID diferente por portfólio de negócios, e a Braze criará perfis separados para cada um.

Para resolver isso, entre em contato com seu ponto de contato na Meta para verificar a elegibilidade para vinculação de portfólios. Quando vinculados, a Meta fornece um BSUID pai compartilhado entre todos os portfólios, e a Braze usará esse identificador para reconhecer consistentemente o usuário em todos os seus WABAs. Consulte [Vincular portfólios de negócios e BSUIDs pai](#link-business-portfolios-and-parent-bsuids) para mais detalhes.

### Posso desativar o Catálogo de Contatos? {#can-i-disable-the-contact-book}

Recomendamos fortemente manter o Catálogo de Contatos ativado. Se o Catálogo de Contatos for desativado, todos os registros históricos de número de telefone dos seus usuários serão perdidos. Usuários que adotaram nomes de usuário apareceriam então como novos usuários somente com BSUID, mesmo que você já tivesse enviado mensagens para eles anteriormente.

## Recursos adicionais {#additional-resources}

* [Configuração do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
* [Aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
* [Grupos de inscrições do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
* [Eventos do WhatsApp no Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#whatsapp-abort-events)
* [Meta: IDs de usuário com escopo de negócio](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)