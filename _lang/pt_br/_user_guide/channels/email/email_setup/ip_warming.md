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

> O aquecimento de IP é a prática de acostumar os provedores de caixa de entrada a receber mensagens dos seus endereços de IP dedicados. É uma parte extremamente importante do envio de e-mails com qualquer provedor de serviços de e-mail (ESP) e prática padrão na Braze para confirmar que suas mensagens alcancem as caixas de entrada de destino a uma taxa consistentemente alta. Se você usa o [aquecimento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming), consulte as [Perguntas frequentes sobre aquecimento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/faq).

O aquecimento de IP é projetado para ajudar você a estabelecer uma reputação positiva com os provedores de serviços de internet (ISPs). Toda vez que um novo endereço de IP é usado para enviar um e-mail, os ISPs monitoram programaticamente esses e-mails para verificar se não estão sendo usados para enviar spam aos usuários. Pense na reputação do seu IP e domínio como uma pontuação de crédito — os ISPs usam essa reputação para determinar se o seu e-mail vai para a caixa de entrada ou para a pasta de spam. Assim como uma pontuação de crédito, leva tempo para construir uma reputação positiva e ainda mais tempo para reconstruir uma reputação ruim.

## Entrega e entregabilidade de e-mail {#email-delivery-and-deliverability}

**Entrega** é a proporção de e-mails que foram aceitos e não sofreram hard bounce. **Entregabilidade** é se o e-mail chega à caixa de entrada em vez de ir para spam — os provedores de caixa de entrada não expõem isso como uma métrica única.

Uma taxa de entrega saudável geralmente fica em torno de 99% de entrega com uma taxa de bounce não superior a cerca de 1%. As taxas podem parecer boas no papel e ainda assim esconder problemas (por exemplo, muitos bounces de um único domínio, ou e-mails entregues mas filtrados para spam). Acompanhe aberturas e cliques, não apenas a entrega. Mesmo uma taxa de relatório de spam pequena pode justificar uma análise mais aprofundada.

### Recomendações antes do aquecimento de IP {#recommendations-before-ip-warming}

Antes de iniciar o aquecimento de IP:

1. Em **Configurações** > **Preferências de e-mail**, defina seu domínio de envio padrão, adicione um link de cancelamento de inscrição válido no seu [rodapé personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), ative o [cabeçalho list-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#list-unsubscribe) e considere páginas personalizadas de cancelamento de inscrição/aceitação quando necessário.
2. Configure o [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) para e-mail.
3. Crie seus modelos necessários acessando **Conteúdo** > **E-mail**.

## E se eu não tiver tempo para aquecer os IPs? {#what-if-i-dont-have-time-to-warm-ips}

**O aquecimento de IP é obrigatório.** Se você não aquecer os IPs adequadamente e o padrão dos seus e-mails causar qualquer suspeita, a velocidade de entrega dos seus e-mails poderá ser significativamente limitada ou reduzida. Seu domínio ou IP também pode ser bloqueado pelos ISPs, o que pode fazer com que seus e-mails vão diretamente para a pasta de spam da caixa de entrada dos seus usuários. Por isso, é importante aquecer seus IPs corretamente.

Os ISPs limitam a entrega de e-mails quando surge suspeita de spam para proteger seus usuários. Por exemplo, se você enviar para 100.000 usuários, o ISP or provedor de acesso à internet or provedor de serviços de internet pode entregar o e-mail para apenas 5.000 desses usuários na primeira hora. Em seguida, o ISP or provedor de acesso à internet or provedor de serviços de internet monitora métricas de engajamento, como taxas de abertura, taxas de cliques, cancelamentos de inscrição e relatórios de spam. Então, se um número significativo de relatórios de spam ocorrer, ele pode optar por direcionar o restante desse envio para a pasta de spam em vez de entregá-lo na caixa de entrada do usuário.

Se o engajamento for moderado, o ISP or provedor de acesso à internet or provedor de serviços de internet pode continuar limitando seus e-mails para coletar mais dados de engajamento e determinar com mais certeza se o e-mail é spam ou não. Se o e-mail tiver métricas de engajamento muito altas, o ISP or provedor de acesso à internet or provedor de serviços de internet pode parar de limitar esse e-mail completamente. Esses dados são usados para criar uma reputação de e-mail que determina se seus e-mails são filtrados automaticamente como spam.

Se seu domínio ou IP for bloqueado por um ISP or provedor de acesso à internet or provedor de serviços de internet, os registros de mensagens no [Registro de atividade de mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) conterão informações sobre quais sites visitar para recorrer junto a esses ISPs e sair dessas listas.

## Cronogramas de aquecimento de IP {#ip-warming-schedules}

Recomendamos fortemente que você siga rigorosamente um cronograma de aquecimento de IP para garantir a entregabilidade. Também é importante não pular dias, pois o escalonamento consistente melhora as métricas de entrega. Escolha um cronograma com base no seu histórico de envio de e-mails e nas métricas de entregabilidade existentes.

{% alert tip %}
Se você tem interesse em ter um recurso dedicado de entregabilidade como parte da sua equipe de conta, entre em contato com o gerente de conta da Braze para saber mais.
{% endalert %}

{% tabs local %}
{% tab Conservador %}

O cronograma conservador é uma abordagem mais lenta e cautelosa que ajuda a estabelecer uma reputação de envio sólida do zero. Ele é recomendado se você é novo no envio de e-mails, está migrando de um IP compartilhado ou enfrentou problemas de entregabilidade, como limitação de taxa ou bloqueio por um provedor de caixa de entrada.

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

O cronograma moderado é uma abordagem equilibrada que aumenta o volume de envio em um ritmo constante. Ele é recomendado para a maioria dos remetentes, incluindo aqueles com algum histórico de envio de e-mails que estão fazendo a transição para um novo IP.

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
O cronograma agressivo é a abordagem mais rápida e só é recomendado para remetentes com um histórico de envio positivo e estabelecido, além de métricas de entregabilidade alinhadas às melhores práticas, incluindo altas taxas de abertura, altas taxas de cliques e baixas taxas de bounce. Usar esse cronograma sem um histórico comprovado pode prejudicar a reputação do remetente.
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

Na maioria dos casos, faça o aquecimento até o seu volume médio de envio diário, e não até o volume de pico. Os ISPs analisam principalmente as últimas semanas de comportamento de envio para avaliar sua reputação. Então, se você atinge o volume de pico apenas a cada poucos meses (por exemplo, 7 milhões durante um período sazonal), você pode aumentar gradualmente em direção a esse pico mais perto da data de envio. No entanto, se você atinge o volume de pico a cada uma ou duas semanas, faça o aquecimento até esse pico desde o início.

Após a conclusão do aquecimento de IP e depois de atingir o volume diário desejado, você deve manter esse volume diariamente. Alguma flutuação é esperada, mas atingir o volume desejado e depois fazer apenas um envio em massa uma vez por semana pode afetar negativamente suas métricas de entrega e a reputação do remetente.

{% alert important %}
A maioria dos ISPs armazena dados de reputação por apenas 30 dias. Se você ficar um mês sem enviar nenhuma mensagem, será necessário repetir o processo de aquecimento de IP.
{% endalert %}

### Endereços IP {#ip-addresses}

Após três meses sem uso, a Braze pode reciclar e reatribuir endereços IP. Independentemente do histórico anterior de um endereço IP, o aquecimento completo de IP é recomendado para todos os IPs recém-atribuídos, já que a maioria dos ISPs armazena dados de reputação por apenas 30 dias. Para a maioria dos ISPs, isso significa que um período de inatividade de três meses efetivamente redefine a reputação. Se você tiver mais dúvidas sobre o histórico de um endereço IP específico, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Como limitar envios durante o aquecimento {#how-to-limit-sends-during-warming}

Nosso recurso integrado de limitação de usuários é uma ferramenta útil para ajudar no aquecimento do seu endereço de IP. Após escolher os Segments de envio de mensagens desejados durante a criação da Campaign, na etapa [Usuários-alvo]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas), selecione o menu suspenso **Advanced Options** para limitar seus usuários. À medida que seu cronograma de aquecimento avança, você pode aumentar gradualmente esse limite para elevar o volume de e-mails enviados.

![O recurso integrado de limitação de usuários serve como uma ferramenta útil para ajudar no aquecimento do seu endereço de IP. Após escolher os segmentos de envio de mensagens desejados durante a criação da campanha, na etapa Usuários-alvo, selecione o menu suspenso Advanced Options para limitar seus usuários. À medida que seu cronograma de aquecimento avança, você pode aumentar gradualmente esse limite para elevar o volume de e-mails enviados.]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentação de subdomínio {#subdomain-segmentation}

Muitos ISPs e provedores de acesso a e-mail não filtram mais apenas pela reputação do endereço IP. Essas tecnologias de filtragem agora também consideram a reputação baseada no domínio. Isso significa que os filtros analisam todos os dados associados ao domínio do remetente, e não apenas o endereço IP isoladamente. Por esse motivo, além de aquecer seu IP de e-mail, também recomendamos ter domínios ou subdomínios separados para e-mails de marketing, transacionais e corporativos.

{% alert important %}
A segmentação de subdomínio é especialmente importante para remetentes de alto volume. Esses remetentes devem trabalhar com um representante da Braze ao configurar sua conta para confirmar que seguem essa prática.
{% endalert %}

Recomendamos segmentar seus domínios para que o e-mail corporativo seja enviado pelo seu domínio de nível superior, e os e-mails de marketing e transacionais sejam enviados por domínios ou subdomínios diferentes.

## Práticas recomendadas {#best-practices}

Você pode evitar todas as consequências de não fazer o aquecimento de IP seguindo estas práticas recomendadas:

### Comece com volumes pequenos de envio de e-mail {#start-with-small-sending-volumes-of-email}

Aumente a quantidade que você envia a cada dia da forma mais gradual possível. Campaigns de e-mail abruptas e de alto volume são vistas com mais desconfiança pelos ISPs. Portanto, comece enviando pequenas quantidades de e-mail e aumente gradualmente até o volume que você pretende enviar. Lembre-se de que você está aquecendo seu IP em cada ISP or provedor de acesso à internet or provedor de serviços de internet individualmente — os ISPs não compartilham dados de reputação entre si. Ao planejar seus volumes de aquecimento, certifique-se de que não está aumentando o volume rápido demais em nenhum ISP or provedor de acesso à internet or provedor de serviços de internet específico. Independentemente do volume, sugerimos aquecer seu IP por segurança. Consulte os [cronogramas de aquecimento de IP](#ip-warming-schedules).

### Tenha conteúdo introdutório envolvente {#have-engaging-introductory-content}

Confirme que seu primeiro conteúdo é altamente envolvente e maximiza a probabilidade de que os usuários cliquem, abram e interajam com seu e-mail. Sempre prefira e-mails bem segmentados a envios indiscriminados ao aquecer IPs.

### Defina uma cadência de envio consistente {#set-a-consistent-sending-cadence}

Quando o aquecimento de IP estiver concluído, crie uma cadência de envio, certificando-se de também distribuir seus e-mails ao longo de um dia ou de vários dias. Ao criar um cronograma o mais consistente possível, você pode evitar um resfriamento de IP, que pode ocorrer se o volume de envio parar ou diminuir significativamente por mais de alguns dias.

Consulte nosso [cronograma de aquecimento de IP](#ip-warming-schedules) para distribuir seu envio ao longo de um período mais longo, em vez de enviar uma grande quantidade de uma só vez em um horário específico.

### Limpe suas listas de e-mail {#clean-your-email-lists}

Confirme que sua lista de e-mails está limpa e não contém e-mails antigos ou não verificados. Garantir que você esteja em conformidade com as regulamentações [CASL e CAN-SPAM]({{site.baseurl}}/user_guide/administer/global/privacy/spam_regulations) é o ideal.

### Monitore a reputação do remetente {#monitor-your-sender-reputation}

Ao conduzir o processo de aquecimento de IP, monitore cuidadosamente a reputação do remetente. Estas métricas específicas são importantes de acompanhar:
- **Taxas de bounce:** Se alguma Campaign tiver uma taxa de bounce acima de 3-5%, você deve avaliar a limpeza da sua lista seguindo as diretrizes do nosso artigo [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). Além disso, considere implementar uma [política de sunset]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies) para parar de enviar e-mails para endereços inativos ou sem engajamento.
- **Relatórios de spam:** Se alguma Campaign for reportada como spam a uma taxa superior a 0,08%, reavalie o conteúdo que está enviando, verifique se ele é direcionado a um público interessado e certifique-se de que seus e-mails estão redigidos de forma adequada para despertar o interesse.
- **Taxas de abertura:** As taxas de abertura são um indicador útil de posicionamento na caixa de entrada. Se suas taxas de abertura únicas estiverem acima de 25%, é provável que você esteja tendo um alto posicionamento na caixa de entrada, o que indica uma reputação positiva do remetente.

{% alert tip %}
A Braze não recomenda usar o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) para aquecer seus IPs. Como as Campaigns de aquecimento de IP são algumas das primeiras que você envia, a Braze não terá informações suficientes sobre seus usuários para calcular um horário de envio ideal. Nesse caso, todas as mensagens com Intelligent Timing usariam o horário de fallback e seriam enviadas no mesmo horário de qualquer forma.
{% endalert %}

{% alert tip %}
É normal que e-mails sejam enviados para a pasta de spam durante o aquecimento de IP, pois seu domínio e IP ainda não estabeleceram uma reputação positiva. Se os e-mails caírem na sua pasta de spam, o administrador de e-mail da sua empresa pode precisar adicionar o domínio de envio e o IP da Braze à lista de permissões da sua empresa.
{% endalert %}