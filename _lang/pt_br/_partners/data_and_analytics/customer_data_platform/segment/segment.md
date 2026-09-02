---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Este artigo de referência descreve a parceria entre a Braze e a Segment, uma CDP que coleta e encaminha informações entre fontes na sua stack de marketing."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> A [Segment](https://segment.com) é uma CDP que ajuda você a coletar, limpar e ativar os dados dos seus clientes.

A integração da Braze com a Segment permite rastrear seus usuários e encaminhar dados para vários provedores de análise de dados de usuários. A Segment permite que você:

- Sincronize o [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage) com a Braze para uso em Campaigns da Braze e na segmentação de Canvas.
- [Importe dados entre as duas plataformas](#integration-options). Oferecemos uma integração lado a lado de SDK para seus aplicativos Android, iOS e web e uma integração de servidor para servidor para sincronizar seus dados com as REST APIs da Braze.
- [Conecte os dados à Segment pelo Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents).

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Segment | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| Source instalado e [bibliotecas](https://segment.com/docs/sources/) de source da Segment | A origem de quaisquer dados enviados para a Segment, como apps móveis, websites ou servidores backend.<br><br>Você deve instalar as bibliotecas no seu app, site ou servidor antes de configurar um fluxo `Source > Destination` com sucesso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar a Braze e a Segment, você deve configurar a [Braze como um destino](#connection-settings) de acordo com o [tipo de integração escolhido](#integration-options) (modo de conexão). Se você é um cliente novo da Braze, pode transmitir dados históricos para a Braze usando os [replays da Segment](#segment-replays). Em seguida, você deve configurar os [mapeamentos](#methods) e [testar sua integração](#step-4-test-your-integration) para garantir um fluxo de dados suave entre a Braze e a Segment.

### Etapa 1: Criar um destino Braze {#connection-settings}

Depois de configurar suas fontes com sucesso, você precisará configurar a Braze como um [destino](https://segment.com/docs/destinations/) para cada fonte (iOS, Android, web, etc.). Você terá muitas opções para personalizar o fluxo de dados entre a Braze e a Segment usando as configurações de conexão.

### Etapa 2: Escolher o framework de destino e o tipo de conexão {#integration-options}

Na Segment, navegue até **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![Página de configuração da fonte. Esta página inclui configurações para definir o framework de destino como "actions" ou "classic" e definir o modo de conexão como "cloud mode" ou "device mode".]({% image_buster /assets/img/segment/setup.png %})

Você pode integrar a fonte web da Segment (Analytics.js) e as bibliotecas nativas do lado do cliente com a Braze usando uma integração lado a lado (device-mode) ou uma integração servidor a servidor (cloud-mode).

Sua escolha de modo de conexão será determinada pelo tipo de fonte para a qual o destino está configurado.

| Integração | Detalhes |
| ----------- | ------- |
| [Lado a lado<br>(device-mode)](#side-by-side-sdk-integration) | Usa o SDK da Segment para traduzir eventos em chamadas nativas da Braze, permitindo acesso a recursos mais profundos e uso mais abrangente da Braze do que a integração servidor a servidor.<br><br>Note que a Segment não suporta todos os métodos da Braze (por exemplo, Content Cards). Para usar um método da Braze que não está mapeado por meio de um mapeamento correspondente, você precisará invocar o método adicionando código nativo da Braze à sua base de código. |
| [Servidor a servidor<br>(cloud-mode)](#server-to-server-integration) | Encaminha dados da Segment para os endpoints da REST API da Braze.<br><br>Não suporta recursos de interface da Braze, como mensagens no app, Content Cards ou notificações por push. Também existem dados capturados automaticamente, como campos no nível do dispositivo, que não estão disponíveis por meio deste método.<br><br>Considere uma integração lado a lado se desejar usar esses recursos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Escolher o framework de destino e o tipo de conexão" }

{% alert note %}
Visite a [Segment](https://segment.com/docs/destinations/#connection-modes) para saber mais sobre as duas opções de integração (modos de conexão), incluindo os benefícios de cada uma.
{% endalert %}

#### Integração SDK lado a lado {#side-by-side-sdk-integration}

Também chamada de device-mode, essa integração mapeia o SDK da Segment e seus [métodos](#methods) para o SDK da Braze, permitindo acesso a todos os recursos que nosso SDK oferece, como push, mensagens no app e outros métodos nativos da Braze.

{% alert note %}
Ao usar o device-mode da Segment, deixe a Segment inicializar a Braze. Não inicialize também o SDK da Braze no seu app. O plugin de destino configura a Braze e abre sessões; uma segunda inicialização nativa pode registrar sessões duplicadas. Use o `identify` da Segment para definir o ID do usuário. O plugin mapeia essa chamada para `changeUser()`.
{% endalert %}

{% alert important %}
Para integrações device-mode em dispositivos móveis, você deve adicionar o plugin de destino da Braze ao seu app além de configurar o destino no dashboard da Segment. O SDK da Segment não inclui o plugin da Braze por padrão — sem ele, o SDK da Segment não consegue encaminhar dados ou chamadas de métodos mapeados para a Braze, e recursos como push, mensagens no app e Content Cards não funcionarão. Consulte as guias específicas por plataforma nesta seção para instruções de instalação.
{% endalert %}

Ao usar uma conexão device-mode, de forma semelhante à integração nativa do SDK da Braze, o SDK da Braze atribuirá um `device_id` e um identificador de backend, `braze_id`, a cada usuário. Isso permite que a Braze capture atividade anônima do dispositivo correspondendo esses identificadores em vez do `userId`.

{% alert note %}
Se você usa [filtros de destino](https://segment.com/docs/connections/destinations/destination-filters/) com destinos device-mode (Kotlin ou Swift), deve configurar o plugin de destino com o suporte a filtros ativado. Consulte a [documentação de filtros de destino da Segment](https://segment.com/docs/connections/destinations/destination-filters/) para detalhes sobre as versões de plugin suportadas.
{% endalert %}

{% tabs local %}
{% tab Android %}

{% alert important %}
O código-fonte da integração device-mode para Android é mantido pela Braze e atualizado regularmente para refletir novos lançamentos do SDK da Braze.

<br>
O SDK da Braze que você usa dependerá de qual SDK da Segment você utiliza:

| | SDK da Segment | SDK da Braze |
| - | ----------- | --------- |
| Preferido | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legado | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integração SDK lado a lado" }


{% endalert %}

Para configurar a Braze como um destino device-mode para sua fonte Android, escolha **Actions** como o **Destination framework** e depois selecione **Save**.

Para concluir a integração lado a lado, você deve adicionar o [plugin de destino Braze Kotlin](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) ao seu app Android. Esse plugin faz a ponte entre o SDK da Segment e o SDK da Braze, permitindo que os dados em device-mode fluam para a Braze. Siga as instruções de instalação da Segment para adicionar a dependência do plugin e inicializá-lo com sua instância de analytics da Segment.

O código-fonte da integração [device-mode para Android](https://github.com/braze-inc/braze-segment-kotlin) é mantido pela Braze e atualizado regularmente para refletir novos lançamentos do SDK da Braze.

{% endtab %}
{% tab iOS %}

{% alert important %}
O código-fonte da integração device-mode para iOS é mantido pela Braze e atualizado regularmente para refletir novos lançamentos do SDK da Braze.

<br>
O SDK da Braze que você usa dependerá de qual SDK da Segment você utiliza:

| | SDK da Segment | SDK da Braze |
| - | ----------- | --------- |
| Preferido | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legado | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Integração SDK lado a lado" }
{% endalert %}

Para configurar a Braze como um destino device-mode para sua fonte iOS, escolha **Actions** como o **Destination framework** e depois selecione **Save**.

Para concluir a integração lado a lado, você deve adicionar o [plugin de destino Braze Swift](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) ao seu app iOS. Esse plugin faz a ponte entre o SDK da Segment e o SDK da Braze, permitindo que os dados em device-mode fluam para a Braze. Siga as instruções de instalação da Segment para adicionar a dependência do plugin (via Swift Package Manager ou CocoaPods) e inicializá-lo com sua instância de analytics da Segment.

O código-fonte da integração [device-mode para iOS](https://github.com/braze-inc/braze-segment-swift) é mantido pela Braze e atualizado regularmente para refletir novos lançamentos do SDK da Braze.

{% endtab %}
{% tab Web ou JavaScript %}

O framework Braze Web Mode (Actions) da Segment é recomendado para configurar a Braze como um destino device-mode para sua fonte web.

Na Segment, selecione **Actions** como seu framework de destino e **Device Mode** como seu modo de conexão.

![Configuração de destino da Segment mostrando o framework Actions e o Device Mode selecionados.]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
O código-fonte do [plugin Braze para React Native](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) é mantido pela Segment e atualizado regularmente para refletir novos lançamentos do SDK da Braze.

Ao conectar uma fonte React Native da Segment à Braze, você deve configurar uma fonte e um destino por sistema operacional. Por exemplo, configurar um destino iOS e um destino Android.

Na base de código do seu app, inicialize condicionalmente o SDK da Segment por tipo de dispositivo, usando a chave de escrita da fonte respectiva associada a cada app.

Quando um token por push é registrado em um dispositivo e enviado à Braze, ele é associado ao identificador de app usado na inicialização do SDK. A inicialização condicional por tipo de dispositivo ajuda a confirmar que quaisquer tokens por push enviados à Braze estão associados ao app relevante.

{% alert important %}
Se o app React Native inicializar a Braze com o mesmo identificador de app da Braze para todos os dispositivos, então todos os usuários do React Native serão considerados usuários Android ou iOS na Braze, e todos os tokens por push serão associados a esse sistema operacional.
{% endalert %}

Para configurar a Braze como um destino device-mode para cada fonte, escolha **Actions** como o **Destination framework** e depois selecione **Save**.

{% endtab %}
{% endtabs %}

#### Integração servidor a servidor {#server-to-server-integration}

Também chamada de cloud-mode, essa integração encaminha dados da Segment para as REST APIs da Braze. Use o framework [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) da Segment para configurar um destino cloud-mode para qualquer uma das suas fontes.

Diferente da integração lado a lado, a integração servidor a servidor não suporta recursos de interface da Braze, como mensagens no app, Content Cards ou registro automático de tokens por push. Também existem dados [capturados automaticamente]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection#user-data-collection) (como usuários anônimos e campos no nível do dispositivo) que não estão disponíveis via cloud-mode.

Se você deseja usar esses dados e recursos, considere usar a integração SDK lado a lado (device-mode).

O código-fonte do [destino Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) é mantido pela Segment.

### Etapa 3: Configurações {#step-3-settings}

Defina as configurações do seu destino. Nem todas as configurações se aplicam a todos os tipos de destino.

{% tabs local %}
{% tab Device-mode móvel %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador de app | O identificador de app usado para referenciar o app específico. Ele pode ser encontrado no dashboard da Braze em **Manage Settings**. |
| Endpoint de API personalizado<br>(endpoint de SDK) | Seu endpoint de SDK da Braze que corresponde à sua instância (como `sdk.iad-01.braze.com`). |
| Região do endpoint | Sua instância da Braze (como US 01, US 02, EU 01, etc.). |
| Ativar registro automático de mensagens no app | Desative esta opção se quiser registrar mensagens no app manualmente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurações" }

{% endtab %}
{% tab Device-mode web %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador de app | O identificador de app usado para referenciar o app específico. Ele pode ser encontrado no dashboard da Braze em **Manage Settings**. |
| Endpoint de API personalizado<br>(endpoint de SDK) | Seu endpoint de SDK da Braze que corresponde à sua instância (como `sdk.iad-01.braze.com`). |
| ID de push do website para Safari | Se você suporta push no Safari, deve especificar esta opção com o ID de push do website que você forneceu à Apple ao criar seu certificado de push para Safari (começa com `web`, por exemplo, `web.com.example.domain`). |
| Versão do Braze Web SDK | A versão do Braze Web SDK que você deseja usar. |
| Enviar automaticamente mensagens no app | Por padrão, todas as mensagens no app para as quais um usuário é elegível são entregues automaticamente. Desative esta opção se deseja exibir mensagens no app manualmente. |
| Não carregar Font Awesome | A Braze usa Font Awesome para ícones de mensagens no app. Por padrão, a Braze carrega automaticamente o FontAwesome a partir da CDN do FontAwesome. Para desativar esse comportamento (por exemplo, porque seu site usa uma versão personalizada do FontAwesome), defina esta opção como `TRUE`. Note que, se fizer isso, você é responsável por garantir que o FontAwesome esteja carregado no seu site — caso contrário, as mensagens no app podem não ser renderizadas corretamente. |
| Ativar mensagens no app em HTML | Ativar esta opção permitirá que os usuários do dashboard da Braze usem mensagens no app em HTML. |
| Abrir mensagens no app em uma nova guia | Por padrão, os links de cliques em mensagens no app carregam na guia atual ou em uma nova guia conforme especificado no dashboard, mensagem por mensagem. Defina esta opção como `TRUE` para forçar que todos os links de cliques em mensagens no app abram em uma nova guia ou janela. |
| Índice z de mensagens no app | Forneça um valor para esta opção para substituir os índices z padrão da Braze. |
| Exigir dispensa explícita de mensagem no app | Por padrão, quando uma mensagem no app está sendo exibida, pressionar a tecla Escape ou clicar no fundo acinzentado da página dispensará a mensagem. Defina esta opção como true para impedir esse comportamento e exigir um clique explícito no botão para dispensar mensagens. |
| Intervalo mínimo entre ações-gatilho em segundos | O padrão é 30.<br>Por padrão, uma ação-gatilho só será disparada se pelo menos 30 segundos tiverem passado desde a última ação-gatilho. Forneça um valor para esta opção de configuração para substituir esse padrão com um valor próprio. Não recomendamos tornar este valor menor que 10 para evitar excesso de notificações ao usuário. |
| Localização do service worker | Por padrão, ao registrar usuários para notificações web push, a Braze procurará o arquivo de service worker necessário no diretório raiz do seu servidor web em `/service-worker.js`. Se você deseja hospedar seu service worker em um caminho diferente nesse servidor, forneça um valor para esta opção que seja o caminho absoluto do arquivo. (por exemplo, `/mycustompath/my-worker.js`). Note que definir um valor aqui limita o escopo das notificações por push no seu site. Por exemplo, neste caso, como o arquivo do service worker está localizado no diretório `/mycustompath/`, `requestPushPermission` só pode ser chamado a partir de páginas web que começam com `http://yoursite.com/mycustompath/`. |
| Desativar manutenção de token por push | Por padrão, usuários que já concederam permissão de web push sincronizarão automaticamente seu token por push com o backend da Braze em novas sessões para garantir a entregabilidade. Para desativar esse comportamento, defina esta opção como `FALSE`. |
| Gerenciar service worker externamente | Se você tem seu próprio service worker que registra e controla o ciclo de vida, defina esta opção como `TRUE`, e o SDK da Braze não registrará nem cancelará o registro de um service worker. Se você definir esta opção como `TRUE`, para que o push funcione corretamente, você deve registrar o service worker por conta própria antes de chamar `requestPushPermission` e garantir que ele contenha o código do service worker da Braze, seja com `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` ou incluindo o conteúdo desse arquivo diretamente. Quando esta opção é `TRUE`, a opção `serviceWorkerLocation` é irrelevante e ignorada. |
| Nonce de segurança de conteúdo | Se você fornecer um valor para esta opção, o SDK da Braze adicionará o nonce a qualquer elemento `<script>` e `<style>` criado pelo SDK. Isso permite que o SDK da Braze funcione com a política de segurança de conteúdo do seu website. Além de definir este nonce, pode ser necessário permitir que o FontAwesome carregue, o que pode ser feito adicionando `use.fontawesome.com` à lista de permissões da sua política de segurança de conteúdo ou usando a opção `doNotLoadFontAwesome` e carregando-o manualmente. |
| Permitir atividade de crawlers | Por padrão, o Braze Web SDK ignora atividade de spiders ou crawlers conhecidos, como o Google, com base na string do user agent. Isso economiza pontos de dados, torna a análise de dados mais precisa e pode melhorar o posicionamento da página. No entanto, se você deseja que a Braze registre a atividade desses crawlers, pode definir esta opção como `TRUE`. |
| Ativar logging | Defina como `TRUE` para ativar o logging por padrão. Note que isso fará com que a Braze registre no console JavaScript, que é visível para todos os usuários. Antes de lançar sua página em produção, você deve remover isso ou fornecer um logger alternativo com `setLogger`. |
| Permitir JavaScript fornecido pelo usuário | Por padrão, o Braze Web SDK não permite ações de clique JavaScript fornecidas pelo usuário, pois isso permite que os usuários do dashboard da Braze executem JavaScript no seu site. Para indicar que você confia nos usuários do dashboard da Braze para escrever ações de clique JavaScript não maliciosas, defina esta propriedade como `TRUE`. Se `enableHtmlInAppMessages` for `TRUE`, esta opção também será definida como `TRUE`. |
| Versão do app | Se você fornecer um valor para esta opção, os eventos de usuário enviados à Braze serão associados à versão fornecida, que pode ser usada para segmentação de usuários. |
| Tempo limite de sessão em segundos | O padrão é 30.<br>Por padrão, as sessões expiram após 30 minutos de inatividade. Forneça um valor para esta opção de configuração para substituir esse padrão com um valor próprio. |
| Lista de permissões de propriedades do dispositivo | Por padrão, o SDK da Braze detecta e coleta automaticamente todas as propriedades do dispositivo em `DeviceProperties`. Para substituir esse comportamento, forneça um array de `DeviceProperties`. Note que sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, a entrega por fuso local não funcionará sem o fuso horário. |
| Localização | Por padrão, quaisquer mensagens geradas pelo SDK visíveis ao usuário serão exibidas no idioma do navegador do usuário. Forneça um valor para esta opção para substituir esse comportamento e forçar um idioma específico. O valor para esta opção deve ser um código de idioma ISO 639-1. |
| Sem cookies | Por padrão, o SDK da Braze armazenará pequenas quantidades de dados (IDs de usuário, IDs de sessão) em cookies. Isso é feito para permitir que a Braze reconheça usuários e sessões em diferentes subdomínios do seu site. Se isso representar um problema para você, passe `TRUE` para esta opção para desativar o armazenamento de cookies e depender inteiramente do HTML 5 localStorage para identificar usuários e sessões. |
| Rastrear todas as páginas | **Apenas para destino web device-mode clássico (manutenção)**<br><br>A Segment recomenda migrar para o destino de framework Web Actions, onde esta configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Isso enviará todas as [chamadas de página](https://segment.com/docs/spec/page/) à Braze como um evento "Loaded/Viewed a Page". |
| Rastrear apenas páginas nomeadas | **Apenas para destino web device-mode clássico (manutenção)**<br><br>A Segment recomenda migrar para o destino de framework Web Actions, onde esta configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Isso enviará à Braze apenas chamadas de página que tenham um nome associado a elas. |
| Registrar compra quando receita estiver presente | **Apenas para destino web device-mode clássico (manutenção)**<br><br>A Segment recomenda migrar para o destino de framework Web Actions, onde esta configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Quando esta opção está ativada, todas as chamadas Track com a propriedade de receita acionarão um evento de compra. |
| Rastrear apenas usuários conhecidos | **Apenas para destino web device-mode clássico (manutenção)**<br><br>A Segment recomenda migrar para o destino de framework Web Actions, onde esta configuração pode ser ativada por meio de mapeamentos.<br><br>Se ativada, esta nova configuração atrasa a chamada de `window.braze.initialize` até que haja um `userId` válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurações" }

{% endtab %}
{% tab Cloud-mode %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador de app | O identificador de app usado para referenciar o app específico. Ele pode ser encontrado no dashboard da Braze em **Manage Settings**. |
| Chave da API REST | Esta pode ser encontrada no seu dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint de REST API personalizado | Seu endpoint REST da Braze que corresponde à sua instância (como rest.iad-01.braze.com). |
| Atualizar apenas usuários existentes | **Apenas para destino cloud-mode clássico (manutenção)**<br><br>A Segment recomenda migrar para o destino de framework Cloud Actions, onde esta configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Determina se apenas usuários existentes devem ser atualizados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurações" }

{% endtab %}
{% endtabs %}

### Etapa 4: Mapear métodos {#methods}

A Braze suporta os métodos [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) e [Track](https://segment.com/docs/spec/track/) da Segment. Os tipos de identificadores usados nesses métodos dependerão de se os dados estão sendo enviados por meio de uma integração servidor a servidor (cloud-mode) ou lado a lado (device-mode). Nos destinos Braze Web Mode Actions e Cloud Mode Actions, você também pode optar por configurar um mapeamento para uma [chamada de alias da Segment](https://segment.com/docs/connections/spec/alias/).

{% alert note %}
Embora aliases de usuário sejam suportados como identificador no destino Braze Cloud Mode (Actions), é importante notar que a chamada de alias da Segment não está diretamente relacionada aos aliases de usuário da Braze.
{% endalert %}

| Tipo de identificador | Destino suportado |
| --------------- | --------------------- |
| `userId` (`external_id`) | Todos |
| Usuário anônimo | Destinos device-mode |
| Alias de usuário | Destinos cloud-mode |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 4: Mapear métodos" }

O destino Cloud Mode (Actions) oferece uma [ação Create Alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) que pode ser usada para criar um usuário somente com alias ou adicionar um alias a um perfil `external_id` existente. A [ação Identify User](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) pode ser usada junto com a ação Create Alias para mesclar um usuário somente com alias com um `external_id` depois que um se torna disponível para o usuário.

Também é possível criar uma solução alternativa e usar `braze_id` para enviar dados de usuários anônimos em cloud-mode. Isso requer incluir manualmente o `braze_id` do usuário em todas as suas chamadas de API da Segment. Você pode saber mais sobre como configurar essa solução alternativa na [documentação da Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Os dados de destinos enviados à Braze podem ser agrupados em lotes no Cloud Mode Actions. Os tamanhos de lote são limitados a 75 eventos, e esses lotes serão acumulados ao longo de um período de 30 segundos antes de serem enviados. O agrupamento em lotes de requisições é feito por ação. Por exemplo, chamadas Identify (atributos) serão agrupadas em uma requisição e chamadas Track (eventos personalizados) serão agrupadas em uma segunda requisição. A Braze recomenda ativar esse recurso, pois ele reduzirá o número de requisições enviadas da Segment para a Braze. Por sua vez, isso reduzirá o risco de o destino atingir os limites de frequência da Braze e ter que reenviar requisições.

Você pode ativar o agrupamento em lotes para uma ação navegando até seu destino Braze > **Mappings**. A partir daí, clique no ícone de 3 pontos ao lado do mapeamento e selecione **Edit Mapping**. Role até o final da seção **Select mappings** e certifique-se de que **Batch Data to Braze** esteja definido como **Yes**.


{% tabs local %}
{% tab Identify %}
#### Identify

A chamada [Identify](https://segment.com/docs/spec/identify/) permite vincular um usuário às suas ações e registrar atributos sobre ele.

Certas traits especiais da Segment são mapeadas para campos de atributos padrão de perfil na Braze:

| Traits especiais da Segment | Atributos padrão da Braze |
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

Outros campos de perfil reservados da Braze, como `email_subscribe` e `push_subscribe`, podem ser enviados usando a convenção de nomenclatura da Braze para esses campos e passando-os como traits em uma chamada identify.

##### Adicionando um usuário a um grupo de inscrições {#adding-a-user-to-a-subscription-group}

Você também pode inscrever ou cancelar a inscrição de um usuário em um determinado grupo de inscrições usando os seguintes campos no parâmetro de traits.

Use o campo de perfil reservado da Braze chamado `braze_subscription_groups`, que pode ser associado a um array de objetos. Cada objeto no array deve ter duas chaves reservadas:

1. `subscription_group_state`: Indica se o usuário está `"subscribed"` ou `"unsubscribed"` em um grupo de inscrições específico.
2. `subscription_group_id`: Representa o ID único do grupo de inscrições. Você pode encontrar este ID no dashboard da Braze em **Subscription Group Management**.

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

Todas as outras traits serão registradas como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Método da Segment | Método da Braze | Exemplo |
|---|---|---|
| Identify com ID de usuário | Definir ID externo | Segment: `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identify com traits reservadas | Definir atributos de usuário | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identify com traits personalizadas | Definir atributos personalizados | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identify com ID de usuário e traits | Segment: Definir ID externo e atributo | Combine os métodos anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos personalizados" }

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), esses mapeamentos podem ser configurados usando a ação Update User Profile.

{% alert important %}
Ao passar dados de atributos de usuário, verifique se você está passando apenas valores para atributos que mudaram desde a última atualização. Isso garantirá que você não registre pontos de dados desnecessariamente. Para fontes do lado do cliente, use a ferramenta de código aberto [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) da Segment para otimizar sua integração e limitar o uso de pontos de dados fazendo debounce de chamadas `identify()` duplicadas da Segment.

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

Quando você rastreia um evento, nós registraremos esse evento como um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events) usando o nome fornecido.

Metadados enviados no objeto de propriedades da chamada track serão registrados na Braze como as propriedades do evento personalizado para o evento associado. Todos os [tipos de dados de propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) são suportados.

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), esses mapeamentos podem ser configurados usando a ação Track Event.

| Método da Segment | Método da Braze | Exemplo |
|---|---|---|
| [Track](https://segment.com/docs/spec/track/) | Registrado como um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events). | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");` |
| [Track com propriedades](https://segment.com/docs/spec/track/) | Registrado como [propriedade do evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Track com produto](https://segment.com/docs/spec/track/) | Registrado como um [evento de compra]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Track" }

##### Pedido concluído {#order-completed}

Quando você rastreia um evento com o nome `Order Completed` usando o formato descrito na [API de eCommerce](https://segment.com/docs/spec/ecommerce/v2/) da Segment, nós registraremos os produtos listados como [compras]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data).

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), o mapeamento padrão pode ser personalizado por meio da ação Track Purchase.

{% endtab %}

{% tab Page %}
#### Page {#page}

A chamada [Page](https://segment.com/docs/spec/page/) permite registrar sempre que um usuário visualiza uma página do seu website, junto com quaisquer propriedades opcionais sobre a página.

Esse tipo de evento pode ser usado como gatilho nos destinos Web Mode Actions e Cloud Actions para registrar um evento personalizado na Braze.
{% endtab %}

{% endtabs %}

### Etapa 5: Testar sua integração {#step-5-test-your-integration}

Ao usar a integração lado a lado (device-mode), suas métricas de [visão geral]({{site.baseurl}}/user_guide/analytics/dashboards/home) (sessões vitalícias, MAU, DAU, aderência, sessões diárias e sessões diárias por MAU) podem ser usadas para garantir que a Braze está recebendo dados da Segment.

Você pode visualizar seus dados nas páginas de [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data#custom-event-data) ou [receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data), ou [criando um Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment). A página **Custom Events** do dashboard permite visualizar contagens de eventos personalizados ao longo do tempo. Note que você não poderá usar [fórmulas]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula#creating-a-formula) que incluem estatísticas de MAU e DAU ao usar uma integração servidor a servidor (cloud-mode).

Se você está enviando dados de compra para a Braze (veja pedido concluído na guia **Track** da [Etapa 3](#methods)), a página de [receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data#revenue-data) permite visualizar dados de receita ou compras em períodos específicos ou a receita total do seu app.

[Criar um Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#creating-a-segment) permite filtrar seus usuários com base nos dados de eventos personalizados e atributos.

{% alert important %}
Se você usa uma integração servidor a servidor (cloud-mode), filtros relacionados a dados de sessão capturados automaticamente (como "primeiro uso do app" e "último uso do app") não funcionarão. Use uma integração lado a lado (device-mode) se quiser usar esses filtros na sua integração entre Segment e Braze.
{% endalert %}

## Exclusão e supressão de usuários {#user-deletion-and-suppression}

Se você precisar excluir ou suprimir usuários, observe que o [recurso de exclusão de usuários da Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **está** mapeado para o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze. A verificação dessas exclusões pode levar até 30 dias.

Você precisa garantir que selecionou um identificador de usuário comum entre a Braze e a Segment (como o `external_id`). Após iniciar uma solicitação de exclusão com a Segment, você pode visualizar o status na guia de solicitações de exclusão no seu dashboard da Segment.

## Replays da Segment {#segment-replays}

A Segment oferece um serviço para seus clientes que permite "reproduzir" todos os dados históricos para uma nova parceira de tecnologia. Novos clientes da Braze que desejam importar todos os dados históricos relevantes podem fazer isso por meio da Segment. Fale com seu representante da Segment se isso for do seu interesse.

A Segment se conectará ao nosso [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para importar dados de usuários na Braze em seu nome.

{% alert important %}
Todos os identificadores compatíveis com o destino Cloud Mode Actions são compatíveis como parte dos Replays da Segment.
{% endalert %}

## Práticas recomendadas {#best-practices}

{% details Revise os casos de uso para evitar excedentes de dados. %}

A Segment **não** limita o número de elementos de dados que os clientes enviam para ela. A Segment permite que você envie todos os eventos ou decida quais eventos serão enviados para a Braze. Em vez de enviar todos os seus eventos usando a Segment, sugerimos que você revise os casos de uso com suas equipes de marketing e editorial para determinar quais eventos serão enviados para a Braze, a fim de evitar excedentes de dados.

{% enddetails %}

{% details Entenda a diferença entre o endpoint de API personalizado e o endpoint de REST API personalizado nas configurações de destino no modo de dispositivo móvel. %}

| Terminologia da Braze | Equivalente na Segment |
| ----------------- | ------------------ |
| Endpoint do SDK da Braze | Custom API endpoint |
| Endpoint REST da Braze | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Práticas recomendadas" }

O endpoint de API da Braze (chamado de "Custom API Endpoint" na Segment) é o endpoint do SDK que a Braze configura para o seu SDK (por exemplo, `sdk.iad-03.braze.com`). O endpoint de REST API da Braze (chamado de "Custom REST API Endpoint" na Segment) é o endpoint da REST API (por exemplo, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Verifique se o endpoint de API personalizado está inserido corretamente nas configurações de destino no modo de dispositivo móvel. %}

| Terminologia da Braze | Equivalente na Segment |
| ----------------- | ------------------ |
| Endpoint do SDK da Braze | Custom API endpoint |
| Endpoint REST da Braze | Custom REST API endpoint |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Práticas recomendadas" }

O formato adequado deve ser seguido para garantir que o endpoint do SDK da Braze seja inserido corretamente. O endpoint do SDK da Braze não deve incluir `https://` (por exemplo, `sdk.iad-03.braze.com`), caso contrário a integração com a Braze será interrompida. Isso é necessário porque a Segment adiciona automaticamente `https://` ao início do seu endpoint, fazendo com que a Braze seja inicializada com um endpoint inválido `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances no mapeamento de dados. %}

Cenários em que os dados não serão transmitidos conforme esperado:

1. Atributos personalizados aninhados
  - Embora [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) possam tecnicamente ser enviados para a Braze por meio da Segment, a **carga útil inteira** será enviada a cada vez. Isso consumirá [pontos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#data-points) por chave transmitida no objeto aninhado a cada envio da carga útil.<br><br> Para consumir apenas um subconjunto de pontos de dados ao enviar a carga útil, você pode usar o recurso de [funções de destino](https://segment.com/docs/connections/functions/destination-functions/) personalizadas da Segment. Esse recurso na plataforma da Segment permite que você personalize como os dados são enviados para destinos downstream.

  {% alert note %}
  As funções de destino personalizadas são controladas dentro da Segment, e a Braze tem visibilidade limitada sobre funções que foram configuradas externamente.
  {% endalert %}

{: start="2"}
2. Transmissão de dados anônimos de servidor para servidor.
  - Os clientes podem usar as bibliotecas de servidor para servidor da Segment para direcionar dados anônimos para outros sistemas. Consulte a seção sobre métodos de mapeamento para saber mais sobre como enviar usuários sem um `external_id` para a Braze por meio de uma integração de servidor para servidor (modo nuvem).

{% enddetails %}

{% details Personalização da inicialização da Braze. %}

Existem diversas maneiras de personalizar a Braze: push, mensagens no app, Content Cards e inicialização. Com uma integração lado a lado, você ainda pode personalizar push, mensagens no app e Content Cards da mesma forma que faria com uma integração direta com a Braze.

No entanto, personalizar quando o SDK da Braze é integrado ou especificar configurações de inicialização pode ser difícil e, em alguns casos, não é possível. Isso acontece porque a Segment inicializa o SDK da Braze para você quando a inicialização da Segment ocorre.

{% enddetails %}

{% details Envio de deltas para a Braze. %}

Ao transmitir dados de atributos de usuário, verifique se você está enviando apenas os valores de atributos que foram alterados desde a última atualização. Isso evitará o registro de pontos de dados desnecessários. Para fontes do lado do cliente, use a ferramenta de código aberto [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) da Segment para otimizar sua integração e limitar o uso de pontos de dados, eliminando chamadas `identify()` duplicadas da Segment.

{% enddetails %}

{% details Use o data center correto da Braze. %}

A Segment usa o data center da Braze para obter o endpoint REST apropriado da Braze (como `https://rest.iad-01.braze.com`) para realizar chamadas de servidor para servidor.

{% enddetails %}

{% details Remova o endpoint de REST API personalizado ao usar o Event Tester da Segment. %}

O Event Tester da Segment envia eventos para o endpoint da REST API `/users/track` da Braze e retorna um erro `401 Invalid API Key` se um endpoint de REST API personalizado estiver definido nas configurações de destino da Braze, mesmo quando esse endpoint estiver correto. Remova o valor do endpoint de REST API personalizado na Segment para permitir que o Event Tester funcione corretamente.

{% enddetails %}

{% details Aguarde um tempo para atualizações após configurar uma nova fonte. %}

A Segment mantém suas configurações em cache por bastante tempo. Portanto, ao configurar uma nova fonte (como alternar do modo nuvem para o modo de dispositivo), seu app pode não apresentar o novo comportamento ou dados até que o cache seja renovado. Tenha isso em mente ao planejar a adição de uma fonte.

{% enddetails %}