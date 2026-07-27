---
nav_title: Perfis de usuário
article_title: Perfis de usuário
page_order: 2
page_type: reference
tool:
  - Dashboard
description: "Este artigo de referência descreve como acessar o perfil de um usuário no dashboard, casos de uso de perfis e o que cada perfil contém."

---

# Perfis de usuário {#user-profiles}

> Os perfis de usuário são uma ótima maneira de encontrar informações sobre usuários específicos. Todos os dados persistentes associados a um usuário são armazenados em seu perfil de usuário.

## Acessar perfis {#access-profiles}

Para acessar o perfil de um usuário, acesse a página **Search Users** e pesquise um usuário por qualquer um dos seguintes critérios:

- ID de usuário externo
- ID da Braze
- E-mail
- Número de telefone
- Token por push
- Alias de usuário no formato "[user_alias]:[alias_name]", como "amplitude_id:user_123"

Se uma correspondência for encontrada, você poderá visualizar as informações registradas para esse usuário com o SDK da Braze. Caso contrário, se a pesquisa retornar vários perfis de usuário, você poderá mesclar cada perfil individualmente ou realizar uma mesclagem de usuários em massa. Para um passo a passo completo, consulte [Mesclar usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

{% alert note %}
**Search Users** não é o mesmo que **User Lookup** no criador de Segment ou Campaign. **User Lookup** testa se um usuário específico corresponde ao seu público e aceita apenas `external_id` ou `braze_id`. **Search Users** nesta página aceita e-mail, telefone, token por push e alias de usuário. Para saber mais, consulte [Testando segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).
{% endalert %}

{% alert important %}
Quando um número de telefone é usado na pesquisa, ele é convertido para o formato [`E.164`](https://en.wikipedia.org/wiki/e.164). Usuários cujos números de telefone não podem ser convertidos para o formato `E.164` (por exemplo, porque o número de telefone tem um código de país ou código de área inválido) não podem ser pesquisados por número de telefone.
{% endalert %}

![Resultados da pesquisa com um banner que diz "Multiple users match your search criteria" e dois botões rotulados Previous e Next.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Casos de uso {#use-cases}

Os perfis de usuário são um ótimo recurso para solução de problemas e testes, pois você pode acessar facilmente informações sobre o histórico de engajamento, a associação a Segments, o dispositivo e o sistema operacional de um usuário.

Por exemplo, se um usuário relatar um problema e você não tiver certeza de qual dispositivo e sistema operacional ele está usando, você pode usar a [guia Visão geral](#overview-tab) para encontrar essa informação (desde que você tenha o e-mail ou o ID do usuário). Você também pode visualizar o idioma de um usuário, o que pode ser útil se estiver solucionando problemas em uma [campanha multilíngue]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) que não se comportou como esperado.

Você pode usar a [guia Engajamento](#engagement-tab) para verificar se um determinado usuário recebeu uma Campaign. Além disso, se esse usuário específico recebeu a Campaign, você pode ver quando ele a recebeu. Também é possível verificar se um usuário está em um determinado Segment e se ele aceitou receber push, e-mail ou ambos. Essas informações são úteis para fins de solução de problemas. Por exemplo, você deve verificar essas informações se um usuário não receber uma Campaign que você esperava que ele recebesse ou se receber uma Campaign que você não esperava que ele recebesse.

## Elementos do perfil de usuário {#elements-of-user-profile}

Existem cinco seções principais no perfil de um usuário.

- **Visão geral:** Informações básicas sobre o usuário, dados de sessão, atributos personalizados, eventos personalizados, compras e o dispositivo mais recente em que o usuário fez login.
- **Engajamento:** Informações sobre as configurações de contato do usuário, Campaigns recebidas, Segments, estatísticas de comunicação, atribuição de instalação e número de bucket aleatório.
- **Histórico de eventos:** Eventos personalizados e compras dos últimos 30 dias, com propriedades completas do evento exibidas em JSON.
- **Histórico de mensagens:** Eventos recentes relacionados a mensagens para este usuário nos últimos 30 dias.
- **Elegibilidade para Feature Flags:** Valide para quais Feature Flags um usuário é atualmente elegível em rollouts, etapas do canva e experimentos.

{% tabs %}
{% tab Guia Visão geral %}

### Guia Visão geral {#overview-tab}

A guia **Visão geral** contém informações básicas sobre um usuário e suas interações com seu app ou website.

| Categoria da visão geral | Contém |
| --- | --- |
| Perfil | Gênero, faixa etária, localização, idioma, localidade, fuso horário e data de nascimento. |
| Visão geral das sessões | Quantas sessões o usuário teve, quando foram a primeira e a última sessão e em quais apps. |
| Atributos personalizados | Quais atributos personalizados estão atribuídos a este usuário e seus valores associados, incluindo atributos personalizados aninhados. |
| Dispositivos recentes | Em quantos dispositivos o usuário fez login, detalhes de cada dispositivo e seus IDs de publicidade associados (se houver). |
| Eventos personalizados | Quais eventos personalizados este usuário realizou, quantas vezes e quando realizou cada evento pela última vez. |
| Compras | Receita total atribuída a este usuário, sua última compra, número total de compras e uma lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Visão geral #overview-tab" }

Para saber mais sobre esses dados, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

{% endtab %}
<a id="engagement-tab"></a>
{% tab Guia Engajamento %}

### Guia Engajamento {#engagement-tab}

A guia **Engajamento** contém informações sobre as interações de um usuário com as mensagens que você enviou usando a Braze.

| Categoria de engajamento | Contém |
| --- | --- |
| Configurações de contato | Status de inscrição para e-mail, SMS e push, e os grupos de inscrições aos quais este usuário está associado para esses três canais. Esta seção também inclui informações de changelog para tokens por push. Consulte [e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) e [push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) para informações sobre como inscrições e aceitações são configuradas. |
| Campaigns recebidas | **Campaigns recebidas** reflete o momento de envio e visualização específico de cada canal. A maioria dos canais registra um envio quando a Braze passa a mensagem para o provedor de entrega, mesmo quando a mensagem não é efetivamente entregue. **Content Cards** são diferentes: as Campaigns aparecem aqui somente depois que o usuário visualiza o cartão no app. Para um detalhamento por canal, consulte [Quando as Campaigns aparecem em Campaigns recebidas](#when-campaigns-appear-in-campaigns-received). <br><br>Quando uma mensagem é recebida, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal do perfil que registrou a interação (por exemplo, o mesmo endereço de e-mail para e-mail, ou o mesmo número de telefone para SMS ou WhatsApp). Usuários que compartilham um identificador com alguém que recebeu, abriu ou clicou na mensagem podem corresponder a esse filtro mesmo que não estivessem originalmente na Campaign ou não tenham recebido a mensagem diretamente.<br><br>Essas listas usam [dados de interação com mensagens]({{site.baseurl}}/api/data_retention/messaging_interaction_data) (incluindo regras de expiração) para determinar o que aparece para redirecionamento e histórico.<br><br> Selecione uma Campaign da lista para visualizá-la. |
| Segments | Segments nos quais este usuário está incluído. Selecione um Segment da lista para visualizá-lo. |
| Estatísticas de comunicação | Quando este usuário recebeu mensagens suas pela última vez em cada canal. |
| Atribuição de instalação | Informações sobre como e quando um usuário instalou seu app. Saiba mais sobre [entender as instalações de usuários]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution). |
| Diversos | O [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) do usuário. |
| Mensagens de Canvas recebidas | Mensagens de Canvas que este usuário recebeu e quando. O momento de envio segue as mesmas regras de canal de **Campaigns recebidas**; consulte [Quando as Campaigns aparecem em Campaigns recebidas](#when-campaigns-appear-in-campaigns-received).<br><br> Quando uma mensagem é recebida, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal do perfil que registrou a interação (por exemplo, o mesmo endereço de e-mail para e-mail, ou o mesmo número de telefone para SMS ou WhatsApp). Usuários que compartilham um identificador com alguém que recebeu, abriu ou clicou na mensagem podem corresponder a esse filtro mesmo que não estivessem originalmente na Campaign ou não tenham recebido a mensagem diretamente.<br><br> Selecione uma mensagem da lista para visualizá-la. |
| Previsões | Pontuações de [previsão de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) e [previsão de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) para este usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Engajamento" }

{% endtab %}
<a id="event-history-tab"></a>
{% tab Guia Histórico de eventos %}

### Guia Histórico de eventos {#event-history-tab}

{% alert note %}
Para visualizar a guia **Histórico de eventos**, você precisa das [permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) **Search Users**, **View User Event Properties** e **View PII**, pois as propriedades de eventos podem conter dados pessoais.
{% endalert %}

A guia **Histórico de eventos** mostra os eventos personalizados e as compras que um usuário registrou. Use-a para verificar se os dados de eventos estão chegando corretamente e solucionar problemas no nível do usuário diretamente no dashboard — sem necessidade de exportações de dados ou ferramentas externas.

| Categoria do histórico de eventos | Contém |
| --- | --- |
| Lista de eventos | Eventos personalizados e compras dos últimos 30 dias (até os 100 mais recentes), ordenados do mais recente para o mais antigo. |
| Tipo de evento | Se a linha é um **Evento personalizado** ou **Compra**. |
| Timestamp | Quando o evento foi registrado. |
| Nome do evento | O nome do evento personalizado ou da compra. |
| Propriedades do evento | Propriedades completas do evento, exibidas em JSON. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Histórico de eventos" }

{% endtab %}
{% endtabs %}

### Quando as Campaigns aparecem em Campaigns recebidas {#when-campaigns-appear-in-campaigns-received}

De modo geral, a Braze lista uma Campaign em **Campaigns recebidas** após tentar enviar a mensagem. Uma entrega ao dispositivo ou caixa de entrada do usuário não é necessária para que um envio seja registrado. **Mensagens de Canvas recebidas** segue as mesmas regras específicas de canal para cada tipo de mensagem de Canvas.

{% alert tip %}
Quando os timestamps são exibidos em formato relativo (como "6 dias atrás"), passe o cursor sobre eles para ver a data e hora exatas.
{% endalert %}

- **E-mail:** A Braze registra um envio quando a mensagem é entregue ao seu provedor de serviços de e-mail (ESP). Após essa entrega, a mensagem não é interrompida por causa de lógica Liquid, limite de frequência ou por o usuário estar marcado como inalcançável. Os próximos eventos geralmente são uma entrega ou um bounce.
- **Push:** A Braze registra um envio quando a mensagem é entregue ao provedor de push (por exemplo, serviço de Notificações por Push da Apple (APN) ou Firebase Cloud Messaging (FCM)). O provedor geralmente tenta entregar imediatamente; se o dispositivo estiver indisponível (por exemplo, offline), o provedor pode tentar novamente até que a mensagem expire.
- **Mensagens no app:** A Braze registra um envio quando a Campaign é lançada.
- **Content Cards:** Quando a Braze registra um evento _Sent_ depende do tipo de entrega e da sua configuração de **Card Creation**. Uma Campaign de Content Cards aparece em **Campaigns recebidas** no perfil do usuário somente depois que o usuário visualiza o cartão no app. Para o detalhamento completo, consulte [Quando os envios são registrados]({{site.baseurl}}/user_guide/channels/content_cards/reporting#when-sends-are-logged) e [Campaigns recebidas e filtros de redirecionamento]({{site.baseurl}}/user_guide/channels/content_cards/reporting#campaigns-received-and-retargeting-filters) no artigo de relatórios de Content Cards.
- **SMS, WhatsApp e webhooks:** A Braze registra um envio quando a mensagem entra no caminho de entrega daquele canal (por exemplo, o provedor de SMS ou WhatsApp, ou seu endpoint de webhook).

{% alert note %}
Essas descrições cobrem quando um envio é registrado para **Campaigns recebidas**. Elas são separadas das [interrupções de mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) que podem interromper uma mensagem antes que ela chegue a um provedor.
{% endalert %}

![A guia Engajamento de um perfil de usuário exibindo suas configurações de contato e estatísticas de comunicação.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Guia Histórico de mensagens {#messaging-history-tab}

A guia **Histórico de mensagens** do perfil do usuário mostra eventos recentes relacionados a mensagens (cerca de 40) para um usuário individual nos últimos 30 dias. Esses eventos incluem as mensagens que o usuário recebeu, com as quais interagiu e mais.

Os dados nesta guia não são atualizados após a mesclagem de um usuário. Além disso, quaisquer eventos associados a mensagens enviadas via API (por exemplo, o [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#creating-new-users-with-api-sends)) não aparecem nesta guia se não houver um ID de Campaign especificado nesses envios.

{% alert important %}
Na guia **Histórico de mensagens**, os eventos de RCS são incluídos junto com os eventos de SMS. Os eventos de RCS não aparecem separadamente.
{% endalert %}

![A guia Histórico de mensagens mostrando quais Campaigns e Canvas um usuário recebeu.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Visualizar e entender eventos {#viewing-and-understanding-events}

Para cada evento na tabela **Histórico de mensagens**, você pode ver o canal de envio de mensagens, o tipo de evento, o timestamp em que o evento ocorreu, a Campaign ou mensagem de Canvas associada e os dados do dispositivo do usuário. Para filtrar eventos específicos, clique em **Filtros** e selecione os eventos da lista.

##### Eventos de engajamento com mensagem {#message-engagement-events}

Os seguintes eventos de engajamento com mensagem estão disponíveis para e-mail, SMS, push, mensagens no app, Content Cards e webhooks. Para saber mais sobre como eventos específicos são rastreados, consulte o [Glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

| Canal | Eventos de engajamento disponíveis |
| --- | --- |
| E-mail | Bounce<br>Clique<br>Eventos de adiamento<br>Entrega<br>Marcar como SPAM<br>Abertura (veja a [nota sobre o evento de abertura de e-mail](#note-on-email-open-event))<br>Envio<br>Soft bounce<br>Cancelar inscrição |
| SMS | Envio pela operadora<br>Entrega<br>Falha na entrega<br>Recebimento de entrada<br>Rejeição<br>Envio |
| Push | Bounce<br>Abertura influenciada<br>iOS Foreground<br>Abertura<br>Envio |
| Mensagem no app | Clique<br>Impressão |
| Content Cards | Clique<br>Dispensar<br>Impressão<br>Envio |
| Webhooks | Envio |
| WhatsApp | Interrupção<br>Entrega<br>Falha<br>Limite de frequência<br>Recebimento de entrada<br>Leitura<br>Envio |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de engajamento com mensagem" }

##### Eventos de interrupção de mensagem {#message-abort-events}

Eventos de interrupção de mensagem ocorrem quando uma mensagem enviada a um usuário foi interrompida devido à lógica condicional em [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) ou [Conteúdo Conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content), ou por timeouts de renderização Liquid.

Eventos de interrupção estão disponíveis para os seguintes canais:

- E-mail
- SMS
- Push
- Webhooks

Eventos de interrupção não estão disponíveis atualmente para mensagens no app e Content Cards.

##### Eventos de limite de frequência {#frequency-cap-events}

Um evento de limite de frequência ocorre quando um usuário é qualificado para receber uma mensagem, mas não a recebe efetivamente devido às configurações de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). Você pode personalizar as configurações de limite de frequência em **Configurações** > **Regras de limite de frequência**.

##### Destinos em branco {#blank-destinations}

Alguns envios de mensagens podem aparecer no Histórico de mensagens com destinos em branco (indicados por "—"). Isso ocorre porque alguns canais, como Content Cards e webhooks, não coletam dados do dispositivo no envio da mensagem.

Os envios de Content Cards são registrados quando o cartão está disponível para ser visualizado. Como Content Cards podem ser visualizados em vários dispositivos, os dados do dispositivo não são registrados no envio. Em vez disso, essas informações são registradas na impressão (quando o cartão é efetivamente visualizado). Webhooks são enviados para um endpoint de sistema (não para um dispositivo), portanto os dados do dispositivo não se aplicam.

#### Nota sobre o evento de abertura de e-mail {#note-on-email-open-event}

O rastreamento de abertura de e-mail é propenso a erros em qualquer ferramenta, incluindo a Braze. Com a variedade de recursos de proteção de privacidade oferecidos por diferentes clientes de e-mail que bloqueiam o carregamento automático de imagens ou as carregam proativamente no servidor, os eventos de abertura de e-mail são suscetíveis tanto a falsos positivos quanto a falsos negativos.

Embora as estatísticas de abertura de e-mail possam ser úteis em agregado, por exemplo, para comparar a eficácia de diferentes linhas de assunto, você não deve presumir que um evento de abertura individual para um usuário individual seja significativo.

#### Por que certos campos estão em branco na guia Histórico de mensagens? {#why-are-certain-fields-blank-in-the-message-history-tab}

Alguns campos podem estar ausentes na guia **Histórico de mensagens** de um usuário nos seguintes cenários:

- Quando um evento não possui dados para **Mensagem enviada**, isso indica que a Campaign não tem variações de mensagem.
- Quando um evento não possui dados para **Campaign/Canvas** e **Mensagem enviada**, isso indica que essa mensagem foi enviada por uma Campaign de API (não Campaigns disparadas por API) que não especificou o `campaign_id` e o `message_variation_id`. Esses campos são opcionais e podem ser omitidos do corpo da requisição. Quando esses campos são especificados, essas informações são preenchidas nos registros do histórico de mensagens.
   - Se uma mensagem específica estiver ausente do histórico de mensagens, mas aparecer no registro de **Campaigns recebidas**, é provável que o usuário tenha recebido a Campaign antes de ser identificado como o usuário atual. Se um perfil existente for órfão, o registro de **Campaigns recebidas** é transferido, mas o histórico de mensagens não.
- Quando os dados estão ausentes para **Campaign/Canvas**, um teste manual pode ter sido enviado. Testes manuais são registrados na guia **Histórico de mensagens**, mas a Campaign ou Canvas que foi enviada não será registrada.
- Quando um usuário está em um grupo de teste ou outro público de teste interno, o **Histórico de mensagens** pode exibir metadados limitados de Campaign ou Canvas em comparação com envios de produção.

## Artigos relacionados {#related-articles}

- [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [POST: Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [POST: Excluir usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)