## Verificações básicas {#basic-checks}

### Minha mensagem no app não foi exibida para um usuário {#my-in-app-message-wasnt-shown-for-one-user}

1. O usuário estava no segmento no início da sessão, quando o SDK solicita novas mensagens no app?
2. O usuário era elegível ou reelegível para receber a mensagem no app de acordo com as regras de direcionamento da Campaign?
3. O usuário foi afetado por um limite de frequência?
4. O usuário estava em um grupo de controle? Verifique se sua Campaign está configurada para testes AB.
5. Uma mensagem no app diferente e de prioridade mais alta foi exibida no lugar da mensagem esperada?
6. Meu dispositivo estava na orientação correta especificada pela Campaign?
7. Minha mensagem foi suprimida pelo intervalo de tempo mínimo padrão de 30 segundos entre disparos, imposto pelo SDK?

### Minha mensagem no app não foi exibida para todos os usuários nesta plataforma {#my-in-app-message-wasnt-shown-to-all-users-on-this-platform}

1. Sua Campaign está configurada para direcionar a aplicativos móveis ou navegadores da web, conforme apropriado? Por exemplo, se sua Campaign tiver como alvo apenas navegadores da web, ela não será enviada para dispositivos Android.
2. Você implementou uma interface de usuário personalizada e ela está funcionando como pretendido? Há outra manipulação ou supressão personalizada no lado do app que possa estar interferindo na exibição?
3. Essa plataforma específica e essa versão do app já exibiram mensagens no app com êxito?
4. O disparo ocorreu localmente no dispositivo? Note que uma chamada REST não pode ser usada para disparar uma mensagem no app no SDK.

### Minha mensagem no app não foi exibida para todos os usuários {#my-in-app-message-wasnt-shown-for-all-users}

1. A ação-gatilho foi configurada corretamente no dashboard, bem como na integração do app?
2. Uma mensagem no app diferente e de prioridade mais alta foi exibida no lugar da mensagem esperada?
3. Você está usando uma versão recente do SDK? Alguns tipos de mensagens no app têm requisitos de versão do SDK.
4. As sessões foram integradas corretamente na sua integração? A análise de dados da sessão está funcionando para esse app?
5. Você está usando uma biblioteca de componentes personalizada que pode interferir na exibição das mensagens no app?

### Minha mensagem no app demorou muito para aparecer {#my-in-app-message-took-a-lot-of-time-to-appear}

1. Se estiver servindo arquivos grandes de imagem ou vídeo da CDN para uma mensagem no app baseada em HTML, verifique se os arquivos estão otimizados para serem os menores possíveis e se a CDN tem bom desempenho.
2. Verifique se você configurou um `delay` para sua mensagem no app no dashboard.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. Dependendo das circunstâncias, as mensagens no app baixarão ou carregarão imagens relevantes do disco antes de serem exibidas. Se estiver em uma conexão de rede lenta ou em dispositivos de desempenho muito baixo, esse processo poderá demorar. Certifique-se de que suas imagens sejam otimizadas para serem tão pequenas quanto possível.
{% endcase %}

Para uma discussão mais aprofundada sobre esses cenários, visite a <a id="troubleshooting-in-app-advanced">seção de solução de problemas avançada</a>.

## Problemas com impressões e análise de dados de cliques {#issues-with-impressions-and-click-analytics}

{% if include.sdk == "iOS" %}
### As impressões e os cliques não estão sendo registrados {#impressions-and-clicks-arent-being-logged}

Se você tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com ações de clique, deverá registrar manualmente [os cliques](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) e [as impressões](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) na mensagem no app.
{% elsif include.sdk == "Android" %}
### As impressões e os cliques não estão sendo registrados {#impressions-and-clicks-arent-being-logged}
Se você tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com ações de clique, deverá registrar manualmente os cliques e as impressões na mensagem no app.
{% endif %}

### *Impressões* são maiores que *Impressões únicas* {#impressions-are-greater-than-unique-impressions}

Esse é um comportamento esperado e pode acontecer quando:

- Mesmo que a reelegibilidade esteja desativada, usuários que receberam a Campaign podem ter mais de um dispositivo. O disparo da Campaign é atualizado no próximo início de sessão, então um dispositivo não saberá se outro dispositivo já disparou a Campaign até que o usuário inicie uma nova sessão.
- Se sua mensagem no app tiver uma postergação programada de alguns minutos após a ocorrência do evento de gatilho, os usuários podem ter recebido a mensagem mais de uma vez.

Para saber mais sobre reelegibilidade, consulte [Reelegibilidade para Campaigns e Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

### As impressões são menores do que o esperado {#impressions-are-lower-than-expected}

1. Os disparos levam tempo para serem sincronizados com o dispositivo no início da sessão, portanto pode haver uma condição de corrida se os usuários registrarem um evento ou uma compra logo após iniciarem uma sessão. Uma possível solução alternativa seria alterar a Campaign para disparar a partir do início da sessão e, em seguida, segmentar pelo evento ou compra pretendida. Note que isso entregaria a mensagem no app no próximo início de sessão após a ocorrência do evento.

2. Se a Campaign for disparada por um início de sessão ou por um evento personalizado, é preciso garantir que esse evento ou sessão esteja ocorrendo com frequência suficiente para disparar a mensagem. Verifique esses dados nas páginas [Visão geral]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (para dados de sessão) ou [Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting):

![A página Eventos personalizados mostra um gráfico do número de vezes que o evento personalizado "Adicionado aos favoritos" ocorreu em um período de um mês]({% image_buster /assets/img_archive/trouble5.png %})

Outros motivos incluem:

- Os usuários não visualizaram a mensagem no app, então as impressões não foram registradas.
- Várias mensagens no app estão interceptando umas às outras (como várias mensagens de alta prioridade).
- Se a mensagem estiver em um Canvas, os usuários podem estar entrando em uma etapa de postergação mais longa que o tempo limite da sessão antes de receber a mensagem no app.

### As impressões são mais baixas do que costumavam ser {#impressions-are-lower-than-they-used-to-be}

1. Certifique-se de que ninguém alterou involuntariamente o segmento ou a Campaign desde o lançamento. Nossos changelogs de Segment e Campaign darão insights sobre as alterações feitas, quem fez a alteração e quando ela ocorreu.

![Link para visualizar o changelog na página Informações da Campaign com sete alterações desde a última vez que o usuário visualizou a Campaign]({% image_buster /assets/img_archive/trouble4.png %})

{: start="2"}
2. Certifique-se de que você não reutilizou seu evento de gatilho em uma Campaign de mensagem no app separada com uma prioridade mais alta.

## Solução de problemas avançada {#troubleshooting-in-app-advanced}

A maioria dos problemas com mensagens no app pode ser dividida em duas categorias principais: entrega e exibição. Para solucionar o motivo pelo qual uma mensagem no app esperada não foi exibida no seu dispositivo, confirme se a <a id="troubleshooting-in-app-message-delivery">mensagem no app foi entregue ao dispositivo</a> e, em seguida, <a id="troubleshooting-in-app-message-display">solucione o problema da exibição da mensagem</a>.

### Solução de problemas de entrega {#troubleshooting-in-app-message-delivery}

O SDK solicita mensagens no app dos servidores da Braze no início da sessão. Para verificar se as mensagens no app estão sendo entregues ao seu dispositivo, você precisará ter certeza de que as mensagens no app estão sendo solicitadas pelo SDK e retornadas pelos servidores da Braze.

#### Verificar se as mensagens são solicitadas e retornadas {#check-if-messages-are-requested-and-returned}

1. Adicione-se como um [usuário teste]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) no dashboard.
2. Configure uma Campaign de mensagens no app direcionada ao seu usuário.
3. Confira se uma nova sessão está ocorrendo no seu aplicativo.
4. Use os [registros de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se seu dispositivo está solicitando mensagens no app no início da sessão. Encontre a solicitação do SDK associada ao evento de início de sessão do usuário teste.
  - Se o seu app foi projetado para solicitar mensagens no app disparadas, você deverá ver `trigger` no campo **Requested Responses** em **Response Data**.
  - Se o seu app foi projetado para solicitar mensagens originais no app, você deverá ver `in_app` no campo **Requested Responses** em **Response Data**.
5. Use os [registros de usuários de eventos]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para verificar se as mensagens no app corretas estão sendo retornadas nos dados de resposta.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Solução de problemas de mensagens que não estão sendo solicitadas {#troubleshoot-messages-not-being-requested}

Se suas mensagens no app não estiverem sendo solicitadas, seu app pode não estar rastreando as sessões corretamente, pois as mensagens no app são atualizadas no início da sessão. Além disso, certifique-se de que o seu app esteja realmente iniciando uma sessão com base na semântica de tempo limite da sessão do seu app:

![A solicitação do SDK encontrada nos registros de usuários de eventos exibindo um evento de início de sessão bem-sucedido.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Solução de problemas de mensagens que não estão sendo retornadas {#troubleshoot-messages-not-being-returned}

Se suas mensagens no app não estiverem sendo retornadas, é provável que haja um problema de direcionamento da Campaign:

1. Seu Segment não contém seu usuário.
  - Verifique a guia [**Engajamento**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) do seu usuário para ver se o Segment correto aparece em **Segments**.
2. Seu usuário já recebeu anteriormente a mensagem no app e não era elegível para recebê-la novamente.
  - Verifique as [configurações de reelegibilidade da Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) na etapa **Delivery** do **Campaign Composer** e certifique-se de que as configurações de reelegibilidade estão alinhadas com sua configuração de teste.
3. Seu usuário atingiu o limite de frequência da Campaign.
  - Verifique as [configurações de limite de frequência da Campaign]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) e certifique-se de que estão alinhadas com sua configuração de teste.
4. Se havia um grupo de controle na Campaign, seu usuário pode ter caído no grupo de controle.
  - É possível verificar se isso aconteceu criando um Segment com um filtro de variante de Campaign recebida, em que a variante de Campaign está definida como **Controle**, e verificando se o usuário se enquadra nesse Segment.
  - Ao criar Campaigns para fins de teste de integração, certifique-se de não incluir um grupo de controle.


### Solução de problemas de exibição {#troubleshooting-in-app-message-display}

Se o seu app estiver solicitando e recebendo mensagens no app com êxito, mas elas não estiverem sendo exibidas, a lógica do lado do dispositivo pode estar impedindo a exibição:

1. O evento de gatilho está disparando conforme o esperado? Para testar isso, tente configurar a mensagem para disparar usando uma ação diferente (como o início da sessão) e verifique se ela é exibida.
{% if include.sdk == "iOS" %}
2. As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
{% elsif include.sdk == "Android" %}
2. As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
{% elsif include.sdk == "Web" %}
2. As mensagens no app disparadas são limitadas de frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), cujo padrão é de 30 segundos.
{% endif %}
3. A falha no download de imagens impedirá a exibição de mensagens no app com imagens. Verifique os registros do dispositivo para garantir que os downloads de imagens não estejam falhando. Tente remover sua imagem temporariamente da mensagem para ver se isso faz com que ela seja exibida.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. Se tiver definido um delegado para personalizar o tratamento de mensagens no app, verifique se o delegado não está afetando a exibição de mensagens no app.
  {% when "Web" %}
5. Se você tiver tratamento personalizado de mensagens no app por meio de `braze.subscribeToInAppMessage` ou `appboy.subscribeToNewInAppMessages`, verifique essa inscrição para garantir que não esteja afetando a exibição de mensagens no app.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Se a orientação do dispositivo não corresponder à orientação especificada pela mensagem no app, a mensagem no app não será exibida. Certifique-se de que o dispositivo esteja na orientação correta.
{% endcase %}
7. Se a sua mensagem no app for disparada pelo início da sessão e você tiver definido um tempo limite de sessão estendido, isso afetará a rapidez com que você pode exibir mensagens. Por exemplo, se o tempo limite da sessão estiver definido para 300 segundos, fechar e reabrir o aplicativo em menos tempo não atualizará a sessão, portanto uma mensagem no app disparada por um início de sessão não será exibida.