---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Este artigo de referência descreve a parceria entre a Braze e a Tealium, um hub de dados universal que permite conectar dados móveis, da web e de outros tipos a fontes de terceiros."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> O Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) é um mecanismo omnicanal de segmentação de clientes e ações em tempo real. O AudienceStream utiliza os dados que fluem para o EventStream e cria perfis de visitantes que representam os atributos mais importantes do engajamento dos seus clientes com a sua marca.

A integração da Braze com a Tealium utiliza os perfis de visitantes do AudienceStream. Os comportamentos compartilhados segmentam esses perfis para criar conjuntos de visitantes com características comuns, conhecidos como públicos. Esses públicos podem ajudar a alimentar sua stack de tecnologia de marketing em tempo real por meio de conectores.

{% alert important %}
O Tealium AudienceStreams e o EventStreams oferecem ações de conector com e sem lote. O conector sem lote deve ser usado quando as solicitações em tempo real forem importantes para o caso de uso e não houver preocupações quanto a atingir as especificações de limite de frequência da API da Braze. Entre em contato com o [Suporte]({{site.baseurl}}/braze_support) da Braze ou com seu gerente de sucesso do cliente se tiver alguma dúvida.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Nome | Descrição |
| ---- | --------- |
| Conta Tealium | Uma [conta Tealium](https://my.tealiumiq.com/) com acesso server-side é necessária. Recomendamos também usar as integrações client-side para aproveitar essa parceria. |
| Chave da API REST | Uma chave da API REST da Braze com as permissões `users.track`, `users.delete` e `subscription.status.set`.<br><br>Ela pode ser criada em **Dashboard da Braze > Console de desenvolvedor > Chave da API REST > Criar nova chave de API** |
| [Endpoint REST da Braze]({{site.baseurl}}/api/basics#endpoints) | A URL do seu endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Configurar atributos e badges {#step-1-set-up-attributes-and-badges}

#### Entendendo os atributos {#understanding-attributes}

A primeira etapa para usar o AudienceStream é criar atributos. Os atributos permitem definir as características importantes que representam os hábitos, preferências, ações e engajamento de um visitante com a sua marca.

**Atributos de visita**: Os atributos de visita estão relacionados à visita (ou sessão) atual do usuário. Os dados armazenados nesses atributos persistem durante toda a visita. Alguns exemplos de atributos de visita incluem:
- Duração da visita (Number)
- Navegador atual (String)
- Dispositivo atual (String)
- Contagem de visualizações de página (Number)

**Atributos de visitante**: Os atributos de visitante estão relacionados ao usuário atual. Os dados armazenados nesses atributos persistem durante todo o ciclo de vida do usuário. Alguns exemplos de atributos de visitante incluem:
- Valor de pedidos vitalício (Number)
- Nome (String)
- Data de nascimento (Date)
- Marcas compradas (Tally)

Acesse a [Tealium](https://docs.tealium.com/server-side/attributes/about/) para ver a lista completa de tipos de dados disponíveis.

##### Enriquecimento de atributos {#attribute-enrichment}

Depois de identificar os atributos desejados, você pode configurá-los com [enriquecimentos](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) — regras de negócio que determinam quando e como atualizar os valores dos atributos. Cada tipo de dado oferece sua própria seleção de enriquecimentos para manipular o valor do atributo. Isso está associado à configuração "WHEN". As seguintes opções estão disponíveis para cada atributo de visita e visitante:

- Novo visitante: ocorre na primeira vez que um visitante acessa seu site.
- Nova visita: ocorre em uma nova visita de um visitante.
- Qualquer evento: ocorre em qualquer evento.
- Visita encerrada: ocorre quando uma visita termina.

Você também pode criar uma condição personalizada, chamada regra, que determinará quando o enriquecimento ocorrerá.

#### Badges

Badges são atributos especiais de visitante que representam padrões de comportamento valiosos. Os badges são atribuídos ou removidos dos visitantes com base na lógica de seus enriquecimentos. Essa lógica geralmente combina múltiplas condições para capturar segmentos de visitantes ou define um limite para quando um determinado valor é atingido.

#### Exemplo de atributo e badge {#attribute-and-badge-example}

{% tabs local %}
{% tab Atributo %}

Crie um atributo de visitante "Valor de Pedidos Vitalício" que calcula o valor acumulado gasto (`order_total`) pelo cliente em todos os pedidos concluídos (evento de compra). Para configurar o valor de pedidos vitalício na sua conta Tealium, siga as instruções abaixo:

1. Navegue até **AudienceStream > Visitor/Visit Attributes** e clique em **Add Attribute**.
2. Selecione o escopo como **Visitor** e clique em **Continue**.
3. Selecione o tipo de dados **Number** e clique em **Continue**.
4. Insira o nome do atributo, "Lifetime Order Value".
5. Clique em **Add Enrichment** e selecione **Increment or Decrement Number**.
6. Selecione o atributo que contém o valor para incrementar (`order_total`).
7. Deixe o "WHEN" configurado como "Any Event" e clique em **Create a New Rule**.
8. Crie uma regra que identifique quando um evento de compra ocorreu.
9. Clique em **Save** e depois em **Finish**.

Agora, todos os clientes terão um atributo de valor de pedidos vitalício vinculado a eles.

{% endtab %}
{% tab Badge %}

Você pode criar badges que ajudam a classificar e segmentar seus usuários por determinados atributos que compartilham. No exemplo a seguir, criamos um Badge VIP para usuários com um "Valor de Pedidos Vitalício" acima de $500.

1. Navegue até **AudienceStream > Visitor/Visit Attributes** e clique em **Add Attribute**.
2. Selecione o escopo como **Visitor** e clique em **Continue**.
3. Selecione o tipo de dados **Badge** e clique em **Continue**.
4. Insira o nome do badge, "VIP".
5. Clique em **Add Enrichment** e selecione **Assign Badge**.
6. Deixe o "WHEN" configurado como "Any Event".
7. Crie uma regra para a atribuição do badge selecionando **Create Rule**. Atribua um título a essa regra e, usando o atributo criado anteriormente, configure a regra para "...has attribute "Lifetime Order Value greater than 500".
8. Clique em **Save** e depois em **Finish**.

{% endtab %}
{% endtabs %}

### Etapa 2: Criar um público {#step-2-create-an-audience}

Na página inicial da Tealium, selecione **Audiences** em **AudienceStream** na navegação lateral. Aqui, você pode criar um público de usuários com atributos em comum. A entrada ou saída de um usuário desse público será o gatilho para a Ação do Conector, configurada na próxima etapa, que enviará essas informações ao perfil de usuário na Braze.

Primeiro, nomeie seu público e depois considere quais atributos se aplicam ao tipo de público que você está tentando criar. Por exemplo, para criar um público de usuários VIP, você poderia criar um público de visitantes que possuem o **badge VIP**.

Certifique-se de **Salvar / Publicar** seu público quando terminar.

### Etapa 3: Criar um conector de evento {#step-3-create-an-event-connector}

Um conector é uma integração entre a Tealium e outro fornecedor, usado para transmitir dados. Esses conectores contêm ações que representam as APIs suportadas pelo parceiro.

1. Na barra lateral da Tealium, em **Server-Side**, navegue até **AudienceStream > Audience Connectors**.
2. Clique no botão azul **+ Add Connector** para navegar pelo marketplace de conectores. Na nova caixa de diálogo que aparece, use a busca para encontrar o conector **Braze**.
3. Para adicionar esse conector, clique no bloco do conector **Braze**. Ao clicar, você poderá ver o resumo da conexão e uma lista das informações necessárias, ações suportadas e instruções de configuração. A configuração é composta por três etapas: origem, configuração e ação.

#### Origem {#source}

Na caixa de diálogo **Source** que aparece, selecione o público que você criou na etapa anterior e um gatilho que seja apropriado para a sua situação. Você também pode ativar o limite de frequência para controlar com que frequência essa ação é disparada.

![Configuração de origem do conector AudienceStream da Tealium com seleção de público e gatilho.]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuração {#configuration}

Em seguida, uma caixa de diálogo de **Configuration** será exibida. Selecione **Add Connector** na parte inferior da página. Nomeie seu conector e forneça o endpoint da API da Braze e a chave da API REST da Braze aqui.

![Caixa de diálogo de configuração do conector Tealium com campos de endpoint e chave da API REST da Braze.]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Se você já criou um conector anteriormente, pode opcionalmente usar um existente da lista de conectores disponíveis e modificá-lo para atender às suas necessidades com o ícone de lápis ou excluí-lo com o ícone de lixeira.

Após criar ou selecionar um conector para vincular a esse público, clique em Done para continuar.

#### Ação {#action}

Em seguida, nomeie a ação do conector e selecione um tipo de ação que enviará dados de acordo com o mapeamento que você configurar. Aqui, você mapeará atributos da Braze para nomes de atributos da Tealium. Dependendo do tipo de ação escolhido, haverá uma seleção variada de campos exigidos pela Tealium. Abaixo estão exemplos e explicações desses campos.

{% alert important %}
Nem todos os campos oferecidos são obrigatórios.

![Painel de mapeamento de ações da Tealium mostrando campos opcionais que podem ser minimizados.]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Rastrear usuário - Em lote e individual %}

Essa ação permite rastrear atributos de usuário, eventos e compras em uma única ação. Embora a ação de rastrear usuário seja a mesma tanto para o AudienceStream quanto para o EventStream, a Tealium recomenda configurar os mapeamentos de atributos de usuário com ações do AudienceStream e os mapeamentos de eventos e compras com ações do EventStream.

| Parâmetros | Descrição |
| ---------- | ----------- |
| User ID | Use este campo para mapear o campo de ID de usuário da Tealium para o equivalente na Braze. Mapeie um ou mais atributos de ID de usuário. Quando múltiplos IDs são especificados, o primeiro valor não vazio é escolhido com base na seguinte ordem de prioridade: External ID, Braze ID, Alias Name e Alias Label.<br><br>- External ID e Braze ID não devem ser especificados ao importar tokens por push.<br>- Se estiver especificando um alias de usuário, o alias name e o alias label devem ser definidos. <br><br>Para saber mais, consulte o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze. |
| User attributes | Use os nomes de campos existentes do perfil de usuário da Braze para atualizar os valores do perfil no dashboard da Braze ou adicione seus próprios dados de [atributo de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object) personalizados aos perfis de usuário.<br><br>- Por padrão, novos usuários são criados se não existirem.<br>- Ao configurar **Update Existing Only** como `true`, apenas os usuários existentes serão atualizados, e nenhum novo usuário será criado.<br>- Se um atributo da Tealium estiver vazio, ele será convertido em nulo e removido do perfil de usuário da Braze. Os enriquecimentos devem ser usados se valores nulos não devem ser enviados à Braze para remover um atributo de usuário. |
| Modify user attributes | Use este campo para incrementar ou decrementar determinados atributos de usuário<br><br>- Atributos do tipo inteiro podem ser incrementados por inteiros positivos ou negativos.<br>- Atributos do tipo array podem ser modificados adicionando ou removendo valores de arrays existentes. |
| Event | Um evento representa uma única ocorrência de um evento personalizado por um determinado usuário em um timestamp. Use este campo para rastrear e mapear atributos de evento como os do [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object) da Braze. <br><br>- O atributo de evento `Name` é obrigatório para cada evento mapeado.<br>- O atributo de evento `Time` é automaticamente definido como agora, a menos que seja mapeado explicitamente. <br>- Por padrão, novos eventos serão criados se não existirem. Ao configurar `Update Existing Only` como `true`, apenas os eventos existentes serão atualizados, e nenhum novo evento será criado.<br>- Mapeie atributos do tipo array para adicionar múltiplos eventos. Atributos do tipo array devem ter comprimentos iguais.<br>- Atributos de valor único podem ser usados e aplicados a cada evento. |
| Event template | Forneça modelos de eventos para serem referenciados nos dados do corpo. Os modelos podem ser usados para transformar dados antes de enviá-los à Braze. Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais. |
| Event template variable | Forneça variáveis de modelo de evento como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
| Purchase | Use este campo para rastrear e mapear atributos de compra do usuário como os do [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) da Braze.<br><br>- Os atributos de compra `Product ID`, `Currency` e `Price` são obrigatórios para cada compra mapeada.<br>- O atributo de compra `Time` é automaticamente definido como agora, a menos que seja mapeado explicitamente.<br>- Por padrão, novas compras serão criadas se não existirem. Ao configurar `Update Existing Only` como `true`, apenas as compras existentes serão atualizadas, e nenhuma nova compra será criada.<br>- Mapeie atributos do tipo array para adicionar múltiplos itens de compra. Atributos do tipo array devem ter comprimentos iguais.<br>- Atributos de valor único podem ser usados e serão aplicados a cada item. |
| Purchase template | Os modelos podem ser usados para transformar dados antes de enviá-los à Braze.<br>- Defina um modelo de compra se precisar de suporte a objetos aninhados.<br>- Quando um modelo de compra é definido, a configuração feita na seção de compras da sua ação será ignorada.<br>- Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais. |
| Purchase template variable | Forneça variáveis de modelo de produto como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ação" }

![Exemplo de ação Rastrear Usuário da Tealium com atributos de usuário e campos de evento mapeados.]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Excluir usuário - Individual %}

Essa ação permite excluir usuários do dashboard da Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| User ID | Use este campo para mapear o campo de ID de usuário da Tealium para o equivalente na Braze.<br><br>- Mapeie um ou mais atributos de ID de usuário. Quando múltiplos IDs são especificados, o primeiro valor não vazio é escolhido com base na seguinte ordem de prioridade: External ID, Braze ID, Alias Name e Alias Label.<br>- Ao especificar um alias de usuário, o Alias Name e o Alias Label devem ser ambos definidos.<br><br>Para saber mais, consulte o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ação" }

![Ação de exclusão de usuário da Tealium com mapeamentos de ID de usuário da Braze configurados.]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Atualizar status do grupo de inscrições do usuário - Individual %}
Essa ação permite adicionar ou remover usuários de grupos de inscrições de SMS ou e-mail da Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| Group type | Use este campo para indicar se é um grupo de inscrições de SMS ou e-mail. |
| Update type | Mapeie esta ação para um evento de cancelamento de inscrição ou inscrição |
| Attributes | - ID do grupo de inscrições (obrigatório): O ID do grupo de inscrições relacionado ao tipo de grupo mapeado no campo anterior.<br>- External ID: O ID externo do usuário.<br><br>Específico para grupo de e-mail:<br>- E-mail: O endereço de e-mail do usuário.<br>**Se o ID externo não estiver definido, o e-mail será obrigatório.**<br><br>Específico para grupo de SMS:<br>- Telefone: O número de telefone no formato E.164. Por exemplo, +14155552671.<br>**Se o ID externo não estiver definido, o telefone será obrigatório.** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ação" }

![Ação de atualização do status do grupo de inscrições da Tealium com mapeamentos de tipo de grupo e tipo de atualização.]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Selecione **Finish**.

#### Resumo {#summary}

Visualize o resumo do conector que você criou. Se desejar modificar as opções escolhidas, selecione **Back** para editar ou **Finish** para concluir.

Seu conector agora é exibido na lista de conectores na página inicial da Tealium.

Certifique-se de salvar ou publicar seu conector quando terminar. As ações configuradas serão disparadas quando as condições de gatilho forem atendidas.

### Etapa 4: Testar o conector da Tealium {#step-4-test-your-tealium-connector}

Depois que o conector estiver funcionando, você deve testá-lo para garantir que está operando corretamente. A maneira mais simples de testar é usar a ferramenta **Trace** da Tealium. Para começar a usar o Trace, certifique-se de ter adicionado a extensão de navegador Tealium Tools.

1. Para iniciar um novo rastreamento, selecione **Trace** na barra lateral em **Server-Side**. Clique em **Start** e capture o Trace ID.
2. Abra a extensão do navegador e insira o Trace ID no AudienceStream Trace.
3. Examine o log em tempo real.
4. Verifique a ação que deseja validar clicando na entrada **Actions Triggered** para expandir.
5. Procure a ação que deseja validar e visualize o status do log.

Consulte a [documentação do Trace](https://docs.tealium.com/server-side/connectors/trace/about/) da Tealium para instruções mais detalhadas sobre a implementação da ferramenta Trace da Tealium.

## Demonstração de integração {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Demonstração de integração do Tealium AudienceStream" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Possíveis excedentes de pontos de dados {#potential-data-point-overages}

Existem três maneiras principais de você acidentalmente atingir excedentes de dados ao integrar a Braze por meio do Tealium:

### Envio de dados duplicados - envie apenas deltas de atributos para a Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
O Tealium não envia deltas de atributos de usuário para a Braze. Por exemplo, se você tem uma ação do EventStream que rastreia o nome, e-mail e número de celular de um usuário, o Tealium enviará todos os três atributos para a Braze sempre que a ação for disparada. O Tealium não verifica o que mudou ou foi atualizado para enviar apenas essa informação.<br><br>
**Solução**: <br>Você pode verificar no seu backend se um atributo mudou ou não e, se tiver mudado, chamar os métodos relevantes do Tealium para atualizar o perfil de usuário. **Isso é o que os usuários que integram a Braze diretamente costumam fazer.** <br>**OU**<br> Se você não armazena sua própria versão do perfil de usuário no seu backend e não consegue identificar se os atributos mudaram ou não, você pode usar o AudienceStream e [criar enriquecimentos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos de usuário apenas quando os valores tiverem mudado.

#### Envio de dados irrelevantes ou sobrescrita desnecessária de dados {#sending-irrelevant-data-or-needlessly-overwriting-data}
Se você tem múltiplos EventStreams que direcionam para o mesmo feed de eventos, **todas as ações ativadas para esse conector** serão disparadas automaticamente sempre que uma única ação for acionada, **o que também pode resultar em dados sendo sobrescritos na Braze.**<br><br>
**Solução**: <br>Configure uma especificação de evento ou feed separado para rastrear cada ação. <br>**OU**<br> Desative as ações (ou conectores) que você não quer que sejam disparadas usando os botões de alternância no dashboard do Tealium.

#### Inicialização da Braze muito cedo {#initializing-braze-too-early}
Se você está integrando com o Tealium usando a tag do SDK para web da Braze, pode observar um aumento significativo no seu MAU. **Se a Braze for inicializada no carregamento da página, ela criará um perfil anônimo toda vez que um usuário da web acessar o website pela primeira vez.** Isso inclui o tráfego de bots, que pode inflar sua contagem de usuários ativos. Alguns podem querer rastrear o comportamento dos usuários apenas quando eles tiverem concluído alguma ação, como "Fez login" ou "Assistiu a um vídeo", para reduzir sua contagem de MAU. <br><br>
**Solução**: <br>Configure [regras de carregamento](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exatamente quando e onde uma tag é carregada no seu site. Para saber mais sobre filtragem de tráfego de bots e inicialização condicional do SDK, consulte [Filtrando tráfego de bots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).