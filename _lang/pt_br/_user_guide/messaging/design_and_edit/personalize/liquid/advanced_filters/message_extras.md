---
nav_title: Tag message extras
article_title: Tag message extras
page_order: 1
description: "Este artigo explica como usar a tag Liquid message extras e como verificar a sintaxe."
alias: "/message_extras_tag/"
---

# Tag Liquid message extras {#message-extras-liquid-tag}

> Use a tag Liquid `message_extras` para anotar seus eventos de envio com dados dinâmicos do Conteúdo conectado, Catálogos, atributos personalizados (como idioma, país), propriedades de entrada do Canvas ou outras fontes de dados.

A tag Liquid `message_extras` anexa pares de chave-valor ao evento de envio correspondente no Currents e no Compartilhamento de dados do Snowflake.

Para enviar dados dinâmicos ou extras de volta ao seu evento de envio do Currents ou do Compartilhamento de dados do Snowflake, insira a tag Liquid adequada no corpo da sua mensagem.

Veja um exemplo do formato padrão da tag Liquid para `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Você pode adicionar essas tags conforme necessário para seus pares de chave-valor no corpo da mensagem. No entanto, o comprimento total de todas as chaves e valores não deve exceder 1.000 bytes (1&nbsp;KB). No Currents e no Compartilhamento de dados do Snowflake, você verá um novo campo de evento chamado `message_extras` para seus eventos de envio. Isso gera uma string serializada em JSON em um único campo.

{% alert note %}
Os extras de e-mail enviam metadados para provedores de serviços de e-mail e não são publicados no Currents ou no Snowflake. Para adicionar metadados ou valores dinâmicos aos eventos de envio do Currents ou do Snowflake, use a tag Liquid `message_extras`.
{% endalert %}

## Como os dados de extras de mensagem são enviados usando Currents {#how-message-extras-data-is-sent-using-currents}

**Extras de mensagem** são pares de chave-valor anexados no momento do envio. A configuração depende do canal. Para e-mail, eles são adicionados usando cabeçalhos. Para push no iOS, eles são incluídos na carga útil do push. Todos os eventos de envio compatíveis exibem o mesmo campo `message_extras` no Currents (e no Snowflake) assim que a mensagem é enviada.

## Canais compatíveis {#supported-channels}

A tag `message_extras` é compatível com todos os tipos de mensagem que possuem um evento de envio, além de eventos de impressão de mensagens no app. O uso de `message_extras` com mensagens no app requer que certas [versões mínimas do SDK](#iam-sdk) sejam atendidas.

## Como usar a tag `message_extras` {#how-to-use-the-message_extras-tag}

1. No corpo da mensagem do canal, insira a tag Liquid `message_extras`. Ou você pode usar o modal **Add Personalization** e selecionar **Message Extras** como o tipo de personalização.

![O modal Add Personalization com Message Extras selecionado como o tipo de personalização.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Insira o [par chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para cada tag `message_extras`.

![Um exemplo de pares chave-valor para a tag message extras. O campo de título diz "Your New Favorites." A mensagem exibe pares chave-valor para a tag message extras e a seguinte frase: "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Depois que sua Campaign ou Canvas for enviada, a Braze anexa os dados dinâmicos no momento do envio ao campo `message_extras` nos eventos de envio do Currents ou do Snowflake Data Sharing.

## Verificação de sintaxe {#checking-syntax}

Qualquer outra entrada que não corresponda ao padrão de tag discutido anteriormente nesta seção pode falhar ao ser enviada para o Currents ou Snowflake. Verifique se sua sintaxe ou formatação não inclui nenhum dos seguintes itens:

- Delimitadores inexistentes, vazios ou digitados incorretamente
- Chaves duplicadas (a Braze envia por padrão o par chave-valor encontrado primeiro)
- Texto extra antes da definição de chaves ou valores
- Chaves e valores fora de ordem
  - {% raw %}Por exemplo, `{% message_extras :value 123 :key test %}`{% endraw %}

## Enviando informações de código de promoção para o Currents {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Considerações {#considerations}

- Pares de chave-valor que excedem 1.000 bytes (1&nbsp;KB) são truncados.
- Espaços em branco contam para a contagem de caracteres. Note que a Braze omite os espaços em branco iniciais e finais.
- Os resultados JSON geram apenas valores de string.
- Você pode incluir variáveis Liquid como chave ou valor, mas não pode aninhar tags Liquid adicionais dentro de `message_extras`.
  - Por exemplo, você pode usar o seguinte Liquid: {% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## Perguntas frequentes {#frequently-asked-questions}

### Como posso associar o campo message_extras nos eventos de envio aos meus eventos de engajamento, como aberturas e cliques? {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

Um `dispatch_id` é gerado e fornecido nos seus eventos de envio, e pode ser usado como um identificador único para vincular a eventos específicos de clique, abertura ou entrega. Consulte esse campo no Currents ou no Snowflake. Para saber mais, consulte [Comportamento do dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

#### Posso usar message_extras com mensagens no app? {#iam-sdk}

Sim, você pode usar `message_extras` nas suas mensagens no app, desde que os dispositivos dos seus usuários estejam nas seguintes versões mínimas do SDK:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}