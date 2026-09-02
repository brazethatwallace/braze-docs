---
nav_title: Status de inscrição
article_title: Status de inscrição
page_order: 0
page_type: reference
description: "Saiba como a Braze rastreia o status de inscrição em e-mail, LINE, SMS, RCS e WhatsApp, e como o status controla a entrega de mensagens."

---

# Status de inscrição {#subscription-status}

> Saiba como a Braze rastreia o status de inscrição nos canais de envio de mensagens, como o status global e o status do grupo de inscrições interagem, e onde as regras específicas de cada canal se aplicam.

O status de inscrição informa à Braze se um usuário é elegível para receber mensagens em um canal. O status pode controlar o direcionamento de Campaigns e Canvas, filtros de segmentos e se a Braze tenta realizar a entrega.

## Como o status de inscrição funciona na Braze {#how-subscription-status-works-in-braze}

A Braze rastreia o status de inscrição em dois níveis:

| Nível | O que controla | Canais |
| ----- | -------------- | ------ |
| Estado global de inscrição | Se um usuário pode receber mensagens naquele canal | E-mail, push |
| Status do grupo de inscrições | Se um usuário aceitou participar de um grupo específico dentro de um canal | E-mail, SMS, MMS, RCS, WhatsApp, LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como o status de inscrição funciona na Braze" }

O estado global e o status do grupo de inscrições funcionam juntos. Para e-mail, um usuário que cancelou a inscrição globalmente não receberá e-mails mesmo que esteja inscrito em um grupo de inscrições. Para SMS, RCS, WhatsApp e LINE, os usuários precisam estar inscritos no grupo de inscrições relevante para receber mensagens daquele grupo.

Você pode visualizar e atualizar o status de inscrição no perfil de um usuário em **Engagement** > **Contact settings**, pela REST or transferir estado representacional API or interface de programação do aplicativo (API), SDK or kit de desenvolvimento de software, importação de CSV, Central de Preferências e fluxos de aceitação específicos de cada canal. A Braze não conta alterações no estado de inscrição como pontos de dados.

{% alert note %}
Os grupos de inscrições adicionam aceitação granular dentro de um canal (por exemplo, SMS promocional versus transacional). O estado global de e-mail e a participação no grupo de inscrições trabalham juntos ao decidir quem pode ser alcançado.
{% endalert %}

## E-mail {#email}

A Braze possui três estados globais de inscrição para e-mail. Esses estados controlam se os usuários recebem mensagens direcionadas a públicos inscritos ou que aceitaram participar. Por exemplo, usuários no estado `unsubscribed` não recebem mensagens direcionadas a usuários `subscribed` ou `opted-in`.

| Estado | Definição |
| ------ | --------- |
| Opted-in | O usuário confirmou explicitamente que deseja receber e-mails. A Braze recomenda um processo explícito de aceitação para obter o consentimento dos usuários para o envio de e-mails. |
| Subscribed | O usuário não cancelou a inscrição nem aceitou explicitamente receber e-mails. Este é o estado de inscrição padrão quando um perfil de usuário é criado. |
| Unsubscribed | O usuário cancelou explicitamente a inscrição dos seus e-mails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição de e-mail" }

### Comportamento específico de e-mail {#email-specific-behavior}

- **Cancelamentos de inscrição e relatórios de spam:** A Braze cancela automaticamente a inscrição de usuários que cancelam a inscrição por meio de um [rodapé personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). Se um usuário marcar um e-mail como spam, a Braze envia apenas e-mails de transação (mensagens enviadas com **Enviar para todos os usuários, incluindo os que cancelaram a inscrição**).
- **Hard bounces:** Quando um endereço de e-mail sofre hard bounce, a Braze não define automaticamente o estado de inscrição do usuário como `unsubscribed`. A Braze marca o endereço como inválido e para de enviar até que o usuário atualize seu endereço de e-mail.
- **Endereços de e-mail compartilhados:** Quando o estado global de inscrição de e-mail de um usuário muda, a Braze propaga esse estado para outros perfis que compartilham o mesmo endereço de e-mail, até 100 perfis por alteração.
- **Atualizações de endereço de e-mail:** Quando um usuário atualiza seu endereço de e-mail, o estado de inscrição é definido como `subscribed`, a menos que o endereço atualizado já exista em outro perfil, caso em que o usuário herda o estado daquele perfil.

Para atualizar o estado de inscrição, verificar o status, Central de Preferências e direcionamento de Campaigns, consulte [Inscrições de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions).

## LINE {#line}

O LINE é a fonte de verdade para o status de inscrição do LINE. Mesmo que um perfil de usuário tenha um `native_line_id`, a Braze não entregará mensagens do LINE a menos que o usuário siga seu canal do LINE.

O status de inscrição do LINE é rastreado por `native_line_id`, não por `external_id`. Se vários perfis compartilham o mesmo `native_line_id`, eles herdam o mesmo status de inscrição do LINE.

| Estado | Definição |
| ------ | --------- |
| Subscribed | O usuário seguiu seu canal do LINE de dentro do app LINE. |
| Unsubscribed | O usuário não seguiu seu canal do LINE ou deixou de segui-lo explicitamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição do LINE" }

### Ferramenta de sincronização de inscrições {#subscription-sync-tool}

Após uma integração bem-sucedida do canal LINE, a Braze implanta uma ferramenta de sincronização de inscrições para alinhar os perfis existentes da Braze com os dados de seguidores do LINE:

- Perfis com um `native_line_id` que seguem seu canal são atualizados para `subscribed`.
- Seguidores sem um perfil correspondente na Braze recebem um perfil anônimo com `native_line_id`, um alias de usuário `line_id` e status `subscribed`.

Você não pode definir o estado do grupo de inscrições do LINE manualmente durante a integração — o LINE controla o status, e a Braze o sincroniza.

### Atualizações de eventos de seguir e deixar de seguir {#follow-and-unfollow-event-updates}

Quando a Braze recebe eventos de webhook do LINE para seu canal integrado:

- **Seguir:** Todos os perfis com um `native_line_id` correspondente são definidos como `subscribed`. Se nenhum perfil existir, a Braze [cria um usuário anônimo]({{site.baseurl}}/user_guide/channels/line/message_users/user_management).
- **Deixar de seguir:** Todos os perfis com um `native_line_id` correspondente são definidos como `unsubscribed`.

Para etapas de configuração, reconciliação de usuários e casos de uso, consulte [Configuração do LINE]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup) e [Grupos de inscrições do LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

## SMS e RCS {#sms-and-rcs}

SMS e RCS usam o status do grupo de inscrições, não um estado global de canal separado. Um usuário pode estar `subscribed` em um grupo transacional e `unsubscribed` de um grupo promocional ao mesmo tempo.

| Estado | Definição |
| ------ | --------- |
| Subscribed | O usuário está inscrito para receber SMS e RCS de um grupo de inscrições específico, seja pela API or interface de programação do aplicativo (API) de inscrições da Braze, por uma palavra-chave de aceitação ou por outro método compatível. Quando a [aceitação dupla]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) está ativada, os usuários precisam confirmar a aceitação antes que o status seja atualizado para `Subscribed`. |
| Unsubscribed | O usuário cancelou a participação naquele grupo de inscrições enviando uma palavra-chave de cancelamento ou pela [API or interface de programação do aplicativo (API) de inscrições da Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição de SMS e RCS" }

### Comportamento específico de SMS e RCS {#sms-and-rcs-specific-behavior}

- **Herança de número de telefone:** Quando um número de telefone é adicionado ou atualizado em um perfil, o número herda o status do grupo de inscrições do perfil ou de qualquer perfil existente que já use aquele número.
- **Tratamento de palavras-chave:** Os usuários podem aceitar ou cancelar a participação enviando [palavras-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) padrão ou personalizadas. A Braze atualiza o estado de inscrição automaticamente.
- **Conformidade:** A Braze nunca envia SMS ou RCS para usuários que não estão inscritos no grupo de inscrições selecionado.

Para configuração, envio e gerenciamento de grupos de inscrições, consulte [Grupos de inscrições de SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

## WhatsApp {#whatsapp}

O WhatsApp também usa o status do grupo de inscrições. A Meta exige [consentimento explícito de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) antes de você enviar mensagens de marketing.

| Estado | Definição |
| ------ | --------- |
| Subscribed | O usuário confirmou explicitamente que deseja receber mensagens do WhatsApp da sua empresa, por meio de um fluxo de aceitação ou pela API or interface de programação do aplicativo (API) de inscrições da Braze. |
| Unsubscribed | O usuário não aceitou participar ou sua aceitação foi removida. Usuários que cancelaram a inscrição não recebem mensagens dos números de telefone daquele grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição do WhatsApp" }

### Requisitos de aceitação {#opt-in-requirements}

Para enviar mensagens aos usuários no WhatsApp, forneça à Braze um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) e um status de inscrição atualizado para cada usuário. Colete aceitações no seu website, app, SMS, mensagens no app, conversas de entrada do WhatsApp ou por meio de uma importação de CSV de usuários que já aceitaram em outro lugar.

### Métodos de cancelamento {#opt-out-methods}

Os usuários podem cancelar a participação por meio de:

- **Fluxos de palavras-chave de entrada:** Canvas ou Campaigns disparados por palavras-chave de cancelamento (por exemplo, "STOP"), com uma etapa de acompanhamento que atualiza o status de inscrição.
- **Respostas rápidas de cancelamento de marketing:** Modelos de mensagem com o botão de cancelamento de marketing da Meta, combinados com uma etapa de atualização do grupo de inscrições no seu Canvas.
- **Bloqueios e denúncias:** Se um usuário bloquear sua empresa, as mensagens subsequentes não serão entregues e não serão cobradas, mas o status de inscrição na Braze não é atualizado. Denúncias de usuários também não alteram o status de inscrição.

### Botão "Ofertas e Anúncios" do WhatsApp {#whatsapp-offers-and-announcements-toggle}

O botão nativo **Ofertas e Anúncios** do WhatsApp é separado dos grupos de inscrições da Braze. Quando um usuário o desativa no WhatsApp, a Meta bloqueia a entrega de marketing mesmo que a Braze mostre `subscribed`. As duas camadas não sincronizam automaticamente.

Para fluxos passo a passo de aceitação e cancelamento, consulte [Aceitações e cancelamentos do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) e [Grupos de inscrições do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

## Segmentar e direcionar por status de inscrição {#segment-and-target-by-subscription-status}

Use filtros de status de inscrição no criador de segmentos para direcionar ou suprimir públicos por canal — por exemplo, filtros de **Email Subscription Status**, **Push Subscription Status** e **Subscription Group**.

Ao criar Campaigns e Canvas, as opções de **Send Settings** e **Target Audience** permitem enviar apenas para usuários com um status de inscrição específico (como inscrito e com aceitação). Para definições de filtros de e-mail e push, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).