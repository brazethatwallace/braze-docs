---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Este artigo de referência descreve a parceria entre a Braze e a Segment, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes na sua stack de marketing."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> A [Segment](https://segment.com) é uma plataforma de dados do cliente que ajuda você a coletar, limpar e ativar os dados dos seus clientes.

A integração da Braze com a Segment permite rastrear seus usuários e encaminhar dados para vários provedores de análise de dados de usuários. A Segment permite que você:

- Sincronize o [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage) com a Braze para uso em Campaigns da Braze e na segmentação de Canvas.
- [Importe dados entre as duas plataformas](#integration-options). Oferecemos uma integração lado a lado de SDK para seus aplicativos Android, iOS e web e uma integração de servidor para servidor para sincronizar seus dados com as REST APIs da Braze.
- [Conecte os dados à Segment pelo Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Segment | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| Fonte instalada e [bibliotecas](https://segment.com/docs/sources/) de fonte da Segment | A origem de todos os dados enviados à Segment, como apps móveis, sites ou servidores backend.<br><br>Instale as bibliotecas no seu app, site ou servidor antes de configurar um fluxo `Source > Destination`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar a Braze e a Segment, você deve definir [a Braze como um destino](#connection-settings) de acordo com o [tipo de integração escolhido](#integration-options) (modo de conexão). Se você for um cliente novo na Braze, poderá retransmitir dados históricos para a Braze usando [replays da Segment](#segment-replays). Em seguida, você deve configurar [mapeamentos](#methods) e [testar sua integração](#step-4-test-your-integration) para garantir um fluxo de dados suave entre a Braze e a Segment.

### Etapa 1: Crie um destino da Braze {#connection-settings}

Depois de configurar suas fontes com êxito, você precisará configurar a Braze como um [destino](https://segment.com/docs/destinations/) para cada fonte (iOS, Android, web etc.). Você terá muitas opções para personalizar o fluxo de dados entre a Braze e a Segment usando as configurações de conexão.

### Etapa 2: Escolha a estrutura do destino e o tipo de conexão {#integration-options}

Na Segment, navegue até **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![A página de configuração da fonte. Esta página inclui configurações para definir a estrutura de destino como "actions" ou "classic" e definir o modo de conexão como "cloud mode" ou "device mode".]({% image_buster /assets/img/segment/setup.png %})

Você pode integrar a fonte web da Segment (Analytics.js) e as bibliotecas nativas do lado do cliente com a Braze usando uma integração lado a lado (modo dispositivo) ou uma integração servidor a servidor (modo nuvem).

Sua escolha do modo de conexão será determinada pelo tipo de fonte para o qual o destino está configurado.

| Integração | Informações |
| ----------- | ------- |
| [Lado a lado<br>(modo dispositivo)](#side-by-side-sdk-integration) | Usa o SDK da Segment para traduzir eventos em chamadas nativas da Braze, permitindo acesso a recursos mais profundos e uso mais abrangente da Braze do que a integração de servidor para servidor.<br><br>Observe que a Segment não é compatível com todos os métodos da Braze (por exemplo, Content Cards). Para usar um método da Braze que não esteja mapeado por um mapeamento correspondente, será necessário invocar o método adicionando o código nativo da Braze à sua base de código. |
| [De servidor para servidor<br>(modo nuvem)](#server-to-server-integration) | Encaminha dados da Segment para os endpoints da REST API da Braze.<br><br>Não oferece suporte aos recursos da interface do usuário da Braze, como mensagens no app, Content Cards ou notificações por push. Também existem dados capturados automaticamente, como campos em nível de dispositivo, que não estão disponíveis por meio desse método.<br><br>Considere uma integração lado a lado se quiser usar esses recursos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Escolha a estrutura do destino e o tipo de conexão" }

{% alert note %}
Visite a [Segment](https://segment.com/docs/destinations/#connection-modes) para saber mais sobre as duas opções de integração (modos de conexão), incluindo os benefícios de cada uma.
{% endalert %}

#### Integração lado a lado de SDK {#side-by-side-sdk-integration}

Também chamada de modo dispositivo, essa integração mapeia o SDK e os [métodos](#methods) da Segment para o SDK da Braze, permitindo o acesso a todos os recursos do nosso SDK, como push, mensagens no app e outros métodos nativos da Braze.

{% alert note %}
Ao usar o modo de dispositivo da Segment, você não precisa integrar o Braze SDK diretamente. Ao adicionar a Braze como um destino do modo dispositivo para a Segment, o Segment SDK inicializará o Braze SDK e chamará os métodos mapeados relevantes da Braze.
{% endalert %}

{% alert important %}
Para integrações no modo dispositivo em dispositivos móveis, você deve adicionar o plugin de destino da Braze ao seu app, além de configurar o destino no dashboard da Segment. O Segment SDK não inclui o plugin da Braze por padrão — sem ele, o Segment SDK não consegue encaminhar dados ou chamadas de métodos mapeados para a Braze, e recursos como push, mensagens no app e Content Cards não funcionarão. Consulte as abas específicas por plataforma nesta seção para instruções de instalação.
{% endalert %}

Ao usar uma conexão no modo dispositivo, semelhante à integração nativa do Braze SDK, o Braze SDK atribuirá um `device_id` e um identificador de backend, `braze_id`, a cada usuário. Isso permite que a Braze capture a atividade anônima do dispositivo fazendo a correspondência com esses identificadores em vez de `userId`.

{% alert note %}
Se você usar [filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) com destinos no modo dispositivo (Kotlin ou Swift), será necessário configurar o plugin de destino com o suporte a filtros ativado. Consulte a [documentação de filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) da Segment para detalhes sobre as versões de plugin compatíveis.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
O código-fonte para a integração do modo de dispositivo Android é mantido pela Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

<br>
O Braze SDK a ser usado depende do Segment SDK que você usa:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Preferencial | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legado | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integração lado a lado de SDK" }


{% endalert %}

Para configurar a Braze como um destino de modo de dispositivo para sua origem Android, escolha **Actions** como a **Destination framework** e, em seguida, selecione **Save**.

Para concluir a integração lado a lado, você deve adicionar o [plugin de destino Braze Kotlin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) ao seu app Android. Esse plugin faz a ponte entre o Segment SDK e o Braze SDK, permitindo que os dados no modo dispositivo fluam para a Braze. Siga as instruções de instalação da Segment para adicionar a dependência do plugin e inicializá-lo com sua instância de analytics da Segment.

O código-fonte para a integração do [modo de dispositivo Android](https://github.com/braze-inc/braze-segment-kotlin) é mantido pela Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

{% endtab %}
{% tab iOS %}

{% alert important %}
O código-fonte para a integração do modo de dispositivo iOS é mantido pela Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

<br>
O Braze SDK a ser usado depende do Segment SDK que você usa:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Preferencial | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legado | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integração lado a lado de SDK" }
{% endalert %}

Para configurar a Braze como um destino no modo dispositivo para sua origem iOS, escolha **Actions** como a **Destination framework** e selecione **Save**.

Para concluir a integração lado a lado, você deve adicionar o [plugin de destino Braze Swift](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) ao seu app iOS. Esse plugin faz a ponte entre o Segment SDK e o Braze SDK, permitindo que os dados no modo dispositivo fluam para a Braze. Siga as instruções de instalação da Segment para adicionar a dependência do plugin (via Swift Package Manager ou CocoaPods) e inicializá-lo com sua instância de analytics da Segment.

O código-fonte da integração do [modo de dispositivo iOS](https://github.com/braze-inc/braze-segment-swift) é mantido pela Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

{% endtab %}
{% tab Web ou JavaScript %}

A estrutura Braze Web Mode (Actions) da Segment é recomendada para configurar a Braze como um destino de modo de dispositivo para sua fonte web.

Na Segment, selecione **Actions** como sua estrutura de destino e **Device Mode** como seu modo de conexão.

![Configuração de destino da Segment mostrando a estrutura Actions e o Device Mode selecionados.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
O código-fonte do [plugin React Native Braze](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) é mantido pela Segment e é atualizado regularmente para refletir as novas versões do Braze SDK.

Ao conectar uma fonte React Native da Segment à Braze, configure uma origem e um destino por sistema operacional. Por exemplo, um destino para iOS e um destino para Android.

Na base de código do seu aplicativo, inicialize condicionalmente o Segment SDK por tipo de dispositivo, usando a respectiva chave de gravação de origem associada a cada app.

Quando um token por push é registrado de um dispositivo e enviado à Braze, ele é associado ao identificador do app usado na inicialização do SDK. A inicialização condicional por tipo de dispositivo ajuda a confirmar que todos os tokens por push enviados à Braze estão associados ao aplicativo relevante.

{% alert important %}
Se o aplicativo React Native inicializar a Braze com o mesmo identificador de aplicativo da Braze para todos os dispositivos, todos os usuários do React Native serão considerados usuários de Android ou iOS na Braze, e todos os tokens por push serão associados a esse sistema operacional.
{% endalert %}

Para configurar a Braze como um destino de modo de dispositivo para cada origem, selecione **Actions** como a **Destination framework** e, em seguida, selecione **Save**.

{% endtab %}
{% endtabs %}

#### Integração de servidor para servidor {#server-to-server-integration}

Também chamada de modo de nuvem, essa integração encaminha dados da Segment para as REST APIs da Braze. Use a estrutura [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) da Segment para configurar um destino em modo de nuvem para qualquer uma de suas origens.

Diferentemente da integração lado a lado, a integração servidor a servidor não oferece suporte aos recursos da interface do usuário da Braze, como mensagens no app, Content Cards ou registro automático de token por push. Também existem dados [capturados automaticamente]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) (como usuários anônimos e campos no nível do dispositivo) que não estão disponíveis no modo de nuvem.

Se quiser usar esses dados e recursos, considere adotar a integração lado a lado (modo de dispositivo) do SDK.

O código-fonte do [destino Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) é mantido pela Segment.

### Etapa 3: Configurações {#step-3-settings}

Defina as configurações para seu destino. Nem todas as configurações se aplicarão a todos os tipos de destinos.

{% tabs local %}
{% tab Mobile Device-Mode %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador do app | O identificador de aplicativo usado para fazer referência ao aplicativo específico. Isso pode ser encontrado no dashboard da Braze em **Manage Settings** |
| Endpoint personalizado da API<br>(endpoint de SDK) | Seu endpoint de SDK da Braze que corresponde à sua instância (como `sdk.iad-01.braze.com`) |
| Região do endpoint | Sua instância da Braze (como US 01, US 02, EU 01 etc.) |
| Ativar o registro automático de mensagens no app | Desative essa opção se quiser registrar manualmente as mensagens no app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurações" }

{% endtab %}
{% tab Web Device-Mode %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador do app | O identificador de aplicativo usado para fazer referência ao aplicativo específico. Isso pode ser encontrado no dashboard da Braze em **Manage Settings** |
| Endpoint personalizado da API<br>(endpoint de SDK) | Seu endpoint de SDK da Braze que corresponde à sua instância (como `sdk.iad-01.braze.com`) |
| ID de push para web do Safari | Caso ofereça suporte ao push do Safari, especifique essa opção com o ID de push para web que você forneceu à Apple ao criar o certificado de push do Safari (começa com `web`, como `web.com.example.domain`). |
| Versão do Braze Web SDK | A versão do Braze Web SDK que você gostaria de usar |
| Enviar automaticamente mensagens no app | Por padrão, todas as mensagens no app para as quais um usuário é elegível são automaticamente entregues ao usuário. Desative essa opção se quiser exibir manualmente as mensagens no app. |
| Não carregar Font Awesome | A Braze usa Font Awesome para os ícones de mensagens no app. Por padrão, a Braze carregará automaticamente o FontAwesome a partir do CDN do FontAwesome. Para desativar esse comportamento (por exemplo, porque seu site usa uma versão personalizada do FontAwesome), defina essa opção como `TRUE`. Observe que, se fizer isso, você será responsável por garantir que o FontAwesome seja carregado em seu site; caso contrário, as mensagens no app poderão não ser renderizadas corretamente. |
| Ativar mensagens no app em HTML | Quando ativada, essa opção permite que os usuários do dashboard da Braze usem mensagens HTML no app. |
| Abrir mensagens no app em uma nova guia | Por padrão, os links de cliques em mensagens no app são carregados na guia atual ou em uma nova guia, conforme especificado no dashboard, mensagem por mensagem. Defina essa opção como `TRUE` para forçar todos os links de cliques em mensagens no app a abrirem em uma nova guia ou janela. |
| Índice z de mensagens no app | Forneça um valor para essa opção para substituir os índices z padrão da Braze. |
| Exigir o cancelamento explícito de mensagens no app | Por padrão, quando uma mensagem no app estiver sendo exibida, pressionar o botão de escape ou clicar no fundo acinzentado da página descartará a mensagem. Defina essa opção como true para evitar esse comportamento e exigir um clique explícito no botão para descartar as mensagens. |
| Intervalo mínimo entre ações-gatilho em segundos | O padrão é 30.<br>Por padrão, uma ação-gatilho só será disparada se pelo menos 30 segundos tiverem se passado desde a última ação-gatilho. Forneça um valor para essa opção de configuração para substituir o padrão por um valor próprio. Não recomendamos que esse valor seja menor que 10 para evitar que o usuário receba notificações em excesso. |
| Local do service worker | Por padrão, ao registrar usuários para notificações por push na web, a Braze procurará o arquivo de service worker necessário no diretório raiz do seu servidor web em `/service-worker.js`. Se quiser hospedar o service worker em um caminho diferente nesse servidor, forneça um valor para essa opção que seja o caminho absoluto para o arquivo. (por exemplo, `/mycustompath/my-worker.js`). Observe que a definição de um valor aqui limita o escopo das notificações por push em seu site. A título de ilustração, no exemplo acima, como o arquivo do service worker está localizado no diretório `/mycustompath/`, `requestPushPermission` só pode ser chamado a partir de páginas da web que comecem com `http://yoursite.com/mycustompath/`. |
| Desativar a manutenção do token por push | Por padrão, os usuários que já concederam permissão de push para web sincronizarão seu token por push com o backend da Braze automaticamente em novas sessões para garantir a entregabilidade. Para desativar esse comportamento, defina a opção como `FALSE`. |
| Gerenciar o service worker externamente | Se você tiver seu próprio service worker para registrar e controlar o ciclo de vida, defina essa opção como `TRUE`, e o Braze SDK não registrará nem cancelará o registro de um service worker. Se essa opção for definida como `TRUE`, para que o push funcione corretamente, você mesmo deverá registrar o service worker antes de chamar `requestPushPermission` e garantir que ele contenha o código do service worker da Braze, seja com `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` ou incluindo o conteúdo desse arquivo diretamente. Quando essa opção é `TRUE`, a opção `serviceWorkerLocation` é irrelevante e é ignorada. |
| Nonce de segurança de conteúdo | Se você fornecer um valor para essa opção, o Braze SDK adicionará o nonce a todos os elementos `<script>` e `<style>` criados pelo SDK. Isso permite que o Braze SDK trabalhe com a política de segurança de conteúdo do seu site. Além de definir esse nonce, talvez seja necessário permitir o carregamento do FontAwesome, o que pode ser feito adicionando `use.fontawesome.com` à sua lista de permissões da política de segurança de conteúdo ou usando a opção `doNotLoadFontAwesome` e carregando-o manualmente. |
| Permitir atividade de rastreador | Por padrão, o Braze Web SDK ignora a atividade de spiders ou rastreadores da web conhecidos, como o Google, com base na string do agente do usuário. Isso economiza pontos de dados, torna a análise de dados mais precisa e pode melhorar a classificação da página. No entanto, se quiser que a Braze registre a atividade desses rastreadores, defina essa opção como `TRUE`. |
| Ativar o registro | Defina como `TRUE` para ativar o registro por padrão. Observe que isso fará com que a Braze registre no console JavaScript, que é visível para todos os usuários. Antes de liberar sua página para produção, você deve removê-lo ou fornecer outro agente de registro com `setLogger`. |
| Permitir JavaScript fornecido pelo usuário | Por padrão, o Braze Web SDK não permite ações de clique em JavaScript fornecidas pelo usuário, pois permite que os usuários do dashboard da Braze executem JavaScript no seu site. Para indicar que você confia nos usuários do dashboard da Braze para escrever ações de clique em JavaScript não maliciosas, defina essa propriedade como `TRUE`. Se `enableHtmlInAppMessages` for `TRUE`, essa opção também será definida como `TRUE`. |
| Versão do app | Se você fornecer um valor para essa opção, os eventos de usuário enviados à Braze serão associados à versão fornecida, que pode ser usada para segmentação de usuários. |
| Tempo limite da sessão em segundos | O padrão é 30.<br>Por padrão, as sessões são encerradas após 30 minutos de inatividade. Forneça um valor para essa opção de configuração para substituir o padrão por um valor próprio. |
| Lista de permissões de propriedades do dispositivo | Por padrão, o Braze SDK detecta e coleta automaticamente todas as propriedades do dispositivo em `DeviceProperties`. Para substituir esse comportamento, forneça uma matriz de `DeviceProperties`. Observe que, sem algumas propriedades, nem todos os recursos funcionam corretamente. Por exemplo, a entrega no fuso local não funcionará sem o fuso horário. |
| Localização | Por padrão, todas as mensagens visíveis ao usuário geradas pelo SDK são exibidas no idioma do navegador do usuário. Forneça um valor para essa opção para substituir esse comportamento e forçar um idioma específico. O valor dessa opção deve ser um código de idioma ISO 639-1. |
| Sem cookies | Por padrão, o Braze SDK armazena pequenas quantidades de dados (IDs de usuário, IDs de sessão) em cookies. Isso é feito para permitir que a Braze reconheça usuários e sessões em diferentes subdomínios do seu site. Se isso for um problema para você, passe `TRUE` para essa opção para desativar o armazenamento de cookies e confiar inteiramente no localStorage do HTML 5 para identificar usuários e sessões. |
| Rastrear todas as páginas | **Somente modo de dispositivo web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino da estrutura Web Actions, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Isso enviará todas as [chamadas de página](https://segment.com/docs/spec/page/) para a Braze como um evento "Loaded/Viewed a Page". |
| Rastrear apenas páginas nomeadas | **Somente modo de dispositivo web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino da estrutura Web Actions, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Isso enviará apenas chamadas de página para a Braze com um nome associado a elas. |
| Registrar compra quando a receita estiver presente | **Somente modo de dispositivo web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino da estrutura Web Actions, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Quando essa opção estiver ativada, todas as chamadas de rastreamento com a propriedade de receita dispararão um evento de compra. |
| Rastrear apenas usuários conhecidos | **Somente modo de dispositivo web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino Web Actions Framework, onde essa configuração pode ser ativada por meio de mapeamentos.<br><br>Se ativada, essa configuração posterga a chamada de `window.braze.initialize` até que haja um `userId` válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurações" }

{% endtab %}
{% tab Cloud-Mode %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador do app | O identificador de aplicativo usado para fazer referência ao aplicativo específico. Isso pode ser encontrado no dashboard da Braze em **Manage Settings** |
| Chave da API REST | Isso pode ser encontrado no dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint personalizado da REST API | O endpoint REST da Braze que corresponde à sua instância (como rest.iad-01.braze.com). |
| Atualizar somente usuários existentes | **Somente modo de nuvem de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino Cloud Actions Framework, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Determina se apenas os usuários existentes serão atualizados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurações" }

{% endtab %}
{% endtabs %}

### Etapa 4: Mapeie os métodos {#methods}

A Braze oferece suporte aos métodos [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) e [Track](https://segment.com/docs/spec/track/) da Segment. Os tipos de identificadores usados nesses métodos dependerão do fato de os dados estarem sendo enviados por meio de uma integração servidor a servidor (modo nuvem) ou lado a lado (modo dispositivo). Nos destinos Braze Web Mode Actions e Cloud Mode Actions, você também pode optar por configurar um mapeamento para uma [chamada de alias da Segment](https://segment.com/docs/connections/spec/alias/).

{% alert note %}
Embora os aliases de usuário sejam suportados como um identificador no destino Braze Cloud Mode (Actions), deve-se notar que a chamada de alias da Segment não está diretamente relacionada aos aliases de usuário da Braze.
{% endalert %}

| Tipo de identificador | Destinos aceitos |
| --------------- | --------------------- |
| `userId` (`external_id`) | Todos |
| Usuário anônimo | Destinos do modo dispositivo |
| Alias de usuário | Destinos no modo nuvem |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Mapeie os métodos" }

O destino Cloud Mode (Actions) oferece uma [ação Create Alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) que pode ser usada para criar um usuário somente de alias ou adicionar um alias a um perfil `external_id` existente. A [ação Identify User](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) pode ser usada juntamente com a ação Create Alias para mesclar um usuário somente de alias com um `external_id` depois que um estiver disponível para o usuário.

Também é possível criar uma solução alternativa e usar o `braze_id` para enviar dados de usuários anônimos no modo de nuvem. Para isso, é necessário incluir manualmente o `braze_id` do usuário em todas as suas chamadas à API da Segment. Você pode saber mais sobre como configurar essa solução alternativa na [documentação da Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Os dados de destinos enviados à Braze podem ser agrupados em lotes dentro do Cloud Mode Actions. Os tamanhos dos lotes são limitados a 75 eventos, e esses lotes se acumulam em um período de 30 segundos antes de serem descarregados. O agrupamento de solicitações é feito por ação. Por exemplo, as chamadas de identificação (atributos) serão agrupadas em uma solicitação e as chamadas de rastreamento (eventos personalizados) serão agrupadas em uma segunda solicitação. A Braze recomenda ativar esse recurso, pois ele reduz o número de solicitações enviadas da Segment para a Braze. Por sua vez, isso reduzirá o risco de o destino atingir os limites de frequência da Braze e tentar novamente as solicitações.

Você pode ativar a criação de lotes para uma ação navegando até Braze Destination > **Mappings**. A partir daí, clique no ícone de três pontos à direita do mapeamento e selecione **Edit Mapping**. Role até a parte inferior da seção **Select mappings** e verifique se a opção **Batch Data to Braze** está definida como **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

A chamada [Identify](https://segment.com/docs/spec/identify/) permite vincular um usuário às suas ações e registrar atributos sobre ele.

Certas características especiais da Segment são mapeadas para campos de perfil de atributo padrão na Braze:

| Características especiais da Segment | Atributos padrão da Braze |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identify" }

Outros campos de perfil reservados da Braze, como `email_subscribe` e `push_subscribe`, podem ser enviados usando a convenção de nomenclatura da Braze para esses campos e passando-os como características em uma chamada de identificação.

##### Adição de um usuário a um grupo de inscrições {#adding-a-user-to-a-subscription-group}

Também é possível inscrever ou cancelar a inscrição de um usuário em um determinado grupo de inscrições usando os seguintes campos no parâmetro traits.

Use o campo reservado do perfil da Braze chamado `braze_subscription_groups`, que pode ser associado a um vetor de objetos. Cada objeto do vetor deve ter duas chaves reservadas:

1. `subscription_group_state`: Indica se o usuário está `"subscribed"` ou `"unsubscribed"` em um grupo de inscrições específico.
2. `subscription_group_id`: Representa o ID exclusivo do grupo de inscrições. Você pode encontrar esse ID no dashboard da Braze, em **Subscription Group Management**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Atributos personalizados {#custom-attributes}

Todas as outras características serão registradas como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Método da Segment | Método da Braze | Exemplo |
|---|---|---|
| Identify com ID do usuário | Definir ID externo | Segment:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identify com características reservadas | Definir atributos do usuário | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identify com características personalizadas | Definir atributos personalizados | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify com ID do usuário e características | Segment: Definir ID externo e atributo | Combine os métodos anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos personalizados" }

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), esses mapeamentos podem ser definidos usando a ação Update User Profile.

{% alert important %}
Ao passar dados de atributos de usuário, verifique se só passa valores para atributos que foram alterados desde a última atualização. Isso garantirá que não registre pontos de dados desnecessariamente. Para fontes do lado do cliente, use a ferramenta [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de código aberto da Segment para otimizar sua integração e limitar o uso de pontos de dados, eliminando chamadas `identify()` duplicadas da Segment.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Quando você rastrear um evento, registraremos esse evento como um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) usando o nome fornecido.

Os metadados enviados dentro do objeto de propriedades da chamada de rastreamento serão registrados na Braze como as propriedades de evento personalizado para o evento associado. Todos os [tipos de dados de propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) são compatíveis.

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), esses mapeamentos podem ser definidos usando a ação Track Event.

| Método da Segment | Método da Braze | Exemplo |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Registrado como um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events). | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");` |
| [Track com propriedades](https://segment.com/docs/spec/track/) | Registrado como [propriedade de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track com produto](https://segment.com/docs/spec/track/) | Registrado como um [evento de compra]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Pedido concluído {#order-completed}

Quando você rastrear um evento com o nome `Order Completed` usando o formato descrito na [API de eCommerce](https://segment.com/docs/spec/ecommerce/v2/) da Segment, registraremos os produtos que você listou como [compras]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), o mapeamento padrão pode ser personalizado pela ação Track Purchase.

{% endtab %}

{% tab Page %}
#### Page {#page}

A chamada [Page](https://segment.com/docs/spec/page/) permite registrar sempre que um usuário vê uma página do seu site, juntamente com quaisquer propriedades opcionais sobre a página.

Esse tipo de evento pode ser usado como um gatilho nos destinos Web Mode Actions e Cloud Actions para registrar um evento personalizado na Braze.
{% endtab %}

{% endtabs %}

### Etapa 5: Teste sua integração {#step-5-test-your-integration}

Ao usar a integração lado a lado (modo de dispositivo), suas métricas de [visão geral]({{site.baseurl}}/user_guide/analytics/dashboards/home) (sessões vitalícias, MAU, usuário ativo diário, aderência, sessões diárias e sessões diárias por MAU) podem ser usadas para assegurar que a Braze receba dados da Segment.

Você pode visualizar seus dados nas páginas de [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) ou [receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data), ou [criando um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment). A página **Eventos personalizados** do dashboard permite que você visualize as contagens de eventos personalizados ao longo do tempo. Observe que você não poderá usar [fórmulas]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula) que incluam estatísticas de MAU e DAU ao usar uma integração de servidor para servidor (modo de nuvem).

Se estiver enviando dados de compra para a Braze (veja o pedido concluído na guia **Track** da [etapa 3](#methods)), a página de [receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) permite visualizar dados sobre receita ou compras em períodos específicos ou a receita total do seu app.

[Criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) permite filtrar os usuários com base nos dados de eventos e atributos personalizados.

{% alert important %}
Se você usar uma integração de servidor para servidor (modo de nuvem), os filtros relacionados aos dados de sessão coletados automaticamente (como "primeiro app usado" e "último app usado") não funcionarão. Use uma integração lado a lado (modo de dispositivo) se quiser usá-los na sua integração da Segment e da Braze.
{% endalert %}

## Exclusão e supressão de usuários {#user-deletion-and-suppression}

Se precisar excluir ou suprimir usuários, note que [o recurso de exclusão de usuários da Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **é** mapeado para o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze. Observe que a verificação dessas exclusões pode levar até 30 dias.

É necessário selecionar um identificador de usuário comum entre a Braze e a Segment (como em `external_id`). Depois de iniciar uma solicitação de exclusão com a Segment, você pode visualizar o status na guia de solicitações de exclusão no dashboard da Segment.

## Replays da Segment {#segment-replays}

A Segment presta um serviço aos clientes para "reproduzir" todos os dados históricos em um novo parceiro de tecnologia. Os novos clientes da Braze que desejarem importar todos os dados históricos relevantes poderão fazê-lo por meio da Segment. Fale com seu representante da Segment se isso for algo de seu interesse.

A Segment se conectará ao nosso [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para importar dados de usuários para a Braze em seu nome.

{% alert important %}
Todos os identificadores compatíveis com o destino Cloud Mode Actions são compatíveis como parte dos replays da Segment.
{% endalert %}

## Melhores práticas {#best-practices}

{% details Revise os casos de uso para evitar excedentes de dados. %}

A Segment **não** limita o número de elementos de dados que os clientes enviam para ela. A Segment permite que você envie todos ou decida quais eventos serão enviados à Braze. Em vez de enviar todos os seus eventos usando a Segment, sugerimos que você analise os casos de uso com suas equipes de marketing e editorial para determinar quais eventos serão enviados à Braze para evitar excedentes de dados.

{% enddetails %}

{% details Entenda a diferença entre o endpoint personalizado da API e o endpoint personalizado da REST API nas configurações de destino do modo dispositivo móvel. %}

| Terminologia da Braze | Equivalente na Segment |
| ----------------- | ------------------ |
| Endpoint do SDK da Braze | Endpoint personalizado da API |
| Endpoint REST da Braze | Endpoint personalizado da REST API |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Melhores práticas" }

Seu endpoint da Braze API (chamado de "Custom API Endpoint" na Segment) é o endpoint de SDK que a Braze configura para seu SDK (por exemplo, `sdk.iad-03.braze.com`). Seu endpoint da REST API da Braze (chamado de "Custom REST API Endpoint" na Segment) é o endpoint da REST API (por exemplo, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Certifique-se de que o endpoint personalizado da API esteja inserido corretamente nas configurações de destino do modo dispositivo móvel. %}

| Terminologia da Braze | Equivalente na Segment |
| ----------------- | ------------------ |
| Endpoint do SDK da Braze | Endpoint personalizado da API |
| Endpoint REST da Braze | Endpoint personalizado da REST API |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Melhores práticas" }

É necessário seguir o formato adequado para não correr o risco de informar o endpoint do Braze SDK incorretamente. Seu endpoint do Braze SDK não deve incluir `https://` (por exemplo, `sdk.iad-03.braze.com`), senão a integração da Braze será interrompida. Isso é necessário porque a Segment prefixa automaticamente seu endpoint com `https://`, o que resulta em uma tentativa de inicialização da Braze com o endereço inválido `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances do mapeamento de dados. %}

Cenários em que os dados não serão transmitidos conforme o esperado:

1. Atributos personalizados aninhados
  - Embora [os atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) possam tecnicamente ser enviados à Braze por meio da Segment, **toda a carga útil** será enviada a cada vez. Isso incorrerá em [pontos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points) por chave passada no objeto aninhado toda vez que a carga útil for enviada.<br><br> Para gastar apenas um subconjunto de pontos de dados quando a carga útil é enviada, você pode usar o recurso de [funções de destino](https://segment.com/docs/connections/functions/destination-functions/) personalizadas pertencente à Segment. Esse recurso da plataforma Segment permite que você personalize a forma como os dados são enviados para destinos downstream.

  {% alert note %}
  As funções de destinos personalizados são controladas na Segment, e a Braze tem insight limitado sobre as funções que foram configuradas externamente.
  {% endalert %}

{: start="2"}
2. Passagem de dados anônimos de servidor para servidor.
  - Os clientes podem usar as bibliotecas de servidor para servidor da Segment para canalizar dados anônimos para outros sistemas. Consulte a seção de mapeamento de métodos para saber mais sobre como enviar usuários sem um `external_id` para a Braze por meio de uma integração de servidor para servidor (modo de nuvem).

{% enddetails %}

{% details Personalização da inicialização da Braze. %}

Há várias maneiras diferentes de personalizar a Braze: push, mensagens no app, Content Cards e inicialização. Com uma integração lado a lado, você ainda pode personalizar o push, as mensagens no app e os Content Cards, como faria com uma integração direta da Braze.

No entanto, personalizar quando o Braze SDK é integrado ou especificar as configurações de inicialização é uma tarefa complicada que nem sempre é possível. Isso ocorre porque a Segment inicializa o Braze SDK para você quando a inicialização da Segment ocorre.

{% enddetails %}

{% details Envio de deltas para a Braze. %}

Ao passar dados de atributos de usuário, verifique se só passa valores para atributos que foram alterados desde a última atualização. Isso evitará o registro de pontos de dados desnecessários. Para fontes do lado do cliente, use a ferramenta [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de código aberto da Segment para otimizar sua integração e limitar o uso de pontos de dados, eliminando chamadas `identify()` duplicadas da Segment.

{% enddetails %}

{% details Use o data center correto da Braze. %}

A Segment usa seu data center da Braze para obter o endpoint REST da Braze apropriado (como `https://rest.iad-01.braze.com`) para fazer chamadas de servidor para servidor.

{% enddetails %}

{% details Remova o endpoint personalizado da REST API ao usar o Event Tester da Segment. %}

O Event Tester da Segment envia eventos para o endpoint da REST API `/users/track` da Braze e retorna um erro `401 Invalid API Key` se um endpoint personalizado da REST API estiver definido nas configurações de destino da Braze, mesmo quando esse endpoint estiver correto. Remova o valor do endpoint personalizado da REST API na Segment para permitir que o Event Tester funcione corretamente.

{% enddetails %}

{% details Aguarde a atualização após configurar uma nova fonte. %}

A Segment mantém suas configurações em cache por um longo período, então ao configurar uma nova fonte (como mudar do modo nuvem para o modo dispositivo), seu app pode não apresentar o novo comportamento ou dados até que o cache seja renovado. Tenha isso em mente ao planejar a adição de uma fonte.

{% enddetails %}