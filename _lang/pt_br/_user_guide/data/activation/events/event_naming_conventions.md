---
nav_title: Convenções de nomenclatura de eventos
article_title: Convenções de nomenclatura de eventos
page_order: 4
page_type: reference
description: "Este artigo de referência aborda as convenções adequadas de nomenclatura de eventos e as práticas recomendadas."

---

# Convenções de nomenclatura de eventos {#event-naming-conventions}

> Esta página aborda as convenções adequadas de nomenclatura de eventos e as práticas recomendadas. Ao manter a consistência em sua taxonomia de eventos e atribuições, você manterá seus dados limpos e utilizáveis por usuários novos e existentes da plataforma Braze. Isso ajuda a evitar problemas posteriores, como disparar uma campanha para o público errado ou gerar resultados errados depois de usar o evento errado.

## Melhores práticas {#best-practices}

- Mantenha sua convenção de nomenclatura clara.
- Use letras maiúsculas e minúsculas e formatação consistentes nos nomes dos eventos.
- Evite dar nomes semelhantes aos eventos.
- Evite longas strings de atribuições de eventos, que serão truncadas ou cortadas no dashboard da Braze.

## Convenções de nomenclatura {#naming-conventions}

### Usar grupos de eventos {#use-event-groups}

Use grupos para diferenciar partes de seu produto para nomear eventos. Ao categorizar seu produto em grupos, qualquer usuário pode entender claramente a que o evento se refere e o que ele faz.

### Estrutura de nomenclatura de eventos {#event-naming-structure}

A estrutura de nomes mais comum é `group_noun_action`. Os eventos devem ser todos em letras minúsculas para evitar erros de instrumentação e identificação de propriedades.

### Propriedades {#properties}

Tag um evento e, em seguida, identifique as diferenças usando as propriedades. Isso é útil para eventos que são inerentemente iguais, mas têm pequenas diferenças, como canais de uma campanha. Dessa forma, também podemos ver facilmente como os usuários fluem pelos eventos. Consulte o [objeto de propriedades de evento]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para ver um exemplo e obter mais contexto.

## Exemplos {#examples}

Digamos que você faz parte de uma empresa de eCommerce e deseja rastrear quando os clientes se cadastraram no seu app e quando se inscreveram na sua newsletter. Aqui estão exemplos de nomes de eventos eficazes:

- `user_signup`
- `newsletter_subscribed`

Esses dois nomes de eventos indicam claramente o que estão rastreando. À medida que você cria mais eventos personalizados, mantenha suas convenções de nomenclatura compreensíveis. Por exemplo, evite usar nomes de eventos como `signup_event_1`, pois isso não é claro e não transmite o que o evento está rastreando, em comparação com `user_signup`.