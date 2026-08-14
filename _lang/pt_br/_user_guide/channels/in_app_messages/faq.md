---
nav_title: FAQ
article_title: FAQ sobre mensagens no app
page_order: 30
description: "Este artigo fornece respostas para perguntas frequentes sobre In-App Messages."
tool: in-app messages

---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre mensagens no app.

## O que é uma mensagem no navegador e como ela difere de uma mensagem no app? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

Mensagens no navegador são mensagens no app enviadas para navegadores web. Para criar uma mensagem no navegador, selecione **Web Browser** no campo **Send To** ao criar sua Campaign de mensagem no app ou Canvas.

## Uma mensagem no app é exibida se o dispositivo estiver offline? {#does-an-in-app-message-display-if-a-device-is-offline}

Depende. Como as mensagens no app são entregues no início da sessão, se o dispositivo conseguir baixar a carga útil antes de ficar offline, a mensagem no app ainda poderá ser exibida enquanto estiver offline. Se a carga útil não for baixada, a mensagem no app não será exibida.

## Se um usuário já tem uma carga útil de mensagem no app no dispositivo e a expiração da mensagem é alterada, a expiração é atualizada no dispositivo? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-does-the-expiration-update-on-their-device}

Quando um usuário inicia uma sessão, a Braze verifica se houve alterações em quaisquer mensagens no app para as quais ele é elegível e as atualiza de acordo. Então, se a expiração foi alterada e ele registra uma sessão, a mensagem no app é enviada ao dispositivo com as informações atualizadas.

## Como configuro o horário de silêncio para uma campanha de mensagem no app? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

O recurso de horário de silêncio não está disponível para uso com campanhas de mensagem no app. Esse recurso é usado para impedir que mensagens sejam enviadas aos seus usuários durante horários específicos. Para campanhas de mensagem no app, seus usuários recebem mensagens no app somente se estiverem ativos dentro do app.

Como alternativa para enviar mensagens no app durante um horário específico, use o seguinte código Liquid de exemplo. Isso permite que a mensagem seja interrompida se a mensagem no app for exibida após 19h59 ou antes das 8h no fuso horário especificado.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

## Os usuários podem receber uma mensagem no app novamente após descartá-la? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

### Campaigns {#campaigns}

Para Campaigns de mensagem no app, você pode permitir que os usuários se tornem elegíveis para receber a Campaign novamente ativando a reelegibilidade em **Controles de entrega** (**Permitir que os usuários se tornem reelegíveis para receber a Campaign**). A rapidez com que podem recebê-la novamente depende da janela de reelegibilidade que você definir e de como a Braze registrou o envio anterior. Consulte [Reelegibilidade para Campaigns e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para o comportamento de Campaigns, incluindo como a reelegibilidade se relaciona com o recebimento de mensagens.

Se a reelegibilidade estiver desativada, os usuários geralmente não receberão a mesma Campaign novamente com base apenas nos critérios de qualificação após já terem recebido.

### Canvas {#canvases}

Para mensagens no app enviadas a partir de um Canvas, a possibilidade de o usuário ver a mensagem novamente depende dos controles de entrada do Canvas (como permitir que os usuários reentrem no Canvas) e da configuração da sua etapa — não apenas dos controles de entrega da Campaign.

## Quando a elegibilidade para uma mensagem no app é calculada? {#when-is-eligibility-for-an-in-app-message-calculated}

A elegibilidade para uma mensagem no app é calculada no momento da entrega. Se uma mensagem no app está agendada para envio às 7h, a elegibilidade é verificada para essa mensagem no app às 7h.

Quando a mensagem no app aparece, a elegibilidade depende de quando a mensagem no app é baixada e disparada.

## Por que minha Campaign de mensagem no app arquivada ainda está entregando impressões de mensagem no app? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Isso pode ocorrer para usuários que atenderam aos critérios do Segment quando a Campaign de mensagem no app estava ativa.

Para evitar isso, durante a configuração da sua Campaign, selecione **Re-evaluate campaign eligibility before displaying**.

## Por que não vejo aberturas para mensagens no app? {#why-dont-i-see-opens-for-in-app-messages}

As mensagens no app não utilizam a métrica *Aberturas*. A Braze registra *Impressões* quando a mensagem se torna visível na tela e *Cliques* quando os usuários interagem com o corpo da mensagem ou com os botões. Se uma exportação ou relatório multicanal incluir linhas de mensagens no app, compare *Impressões* e *Cliques* em vez de aberturas no estilo de e-mail. Para ver as definições, consulte [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting).

## Várias mensagens no app podem ser exibidas na mesma sessão? {#can-multiple-in-app-messages-display-in-the-same-session}

Sim, mas apenas uma mensagem no app pode ser exibida por ocorrência de um [evento-gatilho]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-trigger). Se várias Campaigns de mensagens no app compartilham o mesmo gatilho (por exemplo, início de sessão), apenas a mensagem com maior prioridade é exibida cada vez que esse gatilho ocorre. Para gatilhos de início de sessão, isso significa que apenas uma mensagem pode ser exibida por sessão, e a próxima oportunidade de mostrar outra mensagem elegível é na sessão seguinte.

Quando várias mensagens compartilham o mesmo nível de prioridade, a mensagem criada mais recentemente é exibida primeiro. Para gatilhos de início de sessão, a próxima mensagem mais recente é exibida em uma sessão subsequente; para outros tipos de gatilho, a próxima mensagem mais recente é exibida na próxima vez que o evento-gatilho ocorrer, o que pode ser dentro da mesma sessão ou em uma sessão posterior.

Para controlar a ordem de exibição dentro de um grupo de prioridade, acesse as configurações de entrega de qualquer uma das Campaigns e selecione **Set exact priority**. Em seguida, arraste e solte as Campaigns na ordem desejada. Para saber mais, consulte [Escolher uma prioridade]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

## Como as impressões e cliques de mensagens no app são registrados? {#how-are-in-app-message-impressions-and-clicks-logged}

Consulte [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para saber como as impressões e cliques são registrados por ação do usuário. Para exemplos específicos de mensagens em tela inteira criadas com o editor tradicional, consulte [Métricas de mensagens em tela inteira por ação do usuário]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#fullscreen-metrics-by-user-action).

## Como a Braze calcula a expiração de uma mensagem no app definida como "após 1 dia(s)"? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

A Braze calcula o tempo de expiração de um dia como 24 horas após os usuários se tornarem elegíveis para receber uma mensagem.

## O que são mensagens no app com modelo? {#what-are-templated-in-app-messages}

As mensagens no app são entregues como mensagens no app com modelo quando a opção **Reavaliar a elegibilidade da campanha antes de exibir** está selecionada ou se alguma das seguintes Liquid tags existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que, durante o início da sessão, o dispositivo recebe o gatilho dessa mensagem no app em vez da mensagem completa. Quando o usuário dispara a mensagem no app, o dispositivo do usuário faz uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à internet. A mensagem pode não ser entregue se a lógica do Liquid demorar muito para ser resolvida.
{% endalert %}

## Como funciona o comportamento de interrupção para mensagens no app? {#how-does-abort-behavior-work-for-in-app-messages}

Na Braze, uma interrupção ocorre quando um usuário realiza uma ação que o torna elegível para receber uma mensagem, mas ele não a recebe porque a lógica Liquid a marca como inelegível. Por exemplo:

1. Sam realiza uma ação que deveria disparar uma Campaign de e-mail.
2. O corpo do e-mail contém lógica Liquid que diz: se o atributo personalizado de pontuação for menor que 50, não envie este e-mail.
3. A pontuação do atributo personalizado de Sam é 20.
4. A Braze reconhece que Sam não deveria receber este e-mail, e o e-mail é interrompido.
5. Um evento de interrupção é registrado.

No entanto, como mensagens no app são um canal pull, as interrupções funcionam de forma um pouco diferente para elas.

### Comportamento padrão de interrupção de mensagens no app {#standard-in-app-message-abort-behavior}

As mensagens no app são obtidas pelo dispositivo no início da sessão e armazenadas em cache no dispositivo. Assim, independentemente da qualidade da conexão com a internet, a mensagem pode ser entregue instantaneamente ao usuário. Por exemplo, se um usuário recebe cinco mensagens no app durante a sessão, todas as cinco são recebidas no início da sessão. As mensagens são armazenadas em cache localmente e aparecem quando seus eventos-gatilho definidos ocorrem (início de sessão, clique em um botão que registra um evento personalizado, entre outros).

Em outras palavras, a lógica que determina se uma mensagem no app deve ser interrompida ocorre **antes** de o gatilho ter acontecido. Para demonstrar isso, vamos supor que Sam, do exemplo de e-mail, está inscrito em notificações por push.

1. Sam inicia uma sessão abrindo um app com tecnologia Braze no celular.
2. Com base nos critérios de público das Campaigns ativas no espaço de trabalho, Sam pode ser elegível para cinco Campaigns diferentes. Todas as cinco são baixadas para o celular e armazenadas em cache.
3. Sam **não** realizou nenhuma ação que dispararia essas mensagens, mas poderia recebê-las durante a sessão.
4. O Liquid em duas das mensagens no app possui regras que excluem Sam de receber a mensagem (como o atributo personalizado de pontuação não ser alto o suficiente).
5. Sam não recebe as duas mensagens no app que o excluem, mas recebe as outras três mensagens.
6. Nenhum evento de interrupção é registrado.

A Braze não registra nenhum evento de interrupção no caso de Sam porque isso não atende à definição de interrupção; Sam **não** realizou nenhuma ação que dispararia as mensagens. Para mensagens no app, os usuários nunca realizam de fato o gatilho antes de a Braze determinar que eles não devem ver a mensagem.

### Comportamento de interrupção de mensagens no app com template {#templated-in-app-message-abort-behavior}

[Mensagens no app com template](#what-are-templated-in-app-messages) forçam o SDK a reavaliar se uma mensagem deve ser exibida quando o evento-gatilho ocorre. Isso gera um comportamento de interrupção diferente. Para demonstrar, considere este exemplo:

1. Sam inicia uma sessão Braze abrindo um app com tecnologia Braze no celular.
2. Os critérios de público das Campaigns ativas indicam que Sam pode ser elegível para uma mensagem no app com template, então as informações de gatilho são enviadas ao dispositivo sem a carga útil da mensagem.
3. Sam seleciona um botão que registra um evento personalizado, disparando a mensagem no app com template.
4. O dispositivo de Sam faz uma requisição de rede para buscar a mensagem no app.
5. A lógica Liquid da mensagem resulta em uma interrupção, então a Braze registra isso como uma interrupção; Sam realizou a ação-gatilho antes dessa avaliação.

### Comparando o comportamento de interrupção de mensagens no app {#comparing-in-app-message-abort-behavior}

Esta tabela compara os fluxos de mensagens no app que Sam experimentou:

| Mensagem no app | Comportamento de interrupção |
| --- | --- |
| Padrão | Um evento de interrupção não foi registrado porque Sam não realizou nenhuma ação que dispararia uma mensagem.<br><br>Mensagens no app padrão não registram interrupções porque a definição de interrupção é "não viu a mensagem apesar de ter realizado a ação-gatilho". Como as mensagens no app são entregues ao dispositivo antes de as ações-gatilho ocorrerem, não faz sentido considerar mensagens no app omitidas por causa da lógica Liquid. |
| Com template | Um evento de interrupção foi registrado porque Sam realizou a ação-gatilho para disparar a mensagem no app com template, mas recebeu uma interrupção no processamento do Liquid.<br><br>Mensagens no app com template registram interrupções porque a avaliação do Liquid ocorre após a ação-gatilho ter sido realizada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparando o comportamento de interrupção de mensagens no app" }

### Quando o Connected Content é executado para mensagens no app? {#when-does-connected-content-run-for-in-app-messages}

Para [mensagens no app com template](#what-are-templated-in-app-messages), o Connected Content e outras Liquid tags são resolvidos quando o evento-gatilho ocorre e o dispositivo solicita a carga útil da mensagem — não quando o usuário clica em um botão dentro da mensagem. Cada busca com template pode incluir chamadas de Connected Content para aquela exibição.

Se o seu HTML faz referência a dados REST retornados pelo Connected Content, esses dados ficam disponíveis para a sessão em que a mensagem foi processada com template. Vários botões podem fazer referência à mesma resposta do Connected Content sem disparar chamadas adicionais ao clicar.

### Por que há um atraso antes de minha mensagem no app ser exibida? {#why-is-there-a-delay-before-my-in-app-message-displays}

Mensagens no app padrão são exibidas assim que a carga útil em cache está pronta após o evento-gatilho. No Android e iOS, imagens grandes ou outros ativos hospedados em CDN referenciados na mensagem podem adicionar um pequeno atraso enquanto esses recursos terminam de ser baixados antes de a mensagem no app aparecer.

[Mensagens no app com template](#what-are-templated-in-app-messages) e Campaigns com a opção **Reavaliar elegibilidade da campanha antes de exibir** selecionada exigem uma requisição de rede adicional após o gatilho antes de a mensagem aparecer. Isso pode adicionar um pequeno atraso (normalmente inferior a 100 ms em uma conexão estável). Para saber mais, consulte [Escolher usuários para segmentar]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-users-to-target).

### Por que minha mensagem no app parece diferente da prévia no dashboard? {#why-does-my-in-app-message-look-different-from-the-dashboard-preview}

Mensagens no app entregues podem diferir da prévia no dashboard quando:

- Sua integração aplica estilos personalizados ou sobrescreve a interface padrão de mensagens no app em determinadas plataformas
- A prévia usa um perfil de usuário teste com atributos diferentes dos do destinatário
- O conteúdo com template é resolvido de forma diferente no momento do envio em comparação com o modo de prévia

Use [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) com um usuário teste cujo perfil corresponda ao seu público-alvo ao validar a aparência.

### Por que uma mensagem no app de várias páginas usa o mesmo plano de fundo em todas as páginas? {#why-does-a-multi-page-in-app-message-use-the-same-background-on-every-page}

Quando a opção **Imagem de fundo** está ativada em uma página de uma mensagem no app de várias páginas, esse plano de fundo é aplicado a todas as páginas da mensagem. Para usar planos de fundo diferentes por página, use um bloco HTML personalizado com JavaScript para alternar as imagens entre as páginas.

### Como testo mensagens no app na web? {#how-do-i-test-web-in-app-messages}

O envio de teste de mensagens no app na web exige que o push esteja ativado no dispositivo de teste, pois o fluxo de teste entrega uma notificação por push que abre o app ou site onde a mensagem no app é exibida. O mesmo caminho de teste baseado em push se aplica em qualquer plataforma onde o push não esteja configurado com a Braze, embora a ausência de push seja mais frequentemente encontrada na web, já que muitas integrações mobile já possuem push ativado. Use uma Campaign ativa para um Segment de teste interno. Para ver as etapas, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

### Mensagens no app exigem integração de push? {#do-in-app-messages-require-push-integration}

Mensagens no app não exigem notificações por push para funcionar em produção. As mensagens no app são entregues pelo SDK da Braze e aparecem durante uma sessão ativa do app sem necessidade de integração de push.

No entanto, envios de teste para mensagens no app exigem que o push esteja ativado nos seus dispositivos de teste. Isso ocorre porque mensagens no app de teste são entregues por meio de uma notificação por push que dispara a exibição da mensagem no app. O usuário teste deve ter o push ativado e deve tocar na notificação por push de teste para visualizar a mensagem no app.

Para Campaigns em produção, os usuários veem mensagens no app com base nos gatilhos da sua Campaign (como início de sessão ou eventos personalizados) sem que o push esteja envolvido.

### Por que caracteres extras ou não renderizados aparecem na minha mensagem no app? {#why-do-extra-or-unrendered-characters-appear-in-my-in-app-message}

Copiar texto de outro app (como um processador de texto ou página da web) pode inserir caracteres invisíveis ou não imprimíveis no corpo da sua mensagem. Esses caracteres podem aparecer como símbolos estranhos ou quebrar o Liquid e o HTML em mensagens personalizadas.

Para corrigir caracteres estranhos ou não renderizados, redigite o texto afetado no editor da Braze ou exclua os caracteres indesejados diretamente, em vez de selecionar e substituir apenas o texto visível. Para mensagens HTML personalizadas com caracteres especiais, adicione `<meta charset="UTF-8">` dentro do `<head>` do seu HTML. Consulte [Codificação de caracteres]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) para mais detalhes.

## Por que o botão de fechar fica oculto em mensagens no app HTML em tela inteira no Android? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

Em dispositivos com telas de borda a borda (incluindo Android 15+), mensagens no app HTML em tela inteira podem ser desenhadas atrás da barra de status do sistema, ocultando o controle de fechar no topo do layout.

O SDK da Braze para Android versão 37.0.0 e posteriores aplicam insets de janela às mensagens no app HTML por padrão, para que os controles permaneçam na área segura. Se os usuários ainda perceberem sobreposição, faça upgrade para a versão mais recente do SDK da Braze para Android.

Em versões anteriores do SDK, os desenvolvedores podiam ativar `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` antes de esse comportamento se tornar o padrão.

## O que devo saber ao personalizar mensagens no app com arrastar e soltar? {#what-should-i-know-when-customizing-drag-and-drop-in-app-messages}

O [editor de arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) é compatível com os tipos de exibição modal e tela inteira. Você cria o conteúdo dentro desses contêineres usando blocos do editor.

Tenha em mente:

- **Links e deep links:** Cada ação ao clicar tem um campo de URL por padrão. Use Liquid na URL para variar os links por dispositivo, tipo de app ou atributos do usuário. No **Contêiner de mensagem**, você também pode ativar o comportamento ao clicar específico por plataforma para definir links diferentes para cada plataforma.
- **Opacidade e planos de fundo:** A opacidade no contêiner de mensagem afeta todo o plano de fundo da mensagem. Blocos individuais podem definir suas próprias cores de fundo. Para um controle mais refinado, adicione CSS personalizado em um bloco de Código Personalizado.
- **Largura da mensagem:** A largura máxima do **Contêiner de mensagem** não pode ser definida abaixo de 325 px no editor, o que mantém o conteúdo legível em telas menores. Use CSS personalizado se precisar de um layout mais estreito.
- **Planos de fundo específicos por plataforma:** Uma única mensagem usa a mesma imagem de fundo e cores na web e no mobile. Não é possível definir planos de fundo diferentes por plataforma no editor.
- **Mensagens com várias páginas:** Imagens de fundo e ações ao clicar no nível da mensagem se aplicam a todas as páginas em uma mensagem com várias páginas. Para usar imagens completas diferentes em cada página, adicione botões que direcionem para a próxima página.
- **Estilos no nível da mensagem:** Estilos no nível da mensagem se aplicam à mensagem inteira.
- **Imagens de fundo:** As imagens de fundo se esticam para preencher o modal.

Para saber mais sobre considerações do editor, consulte o [Guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide#drag-and-drop-editor-considerations).

## O que significa "Event was published, but no subscribers were found" nos logs do SDK Android? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Essa linha de log geralmente não é um erro. Ela costuma aparecer quando a Braze publica um evento interno (como `NoMatchingTriggerEvent`) e nenhum listener de mensagem no app ou Content Cards está inscrito naquele momento.

Se você vir esse log quando espera que um evento personalizado dispare uma mensagem no app, confirme se o evento está sendo registrado, se o usuário está no público da Campaign ou do Canvas e se os Content Cards estão sincronizados quando a mensagem depende deles.