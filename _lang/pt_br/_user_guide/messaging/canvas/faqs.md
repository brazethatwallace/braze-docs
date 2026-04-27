---
nav_title: FAQ
article_title: FAQ do Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Este artigo fornece respostas para perguntas frequentes sobre o Canvas."
tool: Canvas
toc_headers: h2 

---

# Perguntas frequentes

> Este artigo fornece respostas para algumas perguntas frequentes sobre o Canvas.

## Criação e edição de Canvas

### Quantas etapas posso incluir em um Canvas?

Você pode adicionar até 200 etapas em um Canvas.

### Qual é a diferença entre um componente e uma etapa?

Um [componente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) é uma parte individual do seu Canvas que você pode usar para determinar a eficácia do seu Canvas. Os componentes podem incluir ações como dividir a jornada do usuário, adicionar uma postergação e até testar múltiplas jornadas do Canvas. Uma etapa no Canvas se refere à jornada personalizada do usuário nos ramos do seu Canvas. Essencialmente, seu Canvas é composto por componentes individuais que criam etapas para a jornada do usuário.

### Posso lançar um Canvas com etapas desconectadas?

Sim. Você também pode salvar Canvas após o lançamento com etapas desconectadas. 

### Para onde os usuários vão quando chegam a uma etapa desconectada?

Se um usuário estiver em uma etapa desconectada do fluxo de trabalho do Canvas, ele avançará para a etapa seguinte, se houver uma, e a configuração da etapa determinará como o usuário deve avançar. Isso permite que você faça alterações nas etapas sem precisar conectá-las diretamente ao restante do Canvas. Também oferece espaço para testes antes de publicar imediatamente, permitindo salvar um rascunho.

Recomendamos verificar a visualização de análise de dados para usuários pendentes em uma etapa do Canvas antes de desconectar uma etapa.

### O que acontece se o público e o horário de envio forem idênticos para um Canvas que tem uma variante, mas múltiplos ramos?

Enfileiramos um trabalho para cada etapa — eles são executados aproximadamente ao mesmo tempo, e um deles "vence". Na prática, isso pode ser distribuído de forma relativamente uniforme, mas é provável que haja pelo menos uma leve tendência para a etapa que foi criada primeiro. 

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser uma divisão uniforme, adicione um filtro de [Número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/).

### Como os públicos do Canvas são avaliados?

Por padrão, filtros e segmentos para etapas completas no Canvas são verificados no momento do envio. A etapa de Divisão de decisão realiza uma avaliação logo após receber uma etapa anterior (ou antes de uma postergação).

### Quando um evento de exceção é disparado?

Os eventos de exceção só são disparados enquanto o usuário está aguardando para receber o componente do Canvas ao qual está associado. Se um usuário realizar uma ação antecipadamente, o evento de exceção não será disparado. Se você quiser excluir usuários que já realizaram um determinado evento, use [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

### Como a edição de um Canvas afeta os usuários que já estão no Canvas?

Se você editar algumas etapas de um Canvas com múltiplas etapas, os usuários que já estavam no público, mas ainda não receberam as etapas, receberão a versão atualizada da mensagem. Isso só acontecerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que você pode editar após o lançamento, consulte [Alterando seu Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

### O que acontece quando você para um Canvas?

Quando você para um Canvas, o seguinte se aplica:

- Os usuários serão impedidos de entrar no Canvas.
- Nenhuma mensagem adicional será enviada, independentemente de onde o usuário esteja no fluxo.
- **Exceção:** Canvas com e-mails não serão interrompidos imediatamente. Depois que as solicitações de envio são enviadas ao SendGrid, não há nada que possamos fazer para impedir que sejam entregues ao usuário.

### Devo criar um único Canvas ou Canvas separados por ciclo de vida do usuário?

Dependendo do que você deseja alcançar com seu Canvas, pode ser necessário adotar abordagens diferentes na construção da jornada do usuário. A flexibilidade do Canvas permite mapear jornadas de usuários para qualquer estágio do ciclo de vida. Confira nossos [modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para vários exemplos de abordagens simplificadas para criar jornadas de usuários eficazes.

## Mensagens e entrega

### Quando as mensagens no app do Canvas são enviadas?

As mensagens no app são enviadas no próximo início de sessão. Isso significa que, se o usuário entrar na etapa do Canvas antes de o Canvas ser parado, ele ainda receberá a mensagem no app no próximo início de sessão, desde que a mensagem no app ainda não tenha expirado.

É possível que um usuário inicie uma sessão antes de o Canvas ser parado, mas não veja a mensagem no app imediatamente. Isso pode ocorrer se a mensagem no app for disparada por um evento personalizado ou estiver com postergação. Portanto, é possível que um usuário registre uma impressão de mensagem no app e "receba" a mensagem no app após o Canvas ser parado. No entanto, o usuário precisaria ter iniciado a sessão antes de o Canvas ser parado, mas **depois** de ter recebido a etapa do Canvas.

{% alert note %}
Parar um Canvas não fará com que os usuários que estão aguardando para receber mensagens saiam da jornada do usuário. Se você reativar o Canvas e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o horário em que a mensagem deveria ter sido enviada já tenha passado — nesse caso, eles não a receberão).
{% endalert %}

### Por que um Canvas pode mostrar zero envios mesmo com impressões registradas?

Se _Mensagens enviadas_ for sempre zero para um Canvas contendo uma etapa de mensagem no app, isso ocorre porque a entrega de mensagens no app funciona de forma diferente dos outros canais de envio de mensagens.

As mensagens no app são "puxadas" pelo SDK, em vez de "empurradas" pela Braze. As mensagens no app para usuários elegíveis são entregues automaticamente no início da sessão e "aguardam" o evento de gatilho antes de serem exibidas. Como os usuários elegíveis recebem a mensagem quando iniciam uma sessão, a Braze não registra isso como um evento de envio. Quando os usuários realizam o evento de gatilho, a mensagem é exibida e a Braze registra uma impressão e marca a etapa do Canvas (ou campanha) como recebida no perfil do usuário. Consequentemente, o total de _Envios_ será zero para mensagens no app.

### Posso programar horários de envio diferentes para cada variante na mesma etapa de Mensagem do Canvas ou envio multivariante?

Não. As variantes na mesma configuração multivariante ou etapa de Mensagem compartilham uma única programação de entrega. Não é possível atribuir uma variante para enviar às 18h e outra às 19h para o mesmo envio programado.

Para escalonar envios ou usar horários diferentes por jornada, tente os seguintes métodos:

- Etapas de Mensagem separadas com etapas de Postergação entre elas, para que cada mensagem tenha sua própria programação.
- Ramos ou uma etapa de [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) para que os usuários sigam jornadas com diferentes horários.
- Campanhas separadas se o caso de uso não precisar permanecer dentro de um único Canvas.

Para conceitos de testes multivariantes e Testes A/B em campanhas, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

## Análise de dados e conversões

### Como as conversões de usuários são rastreadas em um Canvas?

Um usuário só pode converter uma vez por entrada no Canvas. As conversões são atribuídas à mensagem mais recente recebida pelo usuário naquela entrada. O bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários naquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto aquela era a etapa mais recente que o usuário recebeu.

{% alert note %}
Quando um usuário reentra em um Canvas, os eventos de conversão são rastreados apenas para a entrada mais recente. Os eventos de conversão não são registrados para entradas anteriores, mesmo que o evento de conversão seja preenchido retroativamente.
{% endalert %}

{% details Expandir para exemplos %}

**Exemplo 1**

Há uma jornada de Canvas com 10 notificações por push e o evento de conversão é "início de sessão" ("Abre o app"):

- O Usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O Usuário B abre o app após cada notificação por push.

**Resultado:** O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e zero em todas as etapas subsequentes.

{% alert note %}
Se o horário de silêncio estiver ativo quando o evento de conversão acontecer, as mesmas regras se aplicam.
{% endalert %}

**Exemplo 2**

Há um Canvas de uma única etapa com horário de silêncio ativado:

1. O usuário entra no Canvas.
2. A primeira etapa não tem postergação, mas está dentro do horário de silêncio configurado, então a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:** O usuário será contado como convertido na variante geral do Canvas, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

### Qual é a diferença entre os diferentes tipos de taxa de conversão?

- O total de conversões do Canvas reflete quantos usuários únicos completaram um evento de conversão, não quantas conversões cada um completou. 
- A taxa de conversão da variante ou o bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários naquela jornada, independentemente de terem recebido uma mensagem, como um total agregado. 
- A taxa de conversão da etapa reflete quantos indivíduos receberam aquela etapa de mensagem e completaram qualquer um dos eventos de conversão definidos.

### Por que a taxa de conversão da minha etapa do Canvas não é igual à taxa de conversão total da variante do Canvas?

É comum que o total de conversões de uma variante do Canvas seja maior que a soma dos totais de suas etapas. Isso ocorre porque um usuário pode realizar um evento de conversão para uma variante assim que entra nela. No entanto, esse mesmo evento de conversão não conta para uma etapa do Canvas. Portanto, qualquer usuário que entre no Canvas e realize o evento de conversão antes de receber a primeira etapa do Canvas será contado no total de conversões da variante, mas não no total da etapa. O mesmo vale para um usuário que entra no Canvas, mas sai antes de receber qualquer etapa.

### Como posso visualizar a análise de dados de cada um dos meus componentes do Canvas?

Para visualizar a análise de dados de um componente do Canvas, acesse seu Canvas e role para baixo na página **Detalhes do Canvas**. Aqui, você pode visualizar a análise de dados de cada componente. Confira [Análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para mais detalhes.

### Ao analisar o número de usuários únicos, a análise de dados do Canvas ou o segmentador é mais preciso?

O segmentador é uma estatística mais precisa para dados de usuários únicos em comparação com as estatísticas do Canvas ou da campanha. Isso ocorre porque as estatísticas do Canvas e da campanha são números que a Braze incrementa quando algo acontece — o que significa que existem variáveis que podem fazer com que esse número seja diferente do segmentador. Por exemplo, os usuários podem converter mais de uma vez para um Canvas ou campanha.

### Por que o número de usuários que entram em um Canvas não corresponde ao número esperado?

O número de usuários que entram em um Canvas pode diferir do número esperado devido à forma como os públicos e gatilhos são avaliados. Na Braze, o público é avaliado antes do gatilho (a menos que se use um gatilho de [mudança de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam do Canvas se não fizerem parte do público selecionado antes que quaisquer ações-gatilho sejam avaliadas.

### O que acontece com usuários anônimos durante sua jornada no Canvas?

Embora usuários anônimos possam entrar e sair de Canvas, suas ações não são associadas a um perfil de usuário específico até que sejam identificados, então suas interações podem não ser totalmente rastreadas na sua análise de dados. Você pode usar o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) para gerar um relatório dessas métricas.

{% alert tip %}
Para assistência adicional com solução de problemas do Canvas, entre em contato com o suporte da Braze dentro de 30 dias da ocorrência do problema, pois temos apenas os últimos 30 dias de registros de diagnóstico.
{% endalert %}

## Segmentação

### Qual é a diferença entre "Não entrou na variação do Canvas" e "Não está no grupo de controle do Canvas"?

Consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) para as definições completas dos filtros.

#### Não entrou na variação do Canvas

O usuário nunca entrou em uma jornada de variação de um Canvas específico. Todos os usuários que não estão no grupo de controle são incluídos, independentemente de terem entrado no Canvas. Isso inclui usuários que entraram em outra variação e usuários que não entraram em nenhuma variação. 

#### Não está no grupo de controle do Canvas

O usuário entrou no Canvas, mas não está no grupo de controle e, consequentemente, recebeu uma variação. Isso inclui apenas usuários que entraram no Canvas.

Observe que a atribuição de variação ocorre na entrada do Canvas. Se um usuário não entrou em um Canvas, ele não será atribuído a nenhuma variante. Em outras palavras, ele não estará no grupo de controle nem em uma variante.

## Editor original do Canvas

{% details Expandir para FAQs do editor original do Canvas %}

### Como converto um Canvas existente do editor original para o editor atual?

Você pode [clonar seu Canvas]({{site.baseurl}}/cloning_canvases/). Isso cria uma cópia do seu Canvas original no fluxo de trabalho mais atual do Canvas.

### Quais são as principais diferenças entre os editores atual e original do Canvas?

#### Barra de ferramentas de componentes do Canvas

Anteriormente, com o editor original do Canvas, uma etapa completa era adicionada por padrão sempre que você criava qualquer etapa na jornada do usuário. Essas etapas completas foram substituídas por diferentes componentes do Canvas, o que oferece o benefício de maior visibilidade e personalização para sua experiência de edição. Você pode ver imediatamente todos os seus componentes do Canvas na Barra de Ferramentas de Etapas do Canvas.

#### Comportamento das etapas

Anteriormente, cada etapa completa incluía informações como configurações de postergação e programação, eventos de exceção, filtros de público, configuração de mensagem e opções de avanço de mensagem, tudo em um único componente. Essas são configurações separadas no editor atual para tornar sua experiência de criação de Canvas mais personalizável e introduz algumas diferenças na funcionalidade.

#### Avanço do componente de Mensagem

Os [componentes de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) avançam todos os usuários que entram na etapa. Não há necessidade de especificar o comportamento de avanço da mensagem, tornando a configuração da etapa geral mais simples. Se você quiser implementar a opção **Avançar quando a mensagem for enviada**, adicione uma Jornada do público separada para filtrar os usuários que não receberam a etapa anterior.  

#### Comportamento "em" da Postergação

Os [componentes de Postergação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/) aguardarão todo o tempo de postergação antes de prosseguir para a próxima etapa. 

Digamos que em 12 de abril temos um componente de Postergação configurado para enviar o usuário para a próxima etapa em um dia às 14h. Um usuário entra no componente às 14h01 em 13 de abril. 
- No fluxo de trabalho original, o usuário avançaria para a próxima etapa às 14h de 14 de abril, o que é menos de um dia a partir do horário de entrada. 
- No editor atual, o usuário avançaria para a próxima etapa às 14h de 15 de abril. Observe que é o mesmo horário, mas mais de um dia a partir do horário de entrada. 

#### Comportamento do Intelligent Timing

Como o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) está armazenado no componente de Mensagem, as postergações serão aplicadas antes dos cálculos do Intelligent Timing. Isso significa que, dependendo de quando um usuário entra no componente, ele pode receber a mensagem mais tarde do que receberia em um Canvas construído com o fluxo de trabalho original do Canvas.

Digamos que sua postergação está configurada para 2 dias, o Intelligent Timing está ativado e determinou que o melhor horário para enviar sua mensagem é às 14h. Um usuário entra na etapa de Postergação às 14h01.
- **Fluxo de trabalho atual:** Levará 48 horas para a postergação passar, então o usuário recebe a mensagem no terceiro dia às 14h.
- **Fluxo de trabalho original:** O usuário recebe a mensagem no segundo dia às 14h.

Observe que, se o Intelligent Timing estiver ativado, a mensagem será enviada dentro de 24 horas após o usuário entrar no componente de Mensagem, no horário inteligente identificado (mesmo que nenhum componente de Postergação esteja envolvido).

#### Eventos de exceção

##### Horário de silêncio

O evento de exceção é aplicado usando Jornadas de ação, que são separadas das etapas de Mensagem. O horário de silêncio é aplicado no componente de Mensagem. Isso significa que, se um usuário já passou pela Jornada de ação (e não foi excluído pelo evento de exceção), depois encontra o horário de silêncio ao chegar ao componente de Mensagem, e o Canvas foi configurado para reenviar a mensagem após o período de horário de silêncio, o evento de exceção não será mais aplicado. Observe que esse caso de uso não é comum.

Para segmentos e filtros, a etapa de Mensagem possui validações de entrega que permitem aos usuários configurar segmentos e filtros adicionais que são validados no momento do envio. Isso evita o caso extremo mencionado do horário de silêncio.

##### Configuração de programação "em" ou "no próximo"

Os eventos de exceção são criados usando Jornadas de ação. As Jornadas de ação suportam apenas "após uma janela de tempo X" e não "em X tempo" ou "no próximo X tempo".

{% enddetails %}

### O que devo incluir ao enviar um ticket de suporte para um erro "Request Timed Out"?

Se você encontrar um erro "Request Timed Out" ao editar um Canvas e precisar entrar em contato com o [suporte da Braze]({{site.baseurl}}/braze_support/), inclua as seguintes informações para ajudar a acelerar a resolução:

- **Gravação de tela:** Uma gravação das etapas que você realizou antes de ver o erro, incluindo quaisquer transições de página.
- **Carimbo de data/hora e fuso horário:** O horário exato em que o erro ocorreu e seu fuso horário.
- **Navegador e versão:** O navegador que você está usando (por exemplo, Chrome 120, Safari 17) e se você tentou reproduzir o erro em um navegador diferente.
- **Etapas para reproduzir:** Uma descrição clara das ações que disparam o erro, incluindo quaisquer etapas ou configurações específicas do Canvas envolvidas.
- **Registros de rede (opcional):** Abra as ferramentas de desenvolvedor do seu navegador (guia **Network**), reproduza o erro e exporte o registro de rede como um arquivo de registro HTTP Archive (HAR). Isso ajuda a equipe de suporte a identificar qual chamada de API está expirando.