---
nav_title: Usar Liquid
article_title: Usar Liquid
page_order: 0
description: "Este artigo de referência fornece uma visão geral dos casos de uso comuns do Liquid e como incluir Liquid tags no seu envio de mensagens."
search_rank: 2
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Usar Liquid {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdynamic-personalization-with-liquid-stylefloatrightwidth120pxborder0-classnoimgborderuse-liquid}

> Este artigo mostra como você pode usar diversos atributos de usuário para inserir dinamicamente informações pessoais nas suas mensagens.

Liquid é uma linguagem de modelo de código aberto desenvolvida pela Shopify e escrita em Ruby. Você pode usá-la na Braze para extrair dados do perfil de usuário nas suas mensagens e personalizar esses dados. Por exemplo, você pode usar Liquid tags para criar mensagens condicionais, como enviar ofertas diferentes com base na data de aniversário de inscrição de um usuário. Além disso, filtros podem manipular dados, como formatar a data de registro de um usuário de um timestamp para um formato mais legível, como "15 de janeiro de 2022". Para mais detalhes sobre a sintaxe do Liquid e suas capacidades, consulte [Tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Como funciona {#how-it-works}

As Liquid tags funcionam como espaços reservados nas suas mensagens que podem trazer informações consentidas da conta do usuário e possibilitar a personalização e práticas de envio de mensagens relevantes.

No bloco a seguir, você pode ver um uso duplo de uma Liquid tag para chamar o nome do usuário, além de uma tag padrão para o caso de o usuário não ter seu nome registrado.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Para uma usuária chamada Janet Doe, a mensagem apareceria de uma das seguintes formas:

```
Hi Janet, thanks for using the App!
```

Ou...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
Os comentários HTML (`<!-- -->`) são removidos antes de qualquer leitura do Liquid, então as Liquid tags dentro de comentários HTML **não** são renderizadas na sua mensagem. Para uma renderização adequada, certifique-se de que todas as Liquid tags que você deseja usar estejam fora dos comentários HTML.
{% endalert %}

## Valores suportados para substituição {#supported-values-to-substitute}

Os seguintes valores podem ser substituídos em uma mensagem, dependendo da disponibilidade:

- [Informações básicas do usuário]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) (por exemplo, `first_name`, `last_name`, `email_address`)
- [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
    - [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#liquid-templating)
- [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [Informações do dispositivo usado mais recentemente]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information)
- [Informações do dispositivo de destino]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information)

Você também pode obter conteúdo diretamente de um servidor web por meio do [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) da Braze.

{% alert important %}
Atualmente, a Braze oferece suporte ao Liquid até a versão Liquid 5 da Shopify, inclusive.
{% endalert %}

## Usando Liquid {#using-liquid}

Usando [Liquid tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), você pode elevar a qualidade das suas mensagens, enriquecendo-as com um toque pessoal.

### Sintaxe do Liquid {#liquid-syntax}

O Liquid segue uma estrutura, ou sintaxe, específica que você precisa ter em mente ao criar personalização dinâmica. Aqui estão algumas regras básicas para lembrar:

- **Use aspas retas na Braze:** Existe uma diferença entre aspas curvas (**' '**) e aspas retas (**&#39; &#39;**). Use aspas retas (**&#39; &#39;**) no seu Liquid na Braze. Você pode ver aspas curvas ao copiar e colar de certos editores de texto, o que pode causar problemas no seu Liquid. Se você estiver inserindo aspas diretamente no dashboard da Braze, não terá problemas.
- **Colchetes vêm em pares:** Cada colchete deve abrir e fechar **{ }**. Certifique-se de usar chaves.
- **Instruções if vêm em pares:** Para cada `if`, você precisa de um `endif` para indicar que a instrução `if` terminou.
- **Instruções case vêm em pares:** Para cada `case`, você precisa de um `endcase` para fechar o bloco.
- **Nomes de variáveis devem usar caracteres ASCII:** Nomes de variáveis Liquid (criados com `assign` ou `capture`) suportam apenas letras ASCII, dígitos e underscores. Nomes de atributos de personalização da Braze (dentro de `custom_attribute.${...}` ou `event_properties.${...}`) podem incluir caracteres não ASCII.
- **Envolva variáveis Liquid da Braze em tags `assign` de múltiplas linhas:** Use chaves duplas {% raw %}(`{{ }}`){% endraw %} ao redor de variáveis Liquid da Braze quando um `assign` abrange múltiplas linhas.

#### Tags `assign` de múltiplas linhas {#multi-line-assign-tags}

Você pode dividir um `assign` em múltiplas linhas (por exemplo, continuando filtros com `|` antes da tag de fechamento), desde que envolva todas as variáveis Liquid da Braze com chaves duplas {% raw %}(`{{ }}`){% endraw %}. Sem essas chaves, instruções assign de múltiplas linhas podem causar renderização inesperada, incluindo atributos personalizados que falham ao fazer template. O exemplo a seguir mostra um assign de múltiplas linhas funcional:

{% raw %}
```liquid
{%- assign color = {{custom_attribute.${favorite_color}}}
| default: {{custom_attribute.${fav_color}}}
| default: 'blue'
%}
```

Você também pode escrever o `assign` completo em uma única linha:

```liquid
{%- assign color = custom_attribute.${favorite_color} | default: custom_attribute.${fav_color} | default: 'blue' %}
```
{% endraw %}

#### Onde usar operadores e filtros {#where-to-use-operators-and-filters}

Operadores (como `==`, `!=`, `>`, `and`, `or`) e filtros (como `| size`, `| plus`) podem ser usados apenas em contextos Liquid específicos.

| Contexto | Operadores | Filtros |
|-----------|-----------|---------|
| `assign` | Não suportado | Suportado |
| `if`, `elsif`, `unless` | Suportado | Não suportado |
| `case`, `when` | Apenas correspondência de igualdade[^case_when_ops] | Não suportado |
| `for` | Não suportado | Não suportado |
| Acesso a array (`[ ]`) | Não suportado | Não suportado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Onde usar operadores e filtros" }

[^case_when_ops]: Nas tags `case` e `when`, o Liquid compara a expressão `case` com cada valor `when` usando igualdade (semelhante a encadear `if` e `elsif` com `==`). Você não pode usar operadores de comparação ou lógicos arbitrários dentro de uma cláusula `when` da mesma forma que faz com `if` e `elsif`. Para exemplos, consulte [Lógica de mensagens condicionais]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when).

Quando você precisa de um valor filtrado em um contexto que não suporta filtros, atribua o resultado a uma variável primeiro.

{% raw %}

##### Usar um resultado de filtro em uma condicional {#use-a-filter-result-in-a-conditional}

Você não pode usar um filtro diretamente em uma instrução condicional. Isso está incorreto:

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

Em vez disso, atribua o resultado do filtro a uma variável:

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### Usar um resultado de filtro em um loop for {#use-a-filter-result-in-a-for-loop}

Você não pode aplicar um filtro ao iterável em um loop `for`. Isso está incorreto:

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

Em vez disso, atribua o valor filtrado a uma variável:

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### Usar um resultado de filtro para acesso a array {#use-a-filter-result-for-array-access}

Você não pode usar um filtro dentro de colchetes. Isso está incorreto:

```liquid
{{ my_array[my_var | minus: 1] }}
```

Em vez disso, atribua o valor filtrado primeiro:

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### Armazenar um resultado de comparação em uma variável {#store-a-comparison-result-in-a-variable}

Você não pode usar um operador em uma instrução `assign`. Isso está incorreto:

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

Em vez disso, use uma condicional para definir a variável:

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### Atributos padrão e atributos personalizados {#default-attributes-and-custom-attributes}

{% raw %}

Se você incluir o seguinte texto na sua mensagem: `{{${first_name}}}`, o nome do usuário (extraído do perfil do usuário) será substituído quando a mensagem for enviada. Você pode usar o mesmo formato com outros atributos padrão do usuário.

Se quiser usar o valor de um atributo personalizado, você deve adicionar o namespace "custom_attribute" à variável. Por exemplo, para usar um atributo personalizado chamado "zip code", você incluiria `{{custom_attribute.${zip code}}}` na sua mensagem.

### Inserindo tags {#inserting-tags}

Você pode inserir tags digitando duas chaves de abertura `{{` em qualquer mensagem, o que acionará um recurso de autocompletar que continuará atualizando conforme você digita. Você pode até selecionar uma variável das opções que aparecem enquanto digita.

Se estiver usando uma tag personalizada, você pode copiar e colar a tag em qualquer mensagem que desejar.

#### Exceções para chaves duplas {#exceptions-for-double-brackets}

Se estiver usando uma tag dentro de outra tag Liquid, como `{% assign %}` ou `{% if %}`, você pode usar chaves duplas ou nenhuma chave. É apenas quando a tag está sozinha que ela precisa estar envolvida em chaves duplas. Para simplificar, você pode sempre usar chaves duplas.

As seguintes tags estão todas corretas:

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Se você usar Liquid nas suas mensagens de e-mail, certifique-se de:

1. Inseri-lo usando o editor de HTML em vez do editor clássico. O editor clássico pode interpretar o Liquid como texto simples. Por exemplo, o Liquid seria interpretado como {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} em vez de fazer o template com o nome do usuário.
2. Colocar o código Liquid apenas dentro da tag `<body>`. Colocá-lo fora dessa tag pode causar renderização inconsistente na entrega.

{% endalert %}

### Alternando entre os editores HTML e Clássico {#switching-between-html-and-classic-editors}

Quando você alterna entre os editores HTML e Clássico, snippets Liquid e Content Blocks podem mudar de posição na sua mensagem. Revise seu modelo após alternar entre editores. Se precisar de um controle de layout mais previsível, use o editor de arrastar e soltar.

### Inserindo variáveis pré-formatadas {#inserting-pre-formatted-variables}

Você pode inserir variáveis pré-formatadas com valores padrão através do modal **Adicionar personalização** localizado próximo a qualquer campo de texto com template.

![O modal Adicionar personalização que aparece após selecionar inserir personalização. O modal possui campos para tipo de personalização, atributo, valor padrão opcional e exibe uma prévia da sintaxe Liquid.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

O modal inserirá o Liquid com o valor padrão especificado no ponto onde seu cursor estava. O ponto de inserção também é indicado pela caixa de prévia, que mostra o texto antes e depois. Se um bloco de texto estiver destacado, o texto destacado será substituído.

![Um GIF do modal Adicionar personalização mostrando o usuário inserindo "fellow traveler" como valor padrão, e o modal substituindo o texto destacado "name" no criador pelo snippet Liquid.]({% image_buster /assets/img_archive/insert_var_shot.gif %})