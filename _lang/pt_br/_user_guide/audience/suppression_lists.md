---
nav_title: Listas de supressão
article_title: Listas de supressão
page_order: 7
page_type: reference
tool: Segments
description: "Esta página explica como usar listas de supressão para especificar quais usuários nunca devem receber suas mensagens."

---

# Listas de supressão {#suppression-lists}

> Listas de supressão são grupos de usuários que automaticamente não recebem nenhuma Campaign ou Canvas. As listas de supressão são definidas por filtros de segmento, e os usuários entram e saem das listas de supressão conforme atendem aos critérios dos filtros. Você também pode definir tags de exceção para que a lista de supressão não se aplique a Campaigns ou Canvas com essas tags. Mensagens de Campaigns ou Canvas com tags de exceção ainda alcançarão os usuários da lista de supressão que estiverem nos segmentos de destino.

## Por que usar listas de supressão? {#why-use-suppression-lists}

As listas de supressão são dinâmicas e se aplicam automaticamente a todas as formas de envio de mensagens, mas você pode definir exceções para tags selecionadas. Se as tags de exceção selecionadas forem usadas em uma Campaign ou Canvas, a lista de supressão não se aplicará a essa Campaign ou Canvas. Mensagens de Campaigns ou Canvas com tags de exceção ainda alcançarão os usuários da lista de supressão que fazem parte dos seus segmentos de destino.

### Tipos de mensagem e canais afetados por listas de supressão {#message-types-and-channels-affected-by-suppression-lists}

As listas de supressão se aplicam a todos os tipos de mensagem e canais, exceto [Feature Flags]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags/). Isso significa que as listas de supressão, por padrão, se aplicam a todos os canais, Campaigns e Canvas, incluindo:
- [Campaigns da API]({{site.baseurl}}/api/api_campaigns/)
- Campaigns e Canvas disparados por API
- [E-mails de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)

O único tipo de mensagem ao qual as listas de supressão não se aplicam são as Feature Flags. Usuários em uma lista de supressão não serão suprimidos de Feature Flags, mas serão suprimidos de todos os outros canais.

Você pode usar tags de exceção para que os usuários da lista de supressão ainda sejam direcionados por Campaigns e Canvas específicos. Para mais informações, consulte a etapa 4 em [Configurando listas de supressão](#setup). Se você não adicionar tags de exceção a uma lista de supressão, os usuários dessa lista não serão direcionados com nenhum envio de mensagens além de Feature Flags.

{% alert note %}
As listas de supressão são aplicadas a Campaigns da API criadas no dashboard da Braze com um `campaign_id`. As listas de supressão não se aplicam a mensagens enviadas por meio dos [endpoints de envio de mensagens da Braze]({{site.baseurl}}/api/endpoints/messaging/) sem um `campaign_id` associado.
{% endalert %}

![A seção "Configurações de exceção" com uma caixa de seleção para não aplicar a lista de supressão a Campaigns e Canvas disparados por API.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configurando listas de supressão {#setup}

{% alert note %}
Todos os usuários podem visualizar listas de supressão, mas apenas usuários com [permissões de administrador]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions?tab=admin) podem criar e gerenciar listas de supressão.
{% endalert %}

1. Acesse **Público** > **Listas de supressão**.
2. Selecione **Criar lista de supressão** e adicione um nome.
3. Use filtros de segmento para identificar os usuários nas suas listas de supressão. Você deve selecionar pelo menos um.

{% alert important %}
Embora o processo de configuração pareça semelhante à [criação de segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), uma lista de supressão é um grupo de usuários para os quais você **não** deseja enviar mensagens, independentemente da associação ao segmento.
{% endalert %}

![Um construtor de lista de supressão com um filtro para usuários que abriram um e-mail pela última vez há mais de 90 dias.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4. Determine se deseja ter exceções baseadas em tags marcando a caixa abaixo do nome do seu segmento (consulte [Por que usar listas de supressão?](#why-use-suppression-lists) para mais informações) e, em seguida, adicione as tags de Campaigns ou Canvas que os usuários desta lista de supressão ainda devem receber. <br><br>Em outras palavras, se você adicionar a tag de exceção "Shipping confirmation", os usuários da sua lista de supressão serão excluídos de todos os envios de mensagens, exceto aqueles que usam a tag "Shipping confirmation".<br><br>![A seção "Detalhes da lista de supressão" com uma tag de exceção aplicada chamada "Shipping confirmation".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5. Salve ou ative sua lista de supressão.
- Ao salvar, sua lista de supressão será salva, mas não será ativada, o que significa que ela não entrará em vigor. Sua lista de supressão permanecerá inativa até que você a ative, e listas de supressão inativas não impactarão o envio de mensagens (os usuários não serão excluídos das mensagens).
- Ao ativar, sua lista de supressão será salva e entrará em vigor imediatamente, o que significa que os usuários da sua lista de supressão serão imediatamente excluídos de Campaigns ou Canvas (exceto aqueles que contêm uma tag de exceção).

{% alert note %}
Apenas administradores podem salvar ou ativar listas de supressão. Você pode ter até cinco listas de supressão ativas ao mesmo tempo durante o beta.
{% endalert %}

Você pode desativar ou arquivar listas de supressão quando não precisar mais delas.
- Para desativar, selecione uma lista de supressão ativa e selecione **Desativar**. Listas de supressão desativadas podem ser reativadas posteriormente.
- Para arquivar, faça isso na página **Listas de supressão**.

## Uso da lista de supressão {#suppression-list-usage}

Para verificar se sua lista de supressão impediu um usuário de receber uma mensagem, use **User Lookup** na etapa **Público-alvo** dentro da sua Campaign ou Canvas. Aqui, você poderá ver de qual lista de supressão ele faz parte.

{% alert note %}
As listas de supressão são atualizadas antes do envio de uma mensagem, não após o lançamento de uma Campaign. Isso significa que um usuário adicionado a uma lista de supressão após o lançamento da Campaign, mas antes do envio da mensagem, ainda poderá receber a mensagem.
{% endalert %}

![Janela "User Lookup" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Você também pode encontrar as listas de supressão aplicadas na etapa **Resumo**.
{% endalert %}

Ao criar uma Campaign ou Canvas, use **User Lookup** na etapa **Público-alvo** para pesquisar um usuário. Se ele não estiver no público-alvo, você poderá ver a lista de supressão da qual ele faz parte.

![Janela "User Lookup" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaign

Se um usuário estiver em uma lista de supressão, ele não receberá uma Campaign à qual essa lista de supressão se aplica. Consulte [Tipos de mensagem e canais afetados por listas de supressão](#message-types-and-channels-affected-by-suppression-lists) para casos em que uma lista de supressão não se aplica.

![A seção "Listas de supressão" com uma lista de supressão ativa chamada "Low marketing health scores".]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas

A partir do momento em que um usuário é adicionado a uma lista de supressão, ele não entrará em Canvas. Se já tiver entrado em um Canvas, ele não receberá etapas de Mensagem. Isso significa que, se um usuário já estiver dentro de um Canvas quando for adicionado a uma lista de supressão, ele avançará pelo Canvas até a próxima etapa de Mensagem, momento em que sairá sem receber a etapa de Mensagem.

Por exemplo, digamos que um Canvas tenha uma etapa de Atualização de usuário seguida de uma etapa de Mensagem. Se um usuário entrar no Canvas e depois for adicionado a uma lista de supressão, esse usuário ainda passará pela etapa de Atualização de usuário (onde poderá ser atualizado) e, em seguida, sairá na etapa de Mensagem, momento em que será incluído nas métricas de saída.