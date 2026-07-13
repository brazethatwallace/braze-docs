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

## Como os dados de message extras são enviados usando o Currents {#how-message-extras-data-is-sent-using-currents}

**Message extras** são pares de chave-valor anexados no momento do envio. A configuração depende do canal. Para e-mail, eles são adicionados usando cabeçalhos. Para push no iOS, eles são incluídos na carga útil do push. Todos os eventos de envio compatíveis exibem o mesmo campo `message_extras` no Currents (e no Snowflake) assim que a mensagem é enviada.

## Canais compatíveis {#supported-channels}

A tag `message_extras` é compatível com todos os tipos de mensagem que possuem um evento de envio, além de eventos de impressão de mensagens no app. Usar `message_extras` com mensagens no app requer que certas [versões mínimas do SDK](#iam-sdk) sejam atendidas.

## Como usar a tag `message_extras` {#how-to-use-the-message_extras-tag}

1. No corpo da mensagem do canal, insira a tag Liquid `message_extras`. Ou você pode usar o modal **Adicionar personalização** e selecionar **Message Extras** como tipo de personalização.

![O modal Adicionar personalização com Message Extras selecionado como tipo de personalização.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Insira o [par de chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para cada tag `message_extras`.

![Um exemplo de pares de chave-valor para a tag message extras. O campo de título diz "Your New Favorites." A mensagem mostra pares de chave-valor para a tag message extras e a seguinte frase: "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites"]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Após o envio da sua Campaign ou Canvas, a Braze anexará os dados dinâmicos no momento do envio por meio dos eventos de envio do Currents ou do Compartilhamento de dados do Snowflake ao campo `message_extras`.

## Verificando a sintaxe {#checking-syntax}

Qualquer outra entrada que não corresponda ao padrão da tag discutido anteriormente nesta seção pode não ser transmitida ao Currents ou ao Snowflake. Verifique se sua sintaxe ou formatação não inclui nenhum dos seguintes problemas:

- Delimitadores inexistentes, vazios ou digitados incorretamente
- Chaves duplicadas (a Braze enviará por padrão o par de chave-valor encontrado primeiro)
- Texto extra antes da definição das chaves ou valores
- Chaves e valores fora de ordem
  - {% raw %}Por exemplo, `{% message_extras :value 123 :key test %}`{% endraw %}

## Enviando informações de códigos de promoção para o Currents {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Considerações {#considerations}

- Pares de chave-valor que excedem 1.000 bytes (1&nbsp;KB) são truncados.
- Espaços em branco contam para a contagem de caracteres. Observe que a Braze remove os espaços em branco iniciais e finais.
- O JSON resultante gera apenas valores do tipo string.
- Você pode incluir variáveis Liquid como chave ou valor, mas não pode aninhar tags Liquid adicionais dentro de `message_extras`.
  - Por exemplo, você poderia usar o seguinte Liquid: {% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## Perguntas frequentes {#frequently-asked-questions}

### Como posso associar o campo message_extras nos eventos de envio aos meus eventos de engajamento, como aberturas e cliques? {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

Um `dispatch_id` é gerado e fornecido nos seus eventos de envio, podendo ser usado como identificador único para vincular a eventos específicos de clique, abertura ou entrega. Você pode consultar esse campo no Currents ou no Snowflake. Para saber mais, consulte [Comportamento do dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

#### Posso usar message_extras com mensagens no app? {#iam-sdk}

Sim, você pode usar `message_extras` nas suas mensagens no app desde que os dispositivos dos seus usuários estejam nas seguintes versões mínimas do SDK:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}