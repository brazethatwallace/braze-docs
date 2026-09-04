---
nav_title: Liquid
article_title: Liquid no construtor de modelos de WhatsApp
description: "Este artigo de referência aborda Message Extras e lógica condicional Liquid no construtor de modelos de WhatsApp."
alias: /whatsapp_template_builder_liquid/
page_type: reference
channel:
  - WhatsApp
page_order: 1
---

# Liquid no construtor de modelos de WhatsApp {#liquid-in-the-whatsapp-template-builder}

> Você pode usar Liquid para personalizar modelos no construtor de modelos de WhatsApp, mas a estrutura de modelos da Meta cria restrições que não existem em outros canais da Braze. Dois padrões de Liquid em particular exigem tratamento especial: Message Extras e lógica condicional de envio de mensagens.

Para Message Extras e lógica condicional de envio de mensagens, a Meta exige que cada variável em um modelo contenha conteúdo renderizado real no momento do envio. Variáveis que retornam strings vazias, ou que se comportam como metadados invisíveis em vez de texto visível, causam falhas de envio. Condicionais que alteram a estrutura estática da mensagem em vez de apenas o conteúdo da variável também causam comportamento inesperado.

{% alert note %}
As restrições descritas neste artigo se aplicam apenas a mensagens de modelo (mensagens de saída que usam um modelo aprovado pela Meta). As restrições não se aplicam a mensagens de resposta (enviadas dentro de uma janela de envio de mensagens de 24 horas aberta por um usuário), nem a Message Extras, lógica condicional e outros padrões Liquid em outros canais da Braze.
{% endalert %}

## Visão geral {#overview}

| Padrão | Suportado? | Notas |
| ----- | ----- | ----- |
| `message_extras` dentro de uma variável com outro conteúdo visível | ✅ Sim | A tag é capturada; o texto visível satisfaz o requisito de conteúdo de variável da Meta |
| `message_extras` como único conteúdo de uma variável | ❌ Não | Resolve para string vazia; causa falha de envio |
| Liquid condicional dentro de um slot de variável | ✅ Sim | A Braze avalia antes do envio; a Meta vê apenas o valor final renderizado |
| Liquid condicional fora de um slot de variável | ❌ Não | Tags Liquid renderizadas como texto literal; o destinatário vê a sintaxe bruta |
| Modelo começando ou terminando com um slot de variável | ❌ Não | A Meta exige texto estático no início e no final de cada modelo |
| Slot de variável que resolve para uma string vazia | ❌ Não | A Meta exige conteúdo não vazio em cada variável no momento do envio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Referência rápida" }

## Message Extras {#message-extras}

A [Liquid tag `message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) permite anotar uma mensagem com metadados de chave-valor no momento do envio. Esses dados não são renderizados no corpo da mensagem. Em vez disso, os dados fluem para Conteúdo conectado, Currents ou outros mecanismos de captura de dados para fins como atribuição, medição de impacto e enriquecimento de eventos.

{% raw %}
```liquid
{% message_extras :key campaign_id :value "spring_promo_2025" %}
```
{% endraw %}

### Por que variáveis com Message Extras isolados falham {#why-standalone-message-extras-variables-fail}

No construtor de modelos de WhatsApp, as variáveis de modelo (como {% raw %}`{{1}}`, `{{2}}`{% endraw %}) mapeiam diretamente para expressões Liquid. A validação da Meta exige que cada slot de variável no modelo aprovado contenha conteúdo não vazio no momento do envio; deve ser algo que renderize como texto visível para o destinatário.

Como `message_extras` não produz saída, colocá-lo sozinho dentro de uma variável de modelo envia uma string vazia para aquele slot de variável. A Meta rejeita isso, então o envio da mensagem falha.

{% details Uso incorreto para o construtor de modelos de WhatsApp %}

{% raw %}
```
Template variable {{1}}: {% message_extras :key attribution_source :value "canvas_a" %}
```
{% endraw %}

No momento do envio, {% raw %}`{{1}}`{% endraw %} resolve para uma string vazia, causando uma falha de envio.

{% enddetails %}

### Uso correto {#correct-usage}

Para incluir corretamente uma tag `message_extras`, incorpore a tag em uma variável existente. Isso significa colocar a tag dentro de um bloco Liquid que produz saída visível; especificamente, dentro da mesma expressão que preenche uma variável de modelo real. A Meta aceita a variável porque ela contém conteúdo, a Braze captura os metadados e o destinatário vê apenas o texto renderizado.

#### Exemplo {#example}

Digamos que o corpo do modelo seja:

{% raw %}
```
Hi {{1}}, your order has shipped.
```
{% endraw %}

E a variável {% raw %}`{{1}}`{% endraw %} está mapeada para:

{% raw %}
```
{{ ${first_name} | default: "there" }}
```
{% endraw %}

Para anexar um Message Extra, reescreva a expressão da variável como:

{% raw %}
```
{{ ${first_name} | default: "there" }}{% message_extras :key order_source :value "canvas_spring" %}
```
{% endraw %}

No momento do envio, {% raw %}`{{1}}`{% endraw %} resolve para algo como `"Alex"`, conteúdo visível que satisfaz o requisito da Meta. A tag `message_extras` é avaliada e seus dados são capturados, mas ela não contribui com nada para a string renderizada que o destinatário vê.

### Regras principais {#key-rules}

- Nunca atribua `message_extras` como único conteúdo de uma variável de modelo.
- Sempre anexe a tag a uma variável que resolve para texto visível.
- Você pode adicionar múltiplas tags `message_extras` à mesma expressão de variável sem afetar a saída renderizada.
- Use esse padrão no corpo, no cabeçalho e em quaisquer outros slots de variável.

## Lógica condicional de envio de mensagens {#conditional-messaging-logic}

Em canais de envio de mensagens, blocos Liquid `if/elsif/else` podem incluir ou excluir condicionalmente seções inteiras de texto. A Braze renderiza a saída Liquid completa antes do envio, e o resultado é o que a lógica produzir.

No entanto, modelos de WhatsApp aprovados pela Meta têm uma estrutura fixa. A Meta classifica o conteúdo do modelo em duas categorias:

- **Texto estático:** Strings fixas que são confirmadas na criação do modelo e permanecem idênticas para cada destinatário.
- **Slots de variável:** Posições de espaço reservado (como {% raw %}`{{1}}`{% endraw %}) cujo conteúdo é preenchido no momento do envio.

### Por que a lógica condicional fora de um slot de variável falha {#why-conditional-messaging-logic-outside-a-variable-slot-fails}

A proporção de texto estático para slots de variável em um modelo aprovado é fixa, não pode mudar por envio e tem limites rígidos. A Meta exige uma quantidade mínima de texto estático para cada slot de variável no modelo; você não pode ter um modelo que seja majoritariamente ou inteiramente composto por variáveis. Isso significa que você não pode incluir Liquid condicional que adicione ou remova texto que a Meta considera como conteúdo estático confirmado.

Se você tentar usar um bloco `if/else` para incluir ou excluir condicionalmente um trecho de texto estático, a Meta não avalia a lógica. Tags Liquid fora de um slot de variável são tratadas como texto de saída literal. O destinatário vê as tags de sintaxe Liquid brutas ({% raw %}`{% if %}`, `{% else %}`, `{% endif %}`{% endraw %}) e todo o conteúdo das ramificações literalmente na mensagem.

{% details Uso incorreto para o construtor de modelos de WhatsApp %}

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}Hi {{1}}, we have an exclusive Gold member offer.{% else %}Hi {{1}}, we have a special offer for you.{% endif %}
```
{% endraw %}

Isso tenta incluir dois modelos aprovados diferentes em um só. O condicional envolvendo texto estático não se comportará como esperado.

{% enddetails %}

### Uso correto

Condicionais são válidos e suportados dentro de um slot de variável, onde controlam qual valor preenche aquela variável. A Meta vê apenas que {% raw %}`{{1}}`{% endraw %} foi preenchido com conteúdo; ela não inspeciona como o Liquid interno chegou àquele valor.

#### Exemplo

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}exclusive Gold member{% else %}valued customer{% endif %}
```
{% endraw %}

Usado como valor para uma variável de modelo, isso produz `"exclusive Gold member"` ou `"valued customer"`. Ambos são strings não vazias que satisfazem o requisito de conteúdo de variável da Meta.

O corpo do modelo em si permanece estruturalmente inalterado:

{% raw %}
```
Hi {{1}}, we have a special offer for you.
```
{% endraw %}

### Coloque a lógica condicional dentro de um slot de variável {#place-conditional-logic-inside-a-variable-slot}

Existem duas maneiras de colocar Liquid condicional em um slot de variável no construtor de modelos:

1. **Use um Content Block (suporta preenchimento prévio):** Construa sua lógica condicional dentro de um Content Block e depois referencie o bloco a partir da variável. Essa abordagem suporta preenchimento prévio, o que significa que a variável pode exibir um valor de pré-visualização no construtor de modelos antes do envio.
2. **Use um espaço reservado e cole o Liquid (sem preenchimento prévio):** Adicione um espaço reservado como {% raw %}`{{1}}`{% endraw %} ao criar o modelo e depois cole sua expressão Liquid completa diretamente naquele slot de variável. Essa abordagem não suporta preenchimento prévio, mas funciona para qualquer lógica Liquid.

### Outros componentes Liquid afetados pela mesma restrição {#other-liquid-components-affected-by-the-same-constraint}

Qualquer tag Liquid que não produza saída visível é renderizada como texto bruto se colocada fora de uma variável. Isso inclui:

- **`catalog_items`:** Liquid que busca e referencia dados de Catálogo deve estar dentro de um slot de variável, ou as tags aparecem literalmente na mensagem.
- **`assign`:** Tags de atribuição de variável (como {% raw %}{% assign discount = "20%" %}{% endraw %}) não produzem saída por si mesmas. Se usadas fora de um slot de variável para definir um valor para uso posterior na mensagem, a tag `assign` é renderizada literalmente. Inclua qualquer lógica `assign` no início da expressão Liquid dentro do slot de variável onde sua saída é necessária.
- **Content Blocks contendo apenas tags Liquid:** Se um Content Block contém lógica Liquid mas não produz texto visível (por exemplo, usa apenas tags `assign` ou `message_extras`), referenciá-lo fora de um slot de variável faz com que o conteúdo bruto do bloco apareça na mensagem. Content Blocks que não produzem saída visível devem ser incorporados dentro de um slot de variável junto com conteúdo que renderize.

### Restrições estruturais adicionais {#additional-structural-constraints}

A Meta exige que os modelos:

- **Comecem com texto estático.** Modelos não podem abrir com um slot de variável (como {% raw %}`{{1}} is ready for you`{% endraw %}).
- **Terminem com texto estático.** Modelos não podem terminar em um slot de variável.

Essas restrições existem independentemente do uso de Liquid. Elas se aplicam à estrutura do modelo aprovado em si.

### Regras principais

- Use condicionais livremente dentro de expressões de slot de variável para controlar qual valor é renderizado.
- Não use condicionais para adicionar, remover ou trocar texto estático (as partes da mensagem que não são slots de variável).
- Certifique-se de que cada Branch condicional dentro de uma variável produza uma string não vazia (veja [Message Extras](#message-extras) para entender por que strings vazias causam falhas).
- O modelo deve começar e terminar com texto estático conforme enviado à Meta.