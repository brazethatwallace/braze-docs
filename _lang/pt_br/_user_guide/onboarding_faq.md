---
article_title: Perguntas frequentes
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Esta página contém uma coleção de perguntas frequentes, organizadas por categoria."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Como eu lido com dados de usuários anônimos? {#how-do-i-handle-anonymous-user-data}

{% apitags %}
Users
{% endapitags %}

Inicialmente, quando um perfil de usuário é reconhecido via SDK, a Braze cria um perfil de usuário anônimo com um `braze_id` associado: um identificador de usuário único definido pela Braze.

Para acompanhar melhor os usuários anônimos, você pode implementar [aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases), que permitem marcar usuários anônimos com um identificador. Esses usuários podem então ser exportados usando seus aliases ou referenciados pela API.

Se um perfil de usuário anônimo com um alias for posteriormente reconhecido com um `external_id`, ele será tratado como um perfil de usuário identificado normal, mas manterá seu alias existente e ainda poderá ser referenciado por esse alias.

Para usuários de alias que você deseja mesclar com usuários identificados, você pode mesclar quaisquer campos pertinentes ao perfil real que deseja manter. Você precisaria exportar esses dados antes de excluí-los do perfil de alias usando nosso [endpoint Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Em seguida, você pode usar nosso [endpoint de rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para publicar esses eventos no perfil que você manteve. Isso preservará quaisquer dados que você queira manter, como atributos que foram previamente registrados em um perfil, mas não no outro.

Para uma análise completa dos diferentes métodos de coleta de dados de usuários novos e existentes na Braze, confira as [melhores práticas de coleta de dados]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices).

{% endapi %}
{% api %}

### Como posso importar usuários que já coletei e identifiquei fora da Braze? {#how-can-i-import-users-i-have-already-collected-and-identified-outside-of-braze}

{% apitags %}
Users
{% endapitags %}

Para importar usuários previamente identificados, você pode fazer upload de um CSV para a Braze ou enviar dados pela API.

#### CSV

Você pode fazer upload e atualizar perfis de usuários via arquivos CSV em **Público** > **Importar usuários**. Ao importar seus dados de cliente, você precisará especificar o identificador único de cada cliente, também conhecido como `external_id`.

Antes de iniciar sua importação de CSV, é importante entender com sua equipe de engenharia como os usuários serão identificados na Braze. Normalmente, isso seria um ID de banco de dados usado internamente. Isso deve estar alinhado com a forma como os usuários serão identificados pelo SDK da Braze em dispositivos móveis e web, para que cada cliente tenha um único perfil de usuário na Braze em todos os seus dispositivos. Saiba mais sobre o [ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) da Braze.

Quando você fornece um `external_id` na sua importação, a Braze atualizará qualquer usuário existente com o mesmo `external_id` ou criará um novo usuário identificado com esse `external_id` definido, caso nenhum seja encontrado.

Para saber mais e baixar modelos de importação de CSV, consulte [importação de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

#### API

Para fazer upload de usuários via API, você pode usar nosso [endpoint de rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para importá-los para a Braze.

Se você não tiver certeza se o usuário já existe na Braze, pode implementar nosso [endpoint Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para verificar. Se você identificar que o usuário já existe na Braze, pode usar nosso endpoint `/users/track` para publicar os novos dados que deseja adicionar ao perfil de usuário já existente na Braze.

{% alert note %}
Tenha em mente as seguintes nuances ao usar o endpoint `/users/track`:

- Ao criar usuários apenas com alias por meio desse endpoint, você deve definir explicitamente a flag `_update_existing_only` como false.
- Atualizar o status da inscrição com esse endpoint atualizará tanto o usuário especificado pelo seu ID externo (como Usuário1) quanto o status da inscrição de qualquer usuário com o mesmo e-mail que esse usuário (Usuário1).
{% endalert %}

{% endapi %}
{% api %}

### Qual é a diferença entre os status de inscrição push? {#whats-the-difference-between-the-push-subscription-statuses}

{% apitags %}
Users
{% endapitags %}

Existem três opções de estado de inscrição push: inscrito, aceitou e cancelou inscrição.

Por padrão, para que seu usuário receba suas mensagens por push, o estado de inscrição push dele deve ser inscrito ou aceitou, e ele deve estar habilitado para push. Você pode substituir essa configuração, se necessário, ao redigir uma mensagem.

| Estado de aceitação | Descrição |
|---|---|
| Subscribed | Estado de inscrição push padrão quando um perfil de usuário é criado na Braze. |
| Opted-In | Um usuário expressou explicitamente a preferência por receber notificações por push. A Braze moverá automaticamente o estado de aceitação do usuário para `Opted-In` se ele aceitar um prompt de push no nível do sistema operacional.<br><br>Isso não se aplica a usuários no Android 12 ou inferior. |
| Unsubscribed | Um usuário cancelou explicitamente a inscrição de push pelo seu aplicativo ou outros métodos fornecidos pela sua marca. Por padrão, as Campaigns de push da Braze direcionam apenas os usuários que são `Subscribed` ou `Opted-in` para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Qual é a diferença entre os status de inscrição push?" }

{% endapi %}
{% api %}

### E se eu identifiquei usuários duplicados? {#what-if-ive-identified-duplicated-users}

{% apitags %}
Users
{% endapitags %}

Se você identificou usuários duplicados, será necessário limpar esses perfis de usuário. Você pode fazer isso através das seguintes etapas:

1. Exporte os perfis de usuário usando nosso endpoint `/users/export/ids`.
2. Identifique o perfil de usuário correto (em última análise, sua equipe precisará decidir sobre as informações corretas) e então:
    - Mescle quaisquer campos pertinentes ao perfil real que deseja manter usando o endpoint `/user/track`.
    - Exclua o perfil duplicado e não útil sem mesclar nenhum dado usando o endpoint users/delete. Depois de excluir um perfil de usuário, **não há como recuperar as informações**.

{% alert important %}
Recomendamos que você primeiro importe os novos perfis de usuário com o `external_id` correto e os atributos e eventos personalizados correspondentes. Depois que os perfis de usuário são excluídos, eles não podem ser recuperados, então a exclusão deve ser a última etapa.
{% endalert %}

Alguns pontos adicionais a observar:

- Qualquer dado de engajamento (como Campaigns ou Canvas recebidos) em perfis de usuário duplicados será perdido. A única maneira de reter o contexto histórico de engajamento é adicioná-lo como um atributo personalizado (como um atributo personalizado de array de todas as Campaigns ou Canvas recebidos).
- Ao migrar perfis de usuário, também cabe à sua equipe decidir qual perfil de usuário dos duplicados será mantido. A Braze não pode decidir ou fornecer uma lista de perfis para excluir.
- Em última análise, será importante para sua equipe avaliar o processo de cadastro a partir da experiência dos seus usuários e garantir que você esteja chamando o método `changeUser()` apenas quando um usuário se tornar identificado.

{% endapi %}
{% api %}

<!-- Segments -->

### Como crio um Segment quando importo um grupo de usuários por CSV? {#how-do-i-create-a-segment-when-i-import-a-group-of-users-through-csv}

{% apitags %}
Segments
{% endapitags %}

Para importar seu arquivo CSV, navegue até a página **Importação de usuários** na seção Usuários. A tabela **Importações recentes** lista até vinte das suas importações mais recentes, seus nomes de arquivo, número de linhas no arquivo, número de linhas importadas com sucesso, total de linhas em cada arquivo e o status de cada importação.

O painel **Importar CSV** contém instruções de importação e um botão para iniciar sua importação. Clique em **Selecionar arquivo CSV** e selecione seu arquivo de interesse. Em seguida, antes de clicar em **Iniciar importação**, você tem a opção de informar à Braze o que fazer com esta lista em "O que você quer que façamos com os usuários neste CSV".

Selecione **Importar usuários neste CSV e também possibilitar redirecionar este lote específico de usuários como um grupo**, e então selecione **Gerar automaticamente um Segment dos usuários que são importados deste CSV**. Depois que você clicar em **Iniciar importação**, a Braze fará upload do seu arquivo, verificará os cabeçalhos das colunas e os tipos de dados de cada coluna, e criará um Segment.

Para baixar um modelo de CSV, consulte [importação de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv).

{% endapi %}
{% api %}

### Quais tipos de filtros posso usar ao criar um Segment? {#what-types-of-filters-can-i-use-when-creating-a-segment}

{% apitags %}
Segments
{% endapitags %}

O SDK da Braze fornece um arsenal poderoso de filtros para segmentar e direcionar seus usuários com base em recursos e atributos específicos. Você pode usar o glossário de [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para pesquisar ou restringir esses filtros por Categoria de Filtro (Dados personalizados, Atividade do usuário, Redirecionamento, Atividade de marketing, Atributos do usuário, Atribuição da instalação, Atividade social, Testes, Outros).

{% endapi %}
{% api %}

### Como configuro o direcionamento por local para segmentar os usuários pelo local mais recente e usá-lo em minhas campanhas e estratégias baseadas em localização? {#how-do-i-set-up-location-targeting-so-that-i-can-segment-users-by-their-most-recent-location-and-use-it-in-my-location-based-campaigns-and-strategies}

{% apitags %}
Segments
{% endapitags %}

Navegue até a página **Segments**, em Engajamento, para ver todos os seus segmentos de usuários atuais. Nesta página, você pode criar e nomear novos segmentos. Para começar, clique em **Criar Segment** e dê um nome ao seu Segment.

Depois de criar seu Segment, adicione um filtro `Most Recent Location` para segmentar os usuários pelo último lugar em que usaram seu app. Você pode destacar usuários em uma região circular padrão ou criar uma região poligonal personalizada.

- Para regiões circulares, você pode mover a origem e ajustar o raio de localização para sua segmentação.
- Para regiões poligonais, você pode designar mais especificamente quais áreas deseja incluir em seu Segment.

{% alert tip %}
Quer aproveitar o direcionamento por local com a ajuda de um parceiro da Braze? Confira nossos [parceiros de localização contextual]({{site.baseurl}}/partners/message_personalization) disponíveis.
{% endalert %}

{% endapi %}
{% api %}

### Como posso segmentar listas precisas de usuários com base em seus eventos personalizados e comportamento de compra nos últimos 365 dias? {#how-can-i-target-precise-lists-of-users-based-on-their-custom-event-and-purchase-behavior-in-the-past-365-days}

{% apitags %}
Segments
{% endapitags %}

Você pode usar [extensões de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension)! As extensões de Segment permitem que você segmente uma lista mais precisa de usuários do que seria possível com um Segment regular.

Você pode criar até 10 extensões de Segment por espaço de trabalho. Depois que essas listas de extensões são geradas, elas podem ser incluídas ou excluídas como um filtro em seus segmentos. Ao criar uma extensão de Segment, você também pode especificar que a lista seja regenerada uma vez a cada 24 horas.

1. Em Engajamentos, expanda **Segments** e clique em **Extensão de Segment**.
2. Na tabela de extensões de Segment, clique em **+ Criar nova extensão**.
3. Nomeie sua extensão de Segment descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente encontrada ao aplicá-la como um filtro em seu Segment.
4. Selecione entre um critério de compra ou evento personalizado para direcionamento.
5. Escolha qual item comprado ou evento personalizado específico você gostaria de direcionar para sua lista de usuários.
6. Escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter completado o evento, e quantos dias retroceder, até 365 dias.

Para aumentar a precisão do direcionamento, você pode selecionar **Adicionar filtros de propriedade** e segmentar com base nas propriedades específicas da sua compra ou evento personalizado. A Braze suporta segmentação de propriedades de eventos com base em string, numéricos, booleanos e objetos de tempo.

Também suportamos segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

As extensões de Segment dependem do armazenamento de longo prazo das propriedades de eventos e não têm o limite de armazenamento de propriedades de eventos personalizados de 30 dias. Isso significa que você pode consultar propriedades de eventos rastreadas no último ano, e o rastreamento não espera até que a extensão tenha sido configurada primeiro.

{% alert note %}
O uso de propriedades de eventos dentro de extensões de Segment não impacta o uso de pontos de dados.
{% endalert %}

{% endapi %}
{% api %}

#### Manter as extensões de Segment atualizadas {#keeping-segment-extensions-up-to-date}

{% apitags %}
Segments
{% endapitags %}

Você pode especificar se deseja que esta extensão represente um momento específico no tempo ou se deseja que ela seja regenerada diariamente. Sua extensão sempre começará a ser processada após o salvamento inicial. Se você quiser que a extensão seja regenerada diariamente, selecione **Regenerar extensão diariamente** e a regeneração começará a ser processada por volta da meia-noite de cada dia no fuso horário da sua empresa.

Quando terminar, clique em **Salvar**. Sua extensão começará a ser processada. O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias está consultando no histórico.

Por fim, depois de criar uma extensão, você pode usá-la como um filtro ao criar um Segment ou definir um público para uma Campaign ou Canvas. Comece escolhendo `Braze Segment Extension` na lista de filtros na seção **User Attributes**. Na lista de filtros de Braze Segment Extension, escolha a extensão que deseja incluir ou excluir neste Segment. Para ver os critérios da extensão, clique em **Ver detalhes da extensão**. Agora você pode continuar normalmente criando seu Segment.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Como você cria uma Campaign multicanal? {#how-do-you-create-a-multichannel-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Consulte [Campaigns multicanal]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign) em **Criar uma Campaign** para ver as etapas de configuração, canais suportados e como alternar entre criadores.

{% endapi %}
{% api %}

### Quais são algumas maneiras de começar a testar e otimizar Campaigns? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

{% apitags %}
Campaigns
{% endapitags %}

Criar Campaigns multivariantes e executar Canvas com várias variantes é uma ótima maneira de começar! Por exemplo, você pode executar uma [Campaign multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing) para testar uma mensagem com diferentes textos ou linhas de assunto. Canvas com várias variantes são úteis para testar fluxos de trabalho inteiros.

{% endapi %}
{% api %}

### Por que há uma diferença entre o número de destinatários únicos e o número de envios para uma determinada Campaign ou Canvas? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

{% apitags %}
Campaigns
{% endapitags %}

Uma possível explicação para essa diferença pode ser a Campaign ou Canvas ter a re-elegibilidade ativada. Com isso ativado, os usuários que se qualificarem para o Segment e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a re-elegibilidade não estiver ativada, a provável explicação para a diferença entre envios e destinatários únicos pode ser que os usuários possuem vários dispositivos em diferentes plataformas associados aos seus perfis.

Por exemplo, se você tiver um Canvas com notificações por push para iOS e web, um determinado usuário com dispositivos móveis e desktop pode receber mais de uma mensagem.

{% endapi %}
{% api %}

### O que a entrega no fuso local oferece? {#what-does-local-time-zone-delivery-offer}

{% apitags %}
Campaigns
{% endapitags %}

A entrega no fuso local permite que você entregue Campaigns de mensagens para um Segment com base no fuso horário individual de cada usuário. Sem a entrega no fuso local, as Campaigns serão agendadas com base nas configurações de fuso horário da sua empresa na Braze.

Por exemplo, uma empresa com sede em Londres que envia uma Campaign às 12h atingirá usuários na costa oeste dos Estados Unidos às 4h da manhã. Se o seu app estiver disponível apenas em alguns países, isso pode não ser um risco para você. Caso contrário, recomendamos fortemente evitar enviar notificações por push de madrugada para sua base de usuários!

{% endapi %}
{% api %}

### Como a Braze reconhece o fuso horário de um usuário? {#how-does-braze-recognize-a-users-time-zone}

{% apitags %}
Campaigns
{% endapitags %}

A Braze determinará automaticamente o fuso horário de um usuário a partir do seu dispositivo. Isso é projetado para garantir a precisão do fuso horário e a cobertura total dos seus usuários. Os usuários criados pela API de Usuário ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como padrão até serem reconhecidos no seu app pelo SDK.

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administer/global/admin_settings).

{% endapi %}
{% api %}

### Como faço para agendar uma Campaign no fuso local? {#how-do-i-schedule-a-local-time-zone-campaign}

{% apitags %}
Campaigns
{% endapitags %}

Ao agendar uma Campaign, você precisa escolher enviá-la em um horário designado e então selecionar **Enviar Campaign para os usuários no fuso local deles**.

A Braze recomenda fortemente que todas as Campaigns no fuso local sejam agendadas com 24 horas de antecedência. Como essa Campaign precisa ser enviada ao longo de um dia inteiro, agendá-la com 24 horas de antecedência permite que sua mensagem alcance todo o seu Segment. No entanto, você pode agendar essas Campaigns com menos de 24 horas de antecedência, se necessário. Lembre-se de que a Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de 1 hora.

Por exemplo, se for 13h e você agendar uma Campaign no fuso local para 15h, a Campaign será enviada imediatamente para todos os usuários cujo horário local é entre 15h e 16h, mas não para os usuários cujo horário local é 17h. Além disso, o horário de envio que você escolher para sua Campaign ainda não deve ter ocorrido no fuso horário da sua empresa.

Editar uma Campaign no fuso local que está agendada para menos de 24 horas de antecedência não alterará o cronograma da mensagem. Se você decidir editar uma Campaign no fuso local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no Segment-alvo quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar o fuso local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a Campaign ainda será enviada a todos os membros do Segment no horário original (17h).

{% alert note %}
Para etapas do Canvas, os usuários não precisam estar na etapa por 24 horas para receber a próxima etapa na entrega no fuso local.
{% endalert %}

Se você permitiu que os usuários se tornassem re-elegíveis para a Campaign, eles a receberão novamente no horário original (17h). Para todas as ocorrências subsequentes da sua Campaign, no entanto, suas mensagens serão enviadas apenas no horário atualizado.

{% endapi %}
{% api %}

### Quando as alterações nas Campaigns de fuso local entram em vigor? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

{% apitags %}
Campaigns
{% endapitags %}

Os segmentos-alvo para Campaigns de fuso local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo, a fim de garantir a entrega a todo o Segment. Por exemplo, considere um Segment direcionando usuários no seu segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Usou o app pela primeira vez há menos de 2 dias

A entrega no fuso local pode não alcançar os usuários deste Segment com base no horário de entrega e no fuso local dos usuários. Isso ocorre porque um usuário pode sair do Segment no momento em que seu fuso horário aciona a entrega.

{% endapi %}
{% api %}

### Quais mudanças posso fazer nas Campaigns agendadas antes do lançamento? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

{% apitags %}
Campaigns
{% endapitags %}

Quando a Campaign está agendada, edições em qualquer coisa além da composição da mensagem precisam ser feitas antes de colocarmos as mensagens na fila para envio. Como em todas as Campaigns, você não pode editar eventos de conversão após o lançamento da Campaign.

{% endapi %}
{% api %}

### Qual é a "zona segura" antes que as mensagens de uma Campaign agendada sejam enfileiradas? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-queued}

{% apitags %}
Campaigns
{% endapitags %}

- Campaigns agendadas únicas podem ser editadas até o horário de envio agendado.
- Campaigns recorrentes agendadas podem ser editadas até o horário de envio agendado.
- Campaigns de envio no horário local podem ser editadas até 24 horas antes do horário de envio agendado.
- Campaigns de envio no horário ideal podem ser editadas até 24 horas antes do dia em que a Campaign está programada para ser enviada.

{% endapi %}
{% api %}

### E se eu fizer uma edição dentro da "zona segura"? {#what-if-i-make-an-edit-within-the-safe-zone}

{% apitags %}
Campaigns
{% endapitags %}

Alterar o horário de envio das Campaigns dentro desse período pode levar a um comportamento indesejado, por exemplo:

- A Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de uma hora.
- Mensagens que já estavam na fila podem ainda ser enviadas no horário originalmente agendado, em vez do horário ajustado.

{% endapi %}
{% api %}

### O que devo fazer se a "zona segura" já passou? {#what-should-i-do-if-the-safe-zone-has-already-passed}

{% apitags %}
Campaigns
{% endapitags %}

Para garantir que as Campaigns operem conforme desejado, recomendamos parar a Campaign atual (isso interromperá quaisquer mensagens na fila). Você pode então duplicar a Campaign, fazer as alterações necessárias e lançar a nova Campaign. Pode ser necessário excluir desta Campaign os usuários que já receberam a primeira Campaign.

Certifique-se de reajustar os horários da Campaign para permitir o envio por fuso horário.

{% endapi %}
{% api %}

### Quando a Braze avalia os usuários para a entrega no fuso local? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

{% apitags %}
Campaigns
{% endapitags %}

A Braze avalia os usuários para elegibilidade de entrada em:

- Horário de Samoa (UTC+13) no dia agendado
- Horário local do usuário no dia agendado

Para que um usuário seja elegível para entrada, ele deve ser elegível em ambas as verificações. Por exemplo, se um Canvas estiver programado para ser lançado em 7 de agosto de 2021 às 14h no fuso local, então direcionar um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova York em 6 de agosto de 2021 às 21h
- Nova York em 7 de agosto de 2021 às 14h

Para entrar, o usuário precisa corresponder ao seu público e filtros em ambos os momentos de avaliação. Se o usuário não for elegível na primeira verificação, a Braze não executará a segunda verificação. Não há um tempo mínimo que o usuário precise estar no Segment antes do lançamento — apenas a elegibilidade em cada verificação importa.

Esse comportamento de avaliação é separado de [com quanta antecedência você agenda a Campaign no dashboard]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign). Para a explicação completa, exemplos e orientações de agendamento, consulte [Quando a Braze avalia os usuários para a entrega no fuso local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#when-does-braze-evaluate-users-for-local-time-zone-delivery) e [Como faço para agendar uma Campaign no fuso local?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-i-schedule-a-local-time-zone-campaign) nas perguntas frequentes de Campaigns.

{% endapi %}
{% api %}

### Por que o número de usuários que entram em uma Campaign não corresponde ao número esperado? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

{% apitags %}
Campaigns
{% endapitags %}

O número de usuários que entram em uma Campaign pode diferir do número esperado por causa de como os públicos e gatilhos são avaliados. Na Braze, um público é avaliado antes do gatilho (a menos que se use um [gatilho de alteração de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam da Campaign se não fizerem parte do público selecionado antes que quaisquer ações de gatilho sejam avaliadas.

{% endapi %}
{% api %}

<!-- Canvases -->

### O que acontece se o público e o horário de envio forem idênticos para um Canvas que tem uma variante, mas várias ramificações? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

{% apitags %}
Canvases
{% endapitags %}

Enfileiramos um job para cada etapa — eles são executados aproximadamente ao mesmo tempo, e um deles "vence". Na prática, isso pode ser distribuído de forma relativamente uniforme, mas é provável que haja pelo menos uma leve tendência para a etapa que foi criada primeiro.

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser garantir uma divisão uniforme, adicione um filtro de [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers).

{% endapi %}
{% api %}

### O que acontece quando você para um Canvas? {#what-happens-when-you-stop-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Quando você para um Canvas, o seguinte se aplica:

- Os usuários serão impedidos de entrar no Canvas.
- Nenhuma outra mensagem será enviada, independentemente de onde o usuário esteja no fluxo.
    - **Exceção:** Canvas de e-mail não param imediatamente. Depois que as solicitações de envio chegam ao SendGrid, não há nada que possamos fazer para impedir que sejam entregues ao usuário.

{% alert note %}
Parar um Canvas não fará com que os usuários que estão esperando em uma etapa saiam. Se você reativar o Canvas e os usuários ainda estiverem esperando, eles completarão a etapa e passarão para o próximo componente. No entanto, se o tempo em que o usuário deveria ter progredido para o próximo componente já tiver passado, ele sairá do Canvas.
{% endalert %}

{% endapi %}
{% api %}

### Quando um evento de exceção é disparado? {#when-does-an-exception-event-trigger}

{% apitags %}
Canvases
{% endapitags %}

Eventos de exceção só são disparados enquanto o usuário está esperando para receber o componente do Canvas ao qual estão associados. Se um usuário realizar uma ação antecipadamente, o evento de exceção não será disparado.

Se você quiser excluir usuários que realizaram um determinado evento antecipadamente, use [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) em vez disso.

{% endapi %}
{% api %}

### Como a edição de um Canvas afeta os usuários que já estão nele? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

{% apitags %}
Canvases
{% endapitags %}

Se você editar algumas das etapas de um Canvas de várias etapas, os usuários que já estavam no público mas ainda não receberam as etapas receberão a versão atualizada da mensagem. Observe que isso só acontecerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que você pode ou não editar após o lançamento, confira [Alterando seu Canvas após o lançamento]({{site.baseurl}}/post-launch_edits).

{% endapi %}
{% api %}

### Como as conversões de usuários são rastreadas em um Canvas? {#how-are-user-conversions-tracked-in-a-canvas}

{% apitags %}
Canvases
{% endapitags %}

Um usuário só pode converter uma vez por entrada no Canvas.

As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários dentro daquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa era a etapa mais recente que o usuário recebeu.

{% details Casos de uso %}

#### Caso de uso 1 {#use-case-1}

Há uma jornada de Canvas com 10 notificações por push e o evento de conversão é "início de sessão" ("Abre o App"):

- O Usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O Usuário B abre o app após cada notificação por push.

**Resultado:**
O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e zero para todas as etapas subsequentes.

{% alert note %}
Se o horário de silêncio estiver ativo quando o evento de conversão acontecer, as mesmas regras se aplicam.
{% endalert %}

#### Caso de uso 2 {#use-case-2}

Há um Canvas de uma etapa com horário de silêncio:

1. O usuário entra no Canvas.
2. A primeira etapa não tem postergação, mas está dentro do horário de silêncio, então a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:**
O usuário será contado como convertido na variante geral do Canvas, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

{% endapi %}
{% api %}

### Ao observar o número de usuários únicos, a análise de dados do Canvas ou o segmentador é mais preciso? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

{% apitags %}
Canvases
{% endapitags %}

O segmentador é uma estatística mais precisa para dados de usuários únicos em comparação com as estatísticas de Canvas ou Campaign. Isso ocorre porque as estatísticas de Canvas e Campaign são números que a Braze incrementa quando algo acontece — o que significa que há variáveis que podem resultar em esse número ser diferente do segmentador. Por exemplo, os usuários podem converter mais de uma vez para um Canvas ou Campaign.

{% endapi %}
{% api %}

### Por que o número de usuários entrando em um Canvas não corresponde ao número esperado? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

{% apitags %}
Canvases
{% endapitags %}

O número de usuários que entram em um Canvas pode diferir do número esperado devido à forma como os públicos e gatilhos são avaliados. Na Braze, um público é avaliado antes do gatilho (a menos que se use um gatilho de [alteração de atributo]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam do Canvas se não fizerem parte do público selecionado antes que quaisquer ações de gatilho sejam avaliadas.

{% endapi %}
{% api %}

<!-- Analytics -->

### Quais métricas a Braze mede? {#what-metrics-does-braze-measure}

{% apitags %}
Analytics
{% endapitags %}

Dependendo do canal, a Braze mede uma variedade de métricas para permitir que você determine o sucesso de uma Campaign e planeje as futuras. Você pode encontrar uma lista completa em nosso [glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% endapi %}
{% api %}

### Como a receita é calculada na Braze? {#how-is-revenue-calculated-in-braze}

{% apitags %}
Analytics
{% endapitags %}

Na página **Receita**, você pode visualizar dados sobre receita ou compras em períodos específicos, para um produto específico, ou a receita ou compras totais do seu app. Esses números de receita são gerados a partir das compras feitas pelos destinatários da Campaign dentro de um determinado período de conversão.

Dito isso, é importante notar que a Braze é uma ferramenta de marketing e não uma ferramenta de gestão de receita. Nosso [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) não suporta reembolsos e cancelamentos, então você pode ver discrepâncias ao comparar dados com outras ferramentas.

{% endapi %}
{% api %}

### Quais capacidades de relatórios o Currents oferece? {#what-reporting-capabilities-does-currents-enable}

{% apitags %}
Analytics
{% endapitags %}

Nossa ferramenta Currents transmite continuamente tanto dados de engajamento de mensagens quanto dados de comportamento do cliente para um dos nossos muitos parceiros de dados, capacitando você a usar os dados únicos e valiosos que a Braze cria para impulsionar seus esforços de business intelligence e análise de dados em outros parceiros de excelência.

Esses dados vão além das métricas de engajamento de mensagens e também podem incluir números mais complexos, como desempenho de atributos personalizados e eventos. Para mais detalhes, consulte nosso [glossário de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

{% endapi %}
{% api %}

### Como posso agendar um relatório de engajamento recorrente? {#how-can-i-schedule-a-recurring-engagement-report}

{% apitags %}
Analytics
{% endapitags %}

Para agendar um relatório de engajamento recorrente, faça o seguinte:

1. No seu dashboard, navegue até **Relatórios de engajamento**, em **Data**.
2. Clique em **+ Criar novo relatório**.
3. Adicione as [Campaigns e mensagens de Canvas]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#manually-select-campaigns-or-canvases) (individualmente ou [por tag]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#automatically-select-campaigns-or-canvases)) que você gostaria de compilar no seu relatório.
4. [Adicione estatísticas]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#add-statistics-to-your-reports) ao seu relatório.
5. Selecione a compressão e o delimitador para o seu relatório.
6. Insira os endereços de e-mail dos usuários da empresa que devem receber este relatório.
7. Selecione o [período de tempo]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#select-time-frame) a partir do qual você gostaria que seu relatório processasse os dados.
8. Selecione os [intervalos (diários, semanais, etc.)]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#select-data-display) nos quais gostaria de ver a divisão dos seus dados.
9. Agende seu relatório para [enviar imediatamente]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#schedule-your-report) ou em um [momento futuro especificado]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#schedule-your-report).
10. Execute o relatório e abra-o no seu e-mail quando ele chegar!

{% endapi %}
{% api %}

### Qual é a diferença entre relatórios de engajamento e o Criador de relatórios? {#whats-the-difference-between-engagement-reports-and-the-report-builder}

{% apitags %}
Analytics
{% endapitags %}

Os relatórios de engajamento fornecem CSVs de estatísticas de engajamento para mensagens específicas de Campaigns e Canvas via um e-mail disparado. Certos dados são agregados no nível da Campaign ou Canvas, em vez do nível da variante individual ou etapa. Os relatórios não são salvos no dashboard, e reexecutar o relatório pode resultar em estatísticas atualizadas.

O Criador de relatórios permite que você compare os resultados de várias Campaigns ou Canvas em uma única visualização, para que você possa determinar facilmente quais estratégias de engajamento mais impactaram suas métricas principais. Para Campaigns e Canvas, você pode exportar seus dados e salvar seu relatório para visualizar no futuro.

Para saber mais sobre os usos de relatórios e análise de dados na Braze, consulte a [visão geral dos relatórios]({{site.baseurl}}/user_guide/analytics/reports).

{% endapi %}