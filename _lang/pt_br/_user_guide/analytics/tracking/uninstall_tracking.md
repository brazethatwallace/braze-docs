---
nav_title: Rastreamento de desinstalação
article_title: Rastreamento de desinstalação
page_order: 1
page_type: reference
description: "Este artigo de referência aborda a implementação do rastreamento de desinstalação para estatísticas em nível de campanha e de aplicativo."
tool: Reports

---

# Rastreamento de desinstalação {#uninstall-tracking}

> Este artigo mostra como você pode visualizar desinstalações agregadas de aplicativos ao longo do tempo para localizar tendências e anomalias e rastrear desinstalações no nível da campanha para determinar se uma campanha específica está impulsionando ou impedindo instalações de aplicativos.

O rastreamento de desinstalação na Braze fornece os seguintes detalhes:

1. Estatísticas diárias de desinstalação no nível do app em um gráfico de série temporal na página **inicial**.
2. Estatísticas de desinstalação em nível de campanha em um gráfico de série temporal na página **Campaign Details** de uma campanha específica. Essa estatística especifica o número de destinatários da campanha que desinstalam a cada dia.

{% alert note %}
Você deve optar pelo rastreamento de desinstalação no seu dashboard da Braze. Este recurso está disponível para apps no iOS, Android e Fire OS.
{% endalert %}

## Como funciona {#how-it-works}

A Braze coleta automaticamente um nível básico de informações sobre desinstalações a partir das suas Campaigns de push regulares. No entanto, como a frequência com que diferentes usuários recebem Campaigns de push pode variar, oferecemos o rastreamento de desinstalação para fornecer um panorama mais preciso da atividade de desinstalação entre seus usuários.

Quando a Braze detecta uma desinstalação, o usuário é marcado como tendo desinstalado o app. Se você usar o filtro **Has Not Uninstalled** em uma Campaign, esses usuários marcados serão excluídos. Se um usuário reinstalar o app mas não abri-lo, a tag de desinstalação permanece no perfil. A tag só é removida quando o usuário inicia uma nova sessão no app reinstalado. Isso significa que um usuário que reinstala o app mas nunca o abre continua aparecendo como desinstalado.

Para saber mais sobre o uso do rastreamento de desinstalação, consulte nossa postagem no blog [Rastreamento de desinstalação: uma visão do setor sobre seus pontos fortes e limitações](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Ativando o rastreamento de desinstalação {#turning-on-uninstall-tracking}

Você pode ativar o rastreamento de desinstalação na página **App Settings**, em **Settings**, para cada app que deseja rastrear.

Quando você ativa o rastreamento de desinstalação para um app, a Braze envia uma notificação por push silenciosa em segundo plano todas as noites para os usuários que não registraram uma sessão ou receberam um push nas últimas 24 horas.

### Configuração {#configuration}

Para configurar o rastreamento de desinstalação para seu aplicativo iOS, use um [método utilitário]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift). Para seu aplicativo Android, use [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Quando a Braze detecta uma desinstalação, seja por meio do rastreamento de desinstalação ou da entrega normal de uma Campaign de push, registramos o melhor horário estimado da desinstalação no perfil do usuário. Esse horário é armazenado no perfil de usuário como um atributo padrão e pode ser usado para definir um Segment de usuários para campanhas de recuperação.

## Filtrando Segments por desinstalações {#filtering-segments-by-uninstalls}

O filtro **Desinstalado** seleciona usuários que desinstalaram seu app dentro de um período. Como é difícil determinar o momento exato de uma desinstalação, recomendamos que os filtros de desinstalação tenham períodos mais amplos para garantir que todos os que desinstalaram sejam incluídos no Segment em algum momento.

As estatísticas diárias de desinstalações estão na página **Início**.

![Segment de desinstalação.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

O gráfico pode ser detalhado por app e Segment, de forma semelhante a outras estatísticas que a Braze oferece. Na seção **Performance overview**, selecione o período e, se desejar, um app. Em seguida, role para baixo até o gráfico **Performance Over Time** e faça o seguinte:

1. No menu suspenso **Statistics For**, selecione **Uninstalls**.
2. No menu suspenso **Breakdown**, selecione **By segment**.
3. No menu suspenso **Breakdown Values**, selecione os Segments a serem incluídos no gráfico.

{% alert note %}
Apps sem rastreamento de desinstalação ativado reportarão desinstalações apenas de um subconjunto de seus usuários (aqueles que foram direcionados com notificações por push), portanto os totais diários de desinstalação podem ser maiores do que o exibido.
{% endalert %}

## Rastreamento de desinstalação para Campaigns {#uninstall-tracking-for-campaigns}

O rastreamento de desinstalação de Campaigns mostra o número de usuários que receberam uma Campaign específica e, em seguida, desinstalaram seu app dentro do período selecionado. Essa ferramenta oferece insights sobre como as Campaigns podem estar incentivando comportamentos negativos não intencionais dos usuários e ajuda a medir a eficácia geral da Campaign.

As estatísticas de desinstalação para Campaigns estão localizadas na página **Campaign Analytics** de uma Campaign específica. Para Campaigns multicanal e multivariantes, as desinstalações podem ser detalhadas por canal e variante, respectivamente.

![Desinstalação no nível da Campaign.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Como funciona

A Braze rastreia desinstalações observando quando mensagens push enviadas aos dispositivos dos usuários retornam um sinal do Firebase Cloud Messaging (FCM) ou do serviço de Notificações por Push da Apple (APN) indicando que o app não está mais instalado. Se você ativar o Rastreamento Global de Desinstalação para um app, a Braze envia uma mensagem push silenciosa diária aos usuários para detectar se eles desinstalaram o app. A Braze envia esse push "silencioso" para todos os usuários (a menos que o usuário tenha desativado pushes silenciosos nas configurações do app); o push não aparece para os usuários. Se a Braze detectar que um usuário desinstalou o app, nós:

* Incrementamos a contagem total de desinstalações do app em um.
* Incrementamos a contagem de desinstalações de cada Campaign que o usuário recebeu com sucesso nas últimas 24 horas em um.
* Se um usuário receber três Campaigns em um período de 24 horas e depois desinstalar o app, incrementamos a contagem de "desinstalações" de todas as três Campaigns.

O FCM e o APN impõem restrições ao rastreamento de desinstalação. A Braze incrementa a contagem de desinstalações apenas quando o FCM ou o APN nos informa que um usuário desinstalou o app, mas esses sistemas de terceiros podem nos notificar sobre desinstalações a qualquer momento. Use o rastreamento de desinstalação para detectar tendências direcionais em vez de estatísticas precisas.

A Braze trata uma resposta do FCM como uma resposta de remoção de token (desinstalação) quando o FCM informa que o token de registro não é mais válido, como `DEVICE_UNREGISTERED` ou `NotRegistered`. A Braze registra outros erros de push como bounces sem remover o token.

Para saber mais sobre o uso do rastreamento de desinstalação, consulte nosso post no blog [Rastreamento de desinstalação: uma visão do setor sobre seus pontos fortes e limitações](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Solução de problemas {#troubleshooting}

### Quando o perfil de um usuário é marcado como desinstalado? Quando a tag de desinstalação é removida? {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

A Braze marca um usuário como tendo desinstalado quando detecta que o app não está mais no dispositivo (consulte [Como funciona](#how-it-works) para detecção com push regular e rastreamento de desinstalação opcional). Após alguém reinstalar seu app, a tag de desinstalação pode permanecer no perfil até que o usuário **abra o app e inicie uma nova sessão** — apenas reinstalar não remove a tag. Até essa sessão, Segments e filtros que usam o estado de desinstalação (por exemplo, **Has Not Uninstalled**) ainda tratam o usuário como desinstalado.

### Por que estou vendo um pico repentino de desinstalações? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Se você observar um pico de desinstalações do app, pode ser porque o Firebase Cloud Messaging (FCM) e o serviço de Notificações por Push da Apple (APN) estão revogando tokens antigos em uma frequência diferente.

{% alert note %}
Por razões de privacidade, os provedores de push da Braze podem revogar tokens em intervalos irregulares, o que significa que as contagens de desinstalação podem apresentar picos em determinados períodos.<br><br>Para validar essas mudanças, monitore o rastreamento de desinstalação em conjunto com uma métrica de ação do usuário, como a taxa de abertura direta de push. Se as desinstalações aumentarem drasticamente, mas as aberturas diretas de push permanecerem estáveis, o pico provavelmente reflete a revogação de tokens antigos por um parceiro, e não o comportamento real dos usuários.
{% endalert %}

### Como determino se uma Campaign específica causou desinstalações? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Verifique a análise de dados das Campaigns que enviaram mensagens no mesmo período em que o pico de desinstalação ocorreu. Se uma mensagem específica estiver correlacionada com um aumento nas desinstalações, ela pode estar influenciando os usuários a desinstalar.

Para visualizar desinstalações por Segment:
1. Acesse a página **Home** do dashboard.
2. Na seção **Performance Over Time**, selecione **Uninstalls** em **Statistics For** e **By Segment** em **Breakdown**.

Se você tiver um Segment rastreando usuários inativos com o [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) ativado, compare a tendência de desinstalação dele com a tendência geral do app.

### Como confirmo se as desinstalações são genuínas? {#how-do-i-confirm-uninstalls-are-genuine}

Para APNs, verifique os perfis de usuário em busca do erro de push `BadDeviceToken`. Se você observar esse erro em massa no mesmo período do pico de desinstalação, as desinstalações provavelmente são genuínas. `BadDeviceToken` indica que o token por push do dispositivo não é mais válido, o que normalmente acontece quando o app é desinstalado.

### Por que o número de desinstalações do app é diferente do que consta nos APNs? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

A diferença é esperada.

A Apple usa um cronograma aleatório para atrasar a notificação de quando um token por push se torna inválido. Isso significa que, mesmo após um usuário desinstalar um app, os APNs podem continuar retornando respostas de sucesso para notificações por push por um período. Esse atraso é intencional e projetado para proteger a privacidade do usuário. Nenhum bounce ou falha será reportado até que os APNs retornem um status `410` para um token inválido.

### Como o rastreamento de desinstalação se relaciona com push silencioso ou em segundo plano? {#how-does-uninstall-tracking-relate-to-silent-or-background-push}

A detecção de desinstalação pode usar pushes em segundo plano de baixa prioridade que não aparecem como uma notificação visível. Eles são separados dos [**Envios**]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) de Campaign na análise de dados padrão de envio de mensagens. Ao analisar tendências de desinstalação, avalie os gráficos de desinstalação em conjunto com as métricas de engajamento de push, em vez de comparar pushes de desinstalação diretamente com os totais de envio de marketing.