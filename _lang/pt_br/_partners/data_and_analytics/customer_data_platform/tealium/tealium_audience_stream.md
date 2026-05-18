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
O Tealium AudienceStreams e o EventStreams oferecem ações de conector com e sem lote. O conector sem lote deve ser usado quando as solicitações em tempo real forem importantes para o caso de uso e não houver preocupações quanto a atingir as especificações de limite de taxa da API da Braze. Entre em contato com o [Suporte]({{site.baseurl}}/braze_support/) da Braze ou com seu gerente de sucesso do cliente se tiver alguma dúvida.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Nome | Descrição |
| ---- | ----------- |
| Conta Tealium | É necessária uma [conta Tealium](https://my.tealiumiq.com/) com acesso ao lado do servidor. Recomendamos que você também use as integrações do lado do cliente para aproveitar essa parceria. |
| Chave da API REST | Uma chave da API REST da Braze com as permissões `users.track`, `users.delete` e `subscription.status.set`.<br><br>Isso pode ser criado no **dashboard da Braze > Console de desenvolvedor > Chave da API REST > Criar nova chave de API**|
| [Endpoint REST da Braze]({{site.baseurl}}/api/basics/#endpoints) | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Configurar atributos e emblemas {#step-1-set-up-attributes-and-badges}

#### Entendendo os atributos {#understanding-attributes}

A primeira etapa do uso do AudienceStream é a criação de atributos. Os atributos permitem que você defina as características importantes que representam os hábitos, as preferências, as ações e o engajamento de um visitante com a sua marca.

**Atributos de visita**: Os atributos de visita estão relacionados à visita (ou sessão) atual do usuário. Os dados armazenados nesses atributos persistem durante a duração da visita. Alguns exemplos de atributos de visita incluem:
- Duração da visita (número)
- Navegador atual (string)
- Dispositivo atual (string)
- Contagem de visualizações de página (número)

**Atributos do visitante**: Os atributos do visitante estão relacionados ao usuário atual. Os dados armazenados nesses atributos persistem por toda a vida do usuário. Alguns exemplos de atributos de visitante incluem:
- Valor dos pedidos no tempo de vida (número)
- Nome (string)
- Data de nascimento (data)
- Marcas de compras (registro)

Visite a [Tealium](https://docs.tealium.com/server-side/attributes/about/) para obter uma lista completa dos tipos de dados disponíveis.

##### Enriquecimento de atributos {#attribute-enrichment}

Depois de identificar os atributos desejados, você pode configurá-los com [enriquecimentos](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) — regras de negócios que determinam quando e como atualizar os valores dos atributos. Cada tipo de dados oferece sua própria seleção de enriquecimentos para manipular o valor do atributo. Isso está associado à configuração "WHEN". As seguintes opções estão disponíveis para cada atributo de visita e de visitante:

- New Visitor: ocorre na primeira vez que um visitante chega ao seu site.
- New Visit: ocorre em uma nova visita de um visitante.
- Any Event: ocorre em qualquer evento.
- Visit Ended: ocorre quando uma visita termina.

Você também pode criar uma condição personalizada, chamada de regra, que determinará quando o enriquecimento ocorrerá.

#### Emblemas {#badges}

Os emblemas são atributos especiais do visitante que representam padrões de comportamento valiosos. Os emblemas são atribuídos ou removidos dos visitantes com base na lógica de seus enriquecimentos. Essa lógica geralmente combina várias condições para capturar segmentos de visitantes ou define um limite para quando um determinado valor é atingido.

#### Exemplo de atributo e emblema {#attribute-and-badge-example}

{% tabs local %}
{% tab Atributo %}

Crie um atributo de visitante "Valor dos pedidos no tempo de vida" que calcule o valor cumulativo gasto (`order_total`) pelo cliente para todos os pedidos concluídos (evento de compra). Para configurar o valor dos pedidos no tempo de vida na sua conta Tealium, siga as instruções a seguir:

1. Navegue até **AudienceStream > Visitor/Visit Attributes** e clique em **Add Attribute**.
2. Selecione o escopo como **Visitor** e clique em **Continue**.
3. Selecione o tipo de dados **Number** e clique em **Continue**.
4. Digite o nome do atributo, "Lifetime Order Value".
5. Clique em **Add Enrichment** e selecione **Increment or Decrement Number**.
6. Selecione o atributo que contém o valor a ser incrementado (`order_total`).
7. Deixe a opção "WHEN" definida como "Any Event" e clique em **Create a New Rule**.
8. Crie uma regra que identifique a ocorrência de um evento de compra.
9. Clique em **Save** e, em seguida, em **Finish**.

Agora todos os clientes terão um atributo de valor dos pedidos no tempo de vida vinculado a eles.

{% endtab %}
{% tab Emblema %}

Você pode criar emblemas que ajudem a classificar e direcionar seus usuários por determinados atributos que eles compartilham. No exemplo a seguir, criamos um emblema VIP para usuários com um "Valor dos pedidos no tempo de vida" superior a $500.

1. Navegue até **AudienceStream > Visitor/Visit Attributes** e clique em **Add Attribute**.
2. Selecione o escopo como **Visitor** e clique em **Continue**.
3. Selecione o tipo de dados **Badge** e clique em **Continue**.
4. Digite o nome do emblema, "VIP".
5. Clique em **Add Enrichment** e selecione **Assign Badge**.
6. Deixe a opção "WHEN" definida como "Any Event".
7. Crie uma regra para atribuição de emblema selecionando **Create Rule**. Atribua um título a essa regra e, usando o atributo criado anteriormente, defina a regra como "...has attribute "Lifetime Order Value greater than 500".
8. Clique em **Save** e, em seguida, em **Finish**.

{% endtab %}
{% endtabs %}

### Etapa 2: Criar um público {#step-2-create-an-audience}

Na página inicial da Tealium, selecione **Audiences** em **AudienceStream** na barra de navegação lateral. Aqui, você pode criar um público de usuários com atributos comuns. A entrada ou saída de um usuário desse público será o gatilho para a ação do conector, configurada na próxima etapa, que passa essas informações para o perfil do usuário na Braze.

Primeiro, nomeie seu público e, em seguida, considere quais atributos se aplicariam ao tipo de público que está tentando criar. Por exemplo, para criar um público de usuários VIP, você pode criar um público de visitantes que tenham o **emblema VIP**.

Não se esqueça de **Salvar / Publicar** seu público quando terminar.

### Etapa 3: Criar um conector de eventos {#step-3-create-an-event-connector}

Um conector é uma integração entre a Tealium e outro fornecedor usada para transmitir dados. Esses conectores contêm ações que representam as APIs suportadas por seus parceiros.

1. Na barra lateral da Tealium, em **Server-Side**, navegue até **AudienceStream > Audience Connectors**.
2. Selecione o botão azul **+ Add Connector** para examinar o marketplace de conectores. Na nova caixa de diálogo que aparece, use a busca em destaque para encontrar o conector **Braze**.
3. Para adicionar esse conector, clique no bloco do conector **Braze**. Ao clicar, você verá o resumo da conexão e uma lista das informações necessárias, ações compatíveis e instruções de configuração. A configuração compreende três etapas: origem, configuração e ação.

#### Origem {#source}

Na caixa de diálogo **Source** exibida, selecione o público criado na etapa anterior e um gatilho que considere adequado à sua situação. Você também pode ativar o limite de frequência para controlar a frequência com que essa ação é disparada.

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuração {#configuration}

Em seguida, será exibida a caixa de diálogo **Configuration**. Selecione **Add Connector** na parte inferior da página. Dê um nome ao seu conector e forneça seu endpoint da API da Braze e a chave da API REST da Braze aqui.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Se já tiver criado um conector anteriormente, você poderá usar um conector existente da lista de conectores disponíveis e modificá-lo para atender às suas necessidades com o ícone de lápis ou excluí-lo com o ícone de lixeira.

Depois de criar ou selecionar um conector para vincular esse público, clique em Done para continuar.

#### Ação {#action}

Em seguida, nomeie sua ação de conector e selecione um tipo de ação que enviará dados de acordo com o mapeamento a ser configurado. Aqui, você mapeará os atributos da Braze para os nomes de atributos da Tealium. Os campos exigidos pela Tealium variam de acordo com o tipo de ação escolhido. A seguir, exemplos e explicações sobre esses campos.

{% alert important %}
Nem todos os campos oferecidos são obrigatórios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Rastrear usuário - Com e sem lote %}

Essa ação permite rastrear atributos de usuário, evento e compra, tudo em uma única ação. Embora a ação Track User seja a mesma para AudienceStream e EventStream, a Tealium recomenda definir mapeamentos de atributos de usuário com ações do AudienceStream e mapeamentos de evento e compra com ações do EventStream.

| Parâmetros | Descrição |
| ---------- | ----------- |
| ID do usuário | Use esse campo para mapear o campo de ID do usuário da Tealium para seu equivalente na Braze. Mapeie um ou mais atributos de ID de usuário. Quando várias IDs são especificadas, o primeiro valor não vazio é escolhido com base na seguinte ordem de prioridade: ID externo, ID da Braze, nome do alias e rótulo do alias.<br><br>- A ID externa e a ID da Braze não devem ser especificadas se estiver importando tokens por push.<br>- Se estiver especificando um alias de usuário, o nome do alias e o rótulo do alias devem ser definidos. <br><br>Para saber mais, confira o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze. |
| Atributos do usuário | Use os nomes de campo de perfil de usuário existentes na Braze para atualizar os valores de perfil de usuário no dashboard da Braze ou adicione seus próprios dados personalizados de [atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) aos perfis de usuário.<br><br>- Por padrão, novos usuários serão criados se não houver nenhum.<br>- Ao definir **Update Existing Only** como `true`, somente os usuários existentes serão atualizados, e nenhum novo usuário será criado.<br>- Se um atributo da Tealium estiver vazio, ele será convertido em nulo e removido do perfil de usuário da Braze. Os enriquecimentos devem ser usados se os valores nulos não devem ser enviados à Braze para remover um atributo de usuário. |
| Modificar atributos do usuário | Use esse campo para incrementar ou decrementar certos atributos do usuário<br><br>- Os atributos de números inteiros podem ser incrementados por números inteiros positivos ou negativos.<br>- Os atributos de arrays podem ser modificados adicionando ou removendo valores dos arrays existentes. |
| Evento | Um evento representa uma única ocorrência de um evento personalizado por um usuário específico em um registro de data e hora. Use esse campo para rastrear e mapear atributos de eventos como os do [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) da Braze. <br><br>- O atributo de evento `Name` é obrigatório para cada evento mapeado.<br>- O atributo de evento `Time` é automaticamente definido para a hora atual, a menos que seja explicitamente mapeado. <br>- Por padrão, novos eventos serão criados se não houver nenhum. Ao definir `Update Existing Only` como `true`, somente os eventos existentes serão atualizados, e nenhum novo evento será criado.<br>- Mapeie atributos do tipo array para adicionar vários eventos. Os atributos do tipo array devem ter o mesmo comprimento.<br>- Atributos de valor único podem ser usados e aplicados a cada evento. |
| Modelo de evento | Forneça modelos de eventos a serem referenciados nos dados do corpo. Os modelos podem ser usados para transformar os dados antes de enviá-los à Braze. Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais. |
| Variável de modelo de evento | Forneça variáveis de modelo de evento como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
| Compra | Use esse campo para rastrear e mapear os atributos de compra do usuário, como os do [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) da Braze.<br><br>- Os atributos de compra `Product ID`, `Currency` e `Price` são obrigatórios para cada compra mapeada.<br>- O atributo de compra `Time` é automaticamente definido para a hora atual, a menos que seja explicitamente mapeado.<br>- Por padrão, novas compras serão criadas se não houver uma. Ao definir `Update Existing Only` como `true`, somente as compras existentes serão atualizadas, e nenhuma nova compra será criada.<br>- Mapeie atributos do tipo array para adicionar vários itens de compra. Os atributos do tipo array devem ter o mesmo comprimento.<br>- Os atributos de valor único podem ser usados e se aplicarão a cada item. |
| Modelo de compra | Os modelos podem ser usados para transformar os dados antes de serem enviados à Braze.<br>- Defina um modelo de compra se você precisar de suporte a objetos aninhados.<br>- Quando um modelo de compra é definido, a configuração definida na seção de compras da sua ação será ignorada.<br>- Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais. |
| Variável do modelo de compra | Forneça variáveis de modelo de produto como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Excluir usuário - Sem lote %}

Essa ação permite excluir usuários do dashboard da Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| ID do usuário | Use esse campo para mapear o campo de ID do usuário da Tealium para seu equivalente na Braze.<br><br>- Mapeie um ou mais atributos de ID de usuário. Quando várias IDs são especificadas, o primeiro valor não vazio é escolhido com base na seguinte ordem de prioridade: ID externo, ID da Braze, nome do alias e rótulo do alias.<br>- Ao especificar um alias de usuário, o nome do alias e o rótulo do alias devem ser definidos.<br><br>Para saber mais, consulte o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) da Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Atualizar status do grupo de inscrições do usuário - Sem lote %}
Essa ação permite adicionar ou remover usuários dos grupos de inscrições para e-mail ou SMS da Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| Tipo de grupo | Use esse campo para indicar se esse é um grupo de inscrições para SMS ou para e-mail. |
| Tipo de atualização | Mapeie essa ação para um evento de cancelamento de inscrição ou de inscrição. |
| Atributos | - ID do grupo de inscrições (obrigatório): O ID do grupo de inscrições relacionado ao tipo de grupo mapeado no campo anterior.<br>- ID externo: O ID externo do usuário.<br><br>Específico do grupo de e-mail:<br>- E-mail: O endereço de e-mail do usuário.<br>**Se o ID externo não estiver definido, o e-mail será obrigatório.**<br><br>Específico do grupo de SMS:<br>- Telefone: O número de telefone no formato E.164. Por exemplo, +14155552671.<br>**Se o ID externo não estiver definido, o telefone será obrigatório.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Selecione **Finish**.

#### Resumo {#summary}

Visualize o resumo do conector que você criou. Se quiser modificar as opções escolhidas, selecione **Back** para editar ou **Finish** para concluir.

Seu conector agora é exibido na lista de conectores na página inicial da Tealium.

Não se esqueça de salvar ou publicar seu conector quando terminar. As ações que você configurou passarão a ser disparadas quando as conexões do gatilho forem atendidas.

### Etapa 4: Teste seu conector Tealium {#step-4-test-your-tealium-connector}

Depois que o conector estiver instalado e funcionando, teste-o para garantir que esteja funcionando corretamente. A maneira mais simples de testar isso é usar a **Trace Tool** da Tealium. Para começar a usar o Trace, confirme se adicionou a extensão de navegador Tealium Tools.

1. Para iniciar um novo rastreamento, selecione **Trace** na barra lateral em **Server-Side**. Clique em **Start** e capture o Trace ID.
2. Abra a extensão do navegador e insira o Trace ID no AudienceStream Trace.
3. Examine o registro em tempo real.
4. Verifique a ação que deseja validar clicando na entrada **Actions Triggered** para expandi-la.
5. Procure a ação que deseja validar e visualize o status do registro.

Consulte a [documentação do Trace](https://docs.tealium.com/server-side/connectors/trace/about/) da Tealium para obter instruções mais detalhadas sobre a implementação da ferramenta Trace da Tealium.

## Demonstração da integração {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" title="Demonstração da integração Tealium AudienceStream" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Potenciais excedentes de pontos de dados {#potential-data-point-overages}

Há três maneiras principais pelas quais você pode atingir acidentalmente o excedente de dados ao integrar a Braze pela Tealium:

#### Envio de dados duplicados — envie apenas deltas de atributos à Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}
A Tealium não envia à Braze deltas de atributos do usuário. Por exemplo, se você tiver uma ação EventStream que rastreia o nome, o e-mail e o número de telefone celular de um usuário, a Tealium enviará os três atributos à Braze sempre que a ação for disparada. A Tealium não procurará o que mudou ou foi atualizado e enviará apenas essas informações.<br><br>
**Solução**: <br>Você pode verificar seu backend para avaliar se um atributo foi alterado ou não e, em caso afirmativo, chamar os métodos relevantes da Tealium para atualizar o perfil do usuário. **Isso é o que os usuários que integram a Braze diretamente costumam fazer.** <br>**OU**<br> Se você não armazenar sua própria versão de um perfil de usuário no backend e não puder saber se os atributos mudam ou não, poderá usar o AudienceStream e [criar enriquecimentos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos de usuário somente quando os valores forem alterados.

#### Envio de dados irrelevantes ou substituição desnecessária de dados {#sending-irrelevant-data-or-needlessly-overwriting-data}
Se você tiver vários EventStreams que direcionam o mesmo feed de eventos, **todas as ações ativadas para esse conector** serão disparadas automaticamente sempre que uma única ação for disparada, **o que também pode resultar na substituição de dados na Braze.**<br><br>
**Solução**: <br>Configure uma especificação de evento ou feed separado para rastrear cada ação. <br>**OU**<br> Desative as ações (ou conectores) que você não deseja disparar usando os botões de alternância no dashboard da Tealium.

#### Inicialização da Braze muito cedo {#initializing-braze-too-early}
Os usuários que se integram à Tealium usando a tag do SDK para Web da Braze podem observar um aumento drástico no MAU. **Se a Braze for inicializada no carregamento da página, ela criará um perfil anônimo sempre que um usuário da web navegar no site pela primeira vez.** Isso inclui tráfego de bots, o que pode inflar a contagem de usuários ativos. Alguns podem querer rastrear o comportamento do usuário somente quando ele tiver concluído alguma ação, como "Fez login" ou "Assistiu a um vídeo", para reduzir a contagem de MAU. <br><br>
**Solução**: <br>Configure [regras de carregamento](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exatamente quando e onde uma tag é carregada em seu site. Para orientações mais completas sobre filtragem de tráfego de bots e inicialização condicional do SDK, consulte [Filtragem de tráfego de bots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).