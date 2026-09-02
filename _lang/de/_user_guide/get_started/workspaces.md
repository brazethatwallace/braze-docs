---
nav_title: Workspaces
article_title: "Erste Schritte: Workspaces"
page_order: 3
page_type: reference
description: "Alles, was Sie auf der Braze-Plattform tun, geschieht innerhalb eines Workspace. Dieser Artikel beschreibt, wie Workspaces funktionieren und welche wichtigen Aspekte zu beachten sind."
---

# Erste Schritte: Workspaces {#get-started-workspaces}

> Alles, was Sie auf der Braze-Plattform tun, geschieht innerhalb eines Workspace. Workspaces fungieren als separate Datensilos und ermöglichen es Ihnen, verschiedene Marken oder Aktivitäten voneinander zu trennen. Mehrere Versionen Ihrer Website oder mobilen App können Daten an denselben Workspace senden. Die verschiedenen Websites und Apps, die innerhalb eines Workspace zusammengefasst werden, bezeichnen wir als „App-Instanzen“.

## Workspaces verstehen {#understanding-workspaces}

Workspaces erfüllen zwei zentrale Aufgaben:

- **Nutzerdaten vereinheitlichen:** Wenn mehrere App-Instanzen in einem Workspace zusammengefasst sind, können Sie Nutzerdaten nahtlos über verschiedene Versionen Ihrer App hinweg erfassen und gezielt ansprechen – ob iOS, Android oder Internet. So stellen Sie sicher, dass Sie stets aktuelle Informationen über alle Nutzer:innen haben, unabhängig davon, welche Plattform diese verwenden.
- **Unterschiedliche Aktivitäten trennen:** Workspaces bieten außerdem die Möglichkeit, verschiedene Marken oder Aktivitäten voneinander zu trennen. Wenn Sie beispielsweise mehrere Submarken mit unterschiedlichen Nutzergruppen haben, ist es sinnvoll, für jede einen eigenen Workspace zu erstellen.

{% alert tip %}
Dieser Ansatz ist besonders nützlich für Unternehmen wie Mobile-Gaming-Firmen, die einzelne Workspaces für jedes ihrer Spiele verwalten können, oder für E-Commerce-Websites, die separate Workspaces für jede Region einrichten möchten, in der sie tätig sind.
{% endalert %}

## Workspaces planen {#planning-workspaces}

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie entscheiden, welche App-Instanzen in einem Workspace enthalten sein sollen, überlegen Sie, welche Nutzer:innen Sie ansprechen möchten, und gruppieren Sie diese entsprechend.

Es kann verlockend sein, mehrere App-Instanzen in einem Workspace zu haben, da Sie so das Frequency-Capping für Ihr gesamtes App-Portfolio anwenden können. Als Best Practice empfehlen wir jedoch, nur verschiedene Versionen derselben (oder sehr ähnlicher) Apps in einem Workspace zusammenzufassen.

### Gemeinsam genutzte Workspaces {#shared-workspaces}

Typische Beispiele, wann Sie mehrere App-Instanzen im selben Workspace haben möchten:

- Wenn Sie mehrere, nahezu identische Apps auf verschiedenen Plattformen haben
- Wenn Sie verschiedene Hauptversionen der App haben, aber weiterhin dieselben Nutzer:innen ansprechen möchten, wenn sie ein Upgrade durchführen
- Wenn Sie verschiedene Versionen der App haben, zwischen denen dieselben Nutzer:innen wechseln können (z. B. von kostenlos zu Premium)

#### Auswirkungen auf Segmentierungsfilter {#impact-on-segmentation-filters}

Alle Apps, die Sie in einem Workspace zusammenfassen, haben aggregierte Daten. Dies hat spürbare Auswirkungen auf die folgenden Segmentierungsfilter in Braze (dies ist keine vollständige Liste):

- Zuletzt verwendete App
- Zuerst verwendete App
- Sitzungsanzahl
- In-App ausgegebener Betrag
- Push-Abo (Dies wird zu einer Alles-oder-Nichts-Situation – wenn Ihre Nutzer:innen sich von einer App abmelden, sind sie von allen Apps im Workspace abgemeldet.)
- E-Mail-Abo (Dies wird zu einer Alles-oder-Nichts-Situation und kann Compliance-Probleme verursachen.)

{% alert note %}
Die Aggregation von Daten über App-Instanzen hinweg bei diesen Filtern ist der Grund, warum wir davon abraten, grundlegend verschiedene Apps im selben Workspace unterzubringen. Das Targeting kann dadurch schwierig werden!
{% endalert %}

### Getrennte Workspaces {#separate-workspaces}

In anderen Fällen möchten Sie möglicherweise mehrere, getrennte Workspaces haben. Typische Beispiele dafür sind:

- Getrennte Workspaces für Entwicklungs- und Produktionsumgebungen derselben App
- Verschiedene Untermarken, z. B. ein Mobilspiele-Unternehmen, das mehrere Spiele anbietet
- Verschiedene Lokalisierungen derselben App oder Website, die in verschiedenen Ländern betrieben werden oder verschiedene Sprachen ansprechen

### Wichtige Überlegungen {#important-considerations}

Denken Sie daran, dass Workspaces als separate Daten-Silos fungieren. Alle Daten, ob Nutzerdaten oder Marketing-Assets, werden innerhalb eines Workspaces gespeichert. Diese Daten können nicht einfach außerhalb dieses Workspaces geteilt werden.

Die folgenden Elemente werden alle innerhalb eines Workspaces konfiguriert:

- [App-Instanzen](#app-instances)
- [Teams](#teams)
- [Unternehmensnutzer:innen-Berechtigungen](#company-user-permissions) (aber nicht die Unternehmensnutzer:innen selbst)
- [Currents-Konnektoren](#currents-connectors)
- [Nutzerprofile](#user-profiles) und die zugehörigen Nutzerdaten
- [Segments, Campaigns und Canvases](#segments-campaigns-and-canvases)

#### App-Instanzen {#app-instances}

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie z. B. eine Free- und eine Pro-Version Ihrer App sowohl auf iOS als auch auf Android haben, erstellen Sie vier App-Instanzen in Ihrem Workspace (kostenlose iOS-App, kostenlose Android-App, Pro-iOS-App und Pro-Android-App). Dies gibt Ihnen vier API-Schlüssel, einen für jede App-Instanz.

#### Teams {#teams}

[Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) können nach Kundenstandort, Sprache und angepassten Attributen eingerichtet werden, sodass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Features und Kundendaten haben.

#### Unternehmensnutzer:innen-Berechtigungen {#company-user-permissions}

Workspaces haben unabhängige Zugriffs- und Berechtigungsdefinitionen. [Nutzer:innen-Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) ermöglichen es Ihnen, granulare Kontrollen darüber zu erstellen, worauf einzelne Dashboard-Nutzer:innen oder Teams innerhalb eines einzelnen Workspaces Zugriff haben.

#### Currents-Konnektoren {#currents-connectors}

Das [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Tool ist ein Echtzeitdatenstrom Ihrer Engagement-Events und der umfangreichste, aber dennoch granularste Export aus der Braze-Plattform. Currents-Konnektoren sind in bestimmten Braze-Paketen enthalten, und Sie haben möglicherweise zunächst einen erhalten, basierend auf der Annahme eines einzelnen Workspaces.

Wenn Sie sich zwischen getrennten oder kombinierten Workspaces entscheiden, ist es wichtig, an die Anzahl Ihrer Currents-Konnektoren zu denken, da Currents-Konnektoren nicht zwischen Workspaces geteilt werden.

Wenn Sie z. B. getrennte Workspaces für die Entwicklungs- und Produktionsumgebungen derselben App haben, aktivieren Sie Ihren Currents-Konnektor im Produktions-Workspace. Um Currents in beiden Workspaces zu aktivieren, müssen Sie einen zusätzlichen Currents-Konnektor erwerben.

#### Nutzerprofile {#user-profiles}

Alle persistenten Daten, die mit Nutzer:innen verknüpft sind, werden in ihrem [Kundenprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) gespeichert. Nutzerprofile sind jedoch auch eine hervorragende Ressource für Fehlerbehebung und Tests, da Sie einfach auf Informationen zum Engagement-Verlauf, zur Segmentzugehörigkeit, zum Gerät und zum Betriebssystem von Nutzer:innen zugreifen können.

#### Segments, Campaigns und Canvases {#segments-campaigns-and-canvases}

Ein Segment, eine Campaign oder ein Canvas kann nicht auf Daten zugreifen oder diese referenzieren, die in einem anderen Workspace gespeichert sind. Umgekehrt werden die Daten aller Apps im selben Workspace aggregiert, wenn sich mehrere Apps in einem Workspace befinden. Dies hat [Auswirkungen auf Filter in Braze](#impact-on-segmentation-filters).

### Überblick über beide Ansätze {#overview-of-each-approach}

Die folgende Tabelle beschreibt die Vorteile und Nachteile dieser beiden Ansätze zur Workspace-Planung:

- **Getrennte Workspaces und Nutzerprofile:** Ein Workspace hat eine App-Instanz, und eine Person hat ein Kundenprofil für diese App-Instanz.
- **Gemeinsame Workspaces und Nutzerprofile:** Ein Workspace hat mehrere App-Instanzen, und eine Person hat ein Kundenprofil für alle diese App-Instanzen.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
</style>

<table aria-label="Überblick über beide Ansätze">
  <caption>Überblick über beide Ansätze</caption>
    <thead>
    <tr>
        <th></th>
        <th colspan="2" scope="colgroup">Getrennte Workspaces</th>
        <th colspan="2" scope="colgroup">Gemeinsame Workspaces</th>
    </tr>
    <tr>
        <th></th>
        <th scope="col">Vorteile</th>
        <th scope="col">Nachteile</th>
        <th scope="col">Vorteile</th>
        <th scope="col">Nachteile</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th scope="row">Targeting</th>
        <td>Sicherste Methode, um Kommunikation getrennt zu halten. Campaigns sprechen garantiert nur bestimmte Nutzerprofile an.</td>
        <td>Cross-Promotion-Nachrichten können nicht gesendet werden, selbst wenn Sie wissen, dass Nutzer:innen ein weiteres Kundenprofil in einem anderen Workspace haben.</td>
        <td>Cross-Promotion-Nachrichten können gesendet werden, wenn Sie wissen, dass Nutzer:innen mehrere Apps in Ihrem Workspace haben.<br><br>Nutzerdaten aus verschiedenen Apps können referenziert werden. Beispiel: Max hat das Attribut X, das für App 1 relevant ist, und das Attribut Y, das für App 2 relevant ist – beide können in einer Campaign referenziert werden.</td>
        <td>Mehr Raum für menschliche Fehler – Sie könnten versehentlich Nutzer:innen über mehrere App-Instanzen hinweg ansprechen.<br><br>Um In-App-Nachrichten zu senden, benötigen Sie app-spezifische angepasste Events, damit eine Campaign nicht versehentlich in einer anderen App angezeigt wird. Zum Beispiel <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Angepasste Events und Attribute</th>
        <td>Angepasste Attribute und Events sind garantiert spezifisch für eine App-Instanz.</td>
        <td>Nutzerverhalten kann nicht workspace-übergreifend verfolgt werden.<br><br><b>Tipp:</b> Sie können mehrere Currents-Konnektoren nutzen, um dies zu erreichen.</td>
        <td>Nutzerverhalten kann über alle App-Instanzen im Workspace hinweg verfolgt werden.</td>
        <td>Angepasste Attribute und Events gelten für alle App-Instanzen, was es schwierig machen kann, zu erkennen, welche Daten in einem Kundenprofil für welche App-Instanz relevant sind. Beispiel: Ist „date_of_parking“ relevant für App 1 oder App 2? Verwenden Sie daher gut strukturierte Namenskonventionen.</td>
    </tr>
    <tr>
        <th scope="row">Frequency-Capping</th>
        <td>Frequency-Capping kann für jede App-Instanz separat definiert werden (basierend auf dem Workspace).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Frequency-Capping gilt für alle Campaigns, nicht pro App, was es schwieriger macht, Über-Messaging bei Kund:innen zu verhindern.</td>
    </tr>
    <tr>
        <th scope="row">Abo-Status für Nutzerprofile</th>
        <td>Der Abo-Status jedes Nutzerprofils ist eindeutig für jede App-Instanz.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Die Abo-Status eines Nutzerprofils werden über App-Instanzen hinweg zusammengeführt.<br><br><b>Tipp:</b> Sie könnten stattdessen <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>angepasste Attribute</a> verwenden, um die Abos Ihrer Nutzer:innen zu verwalten.</td>
    </tr>
    <tr>
        <th scope="row">Unternehmensnutzer:innen-Berechtigungen</th>
        <td>N/A</td>
        <td>Die Aktualisierung der <a href='/docs/user_guide/administer/global/user_management/permissions'>Nutzer:innen-Berechtigungen</a> für Dashboard-Nutzer:innen muss separat für jeden Workspace erfolgen, auf den sie Zugriff benötigen.</td>
        <td><a href='/docs/user_guide/administer/global/user_management/permissions'>Nutzer:innen-Berechtigungen</a> können einmalig für Dashboard-Nutzer:innen festgelegt werden und gelten dann für alle App-Instanzen im Workspace.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Inhalte duplizieren</th>
        <td>N/A</td>
        <td>Einige Inhalte, wie Segmente und Content-Card-Kampagnen, können nicht zwischen Workspaces kopiert werden.</td>
        <td>Sie können <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces'>Campaigns, Canvases und Landing-Pages über Workspaces kopieren</a>. Unterstützte Inhalte umfassen Campaigns und Canvases für berechtigte Kanäle sowie Landing-Pages, E-Mail-Templates, Feature-Flags und Content Blocks.<br><br>Segmente, Campaigns, Canvases und Landing-Pages können dupliziert werden, um Inhalte von einer App-Instanz für eine andere wiederzuverwenden.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Analytics</th>
        <td>Globale Statistiken sind auf der Startseite korrekt.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Globale Statistiken werden auf der Startseite für alle App-Instanzen im Workspace aggregiert.</td>
    </tr>
    </tbody>
</table>

{% alert note %}
Informationen dazu, wie sich MAU bei der Ansicht aller Apps im Vergleich zu einer einzelnen App unterscheiden, finden Sie unter [Monatlich aktive Nutzer:innen]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users).
{% endalert %}

## Best Practices {#best-practices}

### Einen Test-Workspace einrichten {#set-up-a-testing-workspace}

Es empfiehlt sich, immer dann, wenn Sie einen Produktions-Workspace einrichten möchten (einen Workspace, der Nachrichten an echte Nutzer:innen sendet), auch einen Test-Workspace einzurichten. Ein Test-Workspace ist ein Duplikat Ihres Produktions-Workspace ohne echte Nutzerdaten.

Dies gilt aus mehreren Gründen als Best Practice:

- **Isolation von Änderungen:** Sie können neue Features, Konfigurationen oder Updates in einer isolierten Umgebung testen, ohne Ihre Live-Produktionsumgebung zu beeinträchtigen. Sollte beim Testen etwas schiefgehen, bleibt Ihre Produktionsumgebung davon unberührt.
- **Genaues Testen:** Es ermöglicht genaueres Testen, da die Daten in der Testumgebung kontrolliert und manipuliert werden können, ohne sich um reale Daten sorgen zu müssen.
- **Debugging:** Es ist einfacher, Probleme in einer Testumgebung zu debuggen, da Sie die Umgebung frei verändern können, ohne die Produktionsumgebung zu beeinträchtigen.
- **Schulung:** Neue Teammitglieder können sich mit dem Workspace in einer sicheren Umgebung vertraut machen, in der Fehler keine realen Konsequenzen haben.

{% alert tip %}
Die Reihenfolge, in der Sie einen Test-Workspace und einen Produktions-Workspace einrichten, kann von Ihren spezifischen Anforderungen und Umständen abhängen. Es ist jedoch generell empfehlenswert, zuerst einen Test-Workspace einzurichten. So können Sie Features, Konfigurationen und Updates testen, bevor sie im Produktions-Workspace implementiert werden. Wenn Sie mit den Tests und Ergebnissen zufrieden sind, können Sie anschließend Ihren Produktions-Workspace einrichten.
{% endalert %}

### Administrator:innen hinzufügen {#add-administrators}

Sie sollten mehr als eine:n Braze-Nutzer:in mit Administratorberechtigungen für einen einzelnen Workspace haben. So ist sichergestellt, dass genügend Personen in Ihrer Organisation die Berechtigungen anderer Nutzer:innen verwalten können.

## Nächste Schritte {#next-steps}

Nachdem Sie Ihren Workspace-Plan festgelegt haben, können Sie Ihren Workspace erstellen und App-Instanzen hinzufügen. Die einzelnen Schritte finden Sie unter [Workspaces erstellen und verwalten]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).