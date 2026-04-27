---
nav_title: Gerenciamento de tags
article_title: Gerenciamento de tags
page_order: 6
page_type: reference
description: "Este artigo de referência aborda como gerenciar tags no dashboard da Braze, incluindo aninhamento, renomeação e organização de tags em campanhas, Canvas e segmentos."
---

# Gerenciamento de tags

> Você pode gerenciar as tags usadas em campanhas, Canvas e segmentos a partir de um local centralizado. Para renomear, remover ou adicionar tags, acesse **Configurações** > **Gerenciamento de tags**.

Para saber como adicionar tags a campanhas, Canvas, segmentos e dados personalizados, consulte [Tags]({{site.baseurl}}/user_guide/messaging/governance/tags/).

## Aninhamento de tags

Para organizar ainda mais suas tags, você pode aninhá-las sob uma tag principal. Por exemplo, você pode manter todas as tags de feriados aninhadas sob uma tag principal `Holidays`, ou todas as tags relacionadas a uma etapa do seu funil de marketing sob uma tag principal `Funnel`.

![A página de Gerenciamento de tags mostrando uma lista de tags organizadas por grupos aninhados.]({% image_buster /assets/img_archive/tags_view.png %})

Para aninhar uma nova tag, crie uma tag, selecione **Nest Tag Under** e escolha sob qual tag existente deseja aninhar a nova tag.

Para aninhar uma tag existente, acesse a página **Gerenciamento de tags**, passe o cursor sobre a linha com a tag e selecione **<i class="fas fa-pencil-alt"></i>Edit**. Em seguida, selecione **Nest Tag Under** e escolha a tag principal.

![A caixa de diálogo de nova tag com a opção Nest Tag Under selecionada.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Práticas recomendadas {#tags-best-practices}

Use tags para organizar suas campanhas, Canvas e segmentos por objetivos de negócios, etapas do funil, regiões e muito mais.

A tabela a seguir mostra exemplos de tags que um app de eCommerce pode considerar úteis:

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Funil</th>
    <th>Objetivos de negócios</th>
    <th>Regional</th>
    <th>Campanhas</th>
    <th>Feriados</th>
    <th>Transações</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>On-boarding<br>Re-engagement<br>Loyal<br>PowerUser<br>Churn<br>Lost</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Northeast<br>Midwest<br>South<br>West<br>LATAM<br>AP<br>WesternEurope<br>MiddleEast</td>
    <td>Sales<br>Coupons<br>Events</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Easter<br>Passover<br>MothersDay<br>MemorialDay<br>FathersDay<br>FourthJuly<br>LaborDay<br>VeteransDay<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Christmas<br>Hanukkah<br>NewYears</td>
    <td>Transactional<br>Notification<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## Casos de uso

A seguir estão casos de uso comuns para utilizar tags no gerenciamento do ciclo de vida do envio de mensagens.

{% tabs %}
{% tab Throttling %}

### Limitação de frequência

Limite a frequência com que seus clientes recebem campanhas de um determinado tipo. Por exemplo, você pode definir os seguintes filtros para limitar a frequência de campanhas promocionais:

`Last received campaign` with tag `Promo` more than 5 days ago
<br>`OR`<br>
`Has not received campaign` with tag `Promo`

{% endtab %}
{% tab Reporting %}

### Relatórios

Configure um relatório de engajamento para acompanhar o volume de todas as campanhas com uma determinada tag. Por exemplo, se você deseja monitorar todas as suas campanhas de push, pode adicionar uma tag como `Push Reporting` a essas campanhas e, em seguida, configurar um [relatório de engajamento]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#automatically-select-campaigns-or-canvases) para enviar um relatório dessas campanhas com tag todos os dias.

{% endtab %}
{% endtabs %}