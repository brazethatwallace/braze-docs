---
nav_title: Solução de problemas
article_title: Solução de problemas de mensagens no app para o SDK da Braze
page_order: 50
description: "Diagnostique por que mensagens no app não estão sendo entregues ou exibidas usando um índice de sintomas, caminho de investigação padrão, observações sobre Canvas e verificações específicas de plataforma no SDK."
channel:
  - in-app messages

---

# Solução de problemas de mensagens no app {#troubleshoot-in-app-messages}

> Use esta página para diagnosticar por que mensagens no app não estão sendo entregues ou exibidas em um dispositivo. Para configuração no dashboard (prioridade, gatilhos, Segments e reelegibilidade), consulte as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

Antes de depurar, adicione-se como [usuário teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) e revise [Envio de mensagens de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages).

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

| Sintoma | Acesse |
| --- | --- |
| A mensagem no app não apareceu para um usuário | [Um usuário](#in-app-message-not-shown-for-one-user) |
| A mensagem no app não apareceu em uma plataforma (Android, iOS ou Web) | [Uma plataforma](#in-app-message-not-shown-on-one-platform) |
| A mensagem no app de uma etapa do **Canvas** não apareceu | [Mensagens no app do Canvas](#canvas-in-app-messages) |
| A mensagem no app apareceu com atraso ou após uma postergação | [Tempo e exibição atrasada](#timing-and-delayed-display) |
| Impressões ou cliques parecem incorretos | [Impressões e análise de dados](#impressions-and-analytics) |
| `triggers` ausentes ou vazios nos registros de usuários de eventos | [Solução de problemas de entrega](#delivery-troubleshooting) |
| Gatilhos retornados, mas nada é exibido no dispositivo | [Solução de problemas de exibição por plataforma](#platform-specific-display-troubleshooting) |
| Falha ao carregar ativos da mensagem no app (iOS, `NSURLError` -1008) | [Carregamento de ativos (guia Swift)](?sdktab=swift#swift_asset-loading) |
| Links não são exibidos ou os logs do dispositivo mostram um erro de análise de ação ao clicar | [Configuração de link inválida](#invalid-link-setup) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de mensagem no app" }

## Caminho de investigação padrão {#standard-investigation-path}

Use este fluxo de trabalho para cada incidente. Comece na etapa 1.

1. Confirme que um **início de sessão** foi registrado para o dispositivo de teste. Mensagens no app são solicitadas no início da sessão.
2. Abra os [registros de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) e encontre a solicitação do SDK para o início da sessão. Em **Response Data**:
   - No JSON bruto, confirme que `respond_with` inclui `"triggers": true`.
   - A linha **Requested Responses** deve incluir **`triggers`**.
   - As linhas **Trigger In-App Message** listam cada mensagem no app retornada para essa solicitação.
   - Se não houver a chave `triggers` ou linhas **Trigger In-App Message**, acesse [Solução de problemas: mensagens não estão sendo solicitadas](#troubleshoot-messages-not-being-requested).
   - Se `triggers` estiver presente, mas vazio (`[]`), acesse [Solução de problemas: mensagens não estão sendo retornadas](#troubleshoot-messages-not-being-returned).
   - Se as linhas **Trigger In-App Message** estiverem presentes, mas nada for exibido, acesse [Solução de problemas de exibição por plataforma](#platform-specific-display-troubleshooting).
   - Cada payload de gatilho inclui um `type`: `inapp` (padrão) ou `templated_iam` (requer uma solicitação de modelo antes da exibição). Consulte [Tipos de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
3. Para elegibilidade no dashboard (Segment, reelegibilidade, limites de frequência, prioridade, grupos de controle), consulte [Solução de problemas de entrega](#delivery-troubleshooting) e as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
4. Para problemas de exibição no dispositivo (delegates, limites de taxa, orientação, tempo limite de sessão), selecione a guia do seu SDK em [Solução de problemas de exibição por plataforma](#platform-specific-display-troubleshooting).

## Mensagens no app do Canvas {#canvas-in-app-messages}

**Sintoma:** Um usuário entrou em uma etapa de mensagem no app do Canvas, mas não viu a mensagem quando esperado.

Três comportamentos são responsáveis pela maioria dos chamados sobre Canvas e mensagens no app:

1. **Exibição na próxima sessão:** Mensagens no app do Canvas ficam elegíveis no *próximo* início de sessão após a etapa ser processada — não imediatamente durante a sessão. Consulte [Quando as mensagens no app do Canvas são enviadas?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) nas Perguntas frequentes do Canvas.
2. **Validações de entrega na entrada da etapa:** Se **Validar público no envio da mensagem** estiver ativado na etapa de Mensagem, a associação ao Segment e os limites de frequência são avaliados quando o usuário **entra na etapa**, não no momento da exibição. Consulte [Validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
3. **Postergação e tempo limite de sessão:** Se um usuário entrar em uma etapa de postergação mais longa que o tempo limite de sessão do SDK, ele pode iniciar uma nova sessão antes da etapa de mensagem no app. A mensagem pode não ser buscada no início da sessão quando você espera que ela seja exibida.

Para janelas de disponibilidade, expiração e zero _Envios_ na análise de dados do Canvas, consulte [Mensagens no app e entrega]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery) nas Perguntas frequentes do Canvas.

{% alert important %}
Mensagens no app do Canvas só podem ser disparadas por eventos enviados pelo SDK, não pela REST API.
{% endalert %}

## A mensagem no app não apareceu para um usuário {#in-app-message-not-shown-for-one-user}

**Sintoma:** Um usuário não recebeu uma mensagem no app esperada; outros usuários podem não ter sido afetados.

Verifique o seguinte:

- O usuário estava no Segment no **início da sessão**, quando o SDK solicita novas mensagens no app?
- O usuário estava elegível ou reelegível de acordo com as regras de direcionamento da Campaign ou do Canvas? Consulte [Reelegibilidade para Campaigns e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Um [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) foi aplicado?
- O usuário estava em um grupo de controle da Campaign? Verifique se a Campaign está configurada para testes A/B.
- Uma mensagem no app de maior prioridade foi exibida no lugar? Consulte [Várias mensagens no app podem ser exibidas na mesma sessão?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session) nas Perguntas frequentes sobre In-App Messages.
- O dispositivo estava na orientação especificada pela Campaign?
- A mensagem foi suprimida pelo intervalo mínimo padrão de 30 segundos entre gatilhos? Consulte [Substituindo o limite de taxa padrão]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#overriding-the-default-rate-limit).

Em seguida, siga o [caminho de investigação padrão](#standard-investigation-path).

## A mensagem no app não apareceu em uma plataforma {#in-app-message-not-shown-on-one-platform}

**Sintoma:** Mensagens no app não aparecem no Android, iOS ou Web, mas podem funcionar em outras plataformas.

| Causa provável | O que verificar |
| --- | --- |
| Alvo de **Enviar para** incorreto | Confirme se a Campaign ou etapa do Canvas direciona para **Apps móveis** ou **Navegadores Web** conforme apropriado. Uma Campaign somente para Web não será enviada para dispositivos Android. |
| UI personalizada ou handler suprime a exibição | Revise os delegates (mobile) ou [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) (Web). Consulte [Personalização]({{site.baseurl}}/developer_guide/in_app_messages/customization) e a guia do seu SDK para a sua plataforma. |
| A integração nunca funcionou nesta plataforma | Confirme se esta plataforma e versão do app já exibiram mensagens no app anteriormente. |
| O gatilho não disparou no dispositivo | O gatilho deve ocorrer localmente pelo SDK. Uma chamada da REST API não pode disparar uma mensagem no app no SDK. Consulte [Disparando mensagens]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages). |
| `triggers` vazio nos registros de usuários de eventos | Segment, reelegibilidade, limite de frequência ou grupo de controle. Consulte [Solução de problemas: mensagens não estão sendo retornadas](#troubleshoot-messages-not-being-returned). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa do sintoma por plataforma" }

## A mensagem no app não apareceu para nenhum usuário {#in-app-message-not-shown-for-all-users}

**Sintoma:** Nenhum usuário ou menos usuários do que o esperado receberam a mensagem no app.

Verifique o seguinte:

- A ação-gatilho está configurada corretamente no dashboard e na integração do app?
- Uma mensagem no app de maior prioridade interceptou a Campaign? Consulte as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).
- Você está usando uma versão recente do SDK? Alguns tipos de mensagem no app têm requisitos mínimos de SDK.
- As sessões estão integradas corretamente? Confirme se a análise de dados de sessão funciona para este app.
- Uma biblioteca de UI personalizada está interferindo na exibição? Consulte [Personalização]({{site.baseurl}}/developer_guide/in_app_messages/customization).

Em seguida, siga o [caminho de investigação padrão](#standard-investigation-path).

## Tempo e exibição atrasada {#timing-and-delayed-display}

**Sintoma:** A mensagem no app apareceu mais tarde do que o esperado ou somente em uma nova sessão.

Causas comuns:

- **Pré-busca de Campaign no início da sessão:** Mensagens no app são armazenadas em cache no início da sessão e exibidas quando o gatilho dispara. Um gatilho que ocorre antes do próximo início de sessão não será exibido até essa sessão. Consulte [Disparando mensagens]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).
- **Comportamento de próxima sessão do Canvas:** Consulte [Mensagens no app do Canvas](#canvas-in-app-messages).
- **Postergação agendada no dashboard:** Confirme se uma postergação está configurada na Campaign ou etapa.
- **Condição de corrida na sincronização de gatilhos:** Se os usuários registram um evento imediatamente após o início da sessão, os gatilhos podem ainda não estar sincronizados. Considere disparar pelo início de sessão e segmentar pelo evento pretendido, para que a entrega ocorra na próxima sessão após o evento.
- **Mensagens no app sequenciais:** Se você está adiando ou restaurando mensagens em um tour, consulte [Adiando mensagens no app disparadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
- **Ativos grandes ou CDN lento:** Otimize imagens e vídeos para mensagens no app em HTML. Em dispositivos móveis, as imagens podem ser baixadas antes da exibição em redes lentas — selecione a guia do seu SDK para notas específicas da plataforma.

{% alert note %}
Se sua mensagem no app é disparada pelo início de sessão e você definiu um tempo limite de sessão estendido, fechar e reabrir o app dentro dessa janela não atualizará a sessão. Por exemplo, com um tempo limite de 300 segundos, uma mensagem no app disparada pelo início de sessão não será exibida até que a sessão seja realmente atualizada. Ajuste o tempo limite de sessão ou o tipo de gatilho se isso afetar seu teste.
{% endalert %}

## Solução de problemas de entrega {#delivery-troubleshooting}

A maioria dos problemas com mensagens no app é de **entrega** (o dispositivo não recebeu os gatilhos) ou de **exibição** (os gatilhos chegaram, mas não foram exibidos). Confirme a [entrega](#troubleshooting-in-app-message-delivery) primeiro e depois verifique a [exibição](#platform-specific-display-troubleshooting).

### Solução de problemas de entrega {#troubleshooting-in-app-message-delivery}

O SDK solicita mensagens no app dos servidores da Braze no início da sessão. Confirme se o SDK está solicitando gatilhos e se a Braze está retornando-os.

#### Verifique se as mensagens estão sendo solicitadas e retornadas {#check-if-messages-are-requested-and-returned}

1. Adicione-se como [usuário teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).
2. Configure uma Campaign de mensagem no app direcionada ao seu usuário.
3. Inicie uma nova sessão no seu aplicativo.
4. Nos [registros de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log), encontre a solicitação do SDK para o evento de início de sessão. Em **Response Data**:
   - No JSON bruto, confirme que `respond_with` inclui `"triggers": true`.
   - A linha **Requested Responses** lista as chaves de nível superior na resposta. Para mensagens no app, espere **`triggers`**.
   - As linhas **Trigger In-App Message** listam cada mensagem no app retornada para essa solicitação.

   Em seguida, faça a triagem:
   - Se não houver a chave `triggers` ou linhas **Trigger In-App Message**, consulte [Solução de problemas: mensagens não estão sendo solicitadas](#troubleshoot-messages-not-being-requested).
   - Se `triggers` estiver presente, mas vazio (`[]`), consulte [Solução de problemas: mensagens não estão sendo retornadas](#troubleshoot-messages-not-being-returned).
   - Se as linhas **Trigger In-App Message** estiverem presentes, mas nada for exibido no dispositivo, consulte [Solução de problemas de exibição por plataforma](#platform-specific-display-troubleshooting).
   - Cada payload de gatilho inclui um `type`: `inapp` (padrão) ou `templated_iam` (requer uma solicitação de modelo antes da exibição). Consulte [Tipos de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#types-of-in-app-messages).
5. Confirme se as mensagens no app corretas aparecem nos dados de resposta.

![Registro de usuários de eventos com solicitações do SDK e dados de resposta.]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Solução de problemas: mensagens não estão sendo solicitadas {#troubleshoot-messages-not-being-requested}

Se as mensagens no app não estão sendo solicitadas, seu app pode não estar rastreando sessões corretamente — mensagens no app são atualizadas no início da sessão. Confirme se o app está iniciando uma sessão com base na semântica de tempo limite de sessão:

![A solicitação do SDK encontrada nos registros de usuários de eventos exibindo um evento de início de sessão bem-sucedido.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Solução de problemas: mensagens não estão sendo retornadas {#troubleshoot-messages-not-being-returned}

Se as mensagens no app não estão sendo retornadas, provavelmente há um problema de direcionamento ou elegibilidade:

1. Seu Segment não contém seu usuário.
   - Verifique a guia [**Engajamento**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) do usuário para o Segment esperado.
2. Seu usuário já recebeu a mensagem e não estava reelegível.
   - Verifique as [configurações de reelegibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) e as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#campaigns).
3. Seu usuário atingiu o limite de frequência.
   - Verifique as [configurações de limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).
4. Seu usuário caiu em um grupo de controle.
   - Crie um Segment com um filtro **Recebeu variante de campanha** definido como **Controle**, ou desative os grupos de controle durante os testes de integração.
5. Uma mensagem no app de maior prioridade teve precedência. Consulte as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#can-multiple-in-app-messages-display-in-the-same-session).

Para Campaigns arquivadas, configuração de gatilhos e horário de silêncio, consulte as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Impressões e análise de dados {#impressions-and-analytics}

**Sintoma:** As contagens de impressões ou cliques não correspondem às expectativas.

- **_Impressões_ maiores que _Impressões únicas_:** Esperado quando os usuários têm vários dispositivos ou quando uma postergação agendada faz com que o mesmo usuário se qualifique mais de uma vez. Consulte [Reelegibilidade para Campaigns e Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- **Impressões menores que o esperado:** Os usuários podem não ter visualizado a mensagem (impressões são registradas na exibição), várias mensagens de alta prioridade podem interceptar umas às outras, ou condições de corrida na sincronização de gatilhos podem se aplicar. Para mensagens no app do Canvas, consulte [Mensagens no app do Canvas](#canvas-in-app-messages). Para definições completas de métricas, consulte [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) e as [Perguntas frequentes sobre In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).
- **Impressões menores que antes:** Revise os changelogs do Segment e da Campaign. Confirme se você não reutilizou o mesmo evento-gatilho em uma Campaign de maior prioridade.

![Link para visualizar o changelog na página de detalhes da Campaign com sete alterações desde a última visualização do usuário.]({% image_buster /assets/img_archive/trouble4.png %})

Se você usa um delegate ou handler personalizado para exibir mensagens no app manualmente, é necessário registrar impressões e cliques por conta própria. Consulte a guia do seu SDK em [Solução de problemas de exibição por plataforma](#platform-specific-display-troubleshooting) para detalhes sobre Swift e Android, ou [Registrar dados de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data) para Web.

## Configuração de link inválida {#invalid-link-setup}

**Sintoma:** Links não são exibidos em uma mensagem no app, ou os logs do dispositivo fazem referência a um erro de análise de ação ao clicar (por exemplo, um erro mencionando uma ação de clique de mensagem de plataforma inválida).

Isso geralmente indica um link inválido ou malformado na configuração da mensagem no app.

Verifique o seguinte:

- Altere temporariamente o comportamento ao clicar para **Fechar mensagem**. Se a mensagem for exibida corretamente, o URL do link provavelmente está causando o problema.
- Revise a configuração de links para o seu editor e tipo de mensagem:
  - **HTML personalizado:** [Solução de problemas de links e comportamento de fechamento em HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#troubleshoot-custom-html-links-and-close-behavior)
  - **Arrastar e soltar:** [Links e deep links]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-should-i-know-when-customizing-drag-and-drop-in-app-messages) nas Perguntas frequentes sobre In-App Messages e [requisitos mínimos de SDK para links de texto]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#more-information-on-minimum-sdks)
  - **Mensagens com botões:** [Personalizar mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/customization) para a sua plataforma

## Solução de problemas de exibição por plataforma {#platform-specific-display-troubleshooting}

Se as linhas **Trigger In-App Message** aparecem nos registros de usuários de eventos, mas nada é exibido no dispositivo, selecione a guia do seu SDK para verificações de exibição (delegates, limites de taxa, orientação e handlers personalizados).

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/troubleshooting.md %}
{% endsdktab %}
{% endsdktabs %}