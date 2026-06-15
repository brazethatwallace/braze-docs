---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Este artigo de referência descreve a parceria entre a Braze e a Tealium, um hub de dados universal que permite conectar dados móveis, da web e de outros tipos a fontes de terceiros."
page_type: partner
search_tag: Partner

---

# Tealium

> A [Tealium](https://tealium.com/) é um hub de dados universal e uma plataforma de dados do cliente composta por EventStream, AudienceStream e iQ Tag Management que permite conectar dados móveis, da web e de outros tipos de fontes de terceiros. A conexão da Tealium com a Braze permite um fluxo de dados de eventos personalizados, atributos de usuários e compras que capacita você a agir sobre seus dados em tempo real.

![Um gráfico de visão geral da Tealium que mostra como os diferentes produtos da Tealium e a plataforma da Braze se encaixam para ativar campanhas entre canais em tempo real.]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

A integração da Braze e da Tealium permite rastrear seus usuários e encaminhar dados para vários provedores de análise de dados de usuários. A Tealium permite que você:
- Sincronize públicos da Tealium com o [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) para a Braze para uso na personalização de Campaigns e Canvas da Braze ou na criação de segmentos.
- [Importe dados entre plataformas](#choose-your-integration-type). A Braze oferece uma integração de SDK [lado a lado](#side-by-side-sdk-integration) para seus aplicativos Android, iOS e web e uma integração de [servidor para servidor](#server-to-server-integration) que pode ser usada em qualquer plataforma que possa relatar dados de eventos.<br><br>

{% tabs %}
{% tab EventStream %}
O Tealium EventStream é um hub de coleta de dados e API que fica no centro dos seus dados. O EventStream lida com toda a cadeia de fornecimento de dados, desde a configuração e a instalação até a identificação, a validação e o aprimoramento dos dados de usuários recebidos. O EventStream realiza ações em tempo real com feeds e conectores de eventos. A seguir, estão os recursos que compõem o [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/).
- Fontes de dados (instalação e coleta de dados)
- Eventos em tempo real (inspeção de dados em tempo real)
- Especificações e atributos de eventos (requisitos e validação da camada de dados)
- Feeds de eventos (tipos de eventos filtrados)
- Conectores de eventos (ações do hub de API)

{% endtab %}
{% tab AudienceStream %}

O Tealium AudienceStream é um mecanismo omnicanal de segmentação de clientes e ações em tempo real. O AudienceStream utiliza os dados que fluem para o EventStream e cria perfis de visitantes que representam os atributos mais importantes do engajamento dos seus clientes com a sua marca. Consulte nosso artigo sobre o [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) para obter as etapas de configuração.

{% endtab %}
{% tab iQ Tag Management %}
O Tealium iQ permite disparar códigos em seus apps usando uma tag na interface de gerenciamento de tags do Tealium iQ. Essa tag coletará, controlará e fornecerá dados de eventos de plataformas móveis e da web, permitindo que você configure uma implementação nativa da Braze sem adicionar código específico da Braze aos seus apps. Os usuários podem optar por integrar os comandos remotos móveis por meio do iQ Tag Management ou de arquivos de configuração JSON (abordagem recomendada da Tealium). Os usuários que usam o SDK para web da Braze devem fazer a integração por meio da tag web iQ.

Para saber mais sobre os prós e os contras de cada método, consulte a seguinte seção [do gerenciador de tags Tealium iQ](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
A Tealium oferece ações de conector em lote e sem lote. O conector sem lote deve ser usado quando as solicitações em tempo real forem importantes para o caso de uso e não houver preocupações quanto a atingir as especificações do limite de taxa da API da Braze. Entre em contato com o suporte da Braze ou com seu gerente de sucesso do cliente se tiver alguma dúvida.<br><br>

Para conectores em lote, as solicitações são colocadas em fila até que um dos seguintes limites seja atingido:<br><br>
- Número máximo de solicitações: 75
- Tempo máximo desde a solicitação mais antiga: 10 minutos
- Tamanho máximo das solicitações: 1 MB

Por padrão, a Tealium não agrupa eventos de consentimento (preferências de inscrição) ou eventos de exclusão de usuários.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Tealium | É necessário ter uma [conta Tealium](https://my.tealiumiq.com/) com acesso ao servidor e/ou ao lado do cliente para aproveitar essa parceria. |
| Código-fonte instalado e [bibliotecas](https://docs.tealium.com/platforms/) da fonte da Tealium | A origem de todos os dados enviados à Tealium, como apps móveis, sites ou servidores backend.<br><br>É necessário instalar as bibliotecas em seu app, site ou servidor antes de poder configurar um conector Tealium com êxito. |
| Endpoint REST e SDK da Braze | Seu URL do endpoint REST ou SDK. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| Chave identificadora do app Braze (somente lado a lado) | A chave do identificador do seu app. <br><br>Ela pode ser encontrada em **Braze Dashboard > Manage Settings > API Key**. |
| Versão do código (somente lado a lado) | Corresponde à versão do SDK e deve estar no formato major.minor (por exemplo, 3.2 e não 3.0.1). A versão do código deve ser 3.0 ou superior. |
| Chave da API REST (somente de servidor para servidor) | Uma chave da API REST da Braze com as permissões `users.track` e `users.delete`. <br><br>Isso pode ser criado em **Braze Dashboard > Developer Console > REST API Key > Create New API Key**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Escolha seu tipo de integração {#choose-your-integration-type}

| Integração | Informações |
| ----------- | ------- |
| [Lado a lado](#side-by-side-sdk-integration) | Usa o SDK da Tealium para traduzir eventos em chamadas nativas da Braze, permitindo acesso a recursos mais profundos e uso mais abrangente da Braze do que a integração de servidor para servidor.<br><br>Caso pretenda usar comandos remotos da Braze, observe que a Tealium não é compatível com todos os métodos da Braze (por exemplo, Content Cards). Para usar um método da Braze que não esteja mapeado por um comando remoto correspondente, será necessário invocar o método adicionando o código nativo da Braze à sua base de código.|
| [De servidor para servidor](#server-to-server-integration) | Encaminha dados da Tealium para os endpoints da REST API da Braze.<br><br>Não oferece suporte aos recursos da interface do usuário da Braze, como envio de mensagens no app, Content Cards ou notificações por push. Também existem dados capturados automaticamente, como campos em nível de dispositivo, que não estão disponíveis por meio desse método.<br><br>Considere uma integração lado a lado se quiser usar esses recursos.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Escolha seu tipo de integração" }

## Integração lado a lado de SDK {#side-by-side-sdk-integration}

### Comandos remotos {#remote-commands}

Os comandos remotos são um recurso das bibliotecas Tealium para iOS e Android que permitem fazer chamadas do SDK da Tealium — por meio dos servidores da Braze — para a Braze. O módulo de comando remoto da Braze instalará e criará automaticamente as bibliotecas Braze necessárias e cuidará de toda a renderização de mensagens e do rastreamento de análise de dados. Para usar o comando remoto móvel da Braze, você precisará das bibliotecas da Tealium instaladas nos seus apps.

A Tealium oferece duas maneiras de integrar o comando remoto móvel. Não há perda de funcionalidade entre os tipos de integração, e o código nativo subjacente é idêntico.

| Método de comando remoto móvel | Prós | Contras |
| --- | --- | --- |
| **Tag de comando remoto** | Modifique facilmente os mapeamentos e os dados enviados ao comando remoto usando a interface do Tealium iQ.<br><br>Isso permite enviar dados ou eventos adicionais a um SDK de terceiros depois que o app já estiver na loja de aplicativos, sem que o cliente precise atualizar o app. | O módulo de gerenciamento de tags no app depende de uma visualização da web oculta para processar JavaScript. |
| **Arquivo de configuração JSON**<br>([Recomendado](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | O uso do método JSON elimina a necessidade de ter uma visualização da web oculta no app e reduz muito o consumo de memória.<br><br>O arquivo JSON pode ser hospedado de modo remoto ou localmente no app do cliente. | No momento, não há uma interface para gerenciar isso, então o processo é um pouco mais trabalhoso.<br><br>Nota: A Tealium está trabalhando para adicionar uma interface de gerenciamento que resolverá esse problema e trará o mesmo nível de flexibilidade para os comandos remotos JSON que eles têm com a versão de gerenciamento do iQ Tag |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comandos remotos" }

Use os mapeamentos de dados de comandos remotos móveis da Braze para definir atributos padrão de usuários e atributos personalizados e rastrear compras e eventos personalizados. Consulte a tabela a seguir para obter os métodos correspondentes da Braze.

| Comando remoto | Método Braze |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| initialize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comandos remotos" }

Você pode encontrar mais detalhes sobre como configurar o comando remoto móvel da Braze e uma visão geral dos métodos suportados na documentação do desenvolvedor da Tealium:
- [Comando remoto](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Tag de comando remoto](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Os comandos remotos móveis da Braze não são compatíveis com todos os métodos e canais de envio de mensagens da Braze (por exemplo, Content Cards). Para usar um método da Braze que não esteja mapeado por um comando remoto correspondente, será necessário invocar o método diretamente adicionando o código nativo da Braze à sua base de código.
{% endalert%}

### Tag do SDK para web da Braze {#braze-web-sdk-tag}

Use a tag do SDK para web da Braze para implantar o SDK para web da Braze em seu site. O [Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) permite que os clientes adicionem a Braze como uma tag no dashboard da Tealium para rastrear a atividade dos visitantes. As tags são normalmente usadas por profissionais de marketing para entender a eficácia da publicidade on-line, do e-mail marketing e da personalização de sites.

1. Na Tealium, navegue até **iQ > Tags > + Add Tag > Braze Web SDK**.
2. Na caixa de diálogo de configuração de tag, insira a chave de API (sua chave de identificador do app Braze), o URL base (endpoint do SDK da Braze) e a [versão do código do SDK para web da Braze](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). Também é possível ativar o registro para registrar informações no console da web para fins de depuração.
3. Na caixa de diálogo [Load Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/), escolha "Load on All Pages" ou selecione **Create Rule** para determinar quando e onde carregar uma instância dessa tag em seu site.
4. Na caixa de diálogo **[Data Mappings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)**, selecione **Create Mappings** para mapear os dados da Tealium para a Braze. As variáveis de destino para a tag do SDK para web da Braze são incorporadas à guia **Data Mapping** da tag. As [tabelas a seguir](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) listam as categorias de destino disponíveis e descrevem cada nome de destino.
5. Selecione **Finish**.

### Recursos de integrações lado a lado {#side-by-side-integrations-resources}

- Comando remoto do iOS: [Documentação da Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [repositório GitHub da Tealium](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Comando remoto para Android: [Documentação da Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [repositório GitHub da Tealium](https://github.com/Tealium/tealium-android-braze-remote-command)
- Tag do SDK para web: [Documentação da Tealium](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Integração de servidor para servidor {#server-to-server-integration}

Essa integração encaminha dados da Tealium para a REST API da Braze.

A integração de servidor para servidor não oferece suporte aos recursos da interface do usuário da Braze, como envio de mensagens no app, Content Cards ou notificações por push. Também existem dados capturados automaticamente (como campos em nível de dispositivo) que não estão disponíveis por meio desse método.

Se quiser usar esses dados e recursos, considere nossa integração de SDK [lado a lado]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration).

### Etapa 1: Configurar uma fonte {#step-1-set-up-a-source}

A Tealium exige que você configure primeiro uma fonte de dados válida para o conector.
1. Na barra lateral da Tealium, em **Server-Side**, navegue até **Sources > Data Sources > + Add Data Source**.
2. Localize a plataforma desejada nas categorias disponíveis e dê um nome à sua fonte; esse campo é obrigatório.<br>![]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. Nas opções de **Event Specifications**, escolha as [especificações de evento](https://docs.tealium.com/server-side/event-specifications/about/) que você gostaria de incluir. As especificações de eventos ajudam a identificar os nomes dos eventos e os atributos necessários para rastreamento em sua instalação. Essas especificações serão aplicadas aos eventos recebidos.<br>![]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Reserve algum tempo para pensar sobre quais dados são mais valiosos para você e quais especificações parecem mais apropriadas para o seu caso de uso. Também estão disponíveis [especificações de eventos personalizados](https://docs.tealium.com/iq-tag-management/events/about/). <br>
4. O próximo diálogo avança para a etapa **Get Code**. O código base e o código de rastreamento de eventos fornecidos aqui servem como guia de instalação. Baixe o PDF fornecido se quiser compartilhar essas instruções com sua equipe. Selecione **Save & Continue** quando terminar.<br>
5. Agora você poderá visualizar a fonte salva, bem como adicionar ou remover especificações de eventos. <br>![]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Na visualização detalhada da fonte de dados, você pode executar as seguintes ações:
- Visualizar e copiar a chave da fonte de dados
- Exibir instruções de instalação
- Retornar à página **Get Code**
- Adicionar ou remover especificações de eventos
- Navegar para visualizar eventos em tempo real relacionados a uma especificação de evento
- E mais...<br>
6. Por fim, selecione **Save / Publish** na parte superior da página. Se você não publicar sua fonte, não será possível encontrá-la ao configurar seu conector da Braze.

Consulte [Data Sources](https://docs.tealium.com/server-side/data-sources/about-data-sources/) para obter mais instruções sobre como configurar e editar sua fonte de dados.

### Etapa 2: Criar um conector de eventos {#step-2-create-an-event-connector}

Um conector é uma integração entre a Tealium e outro fornecedor usada para transmitir dados. Esses conectores contêm ações que representam as APIs suportadas por seus parceiros.

1. Na barra lateral da Tealium, em **Server-Side**, navegue até **EventStream > Event Connectors**.
2. Selecione o botão azul **+ Add Connector** para examinar o marketplace de conectores. Na nova caixa de diálogo que aparece, use a busca em destaque para encontrar o conector **Braze**.
3. Para adicionar esse conector, clique no bloco do conector **Braze**. Ao clicar, você verá o resumo da conexão e uma lista das informações necessárias, ações compatíveis e instruções de configuração. A configuração compreende três etapas: fonte, configuração e ação.

#### Origem {#source}

Depois que a fonte tiver sido configurada, volte à página do conector Braze em **EventStream** > **Event Connectors** > **+ Add Connector** > **Braze**.

Em seguida, selecione a fonte de dados que você acabou de criar e, em **Event Feed**, selecione **All Events** ou uma especificação de evento específica, a jornada recomendada para enviar apenas valores alterados para a Braze. Selecione **Continue**.

#### Configuração {#configuration}

Em seguida, selecione **Add Connector** na parte inferior da página. Dê um nome ao seu conector e forneça seu endpoint da API da Braze e a chave da API REST da Braze aqui.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Se já tiver criado um conector anteriormente, você poderá usar um conector existente da lista de conectores disponíveis e modificá-lo para atender às suas necessidades com o ícone de lápis ou excluí-lo com o ícone de lixeira.

#### Ação {#action}

Em seguida, nomeie sua ação de conector e selecione um tipo de ação que enviará dados de acordo com o mapeamento a ser configurado. Aqui, você mapeará atributos, eventos e compras da Braze para nomes de atributos, eventos e compras da Tealium.

{% alert important %}
Nem todos os campos oferecidos são obrigatórios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Rastrear usuário - Em lote e sem lote %}

Essa ação permite rastrear atributos de usuário, evento e compra, tudo em uma única ação.

| Parâmetros | Descrição |
| ---------- | ----------- |
| ID de usuário | Use esse campo para mapear o campo de ID do usuário da Tealium para seu equivalente na Braze. Mapeie um ou mais atributos de ID de usuário. Quando várias IDs são especificadas, o primeiro valor não em branco é escolhido com base na seguinte ordem de prioridade: ID externo, ID da Braze, nome do alias e rótulo do alias.<br><br>- A ID externa e a ID da Braze não devem ser especificadas se estiver importando tokens por push.<br>- Se estiver especificando um alias de usuário, o nome do alias e o rótulo do alias devem ser definidos. <br><br>Para saber mais, confira o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze. |
| Atributos do usuário | Use os nomes de campo de perfil de usuário existentes na Braze para atualizar os valores de perfil de usuário no dashboard da Braze ou adicione seus próprios dados de [atributos de usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) personalizados aos perfis de usuário.<br><br>- Por padrão, novos usuários serão criados se não houver nenhum.<br>- Ao definir **Update Existing Only** como `true`, somente os usuários existentes serão atualizados, e nenhum novo usuário será criado.<br>- Se um atributo da Tealium estiver vazio, ele será convertido em nulo e removido do perfil de usuário da Braze. Os enriquecimentos devem ser usados se os valores nulos não devem ser enviados à Braze para remover um atributo de usuário. |
| Modificar atributos do usuário | Use esse campo para incrementar ou decrementar certos atributos do usuário<br><br>- Atributos de números inteiros podem ser incrementados por números inteiros positivos ou negativos.<br>- Atributos de matrizes podem ser modificados adicionando ou removendo valores das matrizes existentes. |
| Evento | Um evento representa uma única ocorrência de um evento personalizado por um usuário específico em um registro de data e hora. Use esse campo para rastrear e mapear atributos de eventos como os do [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) da Braze. <br><br>- O atributo de evento `Name` é obrigatório para cada evento mapeado.<br>- O atributo de evento `Time` é automaticamente definido para a hora atual, a menos que seja explicitamente mapeado. <br>- Por padrão, novos eventos serão criados se não houver nenhum. Ao definir `Update Existing Only` como `true`, somente os eventos existentes serão atualizados, e nenhum novo evento será criado.<br>- Mapeie atributos do tipo matriz para adicionar vários eventos. Atributos do tipo matriz devem ter o mesmo comprimento.<br>- Atributos de valor único podem ser usados e aplicados a cada evento. |
| Modelo de evento | Forneça modelos de eventos a serem referenciados nos dados do corpo. Os modelos podem ser usados para transformar os dados antes de enviá-los à Braze. Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais. |
| Variável de modelo de evento | Forneça variáveis de modelo de evento como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
| Compra | Use esse campo para rastrear e mapear atributos de compra do usuário, como os do [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) da Braze.<br><br>- Os atributos de compra `Product ID`, `Currency` e `Price` são obrigatórios para cada compra mapeada.<br>- O atributo de compra `Time` é automaticamente definido para a hora atual, a menos que seja explicitamente mapeado.<br>- Por padrão, novas compras serão criadas se não houver uma. Ao definir `Update Existing Only` como `true`, somente as compras existentes serão atualizadas, e nenhuma nova compra será criada.<br>- Mapeie atributos do tipo matriz para adicionar vários itens de compra. Atributos do tipo matriz devem ter o mesmo comprimento.<br>- Atributos de valor único podem ser usados e se aplicarão a cada item.|
| Modelo de compra | Os modelos podem ser usados para transformar os dados antes de serem enviados à Braze.<br>- Defina um modelo de compra se você precisar de suporte a objetos aninhados.<br>- Quando um modelo de compra é definido, a configuração definida na seção de compras da sua ação será ignorada.<br>- Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais.|
| Variável do modelo de compra | Forneça variáveis de modelo de produto como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ação" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Excluir usuário - Sem lote %}

Essa ação permite excluir usuários do dashboard da Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| ID de usuário | Use esse campo para mapear o campo de ID de usuário da Tealium para seu equivalente na Braze. <br><br>- Mapeie um ou mais atributos de ID de usuário. Quando várias IDs são especificadas, o primeiro valor não em branco é escolhido com base na seguinte ordem de prioridade: ID externo, ID da Braze, nome do alias e rótulo do alias.<br>- Ao especificar um alias de usuário, o nome do alias e o rótulo do alias devem ser definidos.<br><br>Para saber mais, consulte o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ação" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Se quiser modificar as opções escolhidas, selecione **Back** para editar ou **Finish** para concluir.

{% endtab %}
{% endtabs %}

Selecione **Continue**.

Seu conector agora é exibido na lista de conectores na página inicial da Tealium. <br>![]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

Certifique-se de selecionar **Save / Publish** para seu conector quando terminar. As ações que você configurou passarão a ser acionadas quando as conexões do gatilho forem atendidas.

### Etapa 3: Teste seu conector Tealium {#step-3-test-your-tealium-connector}

Depois que o conector estiver instalado e funcionando, teste-o para garantir que esteja funcionando corretamente. A maneira mais simples de testar isso é usar a **Trace Tool** da Tealium. Para começar a usar o Trace, confirme se adicionou a extensão de navegador Tealium Tools.

1. Para iniciar um novo rastreamento, selecione **Trace** na barra lateral, em opções **Server-Side**. Selecione **Start** e capture a ID do rastreamento.
2. Abra a extensão do navegador e insira a ID do rastreamento no AudienceStream Trace.
3. Examine o registro em tempo real.
4. Verifique a ação que deseja validar selecionando a entrada **Actions Triggered** para expandir.
5. Procure a ação que deseja validar e visualize o status do registro.

Consulte a [documentação de Trace](https://docs.tealium.com/server-side/connectors/trace/about/) da Tealium para obter instruções mais detalhadas sobre a implementação da ferramenta de rastreamento da Tealium.

## Demonstração da integração {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1mP84vVWifzNMN7eMYNORNy0y-WZurzBs/view?usp=sharing" title="Demonstração da integração com a Tealium" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Potenciais excedentes de pontos de dados {#potential-data-point-overages}

Há três maneiras principais de registrar acidentalmente pontos de dados desnecessários ao integrar a Braze por meio da Tealium:

#### Envio de dados duplicados — envie apenas deltas de atributos para a Braze {#sending-duplicate-data-only-send-braze-deltas-of-attributes}

A Tealium não envia deltas de atributos do usuário para a Braze. Por exemplo, se você tiver uma ação EventStream que rastreia o nome, o e-mail e o número de telefone celular de um usuário, a Tealium enviará os três atributos à Braze sempre que a ação for disparada. A Tealium não procurará o que mudou ou foi atualizado e enviará apenas essas informações.

**Solução**: <br>Você pode verificar seu backend para avaliar se um atributo foi alterado ou não e, em caso afirmativo, chamar os métodos relevantes da Tealium para atualizar o perfil do usuário. **Isso é o que os usuários que integram a Braze diretamente costumam fazer.** <br>**OU**<br> Caso não armazene sua própria versão de um perfil de usuário no seu backend e não tenha como saber se os atributos mudam ou não, você pode usar o AudienceStream e
[criar enriquecimentos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos do usuário somente quando os valores forem alterados. Consulte a documentação da Tealium sobre [regras de enriquecimento](https://docs.tealium.com/server-side-connectors/braze-connector/).

#### Envio de dados irrelevantes ou substituição desnecessária de dados {#sending-irrelevant-data-or-needlessly-overwriting-data}

Se você tiver vários EventStreams que direcionam o mesmo feed de eventos, **todas as ações ativadas para esse conector** serão disparadas automaticamente sempre que uma única ação for disparada. Isso também pode fazer com que os dados sejam sobrescritos na Braze e registrar pontos de dados desnecessários.

**Solução**: <br>Configure uma especificação de evento ou feed separado para rastrear cada ação. <br>**OU**<br> Desative as ações (ou conectores) que você não deseja disparar usando os botões de alternância no dashboard da Tealium.

#### Inicialização da Braze muito cedo {#initializing-braze-too-early}

Se você estiver integrando com a Tealium usando a tag do SDK para web da Braze, poderá observar um aumento drástico no seu MAU. **Se a Braze for inicializada no carregamento da página, ela criará um perfil anônimo sempre que um usuário da web navegar no site pela primeira vez.** Isso inclui tráfego de bots, o que pode inflar sua contagem de usuários ativos. Alguns podem querer rastrear o comportamento do usuário somente quando ele tiver concluído alguma ação, como "fez login" ou "assistiu a um vídeo", para reduzir a contagem de MAU.

**Solução**: <br>Configure [regras de carregamento](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exatamente quando e onde uma tag é carregada em seu site. Para orientações mais abrangentes sobre filtragem de tráfego de bots e inicialização condicional do SDK, consulte [Filtragem de tráfego de bots]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering).