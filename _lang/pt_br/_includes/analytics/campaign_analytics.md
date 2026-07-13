## Visualização de análises de dados {#viewing-analytics}

Uma vez que você lançou sua campanha, pode retornar à página de detalhes dessa campanha para visualizar métricas-chave. Navegue até a página **Campaigns** e selecione sua campanha para abrir a página de detalhes.{% if include.channel != "banner" %} Para {% if include.channel == "Content Card" %}Content Cards {% elsif include.channel == "banner" %}Banner {% elsif include.channel == "email" %}e-mail {% elsif include.channel == "in-app message" %}mensagens no app {% elsif include.channel == "KakaoTalk" %}mensagens KakaoTalk {% elsif include.channel == "push" %}mensagens push {% elsif include.channel == "SMS" %}mensagens SMS {% elsif include.channel == "whatsapp" %}mensagens WhatsApp {% elsif include.channel == "webhook" %}webhooks {% endif %}enviados no Canvas, consulte [Análise de dados do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).{% endif %}

{% alert tip %}
Procurando definições para os termos e métricas listados em seu relatório? Consulte nosso
  {% if include.channel == "email" %}[Glossário de análise de dados de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary)
  {% elsif include.channel == "banner" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por Banners.
  {% elsif include.channel == "Content Card" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por Content Cards.
  {% elsif include.channel == "in-app message" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por in-app message.
  {% elsif include.channel == "push" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por Push.
  {% elsif include.channel == "SMS" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por SMS/MMS e RCS.
  {% elsif include.channel == "whatsapp" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por WhatsApp.
  {% elsif include.channel == "webhook" %}[Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics) e filtre por Webhook.{% endif %}
{% endalert %}

Na guia **Campaign Analytics**, você pode visualizar seus relatórios em uma série de painéis. Você pode ver mais ou menos do que os listados nas seções abaixo, mas cada um tem seu próprio propósito útil.

### Período {#time-range}

Por padrão, o período para **Campaign Analytics** exibirá os últimos 90 dias a partir do momento atual. Isso significa que, se a campanha foi lançada há mais de 90 dias, a análise será exibida como "0" para o período selecionado. Para visualizar todas as análises de campanhas mais antigas, ajuste o período do relatório.

### Informações da campanha {#campaign-details}

O painel **Campaign Details** mostra uma visão geral de alto nível de todo o desempenho do
  {% if include.channel == "banner" %}seu Banner.
  {% elsif include.channel == "Content Card" %}seu cartão de conteúdo.
  {% elsif include.channel == "email" %}seu e-mail.
  {% elsif include.channel == "in-app message" %}sua mensagem no app.
  {% elsif include.channel == "KakaoTalk" %}sua mensagem KakaoTalk.
  {% elsif include.channel == "push" %}sua mensagem push.
  {% elsif include.channel == "SMS" %}SMS, MMS e RCS.
  {% elsif include.channel == "whatsapp" %}suas mensagens do WhatsApp.
  {% elsif include.channel == "webhook" %}seu webhook.
  {% endif %}

Revise este painel para ver métricas gerais, como o número de mensagens enviadas para o número de destinatários, a taxa de conversão primária e a receita total gerada por esta mensagem. Você também pode revisar as configurações de entrega, público e conversão a partir desta página.

{% alert note %}
Os números de análise de dados no dashboard e no Snowflake podem diferir ligeiramente. A Braze mede os números no dashboard e registra as linhas no Snowflake separadamente. O Snowflake é a fonte de dados mais precisa, então se você perceber discrepâncias entre essas fontes, recomendamos consultar os dados do Snowflake.
{% endalert %}

{% if include.channel == "whatsapp" %}
{% alert note %}
O canal do WhatsApp inclui a taxa de leitura. Esta métrica é entregue apenas para usuários com confirmações de leitura ativadas, o que pode variar.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_iam.png %})

No Canvas, você verá o desempenho da mensagem no app mapeado no Canvas que você criou. Você pode usar o painel de controle na parte superior da página para limpar outros tipos de envio de mensagens (canais) e visualizar apenas as mensagens no app em seu Canvas.

![Uma opção para selecionar o canal, com a caixa de seleção In-App Message marcada.]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "KakaoTalk" %}
![A seção de informações da campanha.]({% image_buster /assets/img/kakaotalk/campaign_details.png %})

{% elsif include.channel == "webhook" %}
![Painel de informações da campanha com uma visão geral das métricas usadas para determinar o desempenho da campanha.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

#### Estimated Audience e Current Audience {#estimated-audience-and-current-audience}

Dependendo do tamanho do seu espaço de trabalho, o painel **Campaign Details** pode rotular as estatísticas de público como **Estimated Audience** ou **Current Audience**.

A tabela a seguir resume o que cada rótulo significa.

| Rótulo do rodapé | Quando é usado |
| --- | --- |
| **Estimated Audience** | A Braze não executa uma contagem completa do banco de dados por padrão. O tamanho do público é estimado a partir de uma amostra e extrapolado, de forma semelhante ao intervalo de **usuários contatáveis** no criador de segmentos. Margens de erro são esperadas, especialmente para espaços de trabalho grandes ou segmentos pequenos em relação ao espaço de trabalho. |
| **Current Audience** | A Braze pode calcular a estatística padrão com uma varredura completa dos perfis do espaço de trabalho, então o tamanho do público exibido é uma contagem atual e não amostrada (ainda sujeita à acessibilidade do canal, regras de inscrição e outras opções de direcionamento). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estimated Audience e Current Audience" }

Para mais detalhes sobre o comportamento de amostragem, **Calculate exact statistics** e segmentação de **Reachable users**, consulte [Medir o tamanho do segmento]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

{% if include.channel == "Content Card" %}

#### Grupos de controle {#cc-control-group}

Para medir o impacto de um cartão de conteúdo individual, você pode adicionar um [grupo de controle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a um teste A/B. O painel **Campaign Details** de nível superior não inclui métricas da variante do grupo de controle.

{% elsif include.channel == "SMS" %}

#### Grupos de controle {#sms-control-group}

Para medir o impacto de uma mensagem SMS, MMS ou RCS individual, você pode adicionar um [grupo de controle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a um teste A/B. O painel **Campaign Details** de nível superior não inclui métricas da variante do grupo de controle.

{% elsif include.channel == "whatsapp" %}

#### Grupos de controle {#whatsapp-control-group}

Para medir o impacto de uma mensagem individual do WhatsApp, você pode adicionar um [grupo de controle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a um teste A/B. O painel **Campaign Details** de nível superior não inclui métricas da variante do grupo de controle.

{% elsif include.channel == "webhook" %}

#### Grupos de controle {#webhook-control-group}

Para medir o impacto de uma mensagem de webhook individual, você pode adicionar um [grupo de controle]({{site.baseurl}}/user_guide/intelligence/multivariate_testing#step-4-choose-a-segment-and-distribute-your-users-across-variants) a um teste A/B. O painel **Campaign Details** de nível superior não inclui métricas da variante do grupo de controle.

{% endif %}

#### Changes Since Last Viewed

O número de atualizações da campanha por outros membros da sua equipe é rastreado pela métrica *Changes Since Last Viewed* na página de visão geral da campanha. Selecione **Changes Since Last Viewed** para ver um changelog de atualizações no nome da campanha, cronograma, tags, mensagem, público, status de aprovação ou configuração de acesso da equipe. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar este changelog para auditar as mudanças na sua campanha.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Desempenho do Content Card {#content-card-performance}

O painel **Content Card Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Análise de desempenho da mensagem do Content Card]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### Desempenho de e-mail {#email-performance}

O painel **Email Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode selecionar o ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Análise de desempenho da mensagem de e-mail]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Desempenho de mensagem no app {#in-app-message-performance}

O painel **In-App Message Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Análise de desempenho da mensagem no app]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Desempenho de push {#push-performance}

O painel **Push Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Análise de desempenho da mensagem push]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### Desempenho de SMS/MMS/RCS {#smsmmsrcs-performance}

O painel **SMS/MMS/RCS Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Painel de desempenho de SMS/MMS/RCS que inclui uma tabela de métricas para um grupo de controle, Variante 1 e Variante 2.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Desempenho do Banner {#banner-performance}

O painel **Banner Performance** descreve o desempenho da sua mensagem em várias dimensões. Essas métricas variam dependendo do seu canal de envio de mensagens e se você está ou não realizando um teste multivariante.

![Painel de desempenho de Banner que inclui uma tabela de métricas para um grupo de controle, Variante 1 e Variante 2.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "KakaoTalk" %}
### Desempenho do KakaoTalk {#kakaotalk-performance}

O painel **KakaoTalk Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

{% elsif include.channel == "webhook" %}
### Desempenho de webhook {#webhook-performance}

O painel **Webhook Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Painel de desempenho de webhook que inclui uma tabela de métricas para um grupo de controle e Variante 1.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### Desempenho do WhatsApp {#whatsapp-performance}

O painel **WhatsApp Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está ou não executando um teste multivariante. Você pode clicar no ícone de <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![Painel de desempenho do WhatsApp que inclui uma tabela de métricas para a Variante 1.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Se você quiser simplificar sua visualização, clique em <i class="fas fa-plus"></i> **Add/Remove Columns** e desmarque quaisquer métricas conforme desejado. Por padrão, todas as métricas são exibidas.

{% if include.channel == "email" %}

#### Mapas de calor {#heatmaps}

Usando mapas de calor, você pode ver o desempenho dos diferentes links em uma única campanha de e-mail. Na seção **Message Analytics**, acesse o painel **Email Performance**. Selecione **Preview & Heatmap** para visualizar uma prévia da sua campanha de e-mail e o mapa de calor. Alternativamente, você pode selecionar o hyperlink no nome da variante para ver o mapa de calor.

{% alert note %}
A análise de dados da campanha exibe dados de cliques para até 100 URLs únicas por variante, classificadas por total de cliques. As URLs são agrupadas pela sua forma normalizada, que não inclui parâmetros de consulta. Se uma variante tiver mais de 100 URLs únicas normalizadas, apenas as 100 com mais cliques são exibidas. Os dados de cliques para URLs além desse limite ainda existem, mas não aparecerão no dashboard ou no mapa de calor. Quando o alias de link está ativado, os cliques são rastreados por ID de link em vez de URL bruta, o que normalmente resulta em menos entradas únicas e torna esse limite menos provável de ser atingido.
{% endalert %}

Nesta visualização, você pode usar o botão **Show Heatmap** para exibir uma visão visual do seu e-mail que mostra a frequência geral e a localização dos cliques durante a duração da campanha. No painel **Link Table by Total Clicks**, você pode ver todos os links na sua campanha de e-mail e classificar por total de cliques. Isso pode fornecer um insight adicional sobre onde seus usuários navegam. Para salvar uma cópia do mapa de calor para referência, selecione o botão de download.

{% alert note %}
Se os links usarem Liquid para URLs dinâmicas, as URLs clicadas podem não corresponder ao link renderizado na mensagem de forma suficiente para que o mapa de calor associe os cliques a esse link, então esses links podem não aparecer no mapa de calor. Use os dados de cliques no painel **Link Table by Total Clicks** para ter uma visão completa.
{% endalert %}

![Exemplo da página de Preview & Heatmap que inclui uma campanha de e-mail e um painel com exemplos de alias de link com seus cliques totais.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Imagens {#images}

Recomendamos ativar CORS para suas URLs de imagem para ajudar a evitar que as imagens quebrem nas pré-visualizações e exportações do mapa de calor.

Se as imagens estiverem faltando em uma exportação, trabalhe com seus desenvolvedores para que os ativos de imagem permitam acesso cross-origin: o servidor deve retornar o cabeçalho `Access-Control-Allow-Origin` com `*` ou o domínio do seu dashboard da Braze.

{% endif %}

{% if include.channel == "Content Card" %}

#### Métricas do Content Card {#content-card-metrics}

Aqui está uma análise de algumas métricas-chave que você pode ver ao revisar o desempenho da sua mensagem. Para as definições completas de todas as métricas de Content Cards, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) e filtre por Content Cards.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de Content Card">
    <caption class="sr-only">Métricas de desempenho de Content Card</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Messages Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                Isso é calculado de forma diferente dependendo do que você selecionou para
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Criação de cartão</a>:<br><br>
                <ul>
                    <li><b>No lançamento ou etapa de entrada:</b> O número de cartões criados e disponíveis para serem vistos. Isso não conta se os usuários visualizaram o cartão.</li>
                    <li><b>Na primeira impressão:</b> O número de cartões exibidos para os usuários.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Isso pode ser incrementado várias vezes para o mesmo usuário.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Essa contagem</span> não é incrementada na segunda vez que um usuário visualiza um Content Card.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Como um usuário pode ter uma impressão diária única todos os dias, você deve esperar que esse valor seja maior do que o de <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Unique Dismissals</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
Em relação a como as impressões são registradas, existem algumas nuances entre web, Android e iOS. De maneira geral, a Braze registra uma impressão quando um cartão é visto, o que ocorre após um usuário rolar até o Content Card específico em seu feed.
{% endalert %}

#### Unique Daily Impressions versus Unique Impressions

Existem algumas métricas disponíveis que cobrem a visibilidade da sua mensagem. Isso inclui _Unique Daily Impressions_ e _Unique Impressions_. Vamos usar alguns cenários de exemplo para entender melhor essas métricas.

Vamos supor que você visualize um Content Card hoje, depois receba um novo cartão da mesma campanha amanhã e novamente depois de amanhã — você será contado como _Unique Daily Impression_ três vezes. No entanto, você será contado apenas uma vez como _Unique Impression_. Você também será incluído no número de _Messages Sent_, já que o cartão estava disponível no seu dispositivo.

Como outro exemplo, suponha que você veja cinco _Unique Impressions_ em uma campanha de Content Card mostrando 150.000 _Messages Sent_. Isso significa que o cartão foi disponibilizado (no backend) para um público de 150.000 usuários, mas apenas cinco dispositivos de usuários realizaram todas as seguintes etapas após o envio ocorrer:

1. Iniciaram uma sessão ou o app solicitou explicitamente uma sincronização de Content Cards (ou ambos)
2. Navegaram para a visualização de Content Cards
3. O SDK registrou uma impressão e a enviou ao servidor

Suas _Messages Sent_ referem-se a Content Cards disponíveis para serem vistos, enquanto _Unique Daily Impressions_ referem-se a Content Cards que foram realmente vistos.

{% elsif include.channel == "banner" %}

### Métricas de Banner {#banner-metrics}

Essas são as principais métricas a serem acompanhadas ao revisar o desempenho da sua campanha de Banner. Cliques e impressões para Banners são rastreados automaticamente com o SDK.

Para as definições completas de todas as métricas de Banners, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) e filtre por Banners.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de Banner">
    <caption class="sr-only">Métricas de desempenho de Banner</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Para Banners, as impressões são registradas uma vez por sessão do usuário. Se o mesmo Banner for visualizado várias vezes dentro da mesma sessão, apenas uma impressão é registrada.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Cada usuário é contado apenas uma vez.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split"><i>Total Clicks</i> é o número total (e a porcentagem) de usuários que clicaram na mensagem entregue, independentemente de o mesmo usuário clicar várias vezes.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-dismissals">Total Dismissals</a></td>
            <td class="no-split"><i>Total Dismissals</i> é o número total de vezes que os usuários descartaram o Banner. Disponível apenas para Banners com comportamento de descarte ativado.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks No Dispatch ID' %} Cada usuário é contado apenas uma vez.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primary Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-daily-impressions">Unique Daily Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %} <br><br> Como um espectador pode ter uma impressão diária única todos os dias, você deve esperar que esse valor seja maior do que o de <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Revenue</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Confidence</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Exemplos de cálculo de métricas de Banner {#banner-metrics-calculation-examples}

Existem algumas métricas disponíveis que cobrem a visibilidade da sua mensagem. Isso inclui _Unique Daily Impressions_ e _Unique Impressions_. Vamos usar alguns cenários de exemplo para entender melhor essas métricas.

Vamos supor que você veja um Banner hoje, depois veja o mesmo Banner amanhã e novamente depois de amanhã — você será contado como _Unique Daily Impression_ três vezes. No entanto, você será contado apenas uma vez como _Unique Impression_.

Como outro exemplo, suponha que você veja cinco _Unique Impressions_ em uma campanha de Banner. Isso significa que apenas os dispositivos de cinco usuários realizaram todas as seguintes etapas:

1. Iniciaram uma sessão ou o app solicitou explicitamente uma sincronização de Banner (ou ambos)
2. Navegaram para a visualização de Banners
3. O SDK registrou uma impressão e a enviou ao servidor

_Unique Daily Impressions_ refere-se aos Banners que foram realmente vistos.

{% elsif include.channel == "email" %}

#### Métricas de e-mail {#email-metrics}

Aqui estão algumas métricas específicas de e-mail que você não verá em outros canais. Para ver as definições completas de todas as métricas de e-mail usadas na Braze, consulte nosso [Glossário de análise de dados de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de e-mail">
    <caption class="sr-only">Métricas de desempenho de e-mail</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Unique Clicks</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Isso é rastreado ao longo de um período de sete dias para e-mail e medido por <a href='{{ site.homeurl }}{{ site.baseurl }}/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a>. Isso inclui cliques em links de cancelamento de inscrição fornecidos pela Braze. Este número deve estar entre 5–10%. Qualquer coisa acima de 10% é excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Unique Opens</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Para e-mail, isso é rastreado ao longo de um período de 7 dias. Este número deve estar entre 30–40%. Qualquer coisa acima de 40% é excepcional!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Click-to-Open Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam Rate</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %} Se essa métrica for maior que 0,08, isso pode ser um sinal de que o texto da sua mensagem é muito comercial, ou você deve reconsiderar seus métodos de coleta de endereços de e-mail (para confirmar que você está enviando mensagens para aqueles que estão interessados na sua correspondência).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Unsubscribers or Unsub</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Other Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Estimated Real Opens</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Veja a seção a seguir para mais detalhes.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Machine Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Deferral</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Entregas e bounces {#deliveries-and-bounces}

O dashboard destaca os _Hard Bounces_. Alguns _Bounces_ podem ser soft bounces e não corresponderão a essa contagem sozinhos. Você pode estimar os soft bounces com esta fórmula:

_Envios − (Entregas + Hard Bounces) ≈ Soft Bounces_

As _Entregas_ podem aumentar durante a janela de novas tentativas do seu provedor de serviços de e-mail (ESP) conforme as novas tentativas são bem-sucedidas, enquanto os _Envios_ e hard bounces para um envio único permanecem fixos após a conclusão do envio. O SendGrid e o SparkPost fazem novas tentativas por até 72 horas; o Amazon SES faz novas tentativas por até 14 horas.

###### Cenários comuns de solução de problemas de entrega {#common-delivery-troubleshooting-scenarios}

Ao revisar sua análise de dados de e-mail, tenha estes padrões em mente:

- **Diferença entre _Envios_ e (_Entregas_ + _Hard Bounces_):** Durante a janela de novas tentativas do ESP após um envio único, essa diferença geralmente reflete soft bounces ou adiamentos que ainda estão sendo tentados novamente. Após o término das novas tentativas, qualquer diferença restante geralmente significa mensagens que sofreram soft bounce e nunca foram entregues — esses envios não são contados nas _Entregas_ ou _Bounces_ da campanha. Use a fórmula em [Entregas e bounces](#deliveries-and-bounces) para estimar os soft bounces em andamento.
- **_Entregas_ baixas após o término das novas tentativas:** Se as taxas de entrega permanecerem baixas após o término das novas tentativas, compare o volume deste envio com seus padrões típicos. Os provedores de caixa de e-mail podem adiar, limitar ou fazer soft bounce de e-mails quando o volume aumenta em relação à sua reputação de remetente. Você pode ver mensagens como `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Use o [limite de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) para controlar o ritmo de envios grandes, e consulte [IPs limitados]({{site.baseurl}}/user_guide/channels/email/reporting#throttled-ips) para etapas adicionais de solução de problemas.
- **Soft bounces e adiamentos não exibidos na análise de dados da campanha:** A análise de dados da campanha destaca _Hard Bounces_, mas não inclui _Soft Bounces_ ou _Adiamentos_ como colunas separadas. Monitore esses eventos no Registro de atividades de envio de mensagem, com o [filtro de segmento Soft Bounced]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced), ou através de eventos de adiamento do Currents. Para saber como as novas tentativas funcionam, consulte [Adiamentos](#deferrals).
- **Porcentagens de entrega que podem não somar 100%:** _% de Entregas_, _% de Bounces_ e _% de Spam_ podem não somar 100% dos _Envios_. Mensagens que sofrem soft bounce e nunca são entregues após a janela de novas tentativas do ESP não são contadas nas _Entregas_ ou _Bounces_ da campanha, então podem deixar uma parte dos _Envios_ sem contabilização nessas taxas. Aguarde até que as novas tentativas terminem antes de avaliar o desempenho final de entrega, ou use a fórmula em [Entregas e bounces](#deliveries-and-bounces) para estimar quantos envios ainda estão em nova tentativa.

##### Cliques sem um evento de abertura {#clicks-without-an-open-event}

Um clique pode ser registrado sem uma abertura quando o pixel de rastreamento de abertura nunca é carregado. Por exemplo, a mensagem é cortada no Gmail, ou o usuário desativou as imagens (o pixel de rastreamento de abertura geralmente fica no rodapé). Alguns clientes fazem proxy de imagens (como o Apple Mail), então a abertura pode ser registrada quando o servidor busca o pixel pela primeira vez, não quando o usuário lê o e-mail. Domínios corporativos frequentemente bloqueiam imagens por padrão.

Um clique e uma abertura também podem ocorrer em dias diferentes: um usuário pode clicar em 16 de maio com imagens desativadas (sem abertura), e depois abrir no webmail em 17 de maio (abertura registrada então).

##### _Unique clicks_ maior que _Unique opens_ {#higher-unique-clicks-than-unique-opens}

Você pode ver _Unique clicks_ superando significativamente _Unique opens_ (por exemplo, vários cliques únicos para cada abertura única) mesmo quando espera uma proporção menor do seu público. Esse padrão geralmente significa que as aberturas estão sendo subcontadas, os cliques estão inflados, ou ambos. No entanto, isso não significa que a Braze está contando cliques incorretamente de forma isolada.

A Braze registra uma abertura de e-mail quando o pixel de rastreamento de abertura é carregado. Esse pixel é uma pequena imagem transparente (geralmente descrita como 1 x 1&nbsp;px) que a Braze adiciona ao HTML da mensagem. Se o pixel nunca for carregado, nenhuma abertura é registrada para aquela visualização, mas os cliques em links ainda podem ser registrados — então sua taxa de clique-para-abertura e o equilíbrio entre essas duas métricas podem parecer distorcidos.

**A caixa de entrada nunca carregou o pixel de rastreamento de abertura**

O pixel pode não ser carregado quando:

- **A mensagem é cortada.** HTML longo empurra o conteúdo — incluindo o pixel no final — para trás de um corte do tipo "Ver mensagem completa". No Gmail, mensagens maiores que cerca de [102&nbsp;KB]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size) são frequentemente cortadas, o que pode impedir o carregamento do pixel até que a mensagem completa seja aberta (e às vezes nem assim, dependendo do cliente).
- **As imagens estão bloqueadas ou restritas.** Segurança mais rigorosa da caixa de entrada (comum em contas corporativas) pode bloquear imagens remotas até que o destinatário opte por carregá-las, então o pixel de abertura não é acionado mesmo que eles cliquem em links rastreados.
- **A mensagem está em pastas de spam ou lixo.** Muitos provedores não carregam imagens remotas (incluindo o pixel de abertura) nessas pastas por padrão.

**O que você pode fazer**

- **Corte:** Encurte e simplifique o HTML, remova estilos ou ativos não utilizados e mantenha o tamanho geral da mensagem dentro dos limites do cliente. Para o Gmail, mire em menos de cerca de 102&nbsp;KB conforme descrito em [Tamanho do e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/email_styling#email-size).
- **Segurança da caixa de entrada e carregamento de imagens:** Apenas o destinatário (ou sua política de TI) pode alterar se as imagens são carregadas por padrão.
- **Posicionamento em spam:** Concentre-se em [melhorar a entregabilidade de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability) e a higiene da lista. Se o e-mail está consistentemente caindo no spam e as métricas parecem erradas, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

**Atividade de segurança ou bots nos links**

Alguns produtos de segurança de e-mail seguem links para verificar ameaças. Essas solicitações podem registrar um clique sem carregar imagens, então você pode ver atividade de cliques sem uma abertura correspondente.

##### Adiamentos {#deferrals}

Adiamento é quando um e-mail não foi entregue imediatamente, mas a Braze tenta reenviar o e-mail através do seu ESP após essa falha temporária de entrega para maximizar as chances de entrega bem-sucedida antes que as tentativas para essa campanha específica sejam interrompidas. O SendGrid e o SparkPost fazem novas tentativas por até 72 horas; o Amazon SES faz novas tentativas por até 14 horas. As razões típicas para adiamentos incluem limitação de taxa de volume de e-mail baseada na reputação do provedor de caixa de entrada, problemas temporários de conectividade ou erros de DNS.

Os _Adiamentos_ diferem dos _Soft Bounces_. Se nenhum e-mail foi entregue com sucesso durante este período de nova tentativa, a Braze enviará um evento de soft bounce por campanha enviada. Antes de 25 de fevereiro de 2025, essas tentativas eram contadas como múltiplos soft bounces para 1 envio de campanha.

Observe que os _Adiamentos_ estão atualmente disponíveis apenas usando os recursos Currents ou Snowflake da Braze (como o Criador de consultas, SQL Segment, Compartilhamento de dados Snowflake). {% multi_lang_include product_feedback_cta.md context="gap" feature="Deferrals in campaign or Canvas analytics" %}

##### Taxa de abertura real estimada {#estimated-real-open-rate}

Esta estatística utiliza um modelo analítico proprietário criado pela Braze para reconstruir uma estimativa da taxa de abertura única da campanha como se as aberturas por máquina não existissem. Enquanto recebemos rótulos de *Machine Opens* em alguns eventos de abertura de remetentes de e-mail, esses rótulos podem frequentemente classificar aberturas reais como aberturas por máquina. Em outras palavras, as *Other Opens* provavelmente são uma subestimação das aberturas reais (por usuários reais). Em vez disso, a Braze usa dados de cliques de cada campanha para inferir a taxa na qual humanos reais abriram a mensagem. Isso compensa vários mecanismos de abertura por máquina, incluindo o MPP da Apple.

A _Estimated Real Open Rate_ é calculada 24 horas após o início do envio do e-mail e é recalculada a cada 72 horas a partir de então.

Como essa métrica é recalculada de forma contínua, o valor da _Estimated Real Open Rate_ pode mudar ao longo do tempo à medida que novos sinais de engajamento (como aberturas e cliques) são recebidos e incorporados ao modelo. Na prática, a _Estimated Real Open Rate_ pode continuar a ser atualizada diariamente enquanto uma campanha permanece ativa.

Normalmente, são necessários cerca de 10.000 e-mails entregues para que a estatística seja calculada com sucesso, embora esse número possa variar dependendo da taxa de cliques. Se a estatística não puder ser calculada, a coluna exibe "--".

###### Considerações {#considerations}

A Estimated Real Open Rate está disponível apenas em Campaigns e não é relatada em eventos do Currents. Esta métrica é calculada retroativamente apenas para campanhas ativas lançadas antes de 14 de novembro de 2023.

##### Lidando com aumentos nas taxas de cliques {#handling-increases-in-click-rates}

As taxas de abertura podem ser uma métrica útil para acompanhar suas campanhas de e-mail. No entanto, essas taxas de abertura não são necessariamente indicadores precisos do engajamento humano com campanhas de e-mail. Um evento de abertura, por definição, ocorre quando um usuário abre um e-mail, o que significa que um pixel de rastreamento de abertura transparente foi baixado com sucesso.

Além disso, o uso de ferramentas de verificação de segurança pode inflar as taxas de abertura. Algumas dessas ferramentas protegem seus usuários verificando os e-mails recebidos em busca de conteúdo malicioso, clicando em links para verificar sua legitimidade. Esses cliques são geralmente chamados de "cliques de bots" ou "interação não humana" (NHI).

Em última análise, depois que um e-mail sai de nossos servidores, temos visibilidade limitada sobre o que acontece a seguir, mas aqui estão recomendações para gerenciar NHI que afetam seus resultados:

1. Esteja ciente de que isso pode acontecer com qualquer remetente e quase qualquer destinatário. Os cliques, assim como as aberturas, não são indicadores totalmente confiáveis da interação humana com suas mensagens, o que significa que o NHI não pode ser evitado.
2. Um engajamento positivo mais alto tende a se correlacionar com um NHI mais baixo, por isso é importante seguir as [melhores práticas]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) de envio de e-mails. Isso inclui obter permissão explícita de seus usuários para o envio de e-mail e fazer sunsetting de assinantes não engajados em uma cadência regular.
3. Use links HTTPS em seus e-mails sempre que possível. O NHI é menos comum para remetentes que usam links seguros.
4. Se você usar um processo de cancelamento de inscrição com um único clique, considere criar uma [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) que leve os usuários a uma página para editar e gerenciar suas preferências de notificação. Isso pode ser útil porque o NHI pode cancelar inadvertidamente a inscrição de usuários.
5. Considere o uso de [outras métricas]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance) para medir o sucesso do seu e-mail marketing, como conversões, sessões de app ou visitas ao site.
6. Adicione um link oculto em suas campanhas de e-mail. Esse link seria algo que um ser humano não perceberia, como um texto branco sobre branco ou um sinal de pontuação. Bots tendem a clicar em todos os links, então você pode concluir que os usuários que geram eventos de clique no link invisível são, na verdade, resultado de NHI, portanto, a abertura ou o clique não indicam necessariamente um engajamento positivo.

{% elsif include.channel == "in-app message" %}

#### Métricas de mensagem no app {#in-app-message-metrics}

Aqui estão algumas métricas-chave de mensagem no app que você pode ver na análise de dados. Para ver as definições completas de todas as métricas de mensagem no app usadas na Braze, consulte nosso [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

{% alert note %}
Os relatórios para _Button 1 Clicks_ e _Button 2 Clicks_ funcionam apenas quando você especifica o **Identifier for Reporting** como "0" e "1", respectivamente, na mensagem no app.

![O campo "Identifier for Reporting" com um valor de "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de mensagem no app">
    <caption class="sr-only">Métricas de desempenho de mensagem no app</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Body Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Button 1 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Button 2 Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Unique Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Total Impressions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Conversions (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Total Conversions</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Conversion Rate</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Close Message</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

#### Discrepâncias entre grupos de controle e variantes {#discrepancies-between-control-groups-and-variants}

Quando uma campanha de mensagem no app tem uma divisão de variantes 50-50, às vezes o grupo de controle terá uma porcentagem ligeiramente maior do que a variante (como 51% para o grupo de controle e 49% para a variante). Essa discrepância é causada por uma diferença no tempo de renderização — por exemplo, quando mensagens de variante usam imagens grandes ou Connected Content com templates e os usuários saem antes que a renderização seja concluída, enquanto o grupo de controle registra impressões sem exibir uma mensagem.

A distribuição entre os grupos de controle e variante é projetada para ser aproximadamente equilibrada, mas a atribuição a uma variante ocorre quando a mensagem no app é realmente enviada ao dispositivo. Alguns usuários podem nunca acionar a mensagem no app (por exemplo, nunca realizam a ação que aciona o evento personalizado necessário), o que pode causar diferenças nos tamanhos dos grupos.

{% elsif include.channel == "KakaoTalk" %}

### Métricas do KakaoTalk {#kakaotalk-metrics}

Aqui estão algumas métricas-chave do KakaoTalk que você pode ver na análise de dados. Para mais detalhes, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics).

{% alert note %}
Atualmente, estatísticas de público estimadas ou exatas não estão disponíveis para Campaigns KakaoTalk.
{% endalert %}

| Termo | Definição |
| --- | --- |
| Público | _Público_ é a porcentagem de usuários que receberam uma mensagem específica. <br><br>_(Número de destinatários na variante) / (Destinatários únicos)_ |
| Destinatários únicos | _Destinatários únicos_ é o número de destinatários diários únicos, ou usuários que receberam uma nova mensagem em um dia. Para que essa contagem seja incrementada para um usuário mais de uma vez, o usuário deve receber uma nova mensagem em um dia diferente. Este número é baseado no `user_id`. Para mais detalhes, consulte [Destinatários únicos no Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics#unique-recipients). |
| Envios | O número total de mensagens enviadas em uma Campaign. Isso não significa que a mensagem foi recebida ou entregue a um dispositivo, apenas que a mensagem foi enviada. |
| Total de cliques | O número total de vezes que as mensagens KakaoTalk enviadas foram clicadas pelos usuários. |
| Erros | _Erros_ é o número de erros retornados pelo provedor KakaoTalk (incrementado durante o processo de envio). |
| Receita | _Receita_ é a receita em dólares dos destinatários da Campaign dentro da janela de conversão primária definida. |
| Conversões primárias | _Conversões primárias_ é o número de vezes que um evento definido ocorreu após interagir com ou visualizar uma mensagem recebida de uma Campaign da Braze. Esse evento definido é determinado por você ao criar a Campaign. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas do KakaoTalk" }

{% elsif include.channel == "push" %}

#### Métricas de push {#push-metrics}

Aqui está uma análise de algumas métricas-chave que você pode ver ao revisar o desempenho da sua mensagem. Para as definições completas de todas as métricas de push, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) e filtre por push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de push">
    <caption class="sr-only">Métricas de desempenho de push</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Bounces</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} Veja <a href="#bounced-push">Notificações por push devolvidas</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direct Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Opens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> A entrega de notificações é um "melhor esforço" do serviço de Notificações por Push da Apple (APNs). Não se destina a entregar dados ao seu app, apenas a notificar o usuário de que há novos dados disponíveis. A distinção importante é que exibiremos quantas mensagens entregamos com sucesso ao APNs, não necessariamente quantas o APNs entregou com sucesso aos dispositivos.

##### Rastreamento de cancelamentos de inscrição {#tracking-unsubscribes}

Os cancelamentos de inscrição por push não estão incluídos como uma métrica na análise de dados de Campaign e dependem de atualizações no status de push de um usuário por provedores como Apple ou Google. Essas atualizações podem ser pouco frequentes e imprevisíveis. Como resultado, os cancelamentos de inscrição por push não são incluídos como uma métrica na análise de dados de Campaign por push.

No entanto, o rastreamento manual de cancelamentos de inscrição por push ainda pode fornecer insights valiosos sobre as respostas dos usuários à frequência das notificações e à relevância do conteúdo. Aqui estão duas opções para rastrear cancelamentos de inscrição por push: usando filtros de segmento ou filtros personalizados.

{% tabs local %}
{% tab Filtros de segmento %}

Você pode criar um segmento para identificar usuários que não estão habilitados para push, o que significa que eles não estão inscritos ou não aceitaram receber e não têm um [token por push em primeiro plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration#push-tokens). Por exemplo, para ver o número de cancelamentos de inscrição em seu app, você usaria uma combinação "OU" dos seguintes segmentos:

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![A seção do criador de segmentos com o filtro "Background or Foreground Push Enabled for App" para um app é falso, e o filtro "Has Uninstalled" estão selecionados.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Observe que os filtros de segmentação são aproximados e não podem ser especificamente vinculados a uma data e Campaign.

{% endtab %}
{% tab Filtros personalizados %}

{% alert important %}
Registrar um evento personalizado para alteração de inscrição registrará [pontos de dados]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Como alternativa, use filtros de segmento para identificar e direcionar usuários que não estejam com push habilitado.
{% endalert %}

Para uma solução alternativa, também recomendamos a criação de um evento personalizado para cancelamentos de inscrição por push com base no fato de o status de push habilitado de um usuário ser `true` ou `false` para rastrear essa métrica.

{% endtab %}
{% endtabs %}

##### Entendendo as aberturas {#understanding-opens}

Mesmo que _Direct Opens_ e _Influenced Opens_ incluam a palavra "opens", na verdade são métricas diferentes. _Direct Opens_ refere-se à abertura direta de uma notificação por push. _Influenced Opens_ refere-se à abertura de um app sem abrir uma notificação por push dentro de um período de tempo específico após recebê-la. Portanto, _Influenced Opens_ refere-se às aberturas do app, não às aberturas de notificação por push.

##### Botões de ação por push e relatórios {#push-action-buttons-and-reporting}

Quando você adiciona [botões de ação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), o painel **Push Performance** pode incluir **Body Clicks**, **Button 1 Clicks** e **Button 2 Clicks** junto com métricas como **Direct Opens**. Essas colunas medem interações diferentes, então compare-as ao interpretar o engajamento.

_Direct Opens_ reflete as métricas do dashboard para interações que contam como uma abertura direta da sua mensagem. Os eventos **Push Notification Open** no [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou Snowflake descrevem interações de push de forma mais ampla e podem incluir campos opcionais como `button_action_type` (por exemplo, `close`) e `button_string`. Para definições de campos, consulte [Eventos de Push Notification Open]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#push-notification-open-events).

Para **iOS**, as categorias de notificação padrão da Braze (como **Yes** / **No**, **Accept** / **Decline** ou **Confirm** / **Cancel**) usam um pareamento fixo: a primeira ação suporta `OPEN_APP`, uma URI ou um deep link (alinhado com **On-Click Behavior** no criador). A ação complementar usa `CLOSE` por padrão — ela descarta a notificação e não abre o app. Veja o mapeamento padrão em [Objeto de botão de ação por push da Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-action-button-object-for-braze-default-buttons).

Por causa disso, toques no botão predefinido de descarte (por exemplo, **No** ou **Decline**) normalmente **não** contam para _Direct Opens_. Esses toques ainda podem aparecer nas exportações de **Push Notification Open** quando registrados, com `button_action_type` definido como `close` e `button_string` identificando a ação tocada. Ao comparar a análise de dados da Campaign com dados do warehouse, use esses campos da carga útil para não tratar toques de descarte da mesma forma que toques no corpo da notificação ou na ação principal.

Para **Android**, você define o **On-Click Behavior** por botão (**Open App**, **Redirect to Web URL** ou **Deep Link**), então os relatórios seguem as ações que você configura, em vez da divisão padrão `OPEN_APP` / `CLOSE` do iOS.

##### Por que os envios de push podem exceder os destinatários únicos {#why-push-sends-can-exceed-unique-recipients}

O número de _Sends_ pode exceder o número de _Unique Recipients_ devido aos seguintes motivos:

- **A reelegibilidade está ativada:** Quando a reelegibilidade está habilitada nas configurações da sua Campaign ou Canvas, os usuários que atendem aos critérios de segmento e entrega podem receber a mesma notificação por push várias vezes. Isso resulta em um número maior de envios totais.
- **Os usuários têm múltiplos dispositivos:** Se a reelegibilidade não estiver habilitada, a diferença pode ser explicada pelo fato de os usuários terem vários dispositivos associados ao seu perfil. Por exemplo, um usuário pode ter tanto um smartphone quanto um tablet, e a notificação por push está sendo enviada para todos os dispositivos registrados. Cada entrega conta como um envio, mas apenas um destinatário único é registrado.
- **Os usuários estão atribuídos a vários apps:** Se os usuários estiverem associados a mais de um app (como ao testar um novo app), eles podem receber a mesma notificação por push em cada app. Isso contribui para um maior número de envios.

##### Por que bounces ocorrem {#bounced-push}

{% tabs %}
{% tab Apple Push Notification service %}

Os bounces ocorrem no serviço de Notificações por Push da Apple (APNs) quando uma notificação por push tenta ser entregue a um dispositivo que não tem o app pretendido instalado. O APNs também tem o direito de mudar tokens para dispositivos de forma arbitrária. Se você tentar enviar para o dispositivo de um usuário cujo token por push mudou entre o momento em que registramos anteriormente seu token (como no início de cada sessão, quando registramos um usuário para um token por push) e o momento do envio, isso causaria um bounce.

Se um usuário desativar o push nas configurações do dispositivo, ao abrir o app novamente, o SDK detectará que o push foi desativado e notificará a Braze. Neste ponto, atualizaremos o estado de push habilitado para desabilitado. Quando um usuário desabilitado recebe uma Campaign de push antes de ter uma nova sessão, a Campaign seria enviada com sucesso e apareceria como entregue. O push não sofrerá bounce para este usuário. Após uma sessão subsequente, quando você tenta enviar um push para o usuário, a Braze já está ciente se temos um token em primeiro plano, portanto, nenhuma notificação é enviada.

Notificações por push que expiram antes da entrega não são consideradas como falhas e não serão registradas como um bounce.

{% endtab %}
{% tab Firebase Cloud Messaging %}

O Firebase Cloud Messaging (FCM) pode ter bounces em três casos:

| Cenário | Descrição |
| -- | -- |
| Apps desinstalados | Quando uma mensagem tenta ser entregue a um dispositivo e o app pretendido está desinstalado nesse dispositivo, a mensagem será descartada e o ID de registro do dispositivo será invalidado. Qualquer tentativa futura de envio de mensagens para o dispositivo retornará um erro NotRegistered. |
| App com backup | Quando um app é salvo em backup, seu ID de registro pode se tornar inválido antes que o app seja restaurado. Neste caso, o FCM não armazenará mais o ID de registro do app e o app não receberá mais mensagens. Assim, os IDs de registro **não** devem ser salvos quando um app é salvo em backup. |
| App atualizado | Quando um app é atualizado, o ID de registro da versão anterior pode não funcionar mais. Assim, um app atualizado deve substituir seu ID de registro existente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Por que bounces ocorrem" }

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### Métricas de SMS, MMS e RCS {#sms-mms-and-rcs-metrics}

Aqui está uma análise de algumas métricas-chave que você pode ver ao revisar o desempenho da sua mensagem. Para as definições completas de todas as métricas de SMS, MMS e RCS, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics) e filtre por SMS/MMS e RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de SMS, MMS e RCS">
    <caption class="sr-only">Métricas de desempenho de SMS, MMS e RCS</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Sent</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Delivery Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Confirmed Delivery</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Rejections</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-Out</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Help</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Total Clicks</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Métricas de webhook {#webhook-metrics}

Aqui estão algumas métricas-chave de webhook que você pode ver na análise de dados. Para ver as definições completas de todas as métricas de webhook usadas na Braze, consulte nosso [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas de webhook">
    <caption class="sr-only">Métricas de desempenho de webhook</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Errors</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### Métricas do WhatsApp {#whatsapp-metrics}

Aqui estão algumas métricas importantes do WhatsApp que você pode ver na análise de dados. Para ver as definições completas de todas as métricas do WhatsApp usadas na Braze, consulte nosso [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Métricas do WhatsApp">
    <caption class="sr-only">Métricas de desempenho do WhatsApp</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sends</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Deliveries</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Reads</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Failures</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Métricas de bloqueio e denúncia pelo usuário final {#end-user-blocking-and-reporting-metrics}

Métricas adicionais podem ser acessadas através do [dashboard do WhatsApp Manager](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx), embora a [confirmação do seu acesso](https://www.facebook.com/business/help/218116047387456) seja necessária para acessar todos os insights disponíveis.

{% endif %}

### Desempenho histórico {#historical-performance}

O painel **Historical Performance** permite que você visualize as métricas do painel **Message Performance** como um gráfico ao longo do tempo. Use os filtros na parte superior do painel para modificar as estatísticas e canais mostrados no gráfico. O período deste gráfico sempre refletirá o período especificado no topo da página.

Para obter uma análise dia a dia, clique no menu <i class="fas fa-bars"></i> hambúrguer e selecione **Download CSV** para receber uma exportação CSV do relatório.

![Um gráfico do painel de desempenho histórico com estatísticas de exemplo para um e-mail de fevereiro de 2021 a maio de 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Se você optar por enviar apenas para usuários que podem ver a versão mais recente da Braze das mensagens no app (Geração 3), seu **Público-alvo** não se ajusta para refletir sua escolha.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Respostas de palavras-chave {#keyword-responses}

O painel **Keyword Responses** mostra uma linha do tempo das palavras-chave recebidas com as quais os usuários responderam após receber sua mensagem.

![Painel de respostas de palavras-chave de SMS/MMS/RCS em nível de Campaign que inclui um gráfico de linha da distribuição de palavras-chave ao longo do tempo, e uma seção de categorias de palavras-chave com caixas de seleção marcadas para Opt-In, Opt-Out, Help, Other, More e Coaching.]({% image_buster /assets/img/sms/keyword_responses.png %})

Aqui, você também pode ver a distribuição de respostas de cada categoria de palavra-chave para determinar os próximos passos para [redirecionamento]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) e para convenientemente [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).

![Uma tabela que tem colunas para Keyword Category, Response Distribution e Retargeting, onde você tem a opção de criar um segmento com a categoria de palavra-chave.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Detalhes do evento de conversão {#conversion-event-details}

O painel **Conversion Event Details** mostra o desempenho dos seus eventos de conversão para sua Campaign. Para saber mais, consulte [Eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events#step-3-view-results).

![O painel de detalhes do evento de conversão.]({% image_buster /assets/img/cc-conversion.png %})

### Correlação de conversão {#conversion-correlation}

O painel **Conversion Correlation** oferece insight sobre quais atributos e comportamentos dos usuários ajudam ou prejudicam os resultados que você definiu para as campanhas. Para saber mais, consulte [Correlação de conversão]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

![O painel de correlação de conversão com uma análise sobre atributos e comportamento do usuário a partir do Primary Conversion Event - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "KakaoTalk" %}

## Criador de relatórios {#report-builder}

Você também pode usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reporting/report_builder) para criar relatórios personalizados para suas Campaigns KakaoTalk. Ao criar um relatório, você pode filtrar para incluir apenas Campaigns KakaoTalk selecionando **KakaoTalk** em **Canais**, ou filtrando por quaisquer tags que você tenha aplicado às suas Campaigns KakaoTalk.

{% endif %}

{% if include.channel == "whatsapp" %}

### Análise de dados do Meta {#meta-analytics}

Além da análise de dados da Braze, a análise de dados em nível de modelo pode ser acessada no WhatsApp Business Manager. Para mais informações, consulte a [documentação do Meta](https://www.facebook.com/business/help/218116047387456).

{% endif %}

{% if include.channel == "SMS" %}

### Eventos de Currents de SMS {#sms-currents-events}

Assim como e-mail, a Braze recebe eventos em nível de usuário relacionados a uma mensagem SMS enquanto ela faz sua jornada até um usuário. Qualquer evento de SMS recebido também será enviado como um evento do Currents através do evento [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events). Isso permite que você execute ações adicionais ou relatórios sobre as mensagens que seus usuários estão enviando fora da plataforma Braze.

{% alert note %}
As mensagens de entrada são truncadas após 1.600 caracteres.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Relatório de retenção {#retention-report}

Os relatórios de retenção mostram as taxas em que seus usuários realizaram um evento de retenção selecionado ao longo de períodos de tempo em uma Campaign específica{% if include.channel != "banner" %} ou Canvas{% endif %}. Para saber mais, consulte [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports).

## Relatório de funil {#funnel-report}

Os relatórios de funil oferecem um relatório visual que permite analisar as jornadas que seus clientes fazem após receber uma Campaign{% if include.channel != "banner" %} ou Canvas{% endif %}. Se sua Campaign {% if include.channel != "banner" %}ou Canvas {% endif %}usar um grupo de controle ou múltiplas variantes, você poderá entender como as diferentes variantes impactaram o funil de conversão de forma mais granular e otimizar com base nesses dados.

Para saber mais, consulte [Relatórios de funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports).

{% endif %}