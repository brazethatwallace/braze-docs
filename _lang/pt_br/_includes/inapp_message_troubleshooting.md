### Solução de problemas de exibição {#troubleshooting-in-app-message-display}

Se o seu app estiver solicitando e recebendo mensagens no app com êxito, mas elas não estiverem sendo exibidas, a lógica do lado do dispositivo pode estar impedindo a exibição:

1. O evento de gatilho está disparando conforme o esperado? Para testar, configure a mensagem para disparar usando uma ação diferente (como o início da sessão) e verifique se ela é exibida.
{% if include.sdk == "iOS" %}
2. As mensagens no app disparadas são limitadas por frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit), cujo padrão é de 30 segundos.
{% elsif include.sdk == "Android" %}
2. As mensagens no app disparadas são limitadas por frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit), cujo padrão é de 30 segundos.
{% elsif include.sdk == "Web" %}
2. As mensagens no app disparadas são limitadas por frequência com base no [intervalo de tempo mínimo entre os disparos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit), cujo padrão é de 30 segundos.
{% endif %}
3. Falhas no download de imagens impedem a exibição de mensagens no app que contêm imagens. Verifique os registros do dispositivo para identificar falhas de download. Tente remover a imagem temporariamente para ver se a mensagem é exibida.
{% case include.sdk %}
  {% when "iOS" %}
4. Se você tiver definido um delegado para personalizar o tratamento de mensagens no app, confirme se ele não está suprimindo a exibição. Consulte [Personalização]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift).
  {% when "Android" %}
4. Se você tiver definido um delegado para personalizar o tratamento de mensagens no app, confirme se ele não está suprimindo a exibição. Consulte [Personalização]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
  {% when "Web" %}
4. Se você usa tratamento personalizado de mensagens no app por meio de [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), verifique se o retorno de chamada não está suprimindo a exibição. Consulte [Personalização]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web).
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. Se a orientação do dispositivo não corresponder à configuração da mensagem no app, a mensagem não será exibida.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Dependendo das condições de rede, as imagens podem demorar para ser baixadas antes da exibição. Em conexões lentas ou dispositivos de baixo desempenho, aguarde um tempo extra ou otimize o tamanho dos ativos.
{% endcase %}

{% if include.sdk == "iOS" %}
### As impressões e os cliques não estão sendo registrados {#impressions-and-clicks-arent-being-logged}

Se você tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com ações de clique, deverá registrar manualmente [os cliques](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) e [as impressões](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) na mensagem no app.
{% elsif include.sdk == "Android" %}
### As impressões e os cliques não estão sendo registrados

Se você tiver definido um delegado de mensagem no app para lidar manualmente com a exibição da mensagem ou com ações de clique, deverá registrar manualmente os cliques e as impressões na mensagem no app.
{% endif %}