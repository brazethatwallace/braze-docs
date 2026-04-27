---
nav_title: mParticle para Currents
article_title: mParticle para Currents
alias: /partners/mparticle_for_currents/
description: "Esse artigo de referência descreve a parceria entre a Braze Currents e a mParticle, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle para Currents {#mparticle-for-currents}

> [A mParticle](https://www.mparticle.com) é uma plataforma de dados do cliente que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração entre a Braze e o mParticle permite que você controle com praticidade o fluxo de informações entre os dois sistemas. Com [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), você também pode conectar dados ao mParticle para torná-los acionáveis em todo o growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados de volta para o mParticle, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
| Conta mParticle | É necessário ter uma [conta mParticle](https://app.mparticle.com/login) para usar essa parceria. |
| mParticle chave e segredo de servidor para servidor | Eles podem ser obtidos navegando até seu dashboard do mParticle e criando os [feeds necessários](#step-1-create-feeds) que permitem que o mParticle receba dados de interação da Braze para as plataformas iOS, Android e Web.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Sobre as credenciais do mParticle {#about-mparticle-credentials}

mParticle tem credenciais em nível de app e em nível de espaço de trabalho que impactam como seus eventos são enviados.

- **Nível de app:** o mParticle separa os eventos por cada app individual, o que significa que as credenciais em nível de app fornecidas ao seu app iOS só podem ser usadas para enviar eventos específicos do iOS.
- **Nível de espaço de trabalho:** o mParticle agrupa todos os eventos (que **não** são específicos de app), o que significa que as credenciais em nível de espaço de trabalho fornecidas ao seu grupo de app serão usadas para enviar todos os seus eventos não específicos de app.

Você pode pensar nisso como o mParticle ingerindo um "feed" com base em cada app individual. Por exemplo, se você tem um app para iOS, um para Android e um para Web, seus eventos serão separados. Isso significa que, se você fornecer as mesmas credenciais para cada app, um único feed do mParticle será usado para receber todos os dados de todos os seus apps, sem duplicação.

## Integração {#integration}

### Etapa 1: Criar feeds {#step-1-create-feeds}

Na sua conta de administrador do mParticle, navegue até **Setup > Inputs**. Localize **Braze** no **Directory** do mParticle e adicione a integração de feed.

A integração de feed da Braze suporta quatro feeds separados: iOS, Android, Web e Unbound. O feed unbound pode ser usado para eventos como e-mails que não estão conectados a uma plataforma. Você precisará criar uma entrada para cada feed de plataforma principal. Você pode criar entradas adicionais em **Setup > Inputs**, na guia **Feed Configurations**.

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Para cada feed, em **Act as Platform**, selecione a plataforma correspondente na lista. Se você não vir uma opção para selecionar um feed **act-as**, os dados serão tratados como unbound, mas ainda poderão ser encaminhados para saídas de data warehouse.

![A primeira caixa de diálogo de integração, solicitando que você forneça um nome de configuração, determine um status de feed e selecione uma plataforma para atuar como.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![A segunda caixa de diálogo de integração mostrando a chave de servidor para servidor e o segredo de servidor para servidor.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Ao criar cada entrada, o mParticle fornecerá uma chave e um segredo. Copie essas credenciais, anotando a qual feed cada par de credenciais pertence.

### Etapa 2: Criar Current {#step-2-create-current}

Na Braze, navegue até **Currents > + Create Current > Create mParticle Export**. Forneça um nome de integração, e-mail de contato e a chave de API do mParticle e a chave secreta do mParticle para cada plataforma. Em seguida, selecione os eventos que deseja rastrear; uma lista de eventos disponíveis é fornecida. Por fim, clique em **Launch Current**.

![A página do mParticle Currents na Braze. Aqui, você encontra campos para nome da integração, e-mail de contato, chave de API e chave secreta.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
É importante manter sua chave de API do mParticle e a chave secreta do mParticle atualizadas. Se as credenciais do seu conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

Todos os eventos enviados ao mParticle incluirão o `external_user_id` do usuário como `customerid`. Neste momento, a Braze não envia dados de eventos para usuários que não têm seu `external_user_id` definido. Se você deseja mapear o `external_user_id` para um ID diferente no mParticle que não seja o `customerid` padrão, entre em contato com seu CSM da Braze.

## Eventos de Currents compatíveis {#supported-currents-events}

A Braze suporta a exportação dos seguintes dados listados nos glossários de eventos de [comportamento do usuário]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) e [engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) do Currents para o mParticle:

### Comportamentos {#behaviors}
- Desinstalação: `users.behaviors.Uninstall`
- Inscrição (mudança de estado global): `users.behaviors.subscription.GlobalStateChange`
- Grupo de inscrições (mudança de estado): `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- Cancelamento: `users_campaigns_abort`
- Conversão: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`

### Canvas
- Cancelamento: `users_canvas_abort`
- Conversão: `users.canvas.Conversion`
- Entrada: `users.canvas.Entry`
- Saída (público correspondente, evento realizado)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Etapa de experimento (conversão, entrada dividida)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Mensagens {#messages}
- Cartão de conteúdo (cancelamento, clique, descarte, impressão, envio)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-mail (cancelamento, bounce, clique, entrega, marcar como spam, abertura, envio, soft bounce, cancelamento de inscrição)
- Mensagem no app (cancelamento, clique, impressão)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificação por push (cancelamento, bounce, abertura, envio)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (cancelamento, envio pela operadora, entrega, falha na entrega, recebimento de entrada, rejeição, envio, clique em link curto)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (cancelamento, envio)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (cancelamento, entrega, falha, recebimento de entrada, leitura, envio)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`


Para saber mais sobre a integração com o mParticle, visite a documentação deles [aqui](http://docs.mparticle.com/integrations/braze/feed).