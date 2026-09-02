---
nav_title: Objetos aninhados
article_title: Objetos aninhados em eventos personalizados
page_order: 1
page_type: reference
description: "Este artigo descreve como enviar dados JSON aninhados como propriedades de eventos personalizados e compras, e como usar esses objetos aninhados no seu envio de mensagens."
---

# Objetos aninhados em eventos personalizados {#nested-objects-in-custom-events}

> Esta página aborda como enviar dados JSON aninhados como propriedades de eventos personalizados e compras, e como usar esses objetos aninhados em seu envio de mensagens.

Você pode usar objetos aninhados — objetos que estão dentro de outro objeto — para enviar dados JSON aninhados como propriedades de eventos personalizados e compras. Esses dados aninhados podem ser usados para modelar informações personalizadas em mensagens, disparar envios de mensagens e segmentar usuários.

## Considerações {#considerations}

- Dados aninhados são compatíveis com [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) e [eventos de compra]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), mas não com outros tipos de evento.
- Objetos de propriedades de evento que contêm valores de array ou objeto podem ter uma carga útil de propriedade de evento de até 100 KB.
- Esquemas de propriedades de evento não podem ser gerados para eventos de compra.
- Esquemas de propriedades de evento são gerados por amostragem de eventos personalizados das últimas 24 horas.

### Versões mínimas do SDK or kit de desenvolvimento de software {#minimum-sdk-versions}

As seguintes versões do SDK or kit de desenvolvimento de software são compatíveis com objetos aninhados:

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## Etapa 1: Gerar um esquema {#step-1-generate-a-schema}

Você pode acessar os dados aninhados no seu evento personalizado gerando um esquema para cada evento com propriedades de evento aninhadas. Para gerar um esquema:

1. Acesse **Configurações de dados** > **Eventos personalizados**.
2. Selecione **Gerenciar propriedades** para os eventos com propriedades aninhadas.
3. Selecione o botão <i class="fas fa-arrows-rotate"></i> para gerar o esquema. Para visualizar o esquema, selecione o botão de mais <i class="fas fa-plus"></i>.

![Selecione o botão para gerar o esquema. Para visualizar o esquema, selecione o botão de mais.]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Se novas propriedades forem enviadas no futuro, elas não estarão no esquema até que ele seja regenerado. Os esquemas podem ser regenerados a cada 24 horas.

## Etapa 2: Usar o objeto aninhado {#step-2-use-the-nested-object}

Você pode referenciar os dados aninhados durante a segmentação e personalização. Um esquema não é obrigatório. Consulte as seções a seguir para exemplos de uso:

- [Corpo da requisição de API or interface de programação do aplicativo (API)](#api-request-body)
- [Modelos Liquid](#liquid-templating)
- [Disparo de mensagens](#message-triggering)
- [Segmentação](#segmentation)
- [Personalização](#personalization)

### Corpo da requisição de API or interface de programação do aplicativo (API) {#api-request-body}

{% tabs %}
{% tab Music Example %}

A seguir, um exemplo de `/users/track` com um evento personalizado "Created Playlist". Depois que uma playlist for criada, capture as propriedades da playlist enviando:
- Uma requisição de API or interface de programação do aplicativo (API) que lista "songs" como uma propriedade
- Um array das propriedades aninhadas das músicas

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

A seguir, um exemplo de `/users/track` com um evento personalizado "Ordered". Depois que um pedido for concluído, capture as propriedades desse pedido enviando:
- Uma requisição de API or interface de programação do aplicativo (API) que lista `r_details` como uma propriedade
- As propriedades aninhadas desse pedido

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para propriedades de eventos personalizados aninhadas, se o ano for menor que 0 ou maior que 3000, a Braze não armazena esses valores no usuário.
{% endalert %}

### Modelos Liquid {#liquid-templating}

A seguir, veja como criar um modelo Liquid que referencia as propriedades aninhadas solicitadas na [requisição de API or interface de programação do aplicativo (API) anterior](#api-request-body).

{% tabs %}
{% tab Music Example %}
Modelo em Liquid em uma mensagem disparada pelo evento "Created Playlist":

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Modelo em Liquid em uma mensagem disparada pelo evento "Ordered":

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Disparo de mensagens {#message-triggering}

Para usar essas propriedades para disparar uma Campaign, selecione seu evento personalizado ou compra e adicione um filtro de **Propriedade aninhada**. O disparo de mensagens ainda não é compatível com mensagens no app, mas as propriedades aninhadas na personalização Liquid nas mensagens ainda serão exibidas.

{% tabs %}
{% tab Music Example %}

Disparando uma Campaign com propriedades aninhadas do evento "Created Playlist":

![Um usuário escolhendo uma propriedade aninhada para filtros de propriedade em um evento personalizado.]({% image_buster /assets/img/nested_object2.png %})

A condição de disparo `songs[].album.yearReleased` "is" "1968" corresponderá a um evento em que qualquer uma das músicas tenha um álbum lançado em 1968. Usamos a notação de colchetes `[]` para percorrer arrays e fazemos a correspondência se **qualquer** item no array percorrido corresponder à propriedade do evento.

{% alert important %}
O filtro **não é igual** só corresponde se nenhuma das propriedades no seu array for igual ao valor fornecido. <br><br>Por exemplo, digamos que o Canvas A tenha o filtro de propriedade aninhada de evento personalizado baseado em ação **igual a** "smartwatch", e o Canvas B tenha o filtro de propriedade aninhada de evento personalizado baseado em ação **não é igual a** "simphone". Se você tiver "smartwatch" e "simphone" nas suas propriedades, ambos os Canvas serão disparados. Mas se você tiver "simphone" ou "sim only" em qualquer propriedade, nenhum Canvas será disparado.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Disparando uma Campaign com propriedades aninhadas do evento "Ordered":

![Um usuário adicionando o filtro de propriedade r_details.name is SandwichEmperor para um evento personalizado.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "SandwichEmperor"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Se a propriedade do seu evento contiver os caracteres `[]` ou `.`, faça o escape envolvendo o trecho entre aspas duplas. Por exemplo, `"songs[].album".yearReleased` corresponderá a um evento com a propriedade literal `"songs[].album"`.
{% endalert %}

### Segmentação {#segmentation}

Para segmentar usuários com base em propriedades de evento aninhadas, você deve usar [Extensões de Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Depois de gerar um esquema, o explorador de objetos aninhados será exibido na seção de segmentação.

![Captura de tela relacionada à segmentação.]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

A segmentação usa a mesma notação do disparo (consulte [Disparo de mensagens](#message-triggering)).

Para editar ou criar extensões de Segment or segmento or segmento, você precisará da permissão "Editar segmentos".

### Personalização {#personalization}

Usando o modal **Adicionar personalização**, selecione **Propriedades avançadas de evento** como o tipo de personalização. Isso permite adicionar propriedades de evento aninhadas depois que um esquema for gerado.

![Usando o modal Adicionar personalização, selecione Propriedades avançadas de evento como o tipo de personalização. Isso permite adicionar propriedades de evento aninhadas depois que um esquema for gerado.]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Testando objetos aninhados em mensagens {#testing-nested-objects-in-messages}

A ferramenta **Pré-visualização e teste** do dashboard não permite adicionar dados simulados para objetos aninhados ou atributos personalizados aninhados. Para testar mensagens que referenciam dados aninhados por meio de Liquid, você pode pré-visualizar mensagens com atributos aninhados como um usuário existente que possua esse atributo aninhado, ou pré-visualizar mensagens com propriedades de evento personalizado lançando uma campanha ativa para usuários teste.

### Atributos personalizados aninhados {#nested-custom-attributes}

1. Importe os atributos aninhados para o perfil do usuário teste por meio da API or interface de programação do aplicativo (API).
2. Na sua Campaign ou Canvas, acesse **Pré-visualização e teste**.
3. Selecione **Pré-visualizar como usuário** e pesquise o usuário teste. O Liquid será resolvido usando os atributos aninhados reais no perfil desse usuário.

### Propriedades de evento aninhadas {#nested-event-properties}

As propriedades de evento aninhadas não podem ser pré-visualizadas no dashboard porque exigem um disparo de evento ao vivo. Para testar:

1. Crie uma Campaign ou etapa do Canvas que tenha como alvo apenas seus usuários teste e seja disparada pelo (ou referencie o) evento personalizado com propriedades aninhadas.
2. Lance a Campaign para seu público de teste.
3. Registre o evento personalizado com a carga útil do objeto aninhado no perfil do seu usuário teste (usando a API or interface de programação do aplicativo (API) ou o SDK or kit de desenvolvimento de software).
4. Verifique se a mensagem é renderizada corretamente com os valores das propriedades aninhadas.

## Perguntas frequentes {#frequently-asked-questions}

### O uso de objetos aninhados registra pontos de dados adicionais? {#does-using-nested-objects-log-additional-data-points}

Não há mudança na forma como registramos pontos de dados com a adição dessa funcionalidade. A segmentação baseada em objetos aninhados usa extensões de Segment or segmento or segmento, que não consomem pontos de dados adicionais.

### Quantos dados aninhados podem ser enviados? {#how-much-nested-data-can-be-sent}

Se uma ou mais propriedades do evento contiverem dados aninhados, a carga útil máxima para todas as propriedades combinadas em um evento é de 100 KB. Qualquer requisição acima desse limite de tamanho será rejeitada.