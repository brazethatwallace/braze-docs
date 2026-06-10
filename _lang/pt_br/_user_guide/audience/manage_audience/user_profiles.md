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

Para acessar o perfil de um usuário, acesse a página **Pesquisar usuários** e pesquise um usuário por qualquer um dos seguintes critérios:

- ID de usuário externo
- ID da Braze
- E-mail
- Número de telefone
- Token por push
- Alias de usuário no formato "[user_alias]:[alias_name]", como "amplitude_id:user_123"

Se uma correspondência for encontrada, você poderá visualizar as informações que registrou para esse usuário com o SDK da Braze. Caso contrário, se a pesquisa retornar vários perfis de usuário, você poderá mesclar cada perfil individualmente ou realizar uma mesclagem de usuários em massa. Para um passo a passo completo, consulte [Mesclar usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/).

{% alert note %}
**Pesquisar usuários** não é o mesmo que **Busca de usuário** no criador de Segments ou Campaigns. **Busca de usuário** testa se um usuário específico corresponde ao seu público e aceita apenas `external_id` ou `braze_id`. **Pesquisar usuários** nesta página aceita e-mail, telefone, token por push e alias de usuário. Para saber mais, consulte [Testar segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#testing-segments).
{% endalert %}

{% alert important %}
Quando um número de telefone é usado na pesquisa, ele é convertido para o formato [`E.164`](https://en.wikipedia.org/wiki/e.164). Usuários cujos números de telefone não podem ser convertidos para o formato `E.164` (por exemplo, porque o número de telefone tem um código de país ou código de área inválido) não podem ser pesquisados por número de telefone.
{% endalert %}

![Resultados da pesquisa com um banner que diz "Vários usuários correspondem aos seus critérios de pesquisa" e dois botões rotulados Anterior e Próximo.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Casos de uso {#use-cases}

Os perfis de usuário são um ótimo recurso para solução de problemas e testes, pois você pode acessar facilmente informações sobre o histórico de engajamento de um usuário, associação a segmentos, dispositivo e sistema operacional.

Por exemplo, se um usuário relatar um problema e você não tiver certeza de qual dispositivo e sistema operacional ele está usando, você pode usar a [guia Visão geral](#overview-tab) para encontrar essas informações (desde que você tenha o e-mail ou o ID do usuário). Você também pode visualizar o idioma de um usuário, o que pode ser útil se estiver solucionando problemas de uma [campanha multilíngue]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/) que não se comportou como esperado.

Você pode usar a [guia Engajamento](#engagement-tab) para verificar se um determinado usuário recebeu uma Campaign. Além disso, se esse usuário específico recebeu a Campaign, você pode ver quando ele a recebeu. Você também pode verificar se um usuário está em um determinado Segment e se um usuário fez opt-in para push, e-mail ou ambos. Essas informações são úteis para fins de solução de problemas. Por exemplo, você deve verificar essas informações se um usuário não receber uma Campaign que você esperava que ele recebesse ou receber uma Campaign que você não esperava que ele recebesse.

## Elementos do perfil de usuário {#elements-of-user-profile}

Existem quatro seções principais no perfil de um usuário.

- **Visão geral:** Informações básicas sobre o usuário, dados de sessão, atributos personalizados, eventos personalizados, compras e o dispositivo mais recente em que o usuário fez login.
- **Engajamento:** Informações sobre as configurações de contato do usuário, Campaigns recebidas, Segments, estatísticas de comunicação, atribuição da instalação e número de bucket aleatório.
- **Histórico de mensagens:** Eventos recentes relacionados a mensagens para este usuário nos últimos 30 dias.
- **Elegibilidade para Feature Flags:** Valide para quais Feature Flags um usuário é atualmente elegível em rollouts, etapas do Canvas e experimentos.

### Guia Visão geral {#overview-tab}

A guia **Visão geral** contém informações básicas sobre um usuário e suas interações com seu app ou site.

| Categoria da visão geral | Contém |
| --- | --- |
| Perfil | Gênero, faixa etária, local, idioma, localização, fuso horário e data de nascimento. |
| Visão geral das sessões | Quantas sessões o usuário teve, quando foram a primeira e a última sessão e em quais apps. |
| Atributos personalizados | Quais atributos personalizados estão atribuídos a este usuário e seus valores associados, incluindo atributos personalizados aninhados. |
| Dispositivos recentes | Em quantos dispositivos o usuário fez login, detalhes de cada dispositivo e seus IDs de publicidade associados (se houver). |
| Eventos personalizados | Quais eventos personalizados este usuário realizou, quantas vezes e quando realizou cada evento pela última vez. |
| Compras | Lifetime Revenue atribuída a este usuário, sua última compra, número total de compras e uma lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Visão geral" }

Para saber mais sobre esses dados, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

![A guia Visão geral de um perfil de usuário.]({% image_buster /assets/img_archive/user_profile2.png %})

### Guia Engajamento {#engagement-tab}

A guia **Engajamento** contém informações sobre as interações de um usuário com as mensagens que você enviou usando a Braze.

| Categoria de engajamento | Contém |
| --- | --- |
| Configurações de contato | Status de inscrição para e-mail, SMS e push, e os grupos de inscrições aos quais este usuário está associado para esses três canais. Esta seção também inclui informações de changelog para tokens por push. Consulte [e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) e [push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states/) para informações sobre como inscrições e opt-ins são configurados. |
| Campaigns recebidas | **Campaigns recebidas** reflete o momento de envio e visualização específico de cada canal. A maioria dos canais registra um envio quando a Braze passa a mensagem para o provedor de entrega, mesmo que a mensagem não seja entregue no final. **Content Cards** são diferentes: as Campaigns aparecem aqui somente depois que o usuário visualiza o cartão no app. Para um detalhamento por canal, consulte [Quando as Campaigns aparecem em Campaigns recebidas](#when-campaigns-appear-in-campaigns-received). Quando uma mensagem é recebida, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal que o perfil que registrou a interação (por exemplo, o mesmo endereço de e-mail para e-mail ou o mesmo número de telefone para SMS ou WhatsApp). Usuários que compartilham um identificador com alguém que recebeu, abriu ou clicou na mensagem podem corresponder a esse filtro mesmo que não estivessem originalmente na Campaign ou não tenham recebido a mensagem diretamente.<br><br>Selecione uma Campaign da lista para visualizá-la. |
| Segments | Segments nos quais este usuário está incluído. Selecione um Segment da lista para visualizá-lo. |
| Estatísticas de comunicação | Quando este usuário recebeu mensagens suas pela última vez em cada canal. |
| Atribuição da instalação | Informações sobre como e quando um usuário instalou seu app. Saiba mais sobre [entender as instalações de usuários]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution/). |
| Diversos | O [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) do usuário. |
| Mensagens do Canvas recebidas | Mensagens do Canvas que este usuário recebeu e quando. O momento do envio segue as mesmas regras de canal de **Campaigns recebidas**; consulte [Quando as Campaigns aparecem em Campaigns recebidas](#when-campaigns-appear-in-campaigns-received). Quando uma mensagem é recebida, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal que o perfil que registrou a interação (por exemplo, o mesmo endereço de e-mail para e-mail ou o mesmo número de telefone para SMS ou WhatsApp). Usuários que compartilham um identificador com alguém que recebeu, abriu ou clicou na mensagem podem corresponder a esse filtro mesmo que não estivessem originalmente na Campaign ou não tenham recebido a mensagem diretamente.<br><br>Selecione uma mensagem da lista para visualizá-la. |
| Previsões | Pontuações de [previsão de churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/) e [previsão de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) para este usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guia Engajamento" }

### Quando as Campaigns aparecem em Campaigns recebidas {#when-campaigns-appear-in-campaigns-received}

De modo geral, a Braze lista uma Campaign em **Campaigns recebidas** após tentar enviar a mensagem. A entrega ao dispositivo ou à caixa de entrada do usuário não é necessária para que um envio seja registrado. **Mensagens do Canvas recebidas** segue as mesmas regras específicas de canal para cada tipo de mensagem do Canvas.

- **E-mail:** A Braze registra um envio quando a mensagem é entregue ao seu provedor de serviço de e-mail (ESP). Após essa entrega, a mensagem não é cancelada por causa de lógica Liquid, limite de taxa ou porque o usuário foi marcado como inacessível. Os próximos eventos geralmente são uma entrega ou um bounce.
- **Push:** A Braze registra um envio quando a mensagem é entregue ao provedor de push (por exemplo, serviço de Notificações por Push da Apple (APNs) ou Firebase Cloud Messaging (FCM)). O provedor geralmente tenta entregar imediatamente; se o dispositivo estiver indisponível (por exemplo, offline), o provedor pode tentar novamente até que a mensagem expire.
- **Mensagens no app:** A Braze registra um envio quando a Campaign é lançada.
- **Content Cards:** Quando a Braze registra um evento de _Envio_ depende do tipo de entrega e da sua configuração de **Criação de cartão**. Uma Campaign de Content Cards aparece em **Campaigns recebidas** no perfil do usuário somente depois que o usuário visualiza o cartão no app. Para o detalhamento completo, consulte [Quando os envios são registrados]({{site.baseurl}}/user_guide/channels/content_cards/reporting/#when-sends-are-logged) e [Campaigns recebidas e filtros de redirecionamento]({{site.baseurl}}/user_guide/channels/content_cards/reporting/#campaigns-received-and-retargeting-filters) no artigo de relatórios de Content Cards.
- **SMS, WhatsApp e webhooks:** A Braze registra um envio quando a mensagem entra na jornada de entrega daquele canal (por exemplo, o provedor de SMS ou WhatsApp, ou seu endpoint de webhook).

{% alert note %}
Essas descrições cobrem quando um envio é registrado para **Campaigns recebidas**. Elas são separadas dos [cancelamentos de mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/) que podem interromper uma mensagem antes que ela chegue a um provedor.
{% endalert %}

![A guia Engajamento de um perfil de usuário exibindo as configurações de contato e estatísticas de comunicação.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Guia Histórico de mensagens {#messaging-history-tab}

A guia **Histórico de mensagens** do perfil de usuário mostra eventos recentes relacionados a mensagens (cerca de 40) para um usuário individual nos últimos 30 dias. Esses eventos incluem as mensagens que o usuário recebeu, com as quais interagiu e muito mais.

{% alert note %}
Os dados nesta guia não são atualizados após a mesclagem de um usuário. Além disso, quaisquer eventos associados a mensagens enviadas via API (por exemplo, o [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#creating-new-users-with-api-sends)) não aparecem nesta guia se não houver um ID de Campaign especificado nesses envios.
{% endalert %}

![A guia Histórico de mensagens mostrando quais Campaigns e Canvas um usuário recebeu.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Visualizar e entender eventos {#viewing-and-understanding-events}

Para cada evento na tabela **Histórico de mensagens**, você pode ver o canal de envio de mensagens, o tipo de evento, o timestamp em que o evento ocorreu, a Campaign ou mensagem do Canvas associada e os dados do dispositivo do usuário. Para filtrar eventos específicos, clique em **Filtros** e selecione eventos da lista.

##### Eventos de engajamento com mensagem {#message-engagement-events}

Os seguintes eventos de engajamento com mensagem estão disponíveis para e-mail, SMS, push, mensagens no app, Content Cards e webhooks. Para saber mais sobre como eventos específicos são rastreados, consulte o [Glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

| Canal | Eventos de engajamento disponíveis |
| --- | --- |
| E-mail | Bounce<br>Clique<br>Eventos de adiamento<br>Entrega<br>Marcar como spam<br>Abertura (veja a [nota sobre o evento de abertura de e-mail](#note-on-email-open-event))<br>Envio<br>Soft bounce<br>Cancelamento de inscrição |
| SMS | Envio pela operadora<br>Entrega<br>Falha na entrega<br>Recebimento de entrada<br>Rejeição<br>Envio |
| Push | Bounce<br>Abertura influenciada<br>iOS em primeiro plano<br>Abertura<br>Envio |
| Mensagem no app | Clique<br>Impressão |
| Content Cards | Clique<br>Dispensar<br>Impressão<br>Envio |
| Webhooks | Envio |
| WhatsApp | Cancelamento<br>Entrega<br>Falha<br>Limite de frequência atingido<br>Recebimento de entrada<br>Leitura<br>Envio |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de engajamento com mensagem" }

##### Eventos de cancelamento de mensagem {#message-abort-events}

Eventos de cancelamento de mensagem ocorrem quando uma mensagem enviada a um usuário foi cancelada devido à lógica condicional em [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/) ou [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/#aborting-messages), ou por timeouts de renderização do Liquid.

Eventos de cancelamento estão disponíveis para os seguintes canais:

- E-mail
- SMS
- Push
- Webhooks

Eventos de cancelamento não estão disponíveis atualmente para mensagens no app e Content Cards.

##### Eventos de limite de frequência {#frequency-cap-events}

Um evento de limite de frequência ocorre quando um usuário é qualificado para receber uma mensagem, mas não a recebe de fato devido às configurações de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping). Você pode personalizar as configurações de limite de frequência em **Configurações** > **Regras do limite de frequência**.

##### Destinos em branco {#blank-destinations}

Alguns envios de mensagens podem aparecer no Histórico de mensagens com destinos em branco (indicados por "—"). Isso ocorre porque alguns canais, como Content Cards e webhooks, não coletam dados do dispositivo no envio da mensagem.

Os envios de Content Cards são registrados quando o cartão está disponível para ser visualizado. Como os Content Cards podem ser visualizados em vários dispositivos, os dados do dispositivo não são registrados no envio. Em vez disso, essas informações são registradas na impressão (quando o cartão é realmente visualizado). Webhooks são enviados para um endpoint do sistema (não para um dispositivo), portanto os dados do dispositivo não se aplicam.

#### Nota sobre o evento de abertura de e-mail {#note-on-email-open-event}

O rastreamento de abertura de e-mail é propenso a erros em qualquer ferramenta, incluindo a Braze. Com uma variedade de recursos de proteção de privacidade oferecidos por diferentes clientes de e-mail que bloqueiam o carregamento automático de imagens ou as carregam proativamente no servidor, os eventos de abertura de e-mail são suscetíveis tanto a falsos positivos quanto a falsos negativos.

Embora as estatísticas de abertura de e-mail possam ser úteis em agregado, por exemplo, para comparar a eficácia de diferentes linhas de assunto, você não deve presumir que um evento de abertura individual para um usuário individual seja significativo.

#### Por que certos campos estão em branco na guia Histórico de mensagens? {#why-are-certain-fields-blank-in-the-message-history-tab}

Alguns campos podem estar ausentes na guia **Histórico de mensagens** de um usuário nos seguintes cenários:

- Quando um evento não possui dados para **Mensagem enviada**, isso indica que a Campaign não tem nenhuma variação de mensagem.
- Quando um evento não possui dados para **Campaign/Canvas** e **Mensagem enviada**, isso indica que essa mensagem foi enviada por uma campanha da API (não Campaigns disparadas por API) que não especificou o `campaign_id` e o `message_variation_id`. Esses campos são opcionais e podem ser omitidos do corpo da requisição. Quando esses campos são especificados, essas informações são preenchidas nos registros do histórico de mensagens.
   - Se uma mensagem específica estiver completamente ausente do histórico de mensagens, mas aparecer no registro de **Campaigns recebidas**, é provável que o usuário tenha recebido a Campaign antes de ser identificado como o usuário atual. Se um perfil existente for órfão, o registro de **Campaigns recebidas** é transferido, mas o histórico de mensagens não.
- Quando dados estão ausentes para **Campaign/Canvas**, um teste manual pode ter sido enviado. Testes manuais são registrados na guia **Histórico de mensagens**, mas a Campaign ou o Canvas que foi enviado não será registrado.

## Artigos relacionados {#related-articles}

- [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [POST: Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [POST: Excluir usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)