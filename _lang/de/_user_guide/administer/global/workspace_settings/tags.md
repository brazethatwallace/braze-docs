---
nav_title: Tags verwalten
article_title: Tags verwalten
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt die Verwaltung von Tags im Braze-Dashboard, einschließlich Verschachtelung, Umbenennung und Organisation von Tags über Campaigns, Canvases und Segments hinweg."
---

# Tags verwalten {#managing-tags}

> Sie können die Tags, die Sie in Campaigns, Canvases und Segments verwenden, zentral verwalten. Um Tags umzubenennen, zu entfernen oder hinzuzufügen, gehen Sie zu **Einstellungen** > **Tag-Management**.

Informationen zum Hinzufügen von Tags zu Campaigns, Canvases, Segments und angepassten Daten finden Sie unter [Tags]({{site.baseurl}}/user_guide/messaging/governance/tags/).

## Tags verschachteln {#nesting-tags}

Um Ihre Tags weiter zu organisieren, können Sie sie unter einem übergeordneten Tag verschachteln. Beispielsweise können Sie alle Feiertags-Tags unter einem übergeordneten `Holidays`-Tag zusammenfassen oder alle Tags, die sich auf eine Stufe Ihres Marketing-Funnels beziehen, unter einem übergeordneten `Funnel`-Tag.

![Die Tag-Management-Seite mit einer Liste von Tags, die nach verschachtelten Gruppen organisiert sind.]({% image_buster /assets/img_archive/tags_view.png %})

Um ein neues Tag zu verschachteln, erstellen Sie ein Tag, wählen Sie **Nest Tag Under** und wählen Sie aus, unter welchem vorhandenen Tag Ihr neues Tag verschachtelt werden soll.

Um ein vorhandenes Tag zu verschachteln, gehen Sie zur **Tag-Management**-Seite, bewegen Sie den Mauszeiger über eine Zeile mit Ihrem Tag und wählen Sie **<i class="fas fa-pencil-alt"></i>Edit**. Wählen Sie dann **Nest Tag Under** und wählen Sie das übergeordnete Tag aus.

### Übergeordnetes Tag wird verwendet, fehlt aber in **Nest Tag Under** {#parent-tag-is-in-use-but-missing-from-nest-tag-under}

Wenn ein übergeordnetes Tag im Dashboard angewendet wird, aber beim Erstellen eines neuen Tags nicht im Dropdown **Nest Tag Under** erscheint, erstellen Sie das übergeordnete Tag als eigenständiges Tag neu, damit es in der Liste durchsuchbar wird. Dieses Verhalten ist zu erwarten, wenn das übergeordnete Tag nur als verschachtelte Abhängigkeit an anderer Stelle in Ihrem Workspace existiert.

![Der Dialog für ein neues Tag mit ausgewählter Option „Nest Tag Under“.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Best Practices {#tags-best-practices}

Verwenden Sie Tags, um Ihre Campaigns, Canvases und Segments nach Geschäftszielen, Funnel-Stufen, Regionen und mehr zu organisieren.

Die folgende Tabelle zeigt Beispiel-Tags, die für eine E-Commerce-App nützlich sein könnten:

<style>
table td {
    word-break: break-word;
}
</style>


<table aria-label="Best Practices">
  <caption>Best Practices</caption>
<thead>
  <tr>
    <th>Funnel</th>
    <th>Geschäftsziele</th>
    <th>Regional</th>
    <th>Campaigns</th>
    <th>Feiertage</th>
    <th>Transaktionen</th>
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

## Anwendungsfälle {#use-cases}

Im Folgenden finden Sie gängige Anwendungsfälle für die Verwendung von Tags zur Verwaltung Ihres Messaging-Lebenszyklus.

{% tabs %}
{% tab Drosselung %}

### Drosselung {#throttling}

Begrenzen Sie, wie oft Ihre Kund:innen Campaigns eines bestimmten Typs erhalten. Beispielsweise könnten Sie die folgenden Filter setzen, um die Häufigkeit von Aktions-Campaigns zu begrenzen:

`Last received campaign` mit Tag `Promo` vor mehr als 5 Tagen
<br>`OR`<br>
`Has not received campaign` mit Tag `Promo`

{% endtab %}
{% tab Berichte %}

### Berichte {#reporting}

Richten Sie einen Engagement-Bericht ein, um das Volumen aller Campaigns mit einem bestimmten Tag im Blick zu behalten. Wenn Sie beispielsweise alle Ihre Push-Campaigns überwachen möchten, könnten Sie diesen Campaigns ein Tag wie `Push Reporting` hinzufügen und dann einen [Engagement-Bericht]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/#automatically-select-campaigns-or-canvases) einrichten, der Ihnen täglich einen Bericht über diese getaggten Campaigns sendet.

{% endtab %}
{% endtabs %}