---
nav_title: FAQ
article_title: FAQ sobre Campanhas
page_order: 10
page_type: FAQ
description: "Esta página fornece respostas para perguntas frequentes sobre campanhas."
tool: Campaigns

---

# Perguntas frequentes

> Este artigo fornece respostas para algumas perguntas frequentes sobre campanhas.

### Como crio uma campanha multicanal?

Para criar uma campanha multicanal, selecione **Envio de mensagens** > **Campanhas**. Em seguida, selecione **Criar campanha** > **Multicanal**. A partir daí, você pode selecionar entre os seguintes canais de envio de mensagens: Cartões de conteúdo, e-mail, LINE, notificações por push, SMS/MMS/RCS, webhook ou WhatsApp.

### Posso adicionar um grupo de controle à minha campanha multicanal?

Não, os grupos de controle em campanhas são destinados ao envio de mensagens em canal individual, como E-mail A versus E-mail B. Como alternativa, experimente usar o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) para testar diferentes canais, conteúdos de mensagens e horários de entrega.

### Quais são algumas formas de começar a testar e otimizar campanhas?

Campanhas multivariantes e Canvas com múltiplas variantes são uma ótima forma de começar! Por exemplo, você pode executar uma [campanha multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing/) para testar uma mensagem com diferentes textos ou linhas de assunto. Canvas com múltiplas variantes podem ajudar a testar fluxos de trabalho inteiros.

### Por que a taxa de abertura da minha campanha diminuiu?

Taxas de abertura baixas nem sempre estão relacionadas a um problema técnico. Pode haver problemas com o corte de e-mail, que resulta em um pixel de rastreamento ausente. No entanto, também é possível que menos usuários estejam abrindo seus e-mails devido ao conteúdo ou a mudanças no tamanho do público.

### Como os públicos das campanhas são avaliados?

Por padrão, as campanhas verificam os filtros de público no momento da entrada. Para campanhas baseadas em ação com postergação, existe a opção de reavaliar os critérios do segmento no momento do envio para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada.

### Por que há uma diferença entre o número de destinatários únicos e o número de envios para uma determinada campanha ou Canvas?

Uma possível explicação é que a campanha ou o Canvas tem a reelegibilidade ativada, o que significa que os usuários que se qualificam para o segmento e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a reelegibilidade não estiver ativada, a explicação provável para a diferença entre envios e destinatários únicos pode ser que os usuários possuem múltiplos dispositivos, em diferentes plataformas, associados aos seus perfis.

Por exemplo, se você tiver um Canvas que possui notificações por push tanto para iOS quanto para web, um determinado usuário com dispositivos móvel e desktop pode receber mais de uma mensagem.

### Por que o número de conversões pode exceder o número de usuários únicos em campanhas multicanais?

Em campanhas multicanais, a Braze conta as conversões por canal, não por usuário. Quando um usuário realiza uma única ação de conversão dentro da janela de conversão, a Braze atribui essa conversão a cada canal pelo qual o usuário recebeu uma mensagem. Isso significa que, se um usuário receber mensagens em múltiplos canais (por exemplo, e-mail e push) e converter, a Braze conta múltiplas conversões, uma para cada canal. Como resultado, a contagem total de conversões pode exceder o número de usuários únicos que converteram.

Por exemplo, se uma campanha multicanal envia tanto um e-mail quanto uma notificação por push para um usuário, e esse usuário realiza uma ação de conversão após receber ambas as mensagens e dentro da janela de conversão, a Braze conta isso como duas conversões — uma atribuída ao e-mail e uma atribuída ao push — mesmo sendo uma única ação do mesmo usuário.

### Por que minha campanha tem uma base de usuários contatáveis menor do que o segmento que estou usando para a campanha?

Se você tiver um [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group/) configurado, isso impedirá que uma porcentagem do seu público contatável receba campanhas. Isso significa que o número de usuários contatáveis do seu segmento pode, às vezes, ser maior do que o número de usuários contatáveis da sua campanha, mesmo que a campanha esteja usando o mesmo segmento.

### O que a entrega por fuso horário local oferece?

A entrega por fuso horário local permite entregar campanhas de mensagens a um segmento com base no fuso horário individual de cada usuário. Sem a entrega por fuso horário local, as campanhas serão programadas com base nas configurações de fuso horário da sua empresa na Braze.

Por exemplo, uma empresa sediada em Londres que envia uma campanha às 12h alcançará usuários na costa oeste dos Estados Unidos às 4h da manhã. Se o seu app está disponível apenas em determinados países, isso pode não ser um risco para você. Caso contrário, recomendamos fortemente evitar o envio de notificações por push de madrugada para a sua base de usuários.

### Como a Braze reconhece o fuso horário de um usuário?

A Braze determinará automaticamente o fuso horário de um usuário a partir do seu dispositivo. Isso garante precisão de fuso horário e cobertura completa dos seus usuários. Usuários criados pela API de Usuários ou sem um fuso horário definido terão o fuso horário da sua empresa como fuso horário padrão até serem reconhecidos no seu app pelo SDK.

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings/) no dashboard.

### Quando a Braze avalia os usuários para entrega por fuso horário local?

A Braze avalia os usuários para elegibilidade de entrada em:

- Horário de Samoa (UTC+13) ou UTC+14 durante o horário de verão
- O horário local do dia programado

Para que um usuário seja elegível para entrada, ele deve ser elegível em ambas as verificações. Por exemplo, se um Canvas está programado para ser lançado em 7 de agosto de 2021 às 14h no fuso horário local, o direcionamento de um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova York em 6 de agosto de 2021 às 21h
- Nova York em 7 de agosto de 2021 às 14h

O usuário deve estar no segmento por 24 horas antes do lançamento. Se o usuário não for elegível na primeira verificação, a Braze não tentará a segunda verificação.

#### Exemplos

Por exemplo, se uma campanha está programada para ser entregue às 19h UTC, começamos a enfileirar os envios da campanha assim que um fuso horário é identificado (como Samoa). Isso significa que estamos nos preparando para enviar a mensagem, não enviando a campanha. Se os usuários não corresponderem a nenhum filtro quando verificamos a elegibilidade, eles não farão parte do público-alvo.

Como outro exemplo, digamos que você queira criar duas campanhas programadas para enviar no mesmo dia — uma de manhã e uma à noite — e adicionar um filtro para que os usuários só possam receber a segunda campanha se já tiverem recebido a primeira. Com a entrega por fuso horário local, alguns usuários podem não receber a segunda campanha. Isso acontece porque verificamos a elegibilidade quando o fuso horário do usuário é identificado. Portanto, se o horário programado ainda não ocorreu no fuso horário dele, ele não recebeu a primeira campanha, o que significa que não será elegível para a segunda campanha.

Para uma visualização de como um usuário pode estar em um segmento durante a primeira verificação, mas não na segunda, veja esta linha do tempo:

![Linha do tempo de um usuário entrando no segmento antes da primeira verificação e saindo antes da segunda.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details Descrição da linha do tempo %}

1. O Usuário A entra no segmento às 6:59 PST (4:59 horário de Samoa).
2. A Braze verifica a associação ao segmento às 7h horário de Samoa para determinar quais usuários são elegíveis para receber a campanha nas próximas 24 horas. O Usuário A está no segmento neste momento.
3. O segmento tem uma janela de 24 horas, então o Usuário A sai do segmento 24 horas após ter entrado: 6:59 PST (4:59 horário de Samoa).
4. A campanha por horário local envia às 7h PST, mas o Usuário A já saiu do segmento.

{% enddetails %}

### Como programo uma campanha por fuso horário local?

Ao programar uma campanha, escolha enviá-la em um horário designado e selecione **Enviar campanha para os usuários no fuso horário local deles**.

A Braze recomenda fortemente que todas as campanhas por fuso horário local sejam programadas com 24 horas de antecedência. Como essa campanha precisa ser enviada ao longo de um dia inteiro, programá-la com 24 horas de antecedência garante que sua mensagem alcance todo o seu segmento. No entanto, você pode programar essas campanhas com menos de 24 horas de antecedência, se necessário. Tenha em mente que a Braze não enviará mensagens para usuários que perderam o horário de envio por mais de 1 hora.

Por exemplo, se são 13h e você programa uma campanha por fuso horário local para as 15h, a campanha enviará imediatamente para todos os usuários cujo horário local esteja entre 15h e 16h, mas não para usuários cujo horário local seja 17h. Além disso, o horário de envio que você escolher para sua campanha não pode ter passado no fuso horário da sua empresa.

Editar uma campanha por fuso horário local que está programada com menos de 24 horas de antecedência não alterará a programação da mensagem. Se você decidir editar uma campanha por fuso horário local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento-alvo quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar uma campanha por fuso horário local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada para todos os membros do segmento no horário original (17h).

{% alert note %}
Para componentes do Canvas, os usuários não precisam estar no componente por 24 horas para receber o próximo componente na jornada do usuário para entrega por fuso horário local.
{% endalert %}

Se você permitiu que os usuários se tornem reelegíveis para a campanha, eles a receberão novamente no horário original (17h). Para todas as ocorrências subsequentes da sua campanha, no entanto, suas mensagens serão enviadas apenas no horário atualizado.

### Quando as alterações em campanhas por fuso horário local entram em vigor?

Os segmentos-alvo para campanhas por fuso horário local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo para garantir a entrega a todo o segmento. Por exemplo, considere um segmento que direciona usuários no segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Usou o app pela primeira vez há menos de 2 dias

A entrega por fuso horário local pode não alcançar usuários neste segmento com base no horário de entrega e no fuso horário local dos usuários. Isso acontece porque um usuário pode sair do segmento no momento em que seu fuso horário aciona a entrega.

### Quais alterações posso fazer em campanhas programadas antes do lançamento?

Quando a campanha está programada, você deve fazer edições em qualquer coisa que não seja a composição da mensagem antes de enfileirarmos as mensagens para envio. Como em todas as campanhas, você não pode editar eventos de conversão após o lançamento.

### Atualizei minha campanha programada. Por que ela não foi lançada?

Isso pode acontecer quando uma campanha está programada para ser lançada no exato momento em que foi atualizada. Por exemplo, se são 15:10 e você alterou a campanha para ser lançada às 15:10 e selecionou **Atualizar campanha**, já passou das 15:10, o que significa que o horário programado para o lançamento já passou. Em vez de programar a campanha para o mesmo horário, selecione **Enviar assim que a campanha for lançada**.

### Qual é a "zona segura" antes que as mensagens de uma campanha programada sejam enfileiradas?

Recomendamos fazer alterações nas mensagens dentro dos seguintes prazos:

- **Campanhas programadas únicas:** Edite até o horário de envio programado.
- **Campanhas programadas recorrentes:** Edite até o horário de envio programado.
- **Campanhas por horário local:** Edite até 24 horas antes do horário de envio programado.
- **Campanhas com horário de envio ideal:** Edite até 24 horas antes do dia em que a campanha está programada para enviar.

Se você fizer alterações fora dessas recomendações, pode não ver as atualizações refletidas na mensagem enviada. Por exemplo, se você editar o horário de envio três horas antes de uma campanha programada para enviar às 12h no horário local, o seguinte pode ocorrer:

- A Braze não envia mensagens para usuários que perderam o horário de envio por mais de uma hora.
- Mensagens pré-enfileiradas ainda podem ser enviadas no horário originalmente enfileirado, em vez do horário ajustado.

Se você precisar fazer alterações, recomendamos parar a campanha atual (isso cancela quaisquer mensagens enfileiradas). Você pode então duplicar a campanha, fazer as alterações necessárias e lançar a nova campanha. Pode ser necessário excluir desta campanha os usuários que já receberam a primeira campanha. Certifique-se de reajustar os horários de programação da campanha para permitir o envio por fuso horário.

### Por que nenhum usuário entrou na minha campanha programada diária no dia da mudança de horário de verão?

Nos dias de transição do horário de verão (DST), campanhas programadas diárias podem ser executadas até uma hora antes ou depois do normal, dependendo se os relógios adiantam ou atrasam. Se o seu segmento depende de atributos personalizados ou eventos com timestamps que estão dentro de uma hora do horário de envio programado, esses usuários podem ainda não se qualificar quando a campanha avalia a elegibilidade no dia do DST.

Por exemplo, suponha que os usuários normalmente recebem uma atualização de atributo personalizado às 15h UTC, e sua campanha é executada diariamente às 10:30 em Nova York (Eastern Time). Enquanto Nova York está no horário padrão (UTC-5), 10:30 ET corresponde a 15:30 UTC, então a campanha é executada após o atributo ser registrado. Quando Nova York muda para o horário de verão (UTC-4), 10:30 ET corresponde a 14:30 UTC, então no dia da mudança para o horário de verão a campanha pode ser executada antes da atualização do atributo às 15h UTC. Como o atributo qualificador ainda não existe, esses usuários são filtrados. Se a reelegibilidade estiver desativada, os usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas para aquele dia.

Para evitar isso, garanta que as atualizações de atributos personalizados ou eventos ocorram mais de uma hora antes do horário de envio programado da campanha.

### Por que o número de usuários entrando em uma campanha não corresponde ao número esperado?

O número de usuários entrando em uma campanha pode diferir do número esperado devido à forma como públicos e gatilhos são avaliados. Na Braze, o público é avaliado antes do gatilho (a menos que se use um gatilho de [mudança de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam da campanha se não fizerem parte inicialmente do público selecionado antes que quaisquer ações de gatilho sejam avaliadas.

{% alert tip %}
Para assistência adicional com solução de problemas de campanhas, entre em contato com o suporte da Braze dentro de 30 dias da ocorrência do problema, pois temos apenas os últimos 30 dias de registros de diagnóstico.
{% endalert %}

### Qual é a diferença entre as opções Exportar dados de usuários em CSV e Exportar endereços de e-mail em CSV na página de análise de dados da minha campanha?

Selecionar a opção **Exportar endereços de e-mail em CSV** baixa dados apenas de usuários com endereços de e-mail. Por exemplo, se você tem um segmento de 100.000 usuários, mas apenas 50.000 deles possuem endereços de e-mail, e você clica em **Exportar endereços de e-mail em CSV**, a exportação conterá apenas 50.000 linhas de dados. Em comparação, selecionar **Exportar dados de usuários em CSV** exporta todos os dados de usuários.

### Posso pesquisar uma campanha pelo seu identificador de API?

Sim, use o filtro `api_id:YOUR_API_ID` na página **Campanhas** para pesquisar uma campanha pelo seu identificador de API. Consulte [pesquisando campanhas]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns/) para saber mais.

### Por que os espaços em branco aparecem de forma diferente em campos de entrada versus texto exibido?

O tratamento de espaços em branco difere entre campos de entrada e componentes de texto exibido por causa da estilização CSS. Em componentes de texto com o CSS padrão `white-space: normal`, múltiplos espaços consecutivos são colapsados em um único espaço quando exibidos. Este é o comportamento padrão do HTML para texto renderizado.

Campos de entrada preservam múltiplos espaços exatamente como você os digita, porque você precisa ver e editar o espaçamento exato para entrada de dados precisa. Isso significa que texto com múltiplos espaços pode aparecer de forma diferente quando visualizado em um campo de entrada (onde todos os espaços são preservados) versus quando exibido em outras partes do dashboard (onde o CSS pode colapsar múltiplos espaços).

Por exemplo, se você inserir um nome de campanha ou parâmetro UTM com múltiplos espaços em um campo de entrada, verá todos os espaços preservados. No entanto, quando esse mesmo texto aparece em resultados de pesquisa, listas de campanhas ou outros componentes de texto, múltiplos espaços podem aparecer como um único espaço por causa do tratamento de espaços em branco do CSS.

### Qual é a diferença entre campanhas da API e campanhas disparadas por API?

Campanhas disparadas por API permitem que você gerencie o texto da campanha, testes multivariantes e regras de reelegibilidade dentro do dashboard da Braze enquanto aciona a entrega desse conteúdo a partir dos seus próprios servidores e sistemas. Essas mensagens também podem incluir dados adicionais para serem modelados nas mensagens em tempo real.

Campanhas da API são usadas para rastrear as mensagens enviadas usando a API. Diferentemente da maioria das campanhas, você não especifica a mensagem, os destinatários ou a programação, mas sim passa os identificadores nas suas chamadas de API.

### Qual é a diferença entre campanhas baseadas em ação e campanhas disparadas por API?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Baseadas em ação

Campanhas de entrega baseada em ação ou campanhas disparadas por evento são muito eficazes para mensagens transacionais ou baseadas em conquistas e permitem que você as acione para enviar após um usuário completar um determinado evento.

| Prós | Contras |
| ---- | ---- |
| • Visibilidade das cargas úteis JSON recebidas na plataforma (se o evento for disparado por um usuário teste) através do **Registro de atividades de envio de mensagem**<br><br>• Elementos de personalização são incluídos nas propriedades do evento personalizado<br><br>• O evento personalizado pode ser usado para criar segmentos de usuários elegíveis para a mensagem | • Consome pontos de dados |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Disparadas por API

Campanhas disparadas por API e disparadas por servidor são ideais para lidar com transações mais avançadas, permitindo que você acione a entrega do conteúdo da campanha a partir dos seus próprios servidores e sistemas. A requisição de API para acionar a mensagem também pode incluir dados adicionais para serem modelados na mensagem em tempo real.

| Benefícios | Considerações |
| ---- | ---- |
| • Não registra pontos de dados<br><br>• Elementos de personalização são incluídos nas propriedades da carga útil JSON | • Não permite criar um segmento de usuários elegíveis para a mensagem nas propriedades da carga útil JSON<br><br>• Não é possível ver as cargas úteis JSON recebidas com o **Registro de atividades de envio de mensagem** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### O que devo incluir ao enviar um ticket de suporte para um erro "Request Timed Out"?

Se você encontrar um erro "Request Timed Out" ao criar ou editar uma campanha ou Canvas e precisar entrar em contato com o [suporte da Braze]({{site.baseurl}}/braze_support/), inclua as seguintes informações para ajudar a acelerar a resolução:

- **Gravação de tela:** Uma gravação dos passos que você seguiu antes de ver o erro, incluindo quaisquer transições de página.
- **Timestamp e fuso horário:** O horário exato em que o erro ocorreu e seu fuso horário.
- **Navegador e versão:** O navegador que você está usando (por exemplo, Chrome 120, Safari 17) e se você tentou reproduzir o erro em um navegador diferente.
- **Passos para reproduzir:** Uma descrição clara das ações que acionam o erro, incluindo quaisquer configurações específicas de campanha ou Canvas envolvidas.
- **Registros de rede (opcional):** Abra as ferramentas de desenvolvedor do seu navegador (guia **Network**), reproduza o erro e exporte o registro de rede como um arquivo HAR (HTTP Archive). Isso ajuda a equipe de suporte a identificar qual chamada de API está expirando.

### Por que minha análise de dados de envio não corresponde ao limite máximo de destinatários que defini?

Se você adicionar ou alterar um limite máximo de destinatários em uma campanha ativa, o limite pode não ser refletido na sua análise de dados de envio pelos seguintes motivos:

- **Limite adicionado após o lançamento:** Se o limite máximo de destinatários não estiver definido quando a campanha for lançada, as mensagens que já estão enfileiradas antes de você aplicar o limite ainda serão enviadas. O limite só entra em vigor para envios que você enfileirar após salvar a alteração.
- **Interação com limite de taxa:** Se uma campanha também tem limite de taxa, as mensagens podem ser distribuídas ao longo de uma janela de tempo mais longa. O limite máximo de destinatários é avaliado quando as mensagens são enfileiradas, não quando são entregues. Se o limite for alterado enquanto as mensagens já estão na fila, o limite original se aplica a essas mensagens.
- **Campanhas recorrentes:** Para campanhas recorrentes, cada envio programado avalia o limite máximo de destinatários de forma independente. Alterar o limite entre envios não ajusta retroativamente as contagens de envios anteriores.

Para evitar desalinhamentos, defina o limite máximo de destinatários antes de lançar a campanha e evite modificá-lo enquanto os envios estiverem em andamento.

### Por que os envios são menores do que o tamanho estimado do público?

Vários fatores podem fazer com que o número de envios seja menor do que o tamanho estimado do público:

- **Reavaliação do segmento:** Para campanhas baseadas em ação ou programadas que reavaliam no momento do envio, os usuários que estavam no segmento quando a campanha foi enfileirada podem não se qualificar mais quando a mensagem é realmente enviada.
- **Grupos de controle:** Se um [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group/) ou grupo de controle no nível da campanha estiver em uso, uma parte do público é retida da entrega.
- **Horário e janelas de entrega:** Para campanhas por fuso horário local ou programadas, os usuários devem se qualificar tanto na entrada quanto no momento do envio; usuários em determinados fusos horários podem ficar fora da janela de entrega.
- **Limite de taxa:** Se o limite de taxa estiver aplicado, as mensagens são distribuídas ao longo do tempo e alguns envios podem ser adiados ou ainda não refletidos na contagem.
- **Filtros de entregabilidade de e-mail:** Para campanhas de e-mail, a Braze exclui usuários que tiveram hard bounce, cancelaram a inscrição de e-mails, foram marcados como spam, não possuem endereço de e-mail no perfil ou não estão inscritos em um grupo de inscrições obrigatório. Essas verificações são executadas no momento do envio, então um usuário presente no seu segmento ainda pode ser excluído da contagem real de envios.