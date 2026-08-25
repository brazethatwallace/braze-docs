---
nav_title: Workspaces
article_title: "Erste Schritte: Workspaces"
page_order: 3
page_type: reference
description: "Alles, was Sie auf der Braze-Plattform tun, geschieht innerhalb eines Workspace. Dieser Artikel beschreibt, wie Workspaces funktionieren und welche wichtigen Aspekte Sie bei der Planung Ihrer Workspaces in Braze beachten sollten."
---

# Erste Schritte: Workspaces {#get-started-workspaces}

> Alles, was Sie auf der Braze-Plattform tun, geschieht innerhalb eines Workspace. Workspaces fungieren als separate Datensilos und ermöglichen es Ihnen, verschiedene Marken oder Aktivitäten voneinander zu trennen. Mehrere Versionen Ihrer Website oder mobilen App können Daten an denselben Workspace senden. Die verschiedenen Websites und Apps, die innerhalb eines Workspace zusammengefasst werden, bezeichnen wir als „App-Instanzen“.

## Workspaces verstehen {#understanding-workspaces}

Workspaces erfüllen zwei wichtige Aufgaben:

- **Nutzerdaten vereinen:** Wenn sich mehrere App-Instanzen in einem Workspace befinden, können Sie Nutzerdaten nahtlos über verschiedene Versionen Ihrer App hinweg erfassen und ansprechen – zum Beispiel iOS, Android und Internet. So stellen Sie sicher, dass Sie stets aktuelle Informationen über jede:n Nutzer:in haben, unabhängig davon, welche Plattform verwendet wird.
- **Unterschiedliche Aktivitäten trennen:** Workspaces bieten außerdem die Möglichkeit, unterschiedliche Marken oder Aktivitäten voneinander zu trennen. Wenn Sie beispielsweise mehrere Untermarken mit verschiedenen Nutzergruppen haben, ist es sinnvoll, für jede einen eigenen Workspace zu erstellen.

{% alert tip %}
Dieser Ansatz ist besonders nützlich für Unternehmen wie Mobile-Gaming-Firmen, die einzelne Workspaces für jedes ihrer Spiele verwalten können, oder für E-Commerce-Websites, die separate Workspaces für jede Region einrichten möchten, in der sie tätig sind.
{% endalert %}

## Workspaces planen {#planning-workspaces}

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Überlegen Sie bei der Entscheidung, welche App-Instanzen in einen Workspace aufgenommen werden sollen, welche Nutzer:innen Sie ansprechen möchten, und gruppieren Sie diese entsprechend.

Es kann verlockend sein, mehrere App-Instanzen in einem Workspace zu bündeln, da Sie so das Frequency-Capping für Nachrichten über Ihr gesamtes App-Portfolio hinweg steuern können. Als Best Practice empfehlen wir jedoch, nur verschiedene Versionen derselben (oder sehr ähnlicher) Apps in einem gemeinsamen Workspace zusammenzufassen.

### Gemeinsame Workspaces {#shared-workspaces}

Typische Beispiele, in denen Sie mehrere App-Instanzen im selben Workspace haben möchten:

- Wenn Sie mehrere, nahezu identische Apps auf verschiedenen Plattformen haben
- Wenn Sie verschiedene Hauptversionen der App haben, aber dieselben Nutzer:innen weiterhin ansprechen möchten, wenn sie ein Upgrade durchführen
- Wenn Sie verschiedene Versionen der App haben, zwischen denen dieselben Nutzer:innen wechseln könnten (z. B. von kostenlos zu Premium)

#### Auswirkungen auf Segmentierungsfilter {#impact-on-segmentation-filters}

Die Daten aller Apps, die Sie in einem Workspace zusammenfassen, werden aggregiert. Dies hat erhebliche Auswirkungen auf die folgenden Segmentierungsfilter in Braze (diese Liste ist nicht vollständig):

- Zuletzt verwendete App
- Zuerst verwendete App
- Sitzungsanzahl
- In-App ausgegebener Betrag
- Push-Abo (Dies wird zu einer Alles-oder-nichts-Situation – wenn sich Ihre Nutzer:innen von einer App abmelden, sind sie von allen Apps im Workspace abgemeldet.)
- E-Mail-Abo (Dies wird zu einer Alles-oder-nichts-Situation und kann zu Compliance-Problemen führen.)

{% alert note %}
Die Aggregation der Daten über App-Instanzen hinweg in diesen Filtern ist der Grund, warum wir davon abraten, grundlegend unterschiedliche Apps im selben Workspace unterzubringen. Das kann das Targeting erschweren!
{% endalert %}

### Separate Workspaces {#separate-workspaces}

In anderen Fällen möchten Sie möglicherweise mehrere, separate Workspaces haben. Typische Beispiele hierfür sind:

- Separate Workspaces für Entwicklungs- und Produktionsumgebungen derselben App
- Verschiedene Untermarken, z. B. ein Mobile-Game-Unternehmen mit mehreren Spielen
- Verschiedene Lokalisierungen derselben App oder Website, die in verschiedenen Ländern betrieben werden oder auf verschiedene Sprachen abzielen

### Wichtige Überlegungen {#important-considerations}

Denken Sie daran, dass Workspaces als separate Silos für Daten fungieren. Alle Daten, ob Nutzerdaten oder Marketing-Assets, werden innerhalb eines Workspace gespeichert. Diese Daten können nicht ohne Weiteres außerhalb des Workspace geteilt werden.

Die folgenden Schlüsselelemente werden alle innerhalb eines Workspace konfiguriert:

- [App-Instanzen](#app-instances)
- [Teams](#teams)
- [Benutzerberechtigungen des Unternehmens](#company-user-permissions) (aber nicht die Unternehmensbenutzer selbst)
- [Currents-Konnektoren](#currents-connectors)
- [Nutzerprofile](#user-profiles) und die zugehörigen Nutzerdaten
- [Segments, Campaigns und Canvases](#segments-campaigns-and-canvases)

#### App-Instanzen {#app-instances}

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie beispielsweise eine kostenlose und eine Pro-Version Ihrer App sowohl für iOS als auch für Android haben, erstellen Sie vier App-Instanzen in Ihrem Workspace (kostenlose iOS-App, kostenlose Android-App, Pro-iOS-App und Pro-Android-App). Dadurch erhalten Sie vier API-Schlüssel, einen für jede App-Instanz.

#### Teams {#teams}

[Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) können nach Kundenstandort, Sprache und angepassten Attributen eingerichtet werden, sodass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Features und Kundendaten haben.

#### Benutzerberechtigungen des Unternehmens {#company-user-permissions}

Workspaces verfügen über unabhängige Zugriffs- und Berechtigungsdefinitionen. [Benutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) ermöglichen es Ihnen, granulare Steuerungen dafür zu erstellen, worauf ein einzelner Dashboard-Nutzer oder ein Team innerhalb eines einzelnen Workspace Zugriff hat.

#### Currents-Konnektoren {#currents-connectors}

Das Tool [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ist ein Echtzeit-Datenstrom Ihrer Engagement-Ereignisse und der leistungsfähigste und dennoch granularste Export aus der Braze-Plattform. Currents-Konnektoren sind in bestimmten Braze-Paketen enthalten, und Sie haben möglicherweise zunächst einen erhalten, basierend auf der Annahme eines einzelnen Workspace.

Bei der Entscheidung zwischen separaten oder kombinierten Workspaces sollten Sie die Anzahl Ihrer Currents-Konnektoren berücksichtigen, da diese nicht über Workspaces hinweg geteilt werden.

Wenn Sie beispielsweise separate Workspaces für die Entwicklungs- und Produktionsumgebung derselben App haben, aktivieren Sie Ihren Currents-Konnektor im Produktions-Workspace. Um Currents in beiden Workspaces zu aktivieren, müssen Sie einen zusätzlichen Currents-Konnektor erwerben.

#### Nutzerprofile {#user-profiles}

Alle persistenten Daten, die mit einem Nutzer oder einer Nutzerin verknüpft sind, werden in ihrem [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) gespeichert. Nutzerprofile sind jedoch auch eine hervorragende Ressource für die Fehlerbehebung und das Testen, da Sie leicht auf Informationen zum Engagement-Verlauf, zur Segmentzugehörigkeit, zum Gerät und zum Betriebssystem eines Nutzers oder einer Nutzerin zugreifen können.

#### Segments, Campaigns und Canvases {#segments-campaigns-and-canvases}

Ein Segment, eine Campaign oder ein Canvas kann nicht auf Daten zugreifen oder diese referenzieren, die in einem anderen Workspace gespeichert sind. Umgekehrt werden bei mehreren Apps im selben Workspace die Daten aller Apps aggregiert. Dies hat [Auswirkungen auf die Filter in Braze](#impact-on-segmentation-filters).

### Übersicht über beide Ansätze {#overview-of-each-approach}

Die folgende Tabelle beschreibt die Vor- und Nachteile dieser beiden Ansätze zur Workspace-Planung:

- **Separate Workspaces und Nutzerprofile:** Ein Workspace hat eine App-Instanz, und eine Person hat ein Nutzerprofil für diese App-Instanz.
- **Gemeinsame Workspaces und Nutzerprofile:** Ein Workspace hat mehrere App-Instanzen, und eine Person hat ein Nutzerprofil für alle diese App-Instanzen.

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

<table aria-label="Übersicht über beide Ansätze">
  <caption>Übersicht über beide Ansätze</caption>
    <thead>
    <tr>
        <th></th>
        <th colspan="2" scope="colgroup">Separate Workspaces</th>
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
        <td>Sicherster Weg, Kommunikation getrennt zu halten. Campaigns sind garantiert nur auf bestimmte Nutzerprofile ausgerichtet.</td>
        <td>Es ist nicht möglich, Cross-Promotions zu senden, selbst wenn Sie wissen, dass ein:e Nutzer:in ein weiteres Nutzerprofil in einem anderen Workspace hat.</td>
        <td>Sie können Cross-Promotions senden, wenn Sie wissen, dass ein:e Nutzer:in mehrere Apps in Ihrem Workspace hat.<br><br>Können Nutzerdaten aus verschiedenen Apps referenzieren. Zum Beispiel: John hat Attribut X, das für App 1 relevant ist, und Attribut Y, das für App 2 relevant ist – beide können in einer Campaign referenziert werden.</td>
        <td>Mehr Spielraum für menschliche Fehler – Sie könnten versehentlich Nutzer:innen über mehrere App-Instanzen hinweg ansprechen.<br><br>Um In-App-Nachrichten zu senden, müssen Sie App-spezifische angepasste Events verwenden, damit eine Campaign nicht versehentlich in einer anderen App angezeigt wird. Zum Beispiel <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Angepasste Events und Attribute</th>
        <td>Angepasste Attribute und Events sind garantiert spezifisch für eine App-Instanz.</td>
        <td>Das Nutzerverhalten kann nicht über Workspaces hinweg verfolgt werden.<br><br><b>Tipp:</b> Sie können mehrere Currents-Konnektoren nutzen, um dies zu erreichen.</td>
        <td>Das Nutzerverhalten kann über alle App-Instanzen im Workspace hinweg verfolgt werden.</td>
        <td>Angepasste Attribute und Events würden für alle App-Instanzen gelten, was es schwierig machen kann festzustellen, welche Daten in einem Nutzerprofil für welche App-Instanz relevant sind. Zum Beispiel: Ist „date_of_parking“ für App 1 oder App 2 relevant? Um dem entgegenzuwirken, verwenden Sie gut strukturierte Namenskonventionen.</td>
    </tr>
    <tr>
        <th scope="row">Frequency-Capping</th>
        <td>Frequency-Capping kann separat für jede App-Instanz definiert werden (basierend auf dem Workspace).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Frequency-Capping gilt für alle Campaigns, nicht pro App, was es schwieriger macht, eine Überflutung der Kund:innen mit Nachrichten zu verhindern.</td>
    </tr>
    <tr>
        <th scope="row">Abo-Status für Nutzerprofile</th>
        <td>Der Abo-Status jedes Nutzerprofils ist für jede App-Instanz eindeutig.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Die Abo-Status eines Nutzerprofils werden über App-Instanzen hinweg zusammengeführt.<br><br><b>Tipp:</b> Sie können <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>angepasste Attribute</a> verwenden, um die Abos Ihrer Nutzer:innen stattdessen zu verwalten.</td>
    </tr>
    <tr>
        <th scope="row">Benutzerberechtigungen des Unternehmens</th>
        <td>N/A</td>
        <td>Die Aktualisierung der <a href='/docs/user_guide/administer/global/user_management/permissions'>Benutzerberechtigungen</a> für einen Dashboard-Nutzer muss für jeden Workspace, auf den der Nutzer Zugriff benötigt, separat erfolgen.</td>
        <td><a href='/docs/user_guide/administer/global/user_management/permissions'>Benutzerberechtigungen</a> können einmalig für einen Dashboard-Nutzer festgelegt werden, und diese gelten dann für alle App-Instanzen im Workspace.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Inhalte duplizieren</th>
        <td>N/A</td>
        <td>Einige Inhalte, wie Segments und Content-Card-Kampagnen, können nicht über Workspaces hinweg kopiert werden.</td>
        <td>Sie können <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces'>Campaigns, Canvases und Landing-Pages über Workspaces hinweg kopieren</a>. Unterstützte Inhalte umfassen Campaigns und Canvases für berechtigte Kanäle sowie Landing-Pages, E-Mail-Templates, Feature-Flags und Content Blocks.<br><br>Sie können Segments, Campaigns, Canvases und Landing-Pages duplizieren, um Inhalte von einer App-Instanz in eine andere wiederzuverwenden.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Analytics</th>
        <td>Globale Statistiken sind auf der Startseite korrekt.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Globale Statistiken werden für alle App-Instanzen im Workspace auf der Startseite aggregiert.</td>
    </tr>
    </tbody>
</table>

{% alert note %}
Wie sich MAU bei der Anzeige aller Apps im Vergleich zu einer einzelnen App unterscheidet, erfahren Sie unter [Monatlich aktive Nutzer:innen]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users).
{% endalert %}

## Best Practices {#best-practices}

### Einen Test-Workspace einrichten {#set-up-a-testing-workspace}

Als Best Practice sollten Sie immer dann, wenn Sie einen Produktions-Workspace einrichten möchten (einen Workspace, der Nachrichten an echte Nutzer:innen sendet), auch einen Test-Workspace einrichten. Ein Test-Workspace ist ein Duplikat Ihres Produktions-Workspace ohne echte Nutzerdaten.

Dies gilt aus mehreren Gründen als Best Practice:

- **Isolation von Änderungen:** Sie können neue Features, Konfigurationen oder Updates in einer isolierten Umgebung testen, ohne Ihre Live-Produktionsumgebung zu beeinträchtigen. Wenn beim Testen etwas schiefgeht, bleibt Ihre Produktionsumgebung davon unberührt.
- **Genaues Testen:** Es ermöglicht genaueres Testen, da die Daten in der Testumgebung kontrolliert und manipuliert werden können, ohne sich um reale Daten sorgen zu müssen.
- **Debugging:** In einer Testumgebung lassen sich Probleme leichter debuggen, da Sie die Umgebung frei manipulieren können, ohne die Produktionsumgebung zu beeinträchtigen.
- **Schulung:** Neue Teammitglieder können sich in einer sicheren Umgebung mit dem Workspace vertraut machen, in der Fehler keine realen Konsequenzen haben.

{% alert tip %}
Die Reihenfolge, in der Sie einen Test-Workspace und einen Produktions-Workspace einrichten, kann von Ihren spezifischen Anforderungen und Umständen abhängen. Im Allgemeinen ist es jedoch ratsam, zuerst einen Test-Workspace einzurichten. So können Sie Features, Konfigurationen und Updates testen, bevor sie im Produktions-Workspace implementiert werden. Sobald Sie mit den Tests und Ergebnissen zufrieden sind, können Sie anschließend Ihren Produktions-Workspace einrichten.
{% endalert %}

### Administrator:innen hinzufügen {#add-administrators}

Sie sollten mehr als eine:n Braze-Nutzer:in mit Administratorberechtigungen für einen einzelnen Workspace haben. So ist sichergestellt, dass genügend Personen in Ihrer Organisation die Berechtigungen anderer Nutzer:innen verwalten können.

## Nächste Schritte {#next-steps}

Nachdem Sie Ihren Workspace-Plan festgelegt haben, ist es an der Zeit, Ihren Workspace zu erstellen und App-Instanzen hinzuzufügen. Die einzelnen Schritte finden Sie unter [Workspaces erstellen und verwalten]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).