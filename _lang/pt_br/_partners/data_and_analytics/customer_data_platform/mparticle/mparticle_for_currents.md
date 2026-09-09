---
nav_title: mParticle para Currents
article_title: mParticle para Currents
alias: /partners/mparticle_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e a mParticle, uma CDP que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle para Currents {#mparticle-for-currents}

> A [mParticle](https://www.mparticle.com) é uma CDP que coleta e encaminha informações de várias fontes para uma variedade de outros locais em sua pilha de marketing.

A integração entre a Braze e a mParticle permite que você controle com praticidade o fluxo de informações entre os dois sistemas. Com o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), você também pode conectar dados à mParticle para torná-los acionáveis em todo o growth stack.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Currents | Para exportar dados de volta para a mParticle, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) configurado em sua conta. |
| Conta mParticle | É necessário ter uma [conta mParticle](https://app.mparticle.com/login) para usar essa parceria. |
| Chave e segredo de servidor para servidor da mParticle | Eles podem ser obtidos navegando até seu dashboard da mParticle e criando os [feeds necessários](#step-1-create-feeds) que permitem que a mParticle receba dados de interação da Braze para as plataformas iOS, Android e web. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Sobre as credenciais da mParticle {#about-mparticle-credentials}

A mParticle tem credenciais em nível de app e em nível de espaço de trabalho que impactam como seus eventos são enviados.

- **Nível de app:** a mParticle separa os eventos por cada app individual, o que significa que as credenciais em nível de app fornecidas ao seu app iOS só podem ser usadas para enviar eventos específicos do iOS.
- **Nível de espaço de trabalho:** a mParticle agrupa todos os eventos (que **não** são específicos de app), o que significa que as credenciais em nível de espaço de trabalho fornecidas ao seu grupo de apps serão usadas para enviar todos os seus eventos não específicos de app.

Você pode pensar nisso como a mParticle ingerindo um "feed" com base em cada app individual. Por exemplo, se você tem um app para iOS, um para Android e um para web, seus eventos serão separados. Isso significa que, se você fornecer as mesmas credenciais para cada app, um único feed da mParticle será usado para receber todos os dados de todos os seus apps, sem duplicação.

## Integração {#integration}

### Etapa 1: Criar feeds {#step-1-create-feeds}

Na sua conta de administrador da mParticle, navegue até **Setup > Inputs**. Localize **Braze** no **Directory** da mParticle e adicione a integração de feed.

A integração de feed da Braze suporta quatro feeds separados: iOS, Android, Web e Unbound. O feed unbound pode ser usado para eventos como e-mails que não estão conectados a uma plataforma. Você precisará criar uma entrada para cada feed de plataforma principal. Você pode criar entradas adicionais em **Setup > Inputs**, na guia **Feed Configurations**.

![Configuração de entrada de feed da mParticle mostrando as opções de feed iOS, Android, Web e unbound da Braze.]({% image_buster /assets/img/braze-feed-inputs.png %})

Para cada feed, em **Act as Platform**, selecione a plataforma correspondente na lista. Se você não vir uma opção para selecionar um feed **act-as**, os dados serão tratados como unbound, mas ainda poderão ser encaminhados para saídas de data warehouse.

![A primeira caixa de diálogo de integração, solicitando que você forneça um nome de configuração, determine um status de feed e selecione uma plataforma para atuar como.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![A segunda caixa de diálogo de integração mostrando a chave de servidor para servidor e o segredo de servidor para servidor.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Ao criar cada entrada, a mParticle fornecerá uma chave e um segredo. Copie essas credenciais, anotando a qual feed cada par de credenciais pertence.

### Etapa 2: Criar Current {#step-2-create-current}

Na Braze, navegue até **Currents > + Create Current > Create mParticle Export**. Forneça um nome de integração, e-mail de contato e a chave de API da mParticle e a chave secreta da mParticle para cada plataforma. Em seguida, selecione os eventos que deseja rastrear; uma lista de eventos disponíveis é fornecida. Por fim, clique em **Launch Current**.

![A página do mParticle Currents na Braze. Aqui, você encontra campos para nome da integração, e-mail de contato, chave de API e chave secreta.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
É importante manter sua chave de API da mParticle e a chave secreta da mParticle atualizadas. Se as credenciais do seu conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **5 dias**, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

Todos os eventos enviados à mParticle incluirão o `external_user_id` do usuário como `customerid`. Neste momento, a Braze não envia dados de eventos para usuários que não têm seu `external_user_id` definido. Se você deseja mapear o `external_user_id` para um ID diferente na mParticle que não seja o `customerid` padrão, entre em contato com seu CSM da Braze.

## Eventos de Currents compatíveis {#supported-currents-events}

A Braze suporta a exportação dos seguintes eventos para a mParticle:

- [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Para a estrutura de carga útil de cada evento, selecione a guia **mParticle** no [glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) e no [glossário de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

Para saber mais sobre a integração com a mParticle, visite a [documentação da mParticle](http://docs.mparticle.com/integrations/braze/feed).