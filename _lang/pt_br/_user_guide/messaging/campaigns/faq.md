---
nav_title: FAQ
article_title: FAQ sobre Campaigns
page_order: 10
page_type: FAQ
description: "Esta página fornece respostas para perguntas frequentes sobre Campaigns."
tool: Campaigns

---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre Campaigns.

## Como crio uma Campaign multicanal? {#how-do-i-create-a-multichannel-campaign}

Consulte [Campaigns multicanais]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-campaigns) em **Criar uma Campaign** para etapas de configuração e canais suportados.

### Posso adicionar um grupo de controle à minha Campaign multicanal? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Consulte [Grupos de controle]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) em **Criar uma Campaign**. Para testes entre canais, use o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### Quais são algumas formas de começar a testar e otimizar Campaigns? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Campaigns multivariantes e Canvas com múltiplas variantes são uma ótima forma de começar! Por exemplo, você pode executar uma [Campaign multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing) para testar uma mensagem com diferentes textos ou linhas de assunto. Canvas com múltiplas variantes podem ajudar a testar fluxos de trabalho inteiros.

### Por que a taxa de abertura da minha Campaign diminuiu? {#why-did-the-open-rate-for-my-campaign-decrease}

Taxas de abertura baixas nem sempre estão relacionadas a um problema técnico. Pode haver problemas com o corte de e-mail, que resulta em um pixel de rastreamento ausente. No entanto, também é possível que menos usuários estejam abrindo seus e-mails devido ao conteúdo ou a mudanças no tamanho do público.

### Como os públicos das Campaigns são avaliados? {#how-are-campaign-audiences-evaluated}

Por padrão, as Campaigns verificam os filtros de público no momento da entrada. Para Campaigns baseadas em ação com postergação, existe a opção de reavaliar os critérios do segmento no momento do envio para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

### Por que há uma diferença entre o número de destinatários únicos e o número de envios para uma determinada Campaign ou Canvas? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Uma possível explicação é que a Campaign ou o Canvas tem a reelegibilidade ativada, o que significa que os usuários que se qualificam para o segmento e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a reelegibilidade não estiver ativada, a explicação provável para a diferença entre envios e destinatários únicos pode ser que os usuários possuem múltiplos dispositivos, em diferentes plataformas, associados aos seus perfis.

Por exemplo, se você tiver um Canvas que possui notificações por push tanto para iOS quanto para web, um determinado usuário com dispositivos móvel e desktop pode receber mais de uma mensagem.

### Por que *Destinatários únicos* é maior do que o número de usuários que eu direcionei? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*Destinatários únicos* pode ser maior do que o público esperado porque a Braze rastreia destinatários únicos diários para fins de relatório. Isso permite que a Braze atribua conversões dentro da janela de conversão cada vez que um usuário recebe a mensagem, em vez de consolidar múltiplos recebimentos em uma única contagem vitalícia (o que distorceria os cálculos de conversão).

Por exemplo, se um usuário recebe uma Campaign na segunda-feira e novamente na sexta-feira e converte após cada envio, a Braze pode reportar isso como dois recebimentos e duas conversões. Se a Braze contasse apenas um "único" vitalício em ambos os envios, você perderia uma conversão válida ou contaria em dobro contra um destinatário, o que torna o desempenho da Campaign mais difícil de interpretar.

O mesmo padrão se aplica a Campaigns recorrentes e à reelegibilidade: se dois usuários recebem um envio recorrente hoje e novamente amanhã, *Destinatários únicos* conta quatro linhas de destinatários diários, não dois perfis.

### Por que o número de conversões pode exceder o número de usuários únicos em Campaigns multicanais? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Consulte [Conversões e relatórios]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) em **Criar uma Campaign** e [Regras de rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) em **Eventos de conversão**.

### Por que minha Campaign tem uma base de usuários contatáveis menor do que o segmento que estou usando para a Campaign? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Se você tiver um [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group) configurado, isso impedirá que uma porcentagem do seu público contatável receba Campaigns. Isso significa que o número de usuários contatáveis do seu segmento pode, às vezes, ser maior do que o número de usuários contatáveis da sua Campaign, mesmo que a Campaign esteja usando o mesmo segmento.

### O que a entrega por fuso horário local oferece? {#what-does-local-time-zone-delivery-offer}

A entrega por fuso horário local permite entregar Campaigns de mensagens a um segmento com base no fuso horário individual de cada usuário. Sem a entrega por fuso horário local, as Campaigns serão programadas com base nas configurações de fuso horário da sua empresa na Braze.

Por exemplo, uma empresa sediada em Londres que envia uma Campaign às 12h alcançará usuários na costa oeste dos Estados Unidos às 4h da manhã. Se o seu app está disponível apenas em determinados países, isso pode não ser um risco para você. Caso contrário, recomendamos fortemente evitar o envio de notificações por push de madrugada para a sua base de usuários.

### Como a Braze reconhece o fuso horário de um usuário? {#how-does-braze-recognize-a-users-time-zone}

A Braze determinará automaticamente o fuso horário de um usuário a partir do seu dispositivo. Isso garante precisão de fuso horário e cobertura completa dos seus usuários. Usuários criados pela API de Usuários ou sem um fuso horário definido terão o fuso horário da sua empresa como fuso horário padrão até serem reconhecidos no seu app pelo SDK.

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings) no dashboard.

### Quando a Braze avalia os usuários para entrega por fuso horário local? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

A Braze avalia os usuários para elegibilidade de entrada em:

- Horário de Samoa (UTC+13) no dia programado
- O horário local do dia programado

Para que um usuário seja elegível para entrada, ele deve ser elegível em ambas as verificações. Por exemplo, se um Canvas está programado para ser lançado em 7 de agosto de 2021 às 14h no fuso horário local, o direcionamento de um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova York em 6 de agosto de 2021 às 21h
- Nova York em 7 de agosto de 2021 às 14h

Para entrar, o usuário deve corresponder ao seu público e filtros em ambos os momentos de avaliação. Se o usuário não for elegível na primeira verificação, a Braze não executará a segunda verificação. Não há um tempo mínimo que o usuário precise estar no segmento antes do lançamento. Apenas a elegibilidade em cada verificação importa.

Esse comportamento de avaliação é separado de [com quanta antecedência você programa a Campaign no dashboard](#how-do-i-schedule-a-local-time-zone-campaign). Programar com pelo menos 24 horas de antecedência é uma recomendação porque ajuda as mensagens a serem entregues ao longo de toda a janela de 24 horas de fuso horário local, não um requisito de que cada usuário esteja no público por 24 horas.

#### Exemplos {#examples}

Por exemplo, se uma Campaign está programada para ser entregue às 19h UTC, começamos a enfileirar os envios da Campaign assim que um fuso horário é identificado (como Samoa). Isso significa que estamos nos preparando para enviar a mensagem, não enviando a Campaign. Se os usuários não corresponderem a nenhum filtro quando verificamos a elegibilidade, eles não farão parte do público-alvo.

Como outro exemplo, digamos que você queira criar duas Campaigns programadas para enviar no mesmo dia — uma de manhã e uma à noite — e adicionar um filtro para que os usuários só possam receber a segunda Campaign se já tiverem recebido a primeira. Com a entrega por fuso horário local, alguns usuários podem não receber a segunda Campaign. Isso acontece porque verificamos a elegibilidade quando o fuso horário do usuário é identificado. Portanto, se o horário programado ainda não ocorreu no fuso horário dele, ele não recebeu a primeira Campaign, o que significa que não será elegível para a segunda Campaign.

A linha do tempo a seguir assume uma definição de segmento que inclui uma janela de associação limitada por tempo. Neste exemplo, os usuários saem do segmento 24 horas após entrarem. Esse comportamento de filtro é uma razão pela qual um usuário pode passar na primeira verificação e falhar na segunda.

![Linha do tempo de um usuário entrando no segmento antes da primeira verificação e saindo antes da segunda.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Descrição da linha do tempo %}

1. O Usuário A entra no segmento às 6:59 PST (4:59 horário de Samoa).
2. A Braze verifica a associação ao segmento às 7h horário de Samoa para determinar quais usuários são elegíveis para receber a Campaign nas próximas 24 horas. O Usuário A está no segmento neste momento.
3. O segmento tem uma janela de 24 horas, então o Usuário A sai do segmento 24 horas após ter entrado: 6:59 PST (4:59 horário de Samoa).
4. A Campaign por horário local envia às 7h PST, mas o Usuário A já saiu do segmento.

{% enddetails %}

### Como programo uma Campaign por fuso horário local? {#how-do-i-schedule-a-local-time-zone-campaign}

A seção anterior descreve quando a Braze avalia a elegibilidade para entrega por fuso horário local (as duas verificações). Esta seção descreve quando você define a programação da Campaign no dashboard (tempo de antecedência) e quais usuários ainda recebem a mensagem se você programar com menos de 24 horas de antecedência.

Ao programar uma Campaign, escolha enviá-la em um horário designado e selecione **Send campaign to users in their local time zone**.

A Braze recomenda fortemente que todas as Campaigns por fuso horário local sejam programadas com 24 horas de antecedência. Como essa Campaign precisa ser enviada ao longo de um dia inteiro, programá-la com 24 horas de antecedência garante que sua mensagem alcance todo o seu segmento. No entanto, você pode programar essas Campaigns com menos de 24 horas de antecedência, se necessário. Tenha em mente que a Braze não enviará mensagens para usuários que perderam o horário de envio por mais de 1 hora.

Por exemplo, se são 13h e você programa uma Campaign por fuso horário local para as 15h, a Campaign enviará imediatamente para todos os usuários cujo horário local esteja entre 15h e 16h, mas não para usuários cujo horário local seja 17h. Além disso, o horário de envio que você escolher para sua Campaign não pode ter passado no fuso horário da sua empresa.

Editar uma Campaign por fuso horário local que está programada com menos de 24 horas de antecedência não alterará a programação da mensagem. Se você decidir editar uma Campaign por fuso horário local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento-alvo quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar uma Campaign por fuso horário local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a Campaign ainda será enviada para todos os membros do segmento no horário original (17h).

{% alert note %}
Para componentes do Canvas, os usuários não precisam estar no componente por 24 horas para receber o próximo componente na jornada do usuário para entrega por fuso horário local.
{% endalert %}

Se você permitiu que os usuários se tornem reelegíveis para a Campaign, eles a receberão novamente no horário original (17h). Para todas as ocorrências subsequentes da sua Campaign, no entanto, suas mensagens serão enviadas apenas no horário atualizado.

### Quando as alterações em Campaigns por fuso horário local entram em vigor? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Os segmentos-alvo para Campaigns por fuso horário local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo para garantir a entrega a todo o segmento. Por exemplo, considere um segmento que direciona usuários no segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Usou o app pela primeira vez há menos de 2 dias

A entrega por fuso horário local pode não alcançar usuários neste segmento com base no horário de entrega e no fuso horário local dos usuários. Isso acontece porque um usuário pode sair do segmento no momento em que seu fuso horário aciona a entrega.

### Quais alterações posso fazer em Campaigns programadas antes do lançamento? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Quando a Campaign está programada, você deve fazer edições em qualquer coisa que não seja a composição da mensagem antes de enfileirarmos as mensagens para envio. Como em todas as Campaigns, você não pode editar eventos de conversão após o lançamento.

### Atualizei minha Campaign programada. Por que ela não foi lançada? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Isso pode acontecer quando uma Campaign está programada para ser lançada no exato momento em que foi atualizada. Por exemplo, se são 15:10 e você alterou a Campaign para ser lançada às 15:10 e selecionou **Update campaign**, já passou das 15:10, o que significa que o horário programado para o lançamento já passou. Em vez de programar a Campaign para o mesmo horário, selecione **Send as soon as campaign launch**.

### Qual é a "zona segura" antes que as mensagens de uma Campaign programada sejam enfileiradas? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Recomendamos fazer alterações nas mensagens dentro dos seguintes prazos:

- **Campaigns programadas únicas:** Edite até o horário de envio programado.
- **Campaigns programadas recorrentes:** Edite até o horário de envio programado.
- **Campaigns por horário local:** Edite até 24 horas antes do horário de envio programado.
- **Campaigns com horário de envio ideal:** Edite até 24 horas antes do dia em que a Campaign está programada para enviar.

Se você fizer alterações fora dessas recomendações, pode não ver as atualizações refletidas na mensagem enviada. Por exemplo, se você editar o horário de envio três horas antes de uma Campaign programada para enviar às 12h no horário local, o seguinte pode ocorrer:

- A Braze não envia mensagens para usuários que perderam o horário de envio por mais de uma hora.
- Mensagens pré-enfileiradas ainda podem ser enviadas no horário originalmente enfileirado, em vez do horário ajustado.

Se você precisar fazer alterações, recomendamos parar a Campaign atual (isso cancela quaisquer mensagens enfileiradas). Você pode então duplicar a Campaign, fazer as alterações necessárias e lançar a nova Campaign. Pode ser necessário excluir desta Campaign os usuários que já receberam a primeira Campaign. Certifique-se de reajustar os horários de programação da Campaign para permitir o envio por fuso horário.

### Por que nenhum usuário entrou na minha Campaign programada diária no dia da mudança de horário de verão? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

Nos dias de transição do horário de verão (DST), Campaigns programadas diárias podem ser executadas até uma hora antes ou depois do normal, dependendo se os relógios adiantam ou atrasam. Se o seu segmento depende de atributos personalizados ou eventos com timestamps que estão dentro de uma hora do horário de envio programado, esses usuários podem ainda não se qualificar quando a Campaign avalia a elegibilidade no dia do DST.

Por exemplo, suponha que os usuários normalmente recebem uma atualização de atributo personalizado às 15h UTC, e sua Campaign é executada diariamente às 10:30 em Nova York (Eastern Time). Enquanto Nova York está no horário padrão (UTC-5), 10:30 ET corresponde a 15:30 UTC, então a Campaign é executada após o atributo ser registrado. Quando Nova York muda para o horário de verão (UTC-4), 10:30 ET corresponde a 14:30 UTC, então no dia da mudança para o horário de verão a Campaign pode ser executada antes da atualização do atributo às 15h UTC. Como o atributo qualificador ainda não existe, esses usuários são filtrados. Se a reelegibilidade estiver desativada, os usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas para aquele dia.

Para evitar isso, garanta que as atualizações de atributos personalizados ou eventos ocorram mais de uma hora antes do horário de envio programado da Campaign.

### Por que o número de usuários entrando em uma Campaign não corresponde ao número esperado? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

O número de usuários entrando em uma Campaign pode diferir do número esperado devido à forma como públicos e gatilhos são avaliados. Na Braze, o público é avaliado antes do gatilho (a menos que se use um gatilho de [mudança de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam da Campaign se não fizerem parte inicialmente do público selecionado antes que quaisquer ações de gatilho sejam avaliadas.

{% alert tip %}
Para assistência adicional com solução de problemas de Campaigns, entre em contato com o suporte da Braze dentro de 30 dias da ocorrência do problema, pois temos apenas os últimos 30 dias de registros de diagnóstico.
{% endalert %}

### Por que os usuários receberam minha Campaign duas vezes após eu editá-la? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Se você editar uma Campaign ativa sem pará-la primeiro, os usuários podem receber a mensagem duas vezes. Isso acontece porque editar uma Campaign ativa reenfileira os usuários para a versão atualizada enquanto a fila original ainda está sendo processada. Usuários que ainda não receberam a mensagem original podem acabar em ambas as filas. Para evitar isso, sempre [pare a Campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch#stopping-your-campaign) antes de fazer alterações.

### Qual é a diferença entre as opções Exportar dados de usuários em CSV e Exportar endereços de e-mail em CSV na página de análise de dados da minha Campaign? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Selecionar a opção **CSV Export Email Addresses** baixa dados apenas de usuários com endereços de e-mail. Por exemplo, se você tem um segmento de 100.000 usuários, mas apenas 50.000 deles possuem endereços de e-mail, e você clica em **CSV Export Email Addresses**, a exportação conterá apenas 50.000 linhas de dados. Em comparação, selecionar **CSV Export User Data** exporta todos os dados de usuários.

### Posso pesquisar uma Campaign pelo seu identificador de API? {#can-i-search-for-a-campaign-by-its-api-identifier}

Sim, use o filtro `api_id:YOUR_API_ID` na página **Campaigns** para pesquisar uma Campaign pelo seu identificador de API. Consulte [pesquisando Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) para saber mais.

### Por que os espaços em branco aparecem de forma diferente em campos de entrada versus texto exibido? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

O tratamento de espaços em branco difere entre campos de entrada e componentes de texto exibido por causa da estilização CSS. Em componentes de texto com o CSS padrão `white-space: normal`, múltiplos espaços consecutivos são colapsados em um único espaço quando exibidos. Este é o comportamento padrão do HTML para texto renderizado.

Campos de entrada preservam múltiplos espaços exatamente como você os digita, porque você precisa ver e editar o espaçamento exato para entrada de dados precisa. Isso significa que texto com múltiplos espaços pode aparecer de forma diferente quando visualizado em um campo de entrada (onde todos os espaços são preservados) versus quando exibido em outras partes do dashboard (onde o CSS pode colapsar múltiplos espaços).

Por exemplo, se você inserir um nome de Campaign ou parâmetro UTM com múltiplos espaços em um campo de entrada, verá todos os espaços preservados. No entanto, quando esse mesmo texto aparece em resultados de pesquisa, listas de Campaigns ou outros componentes de texto, múltiplos espaços podem aparecer como um único espaço por causa do tratamento de espaços em branco do CSS.

### Qual é a diferença entre Campaigns da API e Campaigns disparadas por API? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

Campaigns disparadas por API permitem que você gerencie o texto da Campaign, testes multivariantes e regras de reelegibilidade dentro do dashboard da Braze enquanto aciona a entrega desse conteúdo a partir dos seus próprios servidores e sistemas. Essas mensagens também podem incluir dados adicionais para serem modelados nas mensagens em tempo real.

Campaigns da API são usadas para rastrear as mensagens enviadas usando a API. Diferentemente da maioria das Campaigns, você não especifica a mensagem, os destinatários ou a programação, mas sim passa os identificadores nas suas chamadas de API.

### Como posso confirmar se meus usuários receberam uma Campaign disparada por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Você pode [criar um segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando o filtro **Received Campaign** e selecionar a Campaign disparada por API específica que deseja verificar. Após salvar o segmento, use o [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar os usuários desse segmento.

### Posso excluir uma Campaign? {#can-i-delete-a-campaign}

Não, mas você pode [arquivar uma Campaign]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Qual é a diferença entre Campaigns baseadas em ação e Campaigns disparadas por API? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Baseadas em ação {#action-based}

Campaigns de entrega baseada em ação ou Campaigns disparadas por evento são muito eficazes para mensagens transacionais ou baseadas em conquistas e permitem que você as acione para enviar após um usuário completar um determinado evento.

| Prós | Contras |
| ---- | ---- |
| • Visibilidade das cargas úteis JSON recebidas na plataforma (se o evento for disparado por um usuário teste) através do **Registro de atividades de envio de mensagem**<br><br>• Elementos de personalização são incluídos nas propriedades do evento personalizado<br><br>• O evento personalizado pode ser usado para criar segmentos de usuários elegíveis para a mensagem | • Consome pontos de dados |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Baseadas em ação" }

#### Disparadas por API {#api-triggered}

Campaigns disparadas por API e disparadas por servidor são ideais para lidar com transações mais avançadas, permitindo que você acione a entrega do conteúdo da Campaign a partir dos seus próprios servidores e sistemas. A requisição de API para acionar a mensagem também pode incluir dados adicionais para serem modelados na mensagem em tempo real.

| Benefícios | Considerações |
| ---- | ---- |
| • Não registra pontos de dados<br><br>• Elementos de personalização são incluídos nas propriedades da carga útil JSON | • Não permite criar um segmento de usuários elegíveis para a mensagem nas propriedades da carga útil JSON<br><br>• Não é possível ver as cargas úteis JSON recebidas com o **Registro de atividades de envio de mensagem** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disparadas por API" }

### O que devo incluir ao enviar um ticket de suporte para um erro "Request Timed Out"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Se você encontrar um erro "Request Timed Out" ao criar ou editar uma Campaign ou Canvas e precisar entrar em contato com o [suporte da Braze]({{site.baseurl}}/braze_support), inclua as seguintes informações para ajudar a acelerar a resolução:

- **Gravação de tela:** Uma gravação dos passos que você seguiu antes de ver o erro, incluindo quaisquer transições de página.
- **Timestamp e fuso horário:** O horário exato em que o erro ocorreu e seu fuso horário.
- **Navegador e versão:** O navegador que você está usando (por exemplo, Chrome 120, Safari 17) e se você tentou reproduzir o erro em um navegador diferente.
- **Passos para reproduzir:** Uma descrição clara das ações que acionam o erro, incluindo quaisquer configurações específicas de Campaign ou Canvas envolvidas.
- **Registros de rede (opcional):** Abra as ferramentas de desenvolvedor do seu navegador (guia **Network**), reproduza o erro e exporte o registro de rede como um arquivo HAR (HTTP Archive). Isso ajuda a equipe de suporte a identificar qual chamada de API está expirando.

### Por que minha análise de dados de envio não corresponde ao limite máximo de destinatários que defini? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Se você adicionar ou alterar um limite máximo de destinatários em uma Campaign ativa, o limite pode não ser refletido na sua análise de dados de envio pelos seguintes motivos:

- **Limite adicionado após o lançamento:** Se o limite máximo de destinatários não estiver definido quando a Campaign for lançada, as mensagens que já estão enfileiradas antes de você aplicar o limite ainda serão enviadas. O limite só entra em vigor para envios que você enfileirar após salvar a alteração.
- **Interação com limite de frequência:** Se uma Campaign também tem limite de frequência, as mensagens podem ser distribuídas ao longo de uma janela de tempo mais longa. O limite máximo de destinatários é avaliado quando as mensagens são enfileiradas, não quando são entregues. Se o limite for alterado enquanto as mensagens já estão na fila, o limite original se aplica a essas mensagens.
- **Campaigns recorrentes:** Para Campaigns recorrentes, cada envio programado avalia o limite máximo de destinatários de forma independente. Alterar o limite entre envios não ajusta retroativamente as contagens de envios anteriores.

Para evitar desalinhamentos, defina o limite máximo de destinatários antes de lançar a Campaign e evite modificá-lo enquanto os envios estiverem em andamento.

### Por que os envios são menores do que o tamanho estimado do público? {#why-are-sends-lower-than-the-estimated-audience-size}

Vários fatores podem fazer com que o número de envios seja menor do que o tamanho estimado do público:

- **Entrega baseada em ação:** Os usuários só geram envios após realizarem o gatilho, então os envios se acumulam ao longo do tempo e podem ficar atrás da estimativa inicial mostrada quando você criou a Campaign.
- **Edições de público após o lançamento:** Alterar filtros de entrada ou de direcionamento após o lançamento pode deixar o snapshot de **Público estimado** fora de sincronia com quem ainda se qualifica em envios posteriores (por exemplo, quando os usuários não são elegíveis para reentrar).
- **Etapa Jornadas do público:** Para Canvas, uma etapa [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) envia mensagens apenas para os usuários que correspondem à ramificação de maior prioridade para a qual se qualificam, o que pode reduzir os envios em comparação com uma contagem simples de segmento.
- **Grupos de controle:** Se um [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group) ou grupo de controle no nível da Campaign estiver em uso, uma parte do público é retida da entrega.
- **Horário e janelas de entrega:** Para Campaigns por fuso horário local ou programadas, os usuários devem se qualificar tanto na entrada quanto no momento do envio; usuários em determinados fusos horários podem ficar fora da janela de entrega.
- **Deduplicação de e-mail:** Sua Campaign ou Canvas direciona múltiplos usuários com e-mails correspondentes, então um usuário aleatório com aquele endereço de e-mail é escolhido no momento do envio. A mensagem é enviada apenas uma vez e deduplicada para que não seja enviada ao mesmo e-mail várias vezes, mas o tamanho estimado do público inclui todos os usuários.
- **Filtros de entregabilidade de e-mail:** Para Campaigns de e-mail, a Braze exclui usuários que tiveram hard bounce, cancelaram a inscrição de e-mails, foram marcados como SPAM, não possuem endereço de e-mail no perfil ou não estão inscritos em um grupo de inscrições obrigatório. Essas verificações são executadas no momento do envio, então um usuário presente no seu segmento ainda pode ser excluído da contagem real de envios.
- **Limite de frequência global:** Limites no nível do espaço de trabalho podem impedir que usuários elegíveis recebam outra mensagem na mesma janela, o que reduz os envios realizados.
- **Usuários recém-importados:** Perfis que acabaram de se tornar elegíveis podem não receber até a próxima avaliação ou rodada de envio, então as contagens se atualizam em uma execução posterior.
- **Alcançabilidade de push:** Para Campaigns de push, confirme que o público está habilitado para push no app correto. Se você não filtrar por usuários habilitados para push, o público estimado pode incluir perfis que não podem receber push. Verifique **Usuários contatáveis** na etapa **Público-alvo** para uma estimativa operacional mais precisa.
- **Limite de velocidade de entrega:** Um [limite de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) limita quantas mensagens a Braze envia por minuto durante uma única ocorrência de envio. A Braze distribui a entrega ao longo de uma janela mais longa, então alguns envios podem ser adiados, ainda não refletidos na contagem, ou não concluídos se o limite for baixo em relação ao público elegível.
- **Janelas de reelegibilidade:** Usuários que ainda não são reelegíveis não receberão novamente durante o período de espera, então os envios ficam abaixo do tamanho estimado do público para esse período.
- **Janela de relatório:** O intervalo de tempo da análise de dados pode não incluir todos os envios.
- **Reavaliação do segmento:** Para Campaigns baseadas em ação ou programadas que reavaliam no momento do envio, os usuários que estavam no segmento quando a Campaign foi enfileirada podem não se qualificar mais quando a mensagem é realmente enviada.
- **Limites de envio:** Um número máximo de usuários (ou limite similar) em **Público-alvo** interrompe a entrega quando o limite é atingido.
- **Filtros rigorosos de dispositivo ou navegador:** Filtros que correspondem apenas às versões mais recentes de apps ou navegadores reduzem o conjunto alcançável no momento do envio em comparação com uma prévia ampla de segmento.

### Onde estão as perguntas frequentes sobre limite de frequência global? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Para perguntas sobre dias corridos, push silencioso, webhooks, comportamento do Canvas e tópicos relacionados, consulte as [Perguntas frequentes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) de [Limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Por que minha Campaign está com taxas de envio mais baixas? {#why-is-my-campaign-experiencing-lower-send-rates}

Se você perceber que suas Campaigns programadas diárias estão enviando para menos usuários ao longo do tempo, verifique o seguinte:

- **Verifique se a reelegibilidade está ativada:** Sem reelegibilidade, a Braze envia a mensagem para cada usuário apenas uma vez. Em Campaigns programadas diárias, apenas os usuários que correspondem ao público e que ainda não receberam a mensagem são elegíveis para cada envio. À medida que mais usuários recebem a mensagem, cada envio posterior tem menos usuários elegíveis, então o volume de envios diminui.
- **Verifique se o público tem associação fixa:** Públicos construídos a partir de uma lista fixa de usuários (como uma [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) usada como filtro de segmento) não ganham novos membros automaticamente. Sem novos entrantes, o volume de envios não pode se recuperar à medida que os usuários são alcançados.

Para [limites de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) e outros fatores que reduzem os envios em uma única ocorrência, consulte [Por que os envios são menores do que o tamanho estimado do público?](#why-are-sends-lower-than-the-estimated-audience-size).

### Por que os destinatários únicos podem exceder os envios para e-mail e SMS? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Para e-mail e SMS, a Braze incrementa **Destinatários únicos** antes da tentativa de envio pelo ESP e incrementa **Envios** após uma resposta bem-sucedida do ESP. Erros permanentes (como endereços de e-mail inválidos) ou endereços duplicados fazem com que os destinatários únicos excedam os envios.

### Por que **Último envio** não corresponde ao meu horário de envio programado? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Para uma Campaign com um único envio programado, **Último envio** corresponde ao horário de lançamento. Para Campaigns recorrentes com **Enviar no fuso horário local** ativado, **Último envio** pode aparecer antes do horário programado porque os envios para usuários em fusos horários mais adiantados (por exemplo, GMT vs. PST) são concluídos antes do horário programado do seu espaço de trabalho.

### Por que uma Campaign histórica parada não mostra mais métricas na página **Analytics**? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

A guia **Analytics** exibe por padrão os últimos 90 dias. Se a Campaign enviou pela última vez fora dessa janela, as métricas podem aparecer como zero até que você ajuste o intervalo de datas na página **Analytics** para incluir o período em que a Campaign enviou. Para saber mais, consulte [Análise de dados de Campaigns]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Restaurar dados de interação** não restaura a análise de dados de Campaigns. Isso se aplica apenas a filtros de redirecionamento e ao histórico de interações do usuário. Para saber mais, consulte [Dados de interação de envio de mensagens]({{site.baseurl}}/messaging_interaction_data).