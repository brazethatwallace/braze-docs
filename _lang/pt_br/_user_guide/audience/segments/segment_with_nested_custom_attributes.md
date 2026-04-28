---
nav_title: "Caso de uso: Atributos personalizados aninhados"
article_title: "Caso de uso: Segmentar com atributos personalizados aninhados"
page_order: 10
page_type: tutorial
tool: Segments
description: "Crie Segments usando atributos personalizados aninhados: o filtro de atributos personalizados aninhados, caminhos e comparadores, filtros de tempo, segmentação multicritério, geração de esquema e o explorador de objetos aninhados."
---

# Caso de uso: Segmentar com atributos personalizados aninhados {#use-case-segment-with-nested-custom-attributes}

> Estes casos de uso mostram como segmentar usuários com atributos personalizados aninhados na Braze e contêm exemplos de JSON e fluxos de trabalho no dashboard que você pode adaptar aos seus próprios dados.

Digamos que você faz parte de uma equipe de marketing de um app de streaming de música e quer enviar mensagens com base nos atributos personalizados aninhados de um usuário, como objetos de conta com saldos e tipos. Esses casos de uso demonstram diversas formas de usar atributos personalizados aninhados em Segments e ensinam como:

- Configurar um filtro de Segment com atributo personalizado aninhado, validar caminhos e escolher comparadores que correspondam ao tipo de dados de cada propriedade.
- Saber quando usar os operadores **Day of Year** versus **Time** para valores de data aninhados, e como a **Segmentação multicritério** identifica usuários quando pelo menos um objeto em um vetor atende a todos os critérios listados.
- Gerar um esquema para um objeto ou vetor de objeto, explorá-lo no dashboard e finalizar um Segment (por exemplo, usuários com saldo abaixo de 100) usando o seletor de caminho em vez de digitar caminhos de memória.

## Filtrar por atributos personalizados aninhados {#filter-by-nested-custom-attributes}

Vamos criar um Segment com base em um atributo personalizado aninhado para segmentar seus usuários que tocaram a música mais reproduzida mais de 300 vezes.

### Etapa 1: Adicionar o filtro {#step-1-add-the-filter}

Selecione o filtro **Nested Custom Attributes** para exibir um menu suspenso no qual você pode selecionar um atributo personalizado aninhado específico. Vamos selecionar `most_played_song`, que contém dados sobre a música mais reproduzida de um usuário.

### Etapa 2: Selecionar a propriedade {#step-2-select-the-property}

Selecione a **Property** dentro do atributo personalizado aninhado pela qual você deseja filtrar. Vamos selecionar `play_analytics.count`, que rastreia quantas vezes um usuário tocou sua música mais reproduzida.

### Etapa 3: Selecionar uma comparação e o valor do atributo personalizado aninhado {#step-3-select-a-comparison-and-nested-custom-attribute-value}

Ao filtrar por atributos personalizados aninhados, o tipo de dados da sua propriedade determina os comparadores disponíveis para filtragem. Por exemplo, como `play_analytics.count` é um número, você pode selecionar um comparador na categoria **Number**.

Para filtrar por usuários que tocaram sua música mais reproduzida pelo menos 300 vezes, selecione a comparação **More than** e insira "300" como valor.

![Um usuário escolhendo um operador com base no tipo de dados do atributo personalizado aninhado]({% image_buster /assets/img_archive/nca_comparator.png %})

## Filtrar por tipos de dados de tempo {#filter-for-time-data-types}

Ao filtrar um atributo personalizado aninhado de tempo, você pode escolher filtrar com operadores nas categorias **Day of Year** ou **Time** ao comparar o valor de data.

Se você selecionar um operador na categoria **Day of Year**, apenas o mês e o dia serão verificados na comparação, em vez do timestamp completo do valor do atributo personalizado aninhado. Selecionar um operador na categoria **Time** compara o timestamp completo, incluindo o ano.

## Usar segmentação multicritério {#use-multi-criteria-segmentation}

Use a **Multi-Criteria Segmentation** para criar um Segment que corresponda a múltiplos critérios dentro de um único objeto. Isso qualifica o usuário no Segment se ele tiver pelo menos um objeto no vetor que atenda a todos os critérios especificados. Por exemplo, os usuários só correspondem a esse Segment se a chave deles não estiver em branco e se o número for maior que 0.

### Copiar Liquid para Segment {#copy-liquid-for-segment}

Você também pode usar o recurso **Copy Liquid for segment** para gerar código Liquid para esse Segment e usá-lo em uma mensagem. Por exemplo, digamos que você tem um vetor de objetos de conta e um Segment que segmenta clientes com contas tributáveis ativas. Para fazer com que os clientes contribuam para a meta da conta associada a uma de suas contas ativas e tributáveis, você vai querer criar uma mensagem para incentivá-los.

![Um exemplo de Segment com a caixa de seleção marcada para Multi-Criteria Segmentation.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Quando você seleciona **Copy Liquid for segment**, a Braze gera automaticamente código Liquid que retorna um vetor de objeto contendo apenas contas que são ativas e tributáveis.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

A partir daqui, você pode usar `segmented_nested_objects` e personalizar sua mensagem. Neste exemplo, queremos pegar uma meta da primeira conta tributável ativa e personalizá-la:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Isso retorna a seguinte mensagem para o seu cliente: "Get to your retirement goal faster, make a deposit using our new fast deposit feature!"

## Gerar um esquema usando o explorador de objetos aninhados {#generate-schema}

Você pode gerar um esquema para seus objetos para criar filtros de Segment sem precisar memorizar os caminhos de objetos aninhados.

### Etapa 1: Gerar um esquema {#step-1-generate-a-schema}

Por exemplo, suponha que temos um vetor de objeto `accounts` que acabamos de enviar para a Braze:

```json
{"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true}
]}
```

No dashboard da Braze, acesse **Data Settings** > **Custom Attributes**.

Pesquise seu objeto ou vetor de objeto. Na coluna **Attribute Name**, selecione **Generate Schema**.

![Uma lista de atributos personalizados com a opção de gerar o esquema para o atributo accounts.]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
Pode levar alguns minutos para o esquema ser gerado, dependendo da quantidade de dados que você nos enviou.
{% endalert %}

Após o esquema ser gerado, um novo botão de <i class="fas fa-plus"></i> mais aparece no lugar do botão **Generate Schema**. Você pode clicar nele para ver o que a Braze sabe sobre esse atributo personalizado aninhado.

Durante a geração do esquema, a Braze analisa os dados enviados anteriormente e cria uma representação ideal dos seus dados para esse atributo. A Braze também analisa e adiciona um tipo de dados para seus valores aninhados. Isso é feito por amostragem dos dados enviados anteriormente para a Braze para o atributo aninhado em questão.

Para nosso vetor de objeto `accounts`, você pode ver que dentro do vetor de objeto há um objeto que contém o seguinte:

- Um tipo booleano com a chave `active` (independentemente de a conta estar ativa ou não)
- Um tipo número com a chave `balance` (valor do saldo na conta)
- Um tipo string com a chave `type` (conta não tributável ou tributável)

![Esquema para o vetor de objeto accounts com três valores aninhados: active, balance e type.]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:70%" }

Agora que analisamos e criamos uma representação dos dados, vamos criar um Segment.

### Etapa 2: Criar um Segment {#step-2-build-a-segment}

Vamos segmentar clientes que têm um saldo inferior a 100 para enviar uma mensagem incentivando-os a fazer um depósito.

Crie um Segment e adicione o filtro `Nested Custom Attribute`, depois pesquise e selecione seu objeto ou vetor de objeto. Aqui adicionamos o vetor de objeto `accounts`.

![Filtragem de atributo personalizado aninhado para o vetor de objeto accounts.]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Selecione o botão de <i class="fas fa-plus"></i> mais no campo de caminho. Isso abre uma representação do seu objeto ou vetor de objeto. Você pode selecionar qualquer um dos itens listados e a Braze os insere no campo de caminho para você. Neste exemplo, precisamos obter o saldo. Selecione o saldo como caminho (neste caso, `[].balance`) que é automaticamente preenchido no campo de caminho.

![Esquema de accounts com lista pesquisável de caminhos.]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Selecione **less than** como comparador e insira "100" como valor do saldo.

![Um filtro para usuários com saldo de conta inferior a 100.]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

Pronto! Você acabou de criar um Segment usando um atributo personalizado aninhado, tudo sem precisar saber como os dados estão estruturados. O explorador de objetos aninhados da Braze gerou uma representação visual dos seus dados e permitiu que você explorasse e selecionasse exatamente o que precisava para criar um Segment.