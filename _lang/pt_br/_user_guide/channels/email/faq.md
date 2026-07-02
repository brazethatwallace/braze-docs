---
nav_title: FAQ
article_title: FAQ sobre e-mail
page_order: 30
description: "Esta página fornece respostas para perguntas frequentes sobre envio de mensagens por e-mail."
channel: email

---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre e-mails.

## O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail? {#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address}

Se vários usuários com endereços de e-mail correspondentes estiverem em um segmento para receber uma Campaign, um único perfil de usuário com esse endereço de e-mail é selecionado no momento do envio. Dessa forma, o e-mail é enviado apenas uma vez e deduplicado, garantindo que não chegue ao mesmo endereço de e-mail várias vezes.

**Endereços de e-mail únicos:** A Braze não exige endereços de e-mail únicos entre perfis. Se você depende de uma relação um-para-um entre um endereço de e-mail e um perfil, monitore duplicatas internamente ao criar usuários.

**Deduplicação antes do Liquid:** Para envios em que a Braze deduplica por endereço de e-mail dentro de um único despacho (por exemplo, Campaigns agendadas em que vários membros do segmento com o mesmo endereço são processados juntos), essa deduplicação acontece antes de o Liquid ser executado para o perfil escolhido para representar aquele endereço. Se o Liquid abortar para esse perfil (por exemplo, com [`abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)), esse endereço não recebe a mensagem naquele despacho — incluindo perfis já ignorados pela deduplicação. Envios disparados não aplicam essa mesma deduplicação de endereço dentro do despacho; vários perfis que compartilham um endereço podem permanecer elegíveis em um mesmo lote, então esse comportamento de abort não se aplica da mesma forma (veja o próximo parágrafo).

Se vários perfis compartilham um endereço de e-mail e um perfil cancela a inscrição, a Braze atualiza outros perfis (até 100) com esse endereço para o mesmo estado de inscrição. Isso se aplica a cancelamentos de inscrição e outras alterações, como estado de inscrição global e status de grupos de inscrições individuais.

**Grupos de teste:** Para Campaigns com [Grupos de teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#seed-groups), a Braze seleciona um perfil para entrega principal quando vários perfis compartilham um endereço. Esse destinatário principal pode não estar no seu grupo de teste, mesmo quando outro perfil com o mesmo endereço está.

Os cenários a seguir podem fazer parecer que um usuário recebeu um e-mail duas vezes:

- **Listas de teste ou destinatários de teste:** Endereços de teste e destinatários internos de teste podem receber um envio além do seu público principal, o que pode parecer uma duplicata quando uma caixa de entrada corresponde tanto a um perfil quanto a uma entrada de teste.
- **Ocorreu um erro durante a criação da Campaign ou do Canvas:** O usuário pode não receber literalmente o mesmo envio duas vezes, mas pode receber dois e-mails separados com o mesmo assunto. Quando uma Campaign ou Canvas é duplicado, verifique os detalhes de configuração do e-mail, como imagens ou linhas de assunto. Você também pode consultar os changelogs para ver se a Campaign ou o Canvas foi modificado após o lançamento — uma duplicata pode compartilhar o mesmo assunto do original quando o usuário o recebeu.
- **Vários perfis de usuário têm encaminhamento de e-mail:** Se um usuário tem várias contas em um determinado app, mas uma conta encaminha e-mails, o usuário recebe a Campaign uma vez por caixa de entrada; o e-mail pode aparecer duas vezes na caixa de entrada para onde as mensagens são encaminhadas. Apenas alguns provedores indicam quando um e-mail foi encaminhado de outra conta.
- **Configuração de e-mail no destinatário:** Alguns clientes mesclam caixas de entrada ("caixa de entrada universal"). Se a mesma Campaign direciona várias contas que compartilham uma caixa de entrada, pode parecer que uma pessoa recebeu a Campaign duas vezes quando, na verdade, dois perfis distintos foram contatados. O destinatário pode confirmar se várias contas estão combinadas em uma caixa de entrada.

Essa deduplicação se aplica quando os usuários direcionados estão no mesmo despacho. A reelegibilidade é avaliada por perfil, não por endereço de e-mail.

A reelegibilidade de Campaigns de e-mail e etapas do Canvas usa o perfil de cada usuário — não a caixa de entrada — então vários perfis podem se qualificar para envios separados enquanto essa lógica é satisfeita. Combinado com gatilhos, isso pode entregar mais de uma mensagem para a mesma caixa de entrada mesmo quando você está tentando respeitar um único período de inelegibilidade no nível do endereço. Campaigns disparadas (excluindo Campaigns disparadas por API) e Canvas também podem enviar duas vezes para o mesmo endereço quando perfis diferentes com endereços de e-mail correspondentes atendem ao gatilho em momentos diferentes — por exemplo, se o usuário A e o usuário B compartilham `johndoe@example.com`, mas estão em fusos horários diferentes enquanto a entrega usa fusos horários locais.

Os usuários não são deduplicados por e-mail na entrada do Canvas, então podem não ser deduplicados além da primeira etapa de um Canvas se progredirem em momentos ligeiramente diferentes devido à entrada com limite de taxa. Quando um usuário associado a um determinado endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham esse endereço de e-mail são marcados como tendo aberto ou clicado na Campaign.

### Exceção: Campaigns disparadas por API {#exception-api-triggered-campaigns}

Campaigns disparadas por API deduplicarão ou enviarão duplicatas dependendo de onde o público é definido. E-mails duplicados devem ser direcionados separadamente na chamada de API usando `user_ids` distintos para receber múltiplas entregas. Aqui estão três cenários possíveis para Campaigns disparadas por API:

- **Cenário 1: E-mails duplicados no segmento alvo:** Se o mesmo e-mail aparece em vários perfis de usuário que estão agrupados nos filtros de público do dashboard para uma Campaign disparada por API, apenas um dos perfis recebe o e-mail.
- **Cenário 2: E-mails duplicados em diferentes `user_ids` dentro do objeto de destinatários:** Se o mesmo e-mail aparece em vários valores de `external_user_id` referenciados pelo objeto `recipients`, o e-mail é enviado duas vezes.
- **Cenário 3: E-mails duplicados devido a `user_ids` duplicados dentro do objeto de destinatários:** Se você tentar adicionar o mesmo perfil de usuário duas vezes, apenas um dos perfis recebe o e-mail.

{% alert important %}
Se você enviar uma Campaign de API por meio de uma chamada de API (excluindo Campaigns disparadas por API) e vários usuários forem especificados no público do segmento com o mesmo endereço de e-mail, o envio será feito para esse endereço tantas vezes quantas estiver listado na chamada. Isso ocorre porque as chamadas de API são consideradas intencionalmente construídas.
{% endalert %}

#### Testes A/B com endereços de e-mail duplicados {#ab-testing-with-duplicate-email-addresses}

Evite [testes multivariantes e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing) em e-mail quando vários perfis podem compartilhar o mesmo endereço de e-mail. As variantes são atribuídas por perfil, o que pode produzir mais de uma mensagem para a mesma caixa de entrada. Se você precisar testar nessa situação, não combine uma etapa de **variante vencedora** com [entrega por fuso horário local]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) de forma que atrase a seleção do vencedor — essas opções juntas podem aumentar a chance de envios duplicados.

#### Canvas e endereços de e-mail duplicados {#canvas-and-duplicate-email-addresses}

Para jornadas do Canvas, se endereços de e-mail duplicados recebem um envio ou mais de um pode depender do lote de entrada, do timing das etapas e de outros fatores. Trate o comportamento como indefinido até que você o valide para a sua jornada. Sempre que possível, mescle ou consolide perfis duplicados. Se você precisar de uma alteração no produto, envie feedback por meio da sua equipe da Braze.

### O que acontece com o estado de inscrição quando o endereço de e-mail de um usuário é alterado para um compartilhado por outro usuário? {#what-happens-to-the-subscription-state-when-a-users-email-address-changes-to-one-shared-by-another-user}

Se você definir ou atualizar o endereço de e-mail do usuário A para outro endereço de e-mail compartilhado por um usuário B existente, o usuário A herda o estado de inscrição que já existe do usuário B, a menos que a configuração **Reinscrever usuários quando atualizarem seu e-mail** esteja ativada.

### As atualizações nas configurações de e-mail de saída serão aplicadas retroativamente? {#will-updates-to-my-outbound-email-settings-apply-retroactively}

Não. As atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes. Por exemplo, alterar o nome de exibição padrão nas configurações de e-mail não substituirá automaticamente o nome de exibição padrão existente nas suas Campaigns ou Canvas ativos.

### O que é uma "boa" taxa de entrega de e-mail? {#what-is-a-good-email-delivery-rate}

Normalmente, o "número mágico" é em torno de 98% das mensagens entregues com uma taxa de bounce não superior a 3%. Se sua entrega cair abaixo disso, geralmente há motivo para preocupação.

No entanto, uma taxa acima de 98% ainda pode ter problemas de entregabilidade. Por exemplo, se todos os seus bounces vêm de um único domínio, isso é um sinal claro de um problema de reputação com esse provedor.

Além disso, as mensagens podem estar sendo entregues e acabando na pasta de spam, indicando problemas de reputação potencialmente sérios. É importante monitorar não apenas o número de mensagens sendo entregues, mas também as taxas de abertura e clique para determinar se os usuários estão realmente vendo as mensagens em suas caixas de entrada. Como os provedores geralmente não reportam todas as instâncias de spam, uma taxa de spam de apenas 1% pode ser motivo de preocupação e análise adicional.

Por fim, seu negócio e os tipos de e-mails que você envia também podem afetar a entrega. Por exemplo, alguém que envia principalmente [e-mails de transação]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) deve esperar ver uma taxa melhor do que alguém que envia muitas mensagens de marketing.

### Por que minhas métricas de entrega de e-mail não somam 100%? {#why-are-my-email-delivery-metrics-not-adding-up-to-100}

As métricas de entrega de e-mail (entregas, bounces e taxa de spam) podem não somar 100% por causa de e-mails que sofreram soft bounce e não foram entregues após o período de nova tentativa de até 72 horas.

Soft bounces são e-mails que retornam devido a um problema temporário ou transitório, como "caixa de correio cheia", "servidor temporariamente indisponível" e outros. Se um e-mail com soft bounce ainda não for entregue após 72 horas, esse e-mail não será contabilizado nas métricas de entrega da Campaign.

### O que é um loop de feedback de e-mail? {#what-is-an-email-feedback-loop}

Um loop de feedback de e-mail (FBL) permite que os remetentes monitorem sua reputação identificando Campaigns que recebem um alto volume de reclamações. Para etapas de implementação de um loop de feedback do Gmail, consulte o artigo [Loop de Feedback do Google](https://support.google.com/a/answer/6254652).

### O que são pixels de rastreamento de abertura? {#what-are-open-tracking-pixels}

[Pixels de rastreamento de abertura]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#changing-location-of-tracking-pixel) utilizam o domínio de rastreamento de cliques do remetente para rastrear eventos de abertura de e-mail. O pixel é uma tag de imagem adicionada ao HTML do e-mail. Geralmente é o último elemento HTML dentro da tag body. Quando um usuário carrega seu e-mail, uma solicitação é feita para preencher a imagem a partir do domínio de rastreamento personalizado, o que registra um evento de abertura.

### O que acontece quando uma Campaign de e-mail ou Canvas é interrompido? {#what-happens-when-an-email-campaign-or-canvas-is-stopped}

Os usuários são impedidos de entrar no Canvas e nenhuma mensagem adicional é enviada.

Para Campaigns de e-mail e Canvas, o botão de parar não interrompe imediatamente o envio. Quando as solicitações de envio são disparadas, elas não podem ser impedidas de serem entregues ao usuário, o que pode acontecer após algum atraso.

Embora a Braze não envie mais solicitações depois que a Campaign ou o Canvas é interrompido, a análise de dados ainda pode aumentar enquanto o ESP termina de processar as solicitações que já estão em andamento.

### Por que estou vendo mais *Cliques Totais* do que *Aberturas Totais* na minha análise de dados de e-mail? {#why-am-i-seeing-more-_total-clicks_-than-_total-opens_-in-my-email-analytics}

*Aberturas Totais* é a contagem de quantas vezes o e-mail foi aberto pelos usuários, enquanto *Cliques Totais* é a contagem de quantas vezes os usuários clicaram dentro do e-mail entregue, incluindo qualquer tipo de clique, como cliques em links. Você pode estar vendo mais cliques do que aberturas por qualquer um dos seguintes motivos:

- Os usuários estão realizando múltiplos cliques no corpo do e-mail dentro de uma única abertura.
- Os usuários clicam em alguns links do e-mail dentro do painel de pré-visualização de seus celulares. Nesse caso, a Braze registra esse e-mail como clicado, mas não como aberto.
- Os usuários reabrem um e-mail que previamente visualizaram.

### Por que estou vendo zero aberturas e cliques de e-mail? {#why-am-i-seeing-zero-email-opens-and-clicks}

Você pode não ver aberturas ou cliques de e-mail se houver uma configuração incorreta no seu domínio de rastreamento. Isso pode ser devido a qualquer um dos seguintes motivos:
- Há um problema de SSL onde as URLs de rastreamento são `http` em vez de `https`.
- Há um problema com seu CDN onde a string de user agent nos eventos de abertura, eventos de clique ou ambos não está sendo preenchida.

### Quais são os riscos potenciais de disparar cliques de servidor? {#what-are-the-potential-risks-of-triggering-server-clicks}

Certos elementos de uma mensagem de e-mail, como mensagens excessivamente longas ou muitos pontos de exclamação, podem disparar respostas de segurança de e-mail. Essas respostas podem afetar os relatórios e a reputação do IP e levar os usuários a cancelar a inscrição.

Para melhores práticas sobre como lidar com essas respostas, consulte [Lidando com aumentos nas taxas de clique]({{site.baseurl}}/user_guide/channels/email/reporting).

### A Braze pode rastrear links de cancelamento de inscrição contabilizados na métrica "Cancelamento de inscrição"? {#can-braze-track-unsubscribe-links-counted-toward-the-unsubscribe-metric}

A Braze rastreia links de cancelamento de inscrição se o seguinte Liquid for usado nos e-mails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Por que estou vendo um número diferente de cancelamentos de inscrição do que cliques no meu link de cancelamento de inscrição? {#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link}

Se houver mais *Cancelamentos de inscrição* do que usuários que clicaram no link de cancelamento de inscrição no corpo do e-mail, o [**List-unsubscribe**]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) geralmente explica a diferença. O list-unsubscribe é um caminho adicional de cancelamento de inscrição no cabeçalho do e-mail (não o link no corpo da mensagem). Quando um usuário cancela a inscrição dessa forma, isso conta como *Cancelamento de inscrição*, mas não conta como um clique na URL de cancelamento de inscrição rastreada no corpo.

Se o número total de cliques no link de cancelamento de inscrição do corpo for maior que o número de *Cancelamentos de inscrição*, os usuários podem ter clicado no link mais de uma vez — por exemplo, se cancelaram a inscrição, se inscreveram novamente e depois cancelaram a inscrição de novo, a análise de dados de e-mail pode registrar múltiplos cliques no detalhamento de cliques.

Se um usuário clica no link de cancelamento de inscrição duas vezes (por exemplo, se cancelou a inscrição, se inscreveu novamente e depois cancelou a inscrição de novo), isso conta duas vezes na análise de dados de e-mail.

### Posso adicionar um link "visualizar este e-mail no navegador" aos meus e-mails? {#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails}

Não. A Braze não oferece essa funcionalidade. Isso ocorre porque a grande maioria dos e-mails é aberta em dispositivos móveis e em clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Alternativa:** Para alcançar o mesmo resultado, você pode hospedar o conteúdo do seu e-mail em uma landing page externa (como seu site), que pode então ser vinculada a partir da Campaign de e-mail que você está criando usando a ferramenta **Link** ao editar o corpo do e-mail.

### A Braze converte automaticamente URLs em texto simples ou texto "www." em links? {#does-braze-automatically-turn-plain-text-urls-or-www-text-into-links}

Não. A Braze não escaneia sua mensagem e converte texto simples, como texto que começa com `www.` ou que se parece com uma URL, em hiperlinks. Apenas links que você define com tags de âncora HTML (`<a href="...">`) são processados através da renderização normal e dos recursos de link da Braze.

Se um destinatário vê texto simples exibido como um link clicável, esse comportamento geralmente vem do cliente de e-mail dele (por exemplo, Gmail, Outlook ou Apple Mail). Muitos clientes detectam strings semelhantes a URLs após a mensagem ser entregue e as transformam em links no dispositivo do destinatário. A Braze não controla esse comportamento e não pode desativá-lo para o destinatário.

Para aparência, rastreamento e estilização previsíveis de links, use tags `<a href>` explícitas em vez de URLs em texto simples.

### Por que meus usuários estão sendo automaticamente cancelados por software de segurança de e-mail? {#why-are-my-users-being-auto-unsubscribed-by-email-security-software}

Algumas ferramentas corporativas de segurança de e-mail (como Barracuda, Proofpoint e serviços similares) pré-buscam ou escaneiam todas as URLs em e-mails recebidos, incluindo links de cancelamento de inscrição. Isso pode causar cancelamentos de inscrição não intencionais quando a ferramenta de segurança segue o link de cancelamento de inscrição com um clique.

Para mitigar isso:

- **Recomende que os destinatários adicionem seu domínio de envio à lista de permissões:** Trabalhe com as equipes de TI dos destinatários afetados para adicionar seu domínio de envio e os domínios de rastreamento da Braze à lista de permissões de segurança de e-mail.
- **Use uma Central de Preferências:** Em vez de um link direto de cancelamento de inscrição, use uma [Central de Preferências]({{site.baseurl}}/user_guide/channels/email/subscriptions) que exija interação do usuário para confirmar a ação de cancelamento de inscrição. Scanners de segurança normalmente não completam formulários de múltiplas etapas.
- **Revise os registros de cancelamento de inscrição:** Verifique o cabeçalho `User-Agent` e o endereço IP nos dados de eventos de cancelamento de inscrição do Currents para identificar padrões consistentes com escaneamento automatizado (como cabeçalhos `User-Agent` consistentes em múltiplos cancelamentos de inscrição).

Para mais detalhes sobre como o escaneamento do lado do servidor pode afetar as métricas de e-mail, consulte [Lidando com aumentos nas taxas de clique]({{site.baseurl}}/user_guide/channels/email/reporting#handling-increases-in-click-rates).

### Por que minha taxa de abertura por máquina mudou inesperadamente? {#why-has-my-machine-open-rate-changed-unexpectedly}

[Aberturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) são disparadas por recursos de segurança de e-mail, como a proteção de privacidade de e-mail do Apple Mail (MPP), que pré-carrega o conteúdo do e-mail (incluindo o pixel de rastreamento) sem que o usuário abra fisicamente o e-mail. As taxas de abertura por máquina podem flutuar com base em:

- Mudanças na proporção do seu público que usa Apple Mail ou outros clientes de e-mail com privacidade habilitada.
- Atualizações nos recursos de privacidade do provedor de e-mail ou comportamentos de detecção de bots.
- Mudanças na segmentação ou no direcionamento do seu público.

As porcentagens de abertura por máquina não são uma medida confiável do engajamento real. Para uma visão mais precisa do desempenho de e-mail, concentre-se em *Outras Aberturas* (aberturas não realizadas por máquina) e *Cliques Únicos*. Você também pode comparar essas métricas ao longo do tempo usando o [Dashboard de desempenho de e-mail]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance).

### Por que meus deep links não estão funcionando no Gmail? {#why-are-my-deep-links-not-working-in-gmail}

O Gmail remove todos os links não HTTP/HTTPS das mensagens de e-mail. Se seu deep link usa um esquema personalizado (como `myapp://path/to/content`), o Gmail o removerá e o link não funcionará para destinatários que leem o e-mail no Gmail. Essa é uma limitação do Gmail, não da Braze.

Para contornar isso:

- **Use Universal Links (iOS) ou App Links (Android).** Esses usam URLs padrão `https://` que abrem seu app quando instalado e redirecionam para uma página web caso contrário. Consulte [Universal Links e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links) para instruções de configuração.
- **Use um provedor de deep linking.** Serviços como [Branch](https://www.branch.io/) geram deep links em formato HTTP que são compatíveis com clientes de e-mail, incluindo o Gmail.
- **Configure um endpoint de redirecionamento.** Hospede um endpoint `https://` no seu servidor que redirecione para a URL de esquema personalizado do seu app. Os clientes de e-mail preservarão o link `https://`, e o redirecionamento cuida de abrir o app.

### A métrica *Aberturas Únicas* inclui *Aberturas por Máquina*? {#does-the-unique-opens-metric-include-machine-opens}

Sim. *Aberturas Únicas* inclui *Aberturas por Máquina*. Você pode visualizar ambas as métricas na visualização **Analytics** da Campaign e no **Criador de relatórios**.

### Por que meu volume de entrega de e-mail não corresponde ao meu volume de envio? {#why-does-my-email-delivery-volume-not-match-my-send-volume}

Depois que um e-mail é enviado, a caixa de entrada do destinatário decide quando ele é entregue. As mensagens podem ser adiadas por horas ou dias por causa de uma caixa de correio cheia, limitação do ESP a partir de um determinado IP e motivos semelhantes.

Quando mensagens adiadas são entregues em um dia diferente do dia de envio, as *Entregas* podem exceder os *Envios* para o mesmo intervalo de datas. Quando muitos adiamentos chegam em um dia, os *Envios* podem exceder as *Entregas* para esse intervalo.

### Por que estou vendo um aviso para incluir um link de cancelamento de inscrição quando meu e-mail já tem um? {#why-am-i-seeing-a-warning-to-include-an-unsubscribe-link-when-my-email-already-has-one}

Esse aviso pode persistir para Campaigns duplicadas a partir de uma Campaign que não tinha um link de cancelamento de inscrição. Para resolvê-lo:

- Para e-mails HTML, vá para a guia **Texto simples** e selecione **Regenerar a partir do HTML**.
- Após duplicar, duplique a variante e remova a variante original. **Não** selecione a variante original, ou o aviso pode ser transferido.

### Por que um usuário recebeu um e-mail que não deveria ter recebido? {#why-did-a-user-receive-an-email-they-shouldnt-have}

A entrega pode parecer incorreta mesmo quando a Braze se comportou conforme configurado. Analise os seguintes pontos:

- **Perfis duplicados** que compartilham uma caixa de entrada (veja [O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?](#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)).
- **Listas de teste, destinatários de teste ou endereços internos** incluídos no público ou em um envio como CC/BCC.
- **Timing do segmento ou Canvas:** o usuário correspondia ao público ou à etapa do Canvas quando a Braze avaliou a elegibilidade, e então os atributos ou o estado de inscrição mudaram antes de ele ler a mensagem.
- **Grupos de inscrições:** o usuário permaneceu inscrito em um grupo que sua mensagem direcionava, mesmo que o estado de inscrição global dele sugerisse o contrário.
- **Importações de API ou arquivo** que atualizaram o usuário após a segmentação, mas antes de você esperar que a alteração fosse aplicada.

Revise o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), os changelogs da Campaign ou do Canvas e a definição do segmento. Se ainda não conseguir reconciliar o envio, entre em contato com o suporte da Braze com os identificadores do usuário, `dispatch_id` (se disponível) e timestamps.

### Por que um usuário não recebeu minha mensagem de e-mail? {#why-hasnt-a-user-received-my-email-message}

Existem vários motivos pelos quais um usuário não recebe um e-mail que você esperava que ele recebesse, incluindo:

- Ele não era elegível para receber o e-mail.
- O endereço de e-mail dele é inválido ou não existe.
- Ele pode ter perdido ou excluído a mensagem.
- A mensagem pode estar na pasta de spam dele.

{% alert tip %}
Um evento de entrega na Braze significa que o e-mail foi aceito pelo servidor do provedor de caixa de e-mail. No entanto, isso não garante que a mensagem apareça na caixa de entrada do usuário. O provedor de caixa de e-mail pode rotear a mensagem para spam ou, em casos raros, impedir silenciosamente a exibição da mensagem.
{% endalert %}

Use as tabelas a seguir para identificar a causa.

#### O e-mail não foi enviado {#the-email-wasnt-sent}

| Causa possível | O que verificar |
|---|---|
| O usuário não era elegível para a Campaign ou Canvas | Verifique as configurações de **Público-alvo** (para Campaigns) ou **Público-alvo** (para Canvas) nas [configurações]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) para confirmar que o usuário atendeu a todos os filtros de público, critérios de segmento e regras de entrega no momento do envio. |
| A mensagem foi abortada | Verifique o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para motivos de abort, como erros de Liquid ou campos obrigatórios ausentes. |
| O endereço de e-mail do usuário era inválido ou estava ausente | Em **Pesquisa de usuários**, verifique o perfil do usuário para confirmar que um endereço de e-mail válido estava registrado no momento do envio. |
| O endereço de e-mail do usuário sofreu hard bounce anteriormente | Um hard bounce marca o endereço de e-mail como inválido e impede envios futuros para esse endereço. Da mesma forma, se um destinatário marcar seu e-mail como spam, a Braze envia apenas e-mails de transação para esse usuário, não Campaigns padrão. Verifique a guia **Engajamento** no perfil do usuário. Para saber mais, consulte [Endereços de e-mail cancelados]({{site.baseurl}}/user_guide/channels/email/subscriptions#unsubscribed-email-addresses) e [Bounces e e-mails inválidos]({{site.baseurl}}/user_guide/channels/email/subscriptions#bounces-and-invalid-emails). |
| O usuário cancelou a inscrição de e-mail | Verifique o status de inscrição do usuário em **Configurações de contato** na guia **Engajamento**. A Braze não envia e-mails para usuários que cancelaram a inscrição. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa para e-mail não enviado" }

#### O e-mail foi enviado, mas não chegou à caixa de entrada {#the-email-was-sent-but-didnt-arrive-in-their-inbox}

| Causa possível | O que verificar |
|---|---|
| O provedor de caixa de e-mail (MBP) estava inacessível | Um problema temporário impediu que o e-mail chegasse ao MBP do destinatário. Isso normalmente se resolve com novas tentativas. Os provedores de serviço de e-mail tentam novamente soft bounces por até 72 horas. |
| O MBP rejeitou o e-mail | O servidor de e-mail do destinatário rejeitou o e-mail. Revise o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para detalhes do bounce. |
| O MBP descartou silenciosamente o e-mail | O MBP aceitou o e-mail, mas não o exibiu para o usuário e não retornou um bounce. Isso está fora do controle da Braze e não pode ser detectado nos registros da Braze. |
| O e-mail foi para a pasta de spam | O MBP identificou a mensagem como spam e a roteou para a pasta de spam ou lixo eletrônico do usuário. Peça ao usuário para verificar a pasta de spam. |
| O destinatário tem filtragem de e-mail personalizada | O usuário ou o administrador de TI dele pode ter configurado regras de caixa de correio que filtram, redirecionam ou excluem mensagens recebidas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Causa para e-mail não na caixa de entrada" }

### Como posso otimizar imagens no Outlook? {#how-can-i-optimize-images-in-outlook}

O Outlook frequentemente usa renderização no estilo Microsoft Word, que pode adicionar uma borda ao redor das imagens. Você pode envolver o conteúdo para que fique oculto em clientes Office usando comentários condicionais padrão, por exemplo:

```html
<!--[if !mso]><!-- -->
<span>Content hidden in Outlook desktop</span>
<!--<![endif]-->
```

### Posso usar imagens SVG ou WebP nas minhas mensagens de e-mail? {#can-i-use-svg-or-webp-images-in-my-email-messages}

Imagens SVG não são recomendadas para e-mail devido ao suporte limitado entre os clientes de e-mail. O Gmail e vários outros provedores de e-mail importantes não renderizam imagens SVG, o que pode resultar em imagens quebradas ou ausentes para os destinatários. WebP não é consistentemente suportado entre os clientes.

Em vez disso, use formatos amplamente suportados como PNG ou JPEG para que as imagens sejam renderizadas de forma confiável.

### Variáveis Liquid atribuídas em uma parte do criador de mensagens podem ser usadas em outra? {#can-liquid-variables-assigned-in-one-part-of-the-message-composer-be-used-in-another}

Não. Cada parte do e-mail (assunto, corpo, cabeçalhos, botões e assim por diante) é gerada separadamente, então variáveis Liquid atribuídas em um campo não estão disponíveis em outro. Atribua variáveis em cada campo que precisar delas.

### Meu modelo de e-mail está faltando. Onde ele está? {#my-email-template-is-missing-where-is-it}

Primeiro, confirme que você tem as [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para visualizar modelos. Para ver os modelos de e-mail salvos, acesse **Conteúdo** > **E-mail**. Você pode filtrar modelos por status e tipo (HTML ou arrastar e soltar).

### Preciso registrar domínios para e-mails de relay ou mascarados? {#do-i-need-to-register-domains-for-relay-or-masked-emails}

O [Relay de E-mail Privado da Apple]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/email_private_relay_apple_SSO) exige que você registre seus domínios de envio no Portal de Desenvolvedores da Apple para evitar bounces. O Google Shielded Email não exige um processo manual de registro ou lista de permissões de domínio.

### O que significa o motivo de bounce `unable to get mx info` ou `failed to get IPs from PTR record`? {#what-does-the-bounce-reason-unable-to-get-mx-info-or-failed-to-get-ips-from-ptr-record-mean}

No [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), um motivo de bounce semelhante ao descrito acima indica um problema ao resolver a configuração de e-mail do domínio receptor (o domínio após o `@` no endereço), e não com a composição da mensagem na Braze:

As causas típicas incluem:

- **Registros MX** ausentes, incorretos ou inacessíveis para aquele domínio
- Nomes de host de e-mail de entrada que não resolvem ou que falham nas verificações de **PTR (DNS reverso)** esperadas pela infraestrutura receptora
- Domínios inválidos ou digitados incorretamente no endereço de e-mail

**Próximos passos:**

- Confirme a ortografia do endereço e do domínio.
- Se o endereço estiver correto, entre em contato com o proprietário da caixa de correio ou a equipe de TI daquele domínio.
- Peça que auditem os registros MX e registros DNS relacionados, incluindo registros PTR para seus servidores de e-mail, junto ao provedor DNS.

Outros destinatários geralmente não são afetados. Para saber como soft bounces aparecem nos relatórios, consulte [Soft Bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Por que recebo um alerta de spam ao enviar um e-mail da Braze para mim mesmo? {#why-do-i-get-a-spam-alert-when-sending-an-email-from-braze-to-myself}

Se você envia um e-mail de teste da Braze para o seu próprio endereço de e-mail e vê um aviso de spam ou alerta de phishing — como "o domínio de envio é semelhante ao domínio da sua empresa, mas não o reconhecemos" — isso é um recurso comum de segurança anti-phishing, não um erro na configuração da Braze.

Esse alerta normalmente aparece quando o domínio de envio do e-mail corresponde ao domínio do destinatário (por exemplo, ambos são `@suaempresa.com`). Os sistemas de segurança de e-mail sinalizam isso porque golpistas frequentemente falsificam domínios que se parecem com o domínio da empresa do destinatário.

Para verificar se seu e-mail está configurado corretamente:

1. Visualize a mensagem original (cabeçalhos brutos do e-mail) no seu cliente de e-mail.
2. Verifique se as autenticações SPF, DKIM e DMARC passaram.
3. Se todas as três passaram, o envio de e-mail da Braze está configurado corretamente.

Para evitar que esse alerta apareça:

Peça à sua equipe de TI para adicionar seu domínio de envio da Braze e os endereços IP à lista de permissões nos serviços de segurança de e-mail ou gateway de e-mail da sua empresa. Isso informa ao seu sistema de segurança que deve confiar nos e-mails vindos da sua infraestrutura de envio da Braze.