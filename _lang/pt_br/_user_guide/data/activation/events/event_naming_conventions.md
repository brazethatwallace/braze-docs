---
nav_title: Convenções de nomenclatura de eventos
article_title: Convenções de nomenclatura de eventos
page_order: 4
page_type: reference
description: "Este artigo de referência aborda as convenções de nomenclatura de eventos e as melhores práticas."

---

# Convenções de nomenclatura de eventos

> Esta página aborda as convenções de nomenclatura de eventos e as melhores práticas. Ao manter a consistência na taxonomia de eventos e atributos, seus dados permanecerão limpos e utilizáveis para usuários novos e existentes da plataforma Braze. Isso ajuda a evitar problemas futuros, como disparar uma campanha para o público errado ou gerar resultados incorretos ao usar o evento errado.

## Melhores práticas

- Mantenha sua convenção de nomenclatura clara.
- Use formatação e caixa (maiúsculas/minúsculas) consistentes nos nomes dos eventos.
- Evite dar nomes semelhantes a eventos diferentes.
- Evite strings longas de atributos de eventos, pois elas serão truncadas ou cortadas no dashboard da Braze.

## Convenções de nomenclatura

### Use grupos de eventos

Use grupos para diferenciar partes do seu produto ao nomear eventos. Ao categorizar seu produto em grupos, qualquer usuário pode entender claramente a que o evento se refere e o que ele faz.

### Estrutura de nomenclatura de eventos

A estrutura de nomenclatura mais comum é `group_noun_action`. Todos os eventos devem estar em letras minúsculas para evitar erros de instrumentação de caixa e para facilitar a identificação de propriedades.

### Propriedades

Crie uma tag para um evento e depois identifique as diferenças usando propriedades. Isso é útil para eventos que são essencialmente iguais, mas possuem pequenas diferenças, como canais de uma campanha. Dessa forma, também podemos ver facilmente como os usuários fluem pelos eventos. Consulte o [objeto de propriedades de evento]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para ver um exemplo e obter mais contexto.

## Exemplos

Digamos que você faz parte de uma empresa de eCommerce e deseja rastrear quando os clientes se cadastraram no seu app e quando se inscreveram na sua newsletter. Aqui estão exemplos de nomes de eventos eficazes:

- `user_signup`
- `newsletter_subscribed`

Esses dois nomes de eventos indicam claramente o que estão rastreando. À medida que você cria mais eventos personalizados, mantenha suas convenções de nomenclatura compreensíveis. Por exemplo, evite usar nomes de eventos como `signup_event_1`, pois isso não é claro e não transmite o que o evento está rastreando, em comparação com `user_signup`.