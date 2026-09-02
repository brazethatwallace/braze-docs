---
nav_title: Coleta de dados do SDK or kit de desenvolvimento de software
article_title: Coleta de dados do SDK or kit de desenvolvimento de software
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os dados que são coletados pelo SDK or kit de desenvolvimento de software por meio de uma integração personalizada, integração coletada automaticamente."
---

# Coleta de dados do SDK or kit de desenvolvimento de software {#sdk-data-collection}

> Quando você integra o SDK or kit de desenvolvimento de software da Braze com seu app ou site, a Braze coleta automaticamente certos tipos de dados. Alguns desses dados são essenciais para nossos processos e outros podem ser ativados ou desativados de acordo com suas necessidades. Você também pode configurar a Braze para coletar tipos adicionais de dados para aprimorar ainda mais sua segmentação e envio de mensagens.

A Braze foi projetada para permitir a coleta flexível de dados, portanto, você pode integrar o SDK or kit de desenvolvimento de software da Braze das seguintes maneiras:

- **[Integração mínima](#minimum-integration):** A Braze coleta automaticamente os dados necessários para a comunicação com os serviços da Braze.
- **[Dados opcionais coletados por padrão](#optional-data-collected-by-default):** A Braze captura automaticamente alguns dados que são amplamente úteis para a maioria dos seus casos de uso. Você pode optar por desativar a coleta automática desses dados se eles não forem essenciais para a comunicação com os serviços da Braze.
- **[Dados opcionais não coletados por padrão](#data-not-collected-by-default):** A Braze captura alguns dados que são úteis para determinados casos de uso e não ativa automaticamente a coleta por motivos de ampla conformidade. Você pode optar por coletar esses dados onde for mais adequado aos seus casos de uso.
- **[Integração personalizada](#personalized-integration):** A Braze oferece a flexibilidade de coletar dados além dos dados opcionais padrão.

## Integração mínima {#minimum-integration}

A lista a seguir apresenta os dados estritamente necessários gerados e recebidos pela Braze quando você inicializa o SDK or kit de desenvolvimento de software. Esses dados não são configuráveis e são essenciais para as funções principais da plataforma. Exceto pelo início e término da sessão, todos os outros dados rastreados automaticamente não contam para o seu uso de pontos de dados.

| Atributo | Descrição | Por que é coletado |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | A versão mais recente do app | Este atributo é usado para enviar mensagens relacionadas à compatibilidade da versão do app para os dispositivos corretos. Pode ser usado para notificar os usuários sobre interrupções de serviço ou bugs. |
| Country | País identificado pela geolocalização do endereço IP. Se a geolocalização do endereço IP não estiver disponível, ele será identificado pelo [local do dispositivo](#optional-data-collected-by-default). O valor também pode ser o que os SDKs definem diretamente com `setCountry`, mas observe que passar um valor de atributo via SDK or kit de desenvolvimento de software ou API or interface de programação do aplicativo (API) registrará pontos de dados. **Depois que o país for definido manualmente (por meio do método do SDK or kit de desenvolvimento de software, REST or transferir estado representacional API or interface de programação do aplicativo (API) ou upload de CSV), o SDK or kit de desenvolvimento de software não atualizará mais esse valor automaticamente.** | Este atributo é usado para direcionar mensagens com base na localização. |
| Device ID | Identificador do dispositivo, uma string gerada aleatoriamente | Este atributo é usado para diferenciar os dispositivos dos usuários e enviar mensagens para o dispositivo correto. |
| OS and OS version | Sistema operacional e versão do dispositivo ou navegador atualmente reportados | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado na segmentação para direcionar os usuários a atualizar as versões do app. |
| Session start and session end | Quando o usuário começa a usar seu app ou site integrado | O SDK or kit de desenvolvimento de software da Braze reporta dados de sessão usados pelo dashboard da Braze para calcular o engajamento dos usuários e outras análises essenciais para entender seus usuários. O momento exato em que o início e o término da sessão são chamados pelo seu app ou site é configurável por um desenvolvedor ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)). |
| SDK or kit de desenvolvimento de software message interaction data | Aberturas Diretas de push, interações com mensagens no app, interações com Content Cards | Este atributo é usado para fins de controle de qualidade, como verificar se uma mensagem foi recebida e se o envio não foi duplicado. |
| SDK or kit de desenvolvimento de software version | Versão atual do SDK or kit de desenvolvimento de software | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis e evitar interrupções de serviço. |
| Session ID and session timestamp | Identificador da sessão, uma string gerada aleatoriamente e timestamp da sessão | Usado para determinar se o usuário está iniciando uma sessão nova ou existente e para determinar a reelegibilidade de mensagens destinadas a esse usuário.<br><br>Certos canais de envio de mensagens, como mensagens no app e Content Cards, são sincronizados com o dispositivo no início da sessão. Nosso backend então usa dados relacionados a quando ele entrou em contato pela última vez com os servidores da Braze (que o dispositivo armazena e envia de volta) para saber se o usuário é elegível para novas mensagens. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Integração mínima" }

### Métricas calculadas {#calculated-metrics}

A Braze gera métricas calculadas a partir de três entradas: [dados rastreados pelo SDK or kit de desenvolvimento de software](#minimum-integration) (por exemplo, [início e término da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)), [dados de interação de mensagens para canais que não usam SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) e [campos de relatórios derivados da Braze]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Esses valores são gerados pelos serviços da Braze, de modo que um perfil de usuário pode incluir tanto dados rastreados pelo SDK or kit de desenvolvimento de software quanto dados gerados pela Braze.

As métricas calculadas incluem métricas baseadas em canal (listadas no [Glossário de métricas de relatórios]({{site.baseurl}}/user_guide/analytics/metrics_glossary)) e os seguintes atributos.

| Atributo | Descrição |
|------------------------------------------------|----------------------------------------------------------------------|
| First used app | Hora |
| Last used app | Hora |
| Total session count | Número |
| Clicked card | Número |
| Last received any message | Hora |
| Last received email campaign | Hora |
| Last received push campaign | Hora |
| Number of feedback items | Número |
| Number of sessions in the last Y days | Número e hora |
| Received message from campaign | Booleano. Este filtro direciona os usuários com base em terem recebido uma Campaign anterior. |
| Received message from campaign with tag | Booleano. Este filtro direciona os usuários com base em terem recebido uma Campaign que atualmente possui uma tag. |
| Retarget campaign | Booleano. Este filtro direciona os usuários com base em terem aberto ou clicado em um e-mail, push ou mensagem no app específicos no passado. |
| Uninstalled | Booleano e hora |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas calculadas" }

Integração mínima significa que você coleta apenas os dados obrigatórios listados em [Integração mínima](#minimum-integration) e opta por não coletar os [dados opcionais coletados por padrão](#optional-data-collected-by-default) ao [bloquear a coleta opcional de dados do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/getting_started/sdk_overview).

{% alert important %}
Se você deseja uma integração mínima e usa mParticle, Segment or segmento, Tealium ou GTM, observe o seguinte:
- **Plataformas móveis**: você deve atualizar o código manualmente para essas configurações. mParticle e Segment or segmento não oferecem uma maneira de fazer isso por meio de suas plataformas.
- **Web**: a integração da Braze deve ser feita nativamente para permitir a configuração de integração mínima. Gerenciadores de tags não oferecem uma maneira de fazer isso por meio de suas plataformas.
{% endalert %}

## Dados opcionais coletados por padrão {#optional-data-collected-by-default}

Além dos dados mínimos de integração, os seguintes atributos são capturados automaticamente pela Braze quando você inicializa a integração SDK or kit de desenvolvimento de software. Você pode [desativar]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) a coleta desses atributos para permitir uma integração mínima.

| Atributo | Plataforma | Descrição | Por que é coletado |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome do navegador | Web | Nome do navegador | Esse atributo é usado para enviar mensagens apenas para navegadores compatíveis. Também pode ser usado para segmentação baseada em navegador. |
| Localidade do dispositivo | Android, iOS, Web | A localidade padrão do dispositivo | Esse atributo é usado para traduzir mensagens para o idioma preferido do usuário. |
| Localidade mais recente do dispositivo | Android, iOS, Web | A localidade padrão mais recente do dispositivo | Esse atributo vem das configurações do dispositivo do usuário e é usado para traduzir mensagens para o idioma preferido do usuário. É independente do atributo `Most Recent Location`. |
| Modelo do dispositivo | Android, iOS | O hardware específico do dispositivo | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado na segmentação. |
| Marca do dispositivo | Android | A marca do dispositivo (por exemplo, Samsung) | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis. |
| Operadora sem fio do dispositivo | Android, iOS | A operadora móvel | Esse atributo é opcionalmente usado para direcionamento de mensagens.<br><br>**Nota:** Este campo foi descontinuado a partir do iOS 16 e será definido como `--` em uma versão futura do iOS. |
| Idioma | Android, iOS, Web | Idioma do dispositivo ou navegador, obtido a partir da localidade do dispositivo. | Esse atributo é usado para traduzir mensagens para o idioma preferido do usuário. É baseado na localidade do dispositivo. |
| Configurações de notificação | Android, iOS, Web | Se este app tem notificações por push ativadas. | Esse atributo é usado para ativar notificações por push. |
| Resolução | Android, iOS, Web | Resolução do dispositivo ou navegador | Opcionalmente usado para direcionamento de mensagens baseado em dispositivo. O formato desse valor é "`<width>`x`<height>`". |
| Fuso horário | Android, iOS, Web | Fuso horário do dispositivo ou navegador | Esse atributo é usado para enviar mensagens no horário adequado, de acordo com o fuso local de cada usuário. |
| User agent | Web | [User agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado na segmentação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Dados opcionais coletados por padrão" }

Para saber mais sobre o rastreamento de propriedades no nível do dispositivo (como operadora sem fio do dispositivo, fuso horário, resolução e outros), consulte a documentação específica da plataforma: [Android]({{site.baseurl}}/developer_guide/storage?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage#cookies).

## Dados não coletados por padrão {#data-not-collected-by-default}

Por padrão, os atributos a seguir não são coletados. Cada atributo precisa ser integrado manualmente.

| Atributo                  | Plataforma     | Descrição                                                                                                                                                                                                                                                                                                               | Por que não é coletado                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Ad Tracking Enabled | Android, iOS | No iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>No Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Essa propriedade requer permissões adicionais no nível do app, que precisam ser concedidas pelo integrador.                                                                                                                                                                                      |
| Device IDFA                | iOS          | Identificador do dispositivo para anunciantes                                                                                                                                                                                                                                                                                         | Isso requer o framework Ad Tracking Transparency, que acionará uma análise de privacidade adicional pela App Store. Para saber mais, consulte [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| Google Advertising ID      | Android      | Identificador para publicidade em apps do Google Play                                                                                                                                                                                                                                                                        | Isso requer que o app obtenha o GAID e o transmita à Braze. Para saber mais, consulte [Google Advertising ID opcional]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Localização mais recente | Android, iOS | Esta é a última localização GPS conhecida do dispositivo do usuário. Ela é atualizada no início da sessão e armazenada no perfil do usuário. | Isso requer que o usuário conceda permissão de localização ao seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Dados não coletados por padrão" }

{% alert note %}
O SDK or kit de desenvolvimento de software da Braze não armazena nenhum endereço IP localmente.
{% endalert %}

## Integração personalizada {#personalized-integration}

Para aproveitar ao máximo a Braze, nossos integradores de SDK or kit de desenvolvimento de software frequentemente implementam os SDKs da Braze e registram [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events#logging-custom-events) e [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#log-purchase-events) que são relevantes para o negócio, além dos dados coletados automaticamente.

Uma integração personalizada permite uma comunicação customizada e relevante para a experiência dos seus usuários.

{% alert important %}
A Braze bloqueia perfis de usuário ("dummy users") com mais de 5.000.000 de sessões, mais de 20.000 nomes distintos de eventos personalizados ou mais de 20.000 nomes distintos de produtos em compras, e para de ingerir todos os dados de entrada desse perfil, tanto dos SDKs quanto da REST or transferir estado representacional API or interface de programação do aplicativo (API). Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_archival).
{% endalert %}