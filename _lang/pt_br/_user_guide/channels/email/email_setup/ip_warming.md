---
nav_title: Aquecimento de IP
article_title: Aquecimento de IP
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o tema do aquecimento de IP e as melhores práticas."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming'
---

# Aquecimento de IP {#ip-warming}

> O aquecimento de IP é a prática de acostumar os provedores de caixa de e-mail a receber envio de mensagens dos seus endereços de IP dedicados. É uma parte extremamente importante do envio de e-mails com qualquer prestador de serviço de e-mail (ESP) e prática padrão na Braze para confirmar que suas mensagens alcancem as caixas de entrada de destino a uma taxa consistentemente alta.

O aquecimento de IP é projetado para ajudar você a estabelecer uma reputação positiva com os provedores de acesso à internet (ISPs). Toda vez que um novo endereço de IP é usado para enviar um e-mail, os ISPs monitoram programaticamente esses e-mails para verificar se não estão sendo usados para enviar spam aos usuários. Pense na reputação do seu IP e domínio como uma pontuação de crédito — os ISPs usam essa reputação para determinar se o seu e-mail vai para a caixa de entrada ou para a pasta de spam. Assim como uma pontuação de crédito, leva tempo para construir uma reputação positiva e ainda mais tempo para reconstruir uma reputação ruim.

## Entrega e entregabilidade de e-mail {#email-delivery-and-deliverability}

**Entrega** é a proporção de e-mails que foram aceitos e não sofreram hard bounce. **Entregabilidade** é se o e-mail chega à caixa de entrada em vez da pasta de spam — os provedores de caixa de e-mail não expõem isso como uma métrica única.

Uma taxa de entrega saudável geralmente fica em torno de 99% com uma taxa de bounce não superior a cerca de 1%. As taxas podem parecer boas no papel e ainda assim esconder problemas (por exemplo, muitos bounces de um único domínio, ou e-mails entregues mas filtrados para spam). Monitore aberturas e cliques, não apenas a entrega. Mesmo uma pequena taxa de relatório de spam pode justificar uma análise mais aprofundada.

### Recomendações antes do aquecimento de IP {#recommendations-before-ip-warming}

Antes de iniciar o aquecimento de IP:

1. Em **Configurações** > **Preferências de e-mail**, defina seu domínio de envio padrão, adicione um link de cancelamento de inscrição válido no seu [rodapé personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), ative o [cabeçalho list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) e considere páginas personalizadas de cancelamento de inscrição/opt-in quando necessário.
2. Configure o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) para e-mail.
3. Crie seus modelos necessários acessando **Conteúdo** > **E-mail**.

## E se eu não tiver tempo para aquecer os IPs? {#what-if-i-dont-have-time-to-warm-ips}

**O aquecimento de IP é obrigatório.** Se você não aquecer os IPs adequadamente e o padrão dos seus e-mails causar qualquer suspeita, a velocidade de entrega dos seus e-mails pode ser significativamente limitada ou reduzida. Seu domínio ou IP também pode ser bloqueado pelos ISPs, o que pode fazer com que seus e-mails vão diretamente para a pasta de spam da caixa de entrada do usuário. Por isso, é importante aquecer seus IPs corretamente.

Os ISPs limitam a entrega de e-mails quando surge suspeita de spam para proteger seus usuários. Por exemplo, se você enviar para 100.000 usuários, o ISP pode entregar o e-mail apenas para 5.000 desses usuários na primeira hora. Então, o ISP monitora métricas de engajamento como taxas de abertura, taxas de cliques, cancelamentos de inscrição e relatórios de spam. Se um número significativo de relatórios de spam ocorrer, eles podem optar por direcionar o restante desse envio para a pasta de spam em vez de entregá-lo na caixa de entrada do usuário.

Se o engajamento for moderado, eles podem continuar limitando seu e-mail para coletar mais dados de engajamento e determinar com mais certeza se o e-mail é spam ou não. Se o e-mail tiver métricas de engajamento muito altas, eles podem parar de limitar esse e-mail completamente. Eles usam esses dados para criar uma reputação de e-mail que, em última análise, determinará se seus e-mails serão filtrados automaticamente para spam.

Se seu domínio ou IP for bloqueado por um ISP, os registros de mensagens no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) conterão informações sobre quais sites visitar para recorrer junto a esses ISPs e sair dessas listas.

## Cronogramas de aquecimento de IP {#ip-warming-schedules}

Recomendamos fortemente seguir rigorosamente um cronograma de aquecimento de IP para garantir a entregabilidade. Também é importante não pular dias, pois o escalonamento consistente melhora as métricas de entrega. Escolha um cronograma com base no seu histórico de envio de e-mails e nas métricas de entregabilidade existentes.

{% alert tip %}
Se você tiver interesse em ter um recurso dedicado de entregabilidade como parte da sua equipe de conta, entre em contato com o gerente de conta da Braze para mais informações.
{% endalert %}

{% tabs local %}
{% tab Conservador %}

O cronograma conservador é uma abordagem mais lenta e cautelosa que ajuda a estabelecer uma reputação de envio sólida do zero. Isso é recomendado se você é novo no envio de e-mails, está migrando de um IP compartilhado ou enfrentou problemas de entregabilidade, como limitação ou bloqueio por um provedor de caixa de e-mail.

Dia | Número de e-mails a enviar
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1.000
11 | 1.000
12 | 1.000
13 | 2.000
14 | 2.000
15 | 2.000
16 | 4.000
17 | 4.000
18 | 4.000
19 | 8.000
20 | 8.000
21 | 8.000
22+ | Dobre a cada 3 dias até atingir o volume desejado

{% endtab %}
{% tab Moderado %}

O cronograma moderado é uma abordagem equilibrada que aumenta o volume de envio em um ritmo constante. Isso é recomendado para a maioria dos remetentes, incluindo aqueles com algum histórico de envio de e-mails que estão fazendo a transição para um novo IP.

Dia | Número de e-mails a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.000
6 | 4.000
7 | 8.000
8 | 16.000
9 | 25.000
10 | 35.000
11 | 50.000
12 | 75.000
13 | 100.000
14 | 150.000
15 | 200.000
16 | 275.000
17 | 375.000
18 | 500.000
19 | 650.000
20 | 825.000
21 | 1.000.000
22+ | Dobre a cada 2 dias até atingir o volume desejado

{% endtab %}
{% tab Agressivo %}

{% alert important %}
O cronograma agressivo é a abordagem mais rápida e é recomendado apenas para remetentes com um histórico de envio estabelecido e positivo e métricas de entregabilidade alinhadas com as melhores práticas, incluindo altas taxas de abertura, altas taxas de cliques e baixas taxas de bounce. Usar esse cronograma sem um histórico comprovado pode prejudicar a reputação do remetente.
{% endalert %}

Dia | Número de e-mails a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.500
6 | 5.000
7 | 9.000
8 | 16.000
9 | 29.000
10 | 52.000
11 | 98.000
12 | 160.000
13 | 225.000
14 | 315.000
15 | 450.000
16 | 615.000
17 | 875.000
18 | 1.200.000
19 | 1.750.000
20 | 2.750.000
21+ | Dobre diariamente até atingir o volume desejado

{% endtab %}
{% endtabs %}

Na maioria dos casos, aqueça até o seu volume médio de envio diário em vez do volume de pico. Os ISPs analisam principalmente as últimas semanas de comportamento de envio para avaliar sua reputação. Portanto, se você atinge o volume de pico apenas a cada poucos meses (por exemplo, 7 milhões durante um período sazonal), pode aumentar gradualmente em direção a esse pico mais perto da data de envio. No entanto, se você atinge o volume de pico a cada uma ou duas semanas, aqueça até esse pico desde o início.

Após a conclusão do aquecimento de IP e ao atingir o volume diário desejado, você deve manter esse volume diariamente. Alguma flutuação é esperada, mas atingir o volume desejado e depois fazer apenas um envio em massa uma vez por semana pode afetar negativamente suas métricas de entrega e a reputação do remetente.

{% alert important %}
A maioria dos ISPs armazena dados de reputação por apenas 30 dias. Se você ficar um mês sem enviar nenhuma mensagem, precisará repetir o processo de aquecimento de IP.
{% endalert %}

### Endereços de IP {#ip-addresses}

Após três meses sem uso, a Braze pode reciclar e reatribuir endereços de IP. Independentemente do histórico anterior de um endereço de IP, o aquecimento completo de IP é recomendado para todos os IPs recém-atribuídos, pois a maioria dos ISPs armazena dados de reputação por apenas 30 dias. Para a maioria dos ISPs, isso significa que um período de inatividade de três meses efetivamente redefine a reputação. Se você tiver mais dúvidas sobre o histórico de um endereço de IP específico, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Como limitar envios durante o aquecimento {#how-to-limit-sends-during-warming}

Nosso recurso integrado de limitação de usuários é uma ferramenta útil para ajudar você no aquecimento do seu endereço de IP. Após escolher os segmentos de envio de mensagens desejados durante a criação da Campaign, na etapa [Usuários-alvo]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas), selecione o menu suspenso **Opções avançadas** para limitar seus usuários. À medida que seu cronograma de aquecimento avança, você pode aumentar gradualmente esse limite para aumentar o volume de e-mails enviados.

![O recurso integrado de limitação de usuários serve como uma ferramenta útil para ajudar no aquecimento do seu endereço de IP. Após escolher os segmentos de envio de mensagens desejados durante a criação da Campaign, na etapa Usuários-alvo, selecione o menu suspenso Opções avançadas para limitar seus usuários. À medida que seu cronograma de aquecimento avança, você pode aumentar gradualmente esse limite para aumentar o volume de e-mails enviados.]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentação de subdomínio {#subdomain-segmentation}

Muitos ISPs e provedores de acesso a e-mail não filtram mais apenas pela reputação do endereço de IP. Essas tecnologias de filtragem agora também consideram a reputação baseada no domínio. Isso significa que os filtros analisam todos os dados associados ao domínio do remetente e não apenas o endereço de IP isoladamente. Por esse motivo, além de aquecer seu IP de e-mail, também recomendamos ter domínios ou subdomínios separados para e-mails de marketing, transacionais e corporativos.

{% alert important %}
A segmentação de subdomínio é especialmente importante para remetentes de alto volume. Esses remetentes devem trabalhar com um representante da Braze ao configurar sua conta para garantir que sigam essa prática.
{% endalert %}

Recomendamos segmentar seus domínios para que o e-mail corporativo seja enviado pelo seu domínio de nível superior, e os e-mails de marketing e transacionais sejam enviados por domínios ou subdomínios diferentes.

## Melhores práticas {#best-practices}

Você pode evitar todas as consequências de não aquecer o IP seguindo estas melhores práticas:

### Comece com volumes pequenos de envio de e-mail {#start-with-small-sending-volumes-of-email}

Aumente a quantidade enviada a cada dia da forma mais gradual possível. Campaigns de e-mail abruptas e de alto volume são vistas com mais desconfiança pelos ISPs. Portanto, você deve começar enviando pequenas quantidades de e-mail e escalar gradualmente em direção ao volume que pretende enviar. Lembre-se de que você está aquecendo seu IP em cada ISP individualmente — os ISPs não compartilham dados de reputação entre si. Ao planejar seus volumes de aquecimento, certifique-se de não aumentar o volume muito rapidamente em nenhum ISP específico. Independentemente do volume, sugerimos aquecer seu IP por segurança. Consulte os [cronogramas de aquecimento de IP](#ip-warming-schedules).

### Tenha conteúdo introdutório envolvente {#have-engaging-introductory-content}

Garanta que seu primeiro conteúdo seja altamente envolvente e maximize a probabilidade de os usuários clicarem, abrirem e interagirem com seu e-mail. Sempre prefira e-mails bem segmentados a envios indiscriminados ao aquecer IPs.

### Defina uma cadência de envio consistente {#set-a-consistent-sending-cadence}

Após a conclusão do aquecimento de IP, crie uma cadência de envio, certificando-se também de distribuir seus e-mails ao longo de um dia ou vários dias. Ao criar um cronograma o mais consistente possível, você pode evitar um resfriamento de IP, que pode ocorrer se o volume de envio parar ou diminuir significativamente por mais de alguns dias.

Consulte nosso [cronograma de aquecimento de IP](#ip-warming-schedules) para distribuir seu envio ao longo de um período mais longo, em vez de enviar um disparo em massa em um único momento específico.

### Limpe suas listas de e-mail {#clean-your-email-lists}

Garanta que sua lista de e-mail esteja limpa e não contenha e-mails antigos ou não verificados. Assegurar que você esteja em conformidade com [CASL e CAN-SPAM]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations) é o ideal.

### Monitore a reputação do remetente {#monitor-your-sender-reputation}

Ao conduzir o processo de aquecimento de IP, certifique-se de monitorar cuidadosamente a reputação do remetente. Estas métricas específicas são importantes de acompanhar:
- **Taxas de bounce:** Se qualquer Campaign tiver uma taxa de bounce superior a 3-5%, você deve avaliar a limpeza da sua lista seguindo as diretrizes do nosso artigo [Mantenha limpo: a importância da higiene da lista de e-mail](https://www.braze.com/blog/email-list-hygiene/). Além disso, considere implementar uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) para parar de enviar e-mails para endereços inativos ou sem engajamento.
- **Relatórios de spam:** Se qualquer Campaign for reportada como spam a uma taxa superior a 0,08%, você deve reavaliar o conteúdo que está enviando, verificar se está direcionado a um público interessado e garantir que seus e-mails estejam redigidos de forma adequada para despertar o interesse.
- **Taxas de abertura:** As taxas de abertura são um indicador útil de posicionamento na caixa de entrada. Se suas taxas de abertura únicas estiverem acima de 25%, é provável que você esteja tendo um alto posicionamento na caixa de entrada, o que indica uma reputação positiva do remetente.

{% alert tip %}
A Braze não recomenda usar o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) para aquecer seus IPs. Como as Campaigns de aquecimento de IP são algumas das primeiras Campaigns que você envia, a Braze não terá informações suficientes sobre seus usuários para calcular um horário de envio ideal. Nesse caso, todas as mensagens com Intelligent Timing usariam o horário de fallback e seriam enviadas no mesmo horário.
{% endalert %}

{% alert tip %}
É normal que e-mails sejam enviados para a pasta de spam durante o aquecimento de IP, pois seu domínio e IP ainda não estabeleceram uma reputação positiva. Se os e-mails caírem na sua pasta de spam, o administrador de e-mail pode precisar adicionar o domínio de envio e o IP da Braze à lista de permissões da sua empresa.
{% endalert %}