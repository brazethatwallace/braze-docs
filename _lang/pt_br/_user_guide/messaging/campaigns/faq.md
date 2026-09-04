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

## Como faço para criar uma campanha multicanal? {#how-do-i-create-a-multichannel-campaign}

Consulte [Campanhas multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) em **Criar uma campanha** para ver as etapas de configuração e os canais compatíveis.

### Posso adicionar um grupo de controle à minha campanha multicanal? {#can-i-add-a-control-group-to-my-multichannel-campaign}

Consulte [Grupos de controle]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups) em **Criar uma campanha**. Para testes entre canais, use o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas).

### Quais são algumas formas de começar a testar e otimizar campanhas? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

Campanhas multivariantes e Canvas com múltiplas variantes são uma ótima forma de começar! Por exemplo, você pode executar uma [campanha multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing) para testar uma mensagem com diferentes textos ou linhas de assunto. Canvas com múltiplas variantes podem ajudar a testar fluxos de trabalho inteiros.

### Por que a taxa de abertura da minha campanha diminuiu? {#why-did-the-open-rate-for-my-campaign-decrease}

Taxas de abertura baixas nem sempre estão relacionadas a um problema técnico. Pode haver problemas com clipping de e-mail, que resulta em um pixel de rastreamento ausente. No entanto, também é possível que menos usuários estejam abrindo seus e-mails devido ao conteúdo ou a mudanças no tamanho do público.

### Como os públicos de campanhas são avaliados? {#how-are-campaign-audiences-evaluated}

Por padrão, as campanhas verificam os filtros de público no momento da entrada. Para campanhas baseadas em ação com postergação, existe uma opção de reavaliar os critérios do Segment no momento do envio para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

### Por que há uma diferença entre o número de destinatários únicos e o número de envios de uma determinada campanha ou Canvas? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

Uma possível explicação é que a campanha ou o Canvas tem a reelegibilidade ativada, o que significa que os usuários que se qualificam para o Segment e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a reelegibilidade não estiver ativada, a explicação provável para a diferença entre envios e destinatários únicos pode ser que os usuários possuem múltiplos dispositivos, em diferentes plataformas, associados aos seus perfis.

Por exemplo, se você tiver um Canvas com notificações por push para iOS e web, um determinado usuário com dispositivos móvel e desktop pode receber mais de uma mensagem.

### Por que *Destinatários únicos* é maior do que o número de usuários que direcionei? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*Destinatários únicos* pode ser maior do que o público esperado porque a Braze rastreia destinatários únicos diários para fins de relatório. Isso permite que a Braze atribua conversões dentro da janela de conversão cada vez que um usuário recebe a mensagem, em vez de consolidar múltiplos recebimentos em uma única contagem vitalícia (o que distorceria o cálculo de conversão).

Por exemplo, se um usuário recebe uma campanha na segunda-feira e novamente na sexta-feira e converte após cada envio, a Braze pode reportar isso como dois recebimentos e duas conversões. Se a Braze contasse apenas um "único" vitalício para ambos os envios, você perderia uma conversão válida ou contaria duas vezes para um único destinatário, o que torna o desempenho da campanha mais difícil de interpretar.

O mesmo padrão se aplica a campanhas recorrentes e à reelegibilidade: se dois usuários recebem um envio recorrente hoje e novamente amanhã, *Destinatários únicos* conta quatro linhas de destinatários diários, não dois perfis.

### Por que o número de conversões pode exceder o número de usuários únicos em campanhas multicanal? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

Consulte [Conversões e relatórios]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions) em **Criar uma campanha** e [Regras de rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) em **Eventos de conversão**.

### Por que minha campanha tem uma base de usuários contatáveis menor do que o Segment que estou usando? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

Se você tiver um [grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group) configurado, isso impedirá que uma porcentagem do seu público contatável receba campanhas. Isso significa que o número de usuários contatáveis do seu Segment pode ser maior do que o número de usuários contatáveis da sua campanha, mesmo que a campanha esteja usando o mesmo Segment.

### O que a entrega por fuso local oferece? {#what-does-local-time-zone-delivery-offer}

A entrega por fuso local permite enviar campanhas de mensagens para um Segment com base no fuso horário individual de cada usuário. Sem a entrega por fuso local, as campanhas serão agendadas com base nas configurações de fuso horário da sua empresa na Braze.

Por exemplo, uma empresa sediada em Londres enviando uma campanha às 12h alcançará usuários na costa oeste da América às 4h da manhã. Se o seu app estiver disponível apenas em determinados países, isso pode não ser um risco para você. Caso contrário, recomendamos fortemente evitar o envio de notificações por push de madrugada para a sua base de usuários.

### Como a Braze reconhece o fuso horário de um usuário? {#how-does-braze-recognize-a-users-time-zone}

A Braze determinará automaticamente o fuso horário de um usuário a partir do dispositivo dele. Isso garante precisão no fuso horário e cobertura completa dos seus usuários. Usuários criados pela User API ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como fuso horário padrão até serem reconhecidos no seu app pelo SDK.

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings) no dashboard.

### Quando a Braze avalia os usuários para entrega por fuso local? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

A Braze avalia os usuários para elegibilidade de entrada em:

- Horário de Samoa (UTC+13) no dia agendado
- O horário local do dia agendado

Para que um usuário seja elegível para entrada, ele deve ser elegível em ambas as verificações. Por exemplo, se um Canvas estiver agendado para lançamento em 7 de agosto de 2021 às 14h no fuso local, então direcionar um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova York em 6 de agosto de 2021 às 21h
- Nova York em 7 de agosto de 2021 às 14h

Para entrar, um usuário deve corresponder ao seu público e filtros em ambos os momentos de avaliação. Se o usuário não for elegível na primeira verificação, a Braze não executa a segunda verificação. Não há um tempo mínimo que o usuário precisa ter estado no Segment antes do lançamento. Apenas a elegibilidade em cada verificação importa.

Esse comportamento de avaliação é separado de [quanto tempo de antecedência você agenda a campanha no dashboard](#how-do-i-schedule-a-local-time-zone-campaign). Agendar com pelo menos 24 horas de antecedência é uma recomendação porque ajuda as mensagens a serem entregues ao longo de toda a janela de 24 horas de fuso local, não um requisito de que cada usuário tenha estado no público por 24 horas.

#### Exemplos {#examples}

Por exemplo, se uma campanha estiver agendada para ser entregue às 19h UTC, começamos a enfileirar os envios da campanha assim que um fuso horário é identificado (como Samoa). Isso significa que estamos nos preparando para enviar a mensagem, não enviando a campanha. Se os usuários não corresponderem a nenhum filtro quando verificamos a elegibilidade, eles não farão parte do público-alvo.

Como outro exemplo, digamos que você queira criar duas campanhas agendadas para enviar no mesmo dia — uma de manhã e uma à noite — e adicionar um filtro para que os usuários só possam receber a segunda campanha se já tiverem recebido a primeira. Com a entrega por fuso local, alguns usuários podem não receber a segunda campanha. Isso acontece porque verificamos a elegibilidade quando o fuso horário do usuário é identificado. Portanto, se o horário agendado ainda não ocorreu no fuso horário deles, eles não receberam a primeira campanha, o que significa que não serão elegíveis para a segunda campanha.

A linha do tempo a seguir assume uma definição de Segment que inclui uma janela de associação limitada por tempo. Neste exemplo, os usuários saem do Segment 24 horas depois de ingressarem. Esse comportamento de filtro é uma razão pela qual um usuário pode passar na primeira verificação e falhar na segunda.

![Linha do tempo de um usuário entrando no Segment antes da primeira verificação e saindo antes da segunda.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Descrição da linha do tempo %}

1. O Usuário A entra no Segment às 6h59 PST (4h59 no horário de Samoa).
2. A Braze verifica a associação ao Segment às 7h no horário de Samoa para determinar quais usuários são elegíveis para receber a campanha nas próximas 24 horas. O Usuário A está no Segment neste momento.
3. O Segment tem uma janela de 24 horas, então o Usuário A sai do Segment 24 horas após ingressar: 6h59 PST (4h59 no horário de Samoa).
4. A campanha por fuso local é enviada às 7h PST, mas o Usuário A já saiu do Segment.

{% enddetails %}

### Como faço para agendar uma campanha por fuso local? {#how-do-i-schedule-a-local-time-zone-campaign}

A seção anterior descreve quando a Braze avalia a elegibilidade para entrega por fuso local (as duas verificações). Esta seção descreve quando você define o cronograma da campanha no dashboard (tempo de antecedência do agendamento) e quais usuários ainda recebem a mensagem se você agendar com menos de 24 horas de antecedência.

Ao agendar uma campanha, escolha enviá-la em um horário designado e depois selecione **Enviar campanha para os usuários em seus fusos locais**.

A Braze recomenda fortemente que todas as campanhas por fuso local sejam agendadas com 24 horas de antecedência. Como essa campanha precisa ser enviada ao longo de um dia inteiro, agendá-la com 24 horas de antecedência garante que sua mensagem alcançará todo o seu Segment. No entanto, você pode agendar essas campanhas com menos de 24 horas de antecedência, se necessário. Tenha em mente que a Braze não enviará mensagens para usuários que perderam o horário de envio por mais de 1 hora.

Por exemplo, se são 13h e você agenda uma campanha por fuso local para as 15h, a campanha será enviada imediatamente para todos os usuários cujo horário local está entre 15h e 16h, mas não para usuários cujo horário local é 17h. Além disso, o horário de envio escolhido para sua campanha não pode já ter ocorrido no fuso horário da sua empresa.

Editar uma campanha por fuso local que foi agendada com menos de 24 horas de antecedência não altera o cronograma da mensagem. Se você decidir editar uma campanha por fuso local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no Segment direcionado quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar um fuso local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada para todos os membros do Segment no horário original (17h).

{% alert note %}
Para componentes de Canvas, os usuários não precisam estar no componente por 24 horas para receber o próximo componente na jornada do usuário para entrega por fuso local.
{% endalert %}

Se você permitiu que os usuários se tornassem reelegíveis para a campanha, eles a receberão novamente no horário original (17h). Para todas as ocorrências subsequentes da sua campanha, no entanto, suas mensagens serão enviadas apenas no horário atualizado.

### Quando as alterações nas campanhas por fuso local entram em vigor? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

Os Segments de destino para campanhas por fuso local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo para garantir a entrega a todo o Segment. Por exemplo, considere um Segment que direciona usuários no segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Usou o app pela primeira vez há menos de 2 dias

A entrega por fuso local pode perder usuários neste Segment com base no horário de entrega e no fuso local dos usuários. Isso acontece porque um usuário pode sair do Segment no momento em que seu fuso horário aciona a entrega.

### Quais alterações posso fazer em campanhas agendadas antes do lançamento? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Quando a campanha está agendada, você deve fazer edições em qualquer coisa que não seja a composição da mensagem antes de enfileirarmos as mensagens para envio. Como em todas as campanhas, você não pode editar eventos de conversão após o lançamento.

### Atualizei minha campanha agendada. Por que ela não foi lançada? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

Isso pode acontecer quando uma campanha está agendada para ser lançada no exato momento em que foi atualizada. Por exemplo, se agora são 15h10 e você alterou a campanha para lançar às 15h10 e selecionou **Atualizar campanha**, o horário já passou das 15h10, o que significa que o horário agendado para o lançamento já passou. Em vez de agendar a campanha para o mesmo horário, selecione **Enviar assim que a campanha for lançada**.

### Qual é a "zona de segurança" antes que as mensagens de uma campanha agendada sejam enfileiradas? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

Recomendamos fazer alterações nas mensagens dentro dos seguintes prazos:

- **Campanhas agendadas únicas:** edite até o horário de envio agendado.
- **Campanhas agendadas recorrentes:** edite até o horário de envio agendado.
- **Campanhas com horário de envio local:** edite até 24 horas antes do horário de envio agendado.
- **Campanhas com horário de envio ideal:** edite até 24 horas antes do dia em que a campanha está agendada para ser enviada.

Se você fizer alterações fora dessas recomendações, pode não ver as atualizações refletidas na mensagem enviada. Por exemplo, se você editar o horário de envio três horas antes de uma campanha agendada para enviar às 12h no fuso local, o seguinte pode ocorrer:

- A Braze não envia mensagens para usuários que perderam o horário de envio por mais de uma hora.
- Mensagens pré-enfileiradas ainda podem ser enviadas no horário originalmente enfileirado, em vez do horário ajustado.

Se você precisar fazer alterações, recomendamos parar a campanha atual (isso cancela quaisquer mensagens enfileiradas). Você pode então duplicar a campanha, fazer as alterações necessárias e lançar a nova campanha. Pode ser necessário excluir dessa campanha os usuários que já receberam a primeira campanha. Certifique-se de reajustar os horários do cronograma da campanha para permitir o envio por fuso horário.

### Por que nenhum usuário entrou na minha campanha agendada diária no dia do Horário de Verão? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

Em dias de transição do Horário de Verão (DST), campanhas agendadas diárias podem ser executadas até uma hora antes ou depois do normal, dependendo se os relógios adiantam ou atrasam. Se o seu Segment depende de atributos personalizados ou eventos com timestamps que caem dentro de uma hora do horário de envio agendado, esses usuários podem ainda não se qualificar quando a campanha avalia a elegibilidade no dia do DST.

Por exemplo, suponha que os usuários normalmente recebem uma atualização de atributo personalizado às 15h UTC e sua campanha é executada diariamente às 10h30 em Nova York (Eastern Time). Enquanto Nova York está no horário padrão (UTC-5), 10h30 ET corresponde a 15h30 UTC, então a campanha é executada após o atributo ser registrado. Quando Nova York muda para o horário de verão (UTC-4), 10h30 ET corresponde a 14h30 UTC, então no dia de adiantamento do DST a campanha pode ser executada antes da atualização do atributo às 15h UTC. Como o atributo qualificador ainda não existe, esses usuários são filtrados. Se a reelegibilidade estiver desativada, os usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas para aquele dia.

Para evitar isso, garanta que suas atualizações de atributos personalizados ou eventos ocorram mais de uma hora antes do horário de envio agendado da campanha.

### Por que o número de usuários entrando em uma campanha não corresponde ao número esperado? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

O número de usuários entrando em uma campanha pode diferir do número esperado por causa de como os públicos e gatilhos são avaliados. Na Braze, o público é avaliado antes do gatilho (a menos que se use um gatilho de [mudança de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam da campanha se não fizerem parte inicialmente do público selecionado antes que quaisquer ações de gatilho sejam avaliadas.

{% alert tip %}
Para assistência adicional na solução de problemas com campanhas, entre em contato com o suporte da Braze dentro de 30 dias da ocorrência do problema, pois temos apenas os últimos 30 dias de registros de diagnóstico.
{% endalert %}

### Por que os usuários receberam minha campanha duas vezes depois que eu a editei? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

Se você editar uma campanha ativa sem pará-la primeiro, os usuários podem receber a mensagem duas vezes. Isso acontece porque editar uma campanha ativa reenfileira os usuários para a versão atualizada enquanto a fila original ainda está sendo processada. Usuários que ainda não receberam a mensagem original podem acabar em ambas as filas. Para evitar isso, sempre [pare a campanha]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#stopping-your-campaign) antes de fazer alterações.

### Qual é a diferença entre as opções Exportar CSV de dados de usuários e Exportar CSV de endereços de e-mail na página de análise de dados da minha campanha? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

Selecionar a opção **Exportar CSV de endereços de e-mail** baixa dados apenas de usuários com endereços de e-mail. Por exemplo, se você tem um Segment de 100.000 usuários, mas apenas 50.000 desses usuários têm endereços de e-mail, e você clica em **Exportar CSV de endereços de e-mail**, a exportação conterá apenas 50.000 linhas de dados. Em comparação, selecionar **Exportar CSV de dados de usuários** exporta todos os dados de usuários.

### Posso pesquisar uma campanha pelo seu identificador de API? {#can-i-search-for-a-campaign-by-its-api-identifier}

Sim, use o filtro `api_id:YOUR_API_ID` na página de **Campaigns** para pesquisar uma campanha pelo seu identificador de API. Consulte [pesquisando campanhas]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) para saber mais.

### Por que o espaço em branco aparece de forma diferente em campos de entrada versus texto exibido? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

O tratamento de espaços em branco difere entre campos de entrada e componentes de texto exibido por causa da estilização CSS. Em componentes de texto com o CSS padrão `white-space: normal`, múltiplos espaços consecutivos são colapsados em um único espaço quando exibidos. Esse é o comportamento padrão do HTML para texto renderizado.

Campos de entrada preservam múltiplos espaços exatamente como você os insere, porque você precisa ver e editar o espaçamento exato para uma entrada de dados precisa. Isso significa que texto com múltiplos espaços pode aparecer de forma diferente quando visualizado em um campo de entrada (onde todos os espaços são preservados) versus quando exibido em outras partes do dashboard (onde o CSS pode colapsar múltiplos espaços).

Por exemplo, se você inserir o nome de uma campanha ou um parâmetro UTM com múltiplos espaços em um campo de entrada, verá todos os espaços preservados. No entanto, quando esse mesmo texto aparece em resultados de pesquisa, listas de campanhas ou outros componentes de texto, múltiplos espaços podem aparecer como um único espaço por causa do tratamento de espaço em branco do CSS.

### Qual é a diferença entre campanhas de API e campanhas disparadas por API? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

Campanhas disparadas por API permitem que você gerencie o texto da campanha, testes multivariantes e regras de reelegibilidade dentro do dashboard da Braze enquanto dispara a entrega desse conteúdo a partir dos seus próprios servidores e sistemas. Essas mensagens também podem incluir dados adicionais para serem inseridos nos modelos das mensagens em tempo real.

Campanhas de API são usadas para rastrear as mensagens enviadas usando a API. Diferentemente da maioria das campanhas, você não especifica a mensagem, os destinatários ou o cronograma, mas sim passa os identificadores nas suas chamadas de API.

### Como posso confirmar se meus usuários receberam uma campanha disparada por API? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

Você pode [criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) usando o filtro **Recebeu Campaign** e selecionar a campanha disparada por API específica que deseja verificar. Depois de salvar o Segment, use o [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) para exportar os usuários desse Segment.

### Posso excluir uma campanha? {#can-i-delete-a-campaign}

Não, mas você pode [arquivar uma campanha]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Qual é a diferença entre campanhas baseadas em ação e campanhas disparadas por API? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Baseadas em ação {#action-based}

Campanhas de entrega baseada em ação ou campanhas disparadas por evento são muito eficazes para mensagens transacionais ou de conquistas e permitem que você as dispare após um usuário completar um determinado evento.

| Prós | Contras |
| ---- | ---- |
| • Visibilidade dos payloads JSON recebidos na plataforma (se o evento for disparado por um usuário teste) via o **Registro de atividade de mensagens**<br><br>• Elementos de personalização são incluídos nas propriedades do evento personalizado<br><br>• O evento personalizado pode ser usado para criar Segments de usuários elegíveis para a mensagem | • Consome pontos de dados |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Baseadas em ação" }

#### Disparadas por API {#api-triggered}

Campanhas disparadas por API e disparadas por servidor são ideais para lidar com transações mais avançadas, permitindo que você dispare a entrega do conteúdo da campanha a partir dos seus próprios servidores e sistemas. A requisição de API para disparar a mensagem também pode incluir dados adicionais para serem inseridos no modelo da mensagem em tempo real.

| Benefícios | Considerações |
| ---- | ---- |
| • Não registra pontos de dados<br><br>• Elementos de personalização são incluídos nas propriedades do payload JSON | • Não permite criar um Segment de usuários elegíveis para a mensagem nas propriedades do payload JSON<br><br>• Não é possível ver payloads JSON recebidos com o **Registro de atividade de mensagens** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disparadas por API" }

### O que devo incluir ao enviar um ticket de suporte para um erro "Tempo de requisição esgotado"? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Se você encontrar um erro "Tempo de requisição esgotado" ao criar ou editar uma campanha ou Canvas e precisar entrar em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support), inclua as seguintes informações para ajudar a agilizar a resolução:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='campaign' %}

### Por que minhas análises de envio não correspondem ao limite máximo de destinatários que defini? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

Se você adicionar ou alterar um limite máximo de destinatários em uma campanha ativa, o limite pode não ser refletido nas suas análises de envio pelos seguintes motivos:

- **Limite adicionado após o lançamento:** Se o limite máximo de destinatários não estiver definido quando a campanha for lançada, as mensagens que já estiverem enfileiradas antes de você aplicar o limite ainda serão enviadas. O limite só entra em vigor para envios que você enfileirar após salvar a alteração.
- **Interação com limite de frequência:** Se uma campanha também tiver limite de frequência, as mensagens podem ser distribuídas ao longo de uma janela de tempo mais longa. O limite máximo de destinatários é avaliado quando as mensagens são enfileiradas, não quando são entregues. Se o limite for alterado enquanto as mensagens já estiverem na fila, o limite original se aplica a essas mensagens.
- **Campanhas recorrentes:** Para campanhas recorrentes, cada envio agendado avalia o limite máximo de destinatários de forma independente. Alterar o limite entre envios não ajusta retroativamente as contagens de envios anteriores.

Para evitar desalinhamento, defina o limite máximo de destinatários antes de lançar a campanha e evite modificá-lo enquanto os envios estiverem em andamento.

### Por que os envios são menores do que o tamanho estimado do público? {#why-are-sends-lower-than-the-estimated-audience-size}

Vários fatores podem fazer com que o número de envios seja menor do que o tamanho estimado do público:

- **Entrega baseada em ação:** Os usuários só geram envios após realizarem o gatilho, então os envios se acumulam ao longo do tempo e podem ficar atrás da estimativa inicial mostrada quando você criou a campanha.
- **Edições no público após o lançamento:** Alterar filtros de entrada ou direcionamento após o lançamento pode fazer com que o snapshot do **Público estimado** fique dessincronizado com quem ainda se qualifica em envios posteriores (por exemplo, quando os usuários não são elegíveis para reentrar).
- **Etapa de jornadas do público:** Para Canvas, uma etapa de [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) envia mensagens apenas para os usuários que correspondem à Branch de maior prioridade para a qual se qualificam, o que pode reduzir os envios em comparação com uma contagem simples de Segment.
- **Grupos de controle:** Se um [grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group) ou grupo de controle no nível da campanha estiver em uso, uma parte do público é retida da entrega.
- **Timing e janelas de entrega:** Para campanhas por fuso local ou agendadas, os usuários devem se qualificar tanto na entrada quanto no momento do envio; usuários em determinados fusos horários podem ficar fora da janela de entrega.
- **Deduplicação de e-mail:** Sua campanha ou Canvas direciona múltiplos usuários com e-mails correspondentes, então um usuário aleatório com aquele endereço de e-mail é escolhido no momento do envio. A mensagem é enviada apenas uma vez e deduplicada para que não seja enviada ao mesmo e-mail múltiplas vezes, mas o tamanho estimado do público inclui todos os usuários.
- **Filtros de entregabilidade de e-mail:** Para campanhas de e-mail, a Braze exclui usuários que tiveram hard bounce, cancelaram a inscrição de e-mails, foram marcados como SPAM, não têm endereço de e-mail no perfil ou não estão inscritos em um grupo de inscrições obrigatório. Essas verificações são executadas no momento do envio, então um usuário presente no seu Segment ainda pode ser excluído da contagem real de envios.
- **Timing de importação de CSV:** Quando a associação ao Segment é mantida por [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), endereços de e-mail adicionados após o envio de uma campanha agendada não são alcançados por esse envio. Como a Braze não retém um snapshot da associação ao Segment no momento do envio, o tamanho atual do Segment pode exceder o número de usuários que realmente receberam a mensagem.
- **Limite de frequência global:** Limites no nível do espaço de trabalho podem impedir que usuários elegíveis recebam outra mensagem na mesma janela, o que reduz os envios realizados.
- **Usuários recém-importados:** Perfis que acabaram de se tornar elegíveis podem não receber até a próxima avaliação ou rodada de envio, então as contagens se atualizam em uma execução posterior.
- **Alcançabilidade de push:** Para campanhas de push, confirme que o público está habilitado para push no app correto. Se você não filtrar por usuários habilitados para push, o público estimado pode incluir perfis que não podem receber push. Verifique **Usuários contatáveis** na etapa **Públicos-alvo** para uma estimativa operacional mais precisa.
- **Limite de frequência:** Um [limite de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) limita quantas mensagens a Braze envia por minuto durante uma única ocorrência de envio. A Braze distribui a entrega ao longo de uma janela mais longa, então alguns envios podem ser adiados, ainda não refletidos na contagem, ou não concluídos se o limite for baixo em relação ao público elegível.
- **Janelas de reelegibilidade:** Usuários que ainda não são reelegíveis não receberão novamente durante o período de espera, então os envios ficam abaixo do tamanho estimado do público para esse período.
- **Janela de relatório:** O intervalo de tempo da análise de dados pode não incluir todos os envios.
- **Reavaliação de Segment:** Para campanhas baseadas em ação ou agendadas que reavaliam no momento do envio, usuários que estavam no Segment quando a campanha foi enfileirada podem não mais se qualificar quando a mensagem é efetivamente enviada.
- **Limites de envio:** Um número máximo de usuários (ou limite similar) em **Públicos-alvo** interrompe a entrega quando o limite é atingido.
- **Filtros rigorosos de dispositivo ou navegador:** Filtros que correspondem apenas às versões mais recentes de apps ou navegadores reduzem o conjunto contatável no momento do envio em comparação com uma prévia ampla de Segment.

### Onde estão as perguntas frequentes sobre limite de frequência global? {#where-are-frequently-asked-questions-about-global-frequency-capping}

Para perguntas sobre dias de calendário, push silencioso, webhooks, comportamento do Canvas e tópicos relacionados, consulte as [Perguntas frequentes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq) de [Limite de frequência e limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Por que minha campanha está com taxas de envio menores? {#why-is-my-campaign-experiencing-lower-send-rates}

Se você perceber que suas campanhas agendadas diárias enviam para menos usuários ao longo do tempo, verifique o seguinte:

- **Verifique se a reelegibilidade está ativada:** Sem reelegibilidade, a Braze envia a mensagem para cada usuário apenas uma vez. Em campanhas agendadas diárias, apenas os usuários que correspondem ao público e ainda não receberam a mensagem são elegíveis para cada envio. À medida que mais usuários recebem a mensagem, cada envio posterior tem menos usuários elegíveis, então o volume de envio diminui.
- **Verifique se o público tem associação fixa:** Públicos construídos a partir de uma lista fixa de usuários (como uma [importação de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) usada como filtro de Segment) não ganham novos membros automaticamente. Sem novos entrantes, o volume de envio não pode se recuperar à medida que os usuários são alcançados.

Para [limites de velocidade de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) e outros fatores que reduzem os envios de uma única ocorrência, consulte [Por que os envios são menores do que o tamanho estimado do público?](#why-are-sends-lower-than-the-estimated-audience-size).

### Por que os destinatários únicos podem exceder os envios para e-mail e SMS? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

Para e-mail e SMS, a Braze incrementa **Destinatários únicos** antes da tentativa de envio pelo ESP e incrementa **Envios** após uma resposta bem-sucedida do ESP. Erros permanentes (como endereços de e-mail inválidos) ou endereços duplicados fazem com que os destinatários únicos excedam os envios.

### Por que **Último envio** não corresponde ao meu horário de envio agendado? {#why-doesnt-last-sent-match-my-scheduled-send-time}

Para uma campanha com um único envio agendado, **Último envio** corresponde ao horário de lançamento. Para campanhas recorrentes com **Enviar no fuso local** ativado, **Último envio** pode aparecer antes do horário agendado porque os envios para usuários em fusos horários mais adiantados (por exemplo, GMT versus PST) são concluídos antes do horário do cronograma do seu espaço de trabalho.

### Por que uma campanha histórica parada não mostra mais métricas na página **Analytics**? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

A aba **Analytics** tem como padrão os últimos 90 dias. Se a campanha foi enviada pela última vez fora dessa janela, as métricas podem aparecer como zero até que você ajuste o intervalo de datas na página **Analytics** para incluir o período em que a campanha foi enviada. Para saber mais, consulte [Análise de dados de campanhas]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics).

**Recuperar dados de interação** não recupera análises de dados de campanhas. Aplica-se apenas a filtros de redirecionamento e histórico de interação do usuário. Para saber mais, consulte [Dados de interação de mensagens]({{site.baseurl}}/messaging_interaction_data).