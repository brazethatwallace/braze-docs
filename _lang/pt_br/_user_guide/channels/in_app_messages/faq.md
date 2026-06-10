---
nav_title: FAQ
article_title: FAQ sobre mensagens no app
page_order: 30
description: "Este artigo fornece respostas para perguntas frequentes sobre In-App Messages."
tool: in-app messages

---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre mensagens no app.

### O que é uma mensagem no navegador e como ela difere de uma mensagem no app? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

Mensagens no navegador são mensagens no app enviadas para navegadores web. Para criar uma mensagem no navegador, selecione **Web Browser** no campo **Send To** ao criar sua Campaign de mensagem no app ou Canvas.

### Uma mensagem no app será exibida se o dispositivo estiver offline? {#will-an-in-app-message-display-if-a-device-is-offline}

Depende. Como as mensagens no app são entregues no início da sessão, se o dispositivo conseguir baixar a carga útil antes de ficar offline, a mensagem no app ainda poderá ser exibida enquanto estiver offline. Se a carga útil não for baixada, a mensagem no app não será exibida.

### Se um usuário já tiver a carga útil de uma mensagem no app em seu dispositivo e a expiração da mensagem for alterada, a expiração será atualizada no dispositivo? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-will-the-expiration-be-updated-on-their-device}

Quando um usuário inicia uma sessão, a Braze verifica se houve alterações em quaisquer mensagens no app para as quais ele é elegível e as atualiza de acordo. Portanto, se a expiração foi alterada e o usuário registrar uma sessão, a mensagem no app será enviada ao dispositivo com as informações atualizadas.

### Como configuro o horário de silêncio para uma Campaign de mensagem no app? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

O recurso de horário de silêncio não está disponível para uso com Campaigns de mensagem no app. Esse recurso é usado para impedir que mensagens sejam enviadas aos seus usuários durante horários específicos. Para Campaigns de mensagem no app, seus usuários só receberão mensagens no app se estiverem ativos dentro do app.

Como alternativa para enviar mensagens no app durante um horário específico, use o seguinte código Liquid de exemplo. Isso permite que a mensagem seja abortada se a mensagem no app for exibida após 19h59 ou antes das 8h no fuso horário especificado.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Os usuários podem receber uma mensagem no app novamente após descartá-la? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

#### Campaigns {#campaigns}

Para Campaigns de mensagem no app, você pode permitir que os usuários se tornem elegíveis para receber a Campaign novamente ativando a reelegibilidade em **Controles de entrega** (**Permitir que os usuários se tornem reelegíveis para receber a Campaign**). A rapidez com que podem recebê-la novamente depende do período de reelegibilidade que você definir e de como a Braze registrou o envio anterior. Consulte [Reelegibilidade para Campaigns e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) para o comportamento de Campaigns, incluindo como a reelegibilidade se relaciona com o recebimento da mensagem.

Se a reelegibilidade estiver desativada, os usuários geralmente não receberão a mesma Campaign novamente com base apenas nos critérios de qualificação após já terem recebido.

#### Canvas {#canvases}

Para mensagens no app enviadas a partir de um Canvas, se um usuário pode ver a mensagem novamente depende dos controles de entrada do Canvas (como permitir que os usuários reentrem no Canvas) e da configuração da sua etapa — não apenas dos controles de entrega da Campaign.

### Quando a elegibilidade para uma mensagem no app é calculada? {#when-is-eligibility-for-an-in-app-message-calculated}

A elegibilidade para uma mensagem no app é calculada no momento da entrega. Se uma mensagem no app estiver programada para envio às 7h, a elegibilidade será verificada para essa mensagem no app às 7h.

Depois que a mensagem no app é exibida, a elegibilidade dependerá de quando a mensagem no app foi baixada e disparada.

### Por que minha Campaign de mensagem no app arquivada ainda está gerando impressões de mensagem no app? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Isso pode ocorrer para usuários que atenderam aos critérios do segmento quando a Campaign de mensagem no app estava ativa.

Para evitar isso, durante a configuração da sua Campaign, selecione **Re-evaluate campaign eligibility before displaying**.

### Várias mensagens no app podem ser exibidas na mesma sessão? {#can-multiple-in-app-messages-display-in-the-same-session}

Sim, mas apenas uma mensagem no app pode ser exibida por ocorrência de um [evento de gatilho]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create/#choose-a-trigger). Se várias Campaigns de mensagem no app compartilharem o mesmo gatilho (por exemplo, início de sessão), apenas a mensagem de maior prioridade será exibida cada vez que esse gatilho ocorrer. Para gatilhos de início de sessão, isso significa que apenas uma mensagem pode ser exibida por sessão, e a próxima oportunidade de mostrar outra mensagem elegível será na próxima sessão.

Quando várias mensagens compartilham o mesmo nível de prioridade, a mensagem criada mais recentemente é exibida primeiro. Para gatilhos de início de sessão, a próxima mensagem mais recente é exibida em uma sessão subsequente; para outros tipos de gatilho, a próxima mensagem mais recente é exibida na próxima vez que o evento de gatilho ocorrer, o que pode ser dentro da mesma sessão ou em uma sessão posterior.

Para controlar a ordem de exibição dentro de um grupo de prioridade, acesse as configurações de entrega de qualquer uma das Campaigns e selecione **Definir prioridade exata**, depois arraste e solte as Campaigns na ordem desejada. Para mais detalhes, consulte [Escolher uma prioridade]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create/#choose-a-priority).

### Como a Braze calcula a expiração de uma mensagem no app definida como "após 1 dia(s)"? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

A Braze calcula o tempo de expiração de um dia como 24 horas após os usuários se tornarem elegíveis para receber a mensagem.

### O que são mensagens no app com modelo? {#what-are-templated-in-app-messages}

As mensagens no app são entregues como mensagens no app com modelo quando **Re-evaluate campaign eligibility before displaying** está selecionado ou se qualquer uma das seguintes Liquid tags existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que, durante o início da sessão, o dispositivo recebe o gatilho dessa mensagem no app em vez da mensagem completa. Quando o usuário dispara a mensagem no app, o dispositivo faz uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à internet. A mensagem pode não ser entregue se a lógica Liquid demorar muito para ser resolvida.
{% endalert %}

### Como funciona o comportamento de aborto para mensagens no app? {#how-does-abort-behavior-work-for-in-app-messages}

Na Braze, um aborto ocorre quando um usuário realiza uma ação que o torna elegível para receber uma mensagem, mas ele não a recebe porque a lógica Liquid o marca como inelegível. Por exemplo:

1. Sam realiza uma ação que deveria disparar uma Campaign de e-mail.
2. O corpo do e-mail contém lógica Liquid que diz que, se um atributo personalizado de pontuação for menor que 50, não envie este e-mail.
3. A pontuação do atributo personalizado de Sam é 20.
4. A Braze reconhece que Sam não deveria receber este e-mail, e o e-mail é abortado.
5. Um evento de aborto é registrado.

No entanto, como as mensagens no app são um canal pull, os abortos funcionam de forma um pouco diferente para elas.

#### Comportamento padrão de aborto de mensagem no app {#standard-in-app-message-abort-behavior}

As mensagens no app são puxadas pelo dispositivo no início da sessão e armazenadas em cache no dispositivo, de modo que, independentemente da qualidade da conexão com a internet, a mensagem pode ser entregue instantaneamente ao usuário. Por exemplo, se um usuário receber cinco mensagens no app dentro de sua sessão, ele receberá todas as cinco no início da sessão. As mensagens são armazenadas em cache localmente e aparecem quando seus eventos de gatilho definidos ocorrem (início de sessão, o usuário clica em um botão que registra um evento personalizado, ou outros).

Em outras palavras, a lógica que determina se uma mensagem no app deve ser abortada ocorre **antes** de o gatilho ter ocorrido. Para demonstrar isso, vamos supor que Sam do exemplo de e-mail está inscrito em notificações por push.

1. Sam inicia uma sessão abrindo um app com tecnologia Braze em seu telefone.
2. Com base nos critérios de público das Campaigns ativas no espaço de trabalho, Sam pode ser elegível para cinco Campaigns diferentes. Todas as cinco são puxadas para o telefone e armazenadas em cache.
3. Sam **não** realizou nenhuma ação que dispararia essas mensagens, mas poderia recebê-las na sessão.
4. O Liquid em duas das mensagens no app tem regras que excluem Sam de receber a mensagem (como o atributo personalizado de pontuação não ser alto o suficiente).
5. Sam não recebe as duas mensagens no app que o excluem, mas recebe as outras três mensagens.
6. Nenhum evento de aborto é registrado.

A Braze não registra nenhum evento de aborto no caso de Sam porque isso não atende à definição de um aborto; Sam **não** realizou nenhuma ação que dispararia as mensagens. Para mensagens no app, os usuários nunca realizam de fato o gatilho antes de a Braze determinar que eles não devem ver a mensagem.

#### Comportamento de aborto de mensagem no app com modelo {#templated-in-app-message-abort-behavior}

[Mensagens no app com modelo](#what-are-templated-in-app-messages) forçam o SDK a reavaliar se uma mensagem deve ser exibida quando o evento de gatilho ocorre. Isso tem um comportamento de aborto diferente. Para demonstrar, considere este exemplo:

1. Sam inicia uma sessão da Braze abrindo um app com tecnologia Braze em seu telefone.
2. Os critérios de público das Campaigns ativas dizem que Sam pode ser elegível para uma mensagem no app com modelo, então as informações de gatilho são enviadas ao dispositivo sem a carga útil da mensagem.
3. Sam seleciona um botão que registra um evento personalizado, disparando a mensagem no app com modelo.
4. O dispositivo de Sam faz uma solicitação de rede para buscar a mensagem no app.
5. A lógica Liquid da mensagem leva a um aborto, então a Braze registra isso como um aborto; Sam realizou a ação-gatilho antes dessa avaliação.

#### Comparando o comportamento de aborto de mensagens no app {#comparing-in-app-message-abort-behavior}

Esta tabela compara os fluxos de mensagem no app que Sam experimentou:

| Mensagem no app | Comportamento de aborto |
| --- | --- |
| Padrão | Um evento de aborto não foi registrado porque Sam não realizou nenhuma ação que dispararia uma mensagem.<br><br>Mensagens no app padrão não registram abortos porque a definição de um aborto é "não viu a mensagem apesar de ter realizado a ação-gatilho". Como as mensagens no app são entregues ao dispositivo antes das ações de gatilho ocorrerem, não faz sentido considerar mensagens no app omitidas por causa da lógica Liquid. |
| Com modelo | Um evento de aborto foi registrado porque Sam realizou a ação-gatilho para disparar a mensagem no app com modelo, mas recebeu um aborto no modelo Liquid.<br><br>Mensagens no app com modelo registram abortos porque a avaliação Liquid ocorre após a ação-gatilho ter sido realizada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparação do comportamento de aborto de mensagens no app" }

### Por que o botão de fechar está oculto em mensagens no app HTML de tela inteira no Android? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

Em dispositivos com telas de borda a borda (incluindo Android 15+), mensagens no app HTML de tela inteira podem ser desenhadas atrás da barra de status do sistema e ocultar um controle de fechar no topo do layout.

O SDK da Braze para Android versão 37.0.0 e posteriores aplicam insets de janela a mensagens no app HTML por padrão, para que os controles permaneçam na área segura. Se os usuários ainda virem sobreposição, faça upgrade para a versão mais recente do SDK da Braze para Android.

Em versões anteriores do SDK, os desenvolvedores podiam ativar `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` antes de esse comportamento se tornar o padrão.

### Quais são as limitações conhecidas do editor de arrastar e soltar de mensagens no app? {#what-are-known-limitations-of-the-drag-and-drop-in-app-message-editor}

O [editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) não suporta todas as personalizações disponíveis em mensagens no app de [HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/). Tenha em mente:

- Um deep link por mensagem (não links diferentes por tipo de dispositivo)
- A opacidade se aplica ao fundo inteiro da mensagem, não a elementos individuais
- A largura máxima da mensagem não pode ser definida abaixo de 325 px
- Imagens e cores de fundo se aplicam à mensagem inteira, não por plataforma
- Estilos no nível da mensagem se aplicam à mensagem inteira
- Blocos de espaçamento usam apenas valores em pixels
- Apenas tipos de mensagem modal e tela inteira
- Imagens de fundo são esticadas para caber no modal
- Imagens de fundo e ações ao clicar persistem entre páginas em mensagens de várias páginas

### O que significa "Event was published, but no subscribers were found" nos logs do SDK Android? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Essa linha de log geralmente não é um erro. Ela aparece frequentemente quando a Braze publica um evento interno (como `NoMatchingTriggerEvent`) e nenhum listener de mensagem no app ou Content Cards está inscrito naquele momento.

Se você vir esse log quando espera que um evento personalizado dispare uma mensagem no app, confirme que o evento está sendo registrado, que o usuário está no público da Campaign ou Canvas e que os Content Cards estão sincronizados quando a mensagem depende deles.