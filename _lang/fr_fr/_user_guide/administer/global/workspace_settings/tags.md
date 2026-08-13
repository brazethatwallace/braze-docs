---
nav_title: Gestion des balises
article_title: Gestion des balises
page_order: 6
page_type: reference
description: "Cet article de référence explique comment gérer les balises dans le tableau de bord de Braze, notamment l'imbrication, le renommage et l'organisation des balises pour les campagnes, les Canvas et les segments."
---

# Gestion des balises {#managing-tags}

> Vous pouvez gérer les balises que vous utilisez pour les campagnes, les Canvas et les segments depuis un emplacement centralisé. Pour renommer, supprimer ou ajouter des balises, accédez à **Paramètres** > **Gestion des balises**.

Pour savoir comment ajouter des balises aux campagnes, Canvas, segments et données personnalisées, consultez [Balises]({{site.baseurl}}/user_guide/messaging/governance/tags).

## Imbrication des balises {#nesting-tags}

Pour mieux organiser vos balises, vous pouvez les imbriquer sous une balise parente. Par exemple, vous pouvez regrouper toutes les balises de vacances sous une balise parente `Holidays`, ou toutes les balises liées à une étape de votre entonnoir marketing sous une balise parente `Funnel`.

- **Imbriquer une nouvelle balise :** créez une balise, sélectionnez **Nest Tag Under**, puis choisissez la balise existante sous laquelle imbriquer votre nouvelle balise.
- **Imbriquer une balise existante :** accédez à la page **Gestion des balises**, survolez la ligne contenant votre balise et sélectionnez **<i class="fas fa-pencil-alt"></i>Edit**. Ensuite, sélectionnez **Nest Tag Under** et choisissez la balise parente.

### La balise parente est utilisée mais absente de **Nest Tag Under** {#parent-tag-is-in-use-but-missing-from-nest-tag-under}

Lorsqu'une balise parente est appliquée dans le tableau de bord mais n'apparaît pas dans le menu déroulant **Nest Tag Under** lors de la création d'une nouvelle balise, recréez la balise parente en tant que balise autonome afin qu'elle devienne consultable dans la liste. Ce comportement est attendu lorsque la balise parente n'existe que comme dépendance imbriquée ailleurs dans votre espace de travail.

![Boîte de dialogue de nouvelle balise avec l'option Nest Tag Under sélectionnée.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Bonnes pratiques {#tags-best-practices}

Utilisez les balises pour organiser vos campagnes, Canvas et segments par objectifs commerciaux, étapes de l'entonnoir, régions, et plus encore.

Le tableau suivant présente des exemples de balises qu'une application eCommerce pourrait trouver utiles :

<style>
table td {
    word-break: break-word;
}
</style>


<table aria-label="Bonnes pratiques">
  <caption>Bonnes pratiques</caption>
<thead>
  <tr>
    <th>Entonnoir</th>
    <th>Objectifs commerciaux</th>
    <th>Régional</th>
    <th>Campaigns</th>
    <th>Vacances</th>
    <th>Transactions</th>
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

## Cas d'usage {#use-cases}

Voici des cas d'usage courants pour gérer le cycle de vie de vos messages à l'aide de balises.

{% tabs %}
{% tab Limitation de fréquence %}

### Limitation de fréquence {#throttling}

Limitez la fréquence à laquelle vos clients reçoivent des campagnes d'un certain type. Par exemple, vous pourriez définir les filtres suivants pour limiter la fréquence des campagnes promotionnelles :

`Last received campaign` with tag `Promo` more than 5 days ago
<br>`OR`<br>
`Has not received campaign` with tag `Promo`

{% endtab %}
{% tab Rapports %}

### Rapports {#reporting}

Configurez un rapport d'engagement pour surveiller le volume de toutes les campagnes associées à une certaine balise. Par exemple, si vous souhaitez suivre toutes vos campagnes de notifications push, vous pouvez ajouter une balise comme `Push Reporting` à ces campagnes, puis configurer un [rapport d'engagement]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#automatically-select-campaigns-or-canvases) pour recevoir chaque jour un rapport sur ces campagnes balisées.

{% endtab %}
{% endtabs %}