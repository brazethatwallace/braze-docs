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

Workspaces dienen zwei wesentlichen Zwecken:

- **Nutzerdaten vereinheitlichen:** Wenn sich mehrere App-Instanzen in einem Workspace befinden, können Sie Nutzerdaten nahtlos über verschiedene Versionen Ihrer App hinweg – wie iOS, Android und Internet – zusammenstellen und adressieren. So stellen Sie sicher, dass Sie immer über aktuelle Informationen zu jeder Nutzerin und jedem Nutzer verfügen, unabhängig von der verwendeten Plattform.
- **Verschiedene Aktivitäten trennen:** Workspaces bieten auch die Möglichkeit, verschiedene Marken oder Aktivitäten voneinander zu trennen. Wenn Sie zum Beispiel mehrere Untermarken mit unterschiedlichen Nutzerbasen haben, ist es von Vorteil, für jede Marke einen eigenen Workspace zu erstellen.

{% alert tip %}
Dieser Ansatz ist besonders nützlich für Unternehmen wie Firmen für mobile Spiele, die individuelle Workspaces für jedes ihrer Spiele verwalten können, oder für E-Commerce-Websites, die für jede Region, in der sie tätig sind, separate Workspaces wünschen.
{% endalert %}

## Workspaces planen {#planning-workspaces}

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie entscheiden, welche App-Instanzen in einen Workspace aufgenommen werden sollen, denken Sie an die Nutzer:innen, die Sie ansprechen möchten, und gruppieren Sie sie entsprechend.

Die Möglichkeit, mehrere App-Instanzen in einem Workspace zu haben, kann verlockend sein, da Sie so Rate-Limits für das Messaging in Ihrem gesamten App-Portfolio festlegen können. Es empfiehlt sich jedoch, nur verschiedene Versionen derselben (oder sehr ähnlicher) Apps in einem Workspace zusammenzufassen.

### Gemeinsame Workspaces {#shared-workspaces}

Häufige Beispiele dafür, wann Sie mehrere App-Instanzen im selben Workspace haben möchten:

- Wenn Sie mehrere, nahezu identische Apps auf verschiedenen Plattformen haben
- Wenn Sie verschiedene Hauptversionen der App haben, aber dieselben Nutzer:innen beim Upgrade weiterhin einbeziehen möchten
- Wenn Sie verschiedene Versionen der App haben, zwischen denen ein und dieselbe Person wechseln kann (z. B. von kostenlos zu Premium)

#### Auswirkungen auf Segmentierungsfilter {#impact-on-segmentation-filters}

Die Daten aller Apps, die Sie in einem Workspace zusammenfassen, werden aggregiert. Dies hat erhebliche Auswirkungen auf die folgenden Segmentierungsfilter in Braze (diese Liste ist nicht vollständig):

- Letzte App-Nutzung
- Erste App-Nutzung
- Sitzungsanzahl
- In-App ausgegebenes Geld
- Push-Abo (Dies wird zu einer Alles-oder-nichts-Situation – wenn Ihre Nutzer:innen sich von einer App abmelden, werden sie von allen Apps im Workspace abgemeldet.)
- E-Mail-Abo (Dies wird zu einer Alles-oder-nichts-Situation und kann zu Compliance-Problemen führen.)

{% alert note %}
Die Aggregation von Daten über App-Instanzen hinweg in diesen Filtern ist der Grund, warum wir nicht empfehlen, wesentlich unterschiedliche Apps im selben Workspace unterzubringen. Das kann das Targeting erschweren!
{% endalert %}

### Getrennte Workspaces {#separate-workspaces}

In anderen Fällen möchten Sie vielleicht mehrere, separate Workspaces haben. Gängige Beispiele hierfür sind:

- Getrennte Workspaces für Entwicklungs- und Produktionsumgebungen derselben App
- Verschiedene Untermarken, z. B. ein Handyspiel-Unternehmen, das mehrere Spiele anbietet
- Unterschiedliche Lokalisierungen derselben App oder Website, die in verschiedenen Ländern betrieben werden oder auf verschiedene Sprachen abzielen

### Wichtige Überlegungen {#important-considerations}

Denken Sie daran, dass Workspaces als separate Datensilos fungieren. Alle Daten – seien es Nutzerdaten oder Marketing-Assets – werden innerhalb eines Workspace gespeichert. Diese Daten können nicht ohne Weiteres außerhalb dieses Workspace geteilt werden.

Im Folgenden finden Sie alle wichtigen Elemente, die innerhalb eines Workspace konfiguriert werden:

- [App-Instanzen](#app-instances)
- [Teams](#teams)
- [Unternehmensnutzer:innen-Berechtigungen](#company-user-permissions) (jedoch nicht die Unternehmensnutzer:innen selbst)
- [Currents-Konnektoren](#currents-connectors)
- [Nutzerprofile](#user-profiles) und die zugehörigen Nutzerdaten
- [Segmente, Campaigns und Canvases](#segments-campaigns-and-canvases)

#### App-Instanzen {#app-instances}

Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie zum Beispiel eine kostenlose und eine Pro-Version Ihrer App für iOS und Android haben, erstellen Sie vier App-Instanzen in Ihrem Workspace (kostenlose iOS-App, kostenlose Android-App, Pro-iOS-App und Pro-Android-App). So erhalten Sie vier API-Schlüssel – einen für jede App-Instanz.

#### Teams {#teams}

[Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) können nach Kundenstandort, Sprache und angepassten Attributen eingerichtet werden, sodass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Funktionen und Kundendaten haben.

#### Unternehmensnutzer:innen-Berechtigungen {#company-user-permissions}

Workspaces haben unabhängige Zugriffs- und Berechtigungsdefinitionen. Mit [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) können Sie granular festlegen, worauf eine einzelne Dashboard-Nutzerin bzw. ein einzelner Dashboard-Nutzer oder ein Team innerhalb eines einzelnen Workspace Zugriff hat.

#### Currents-Konnektoren {#currents-connectors}

Das [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)-Tool ist ein Realtime-Daten-Stream Ihrer Engagement-Ereignisse und der robusteste und zugleich granularste Export der Braze-Plattform. Currents-Konnektoren sind in bestimmten Braze-Paketen enthalten, und möglicherweise haben Sie zunächst einen erhalten, der einen einzigen Workspace voraussetzt.

Wenn Sie sich entscheiden, ob Sie getrennte oder kombinierte Workspaces erstellen möchten, sollten Sie die Anzahl Ihrer Currents-Konnektoren berücksichtigen, da Currents-Konnektoren nicht über Workspaces hinweg gemeinsam genutzt werden.

Wenn Sie beispielsweise getrennte Workspaces für die Entwicklungs- und die Produktionsumgebung derselben App haben, aktivieren Sie Ihren Currents-Konnektor im Produktions-Workspace. Um Currents in beiden Workspaces zu aktivieren, müssen Sie einen zusätzlichen Currents-Konnektor erwerben.

#### Nutzerprofile {#user-profiles}

Alle persistenten Daten, die mit einer Nutzerin oder einem Nutzer verknüpft sind, werden in ihrem [Nutzerprofil]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) gespeichert. Nutzerprofile sind jedoch auch eine hervorragende Ressource für die Fehlerbehebung und das Testen, da Sie einfach auf Informationen zur Engagement-Historie, Segmentzugehörigkeit, zum Gerät und zum Betriebssystem zugreifen können.

#### Segmente, Campaigns und Canvases {#segments-campaigns-and-canvases}

Ein Segment, eine Campaign oder ein Canvas kann nicht auf Daten zugreifen oder diese referenzieren, die sich in einem anderen Workspace befinden. Befinden sich dagegen mehrere Apps im selben Workspace, werden die Daten aller Apps zusammengefasst. Dies hat [Auswirkungen auf die Filter in Braze](#impact-on-segmentation-filters).

### Überblick über die einzelnen Ansätze {#overview-of-each-approach}

Die folgende Tabelle beschreibt die Vor- und Nachteile dieser beiden Ansätze zur Workspace-Planung:

- **Getrennte Workspaces und Nutzerprofile:** Ein Workspace hat eine App-Instanz und eine Person hat ein Nutzerprofil für diese App-Instanz.
- **Gemeinsame Workspaces und Nutzerprofile:** Ein Workspace hat mehrere App-Instanzen und eine Person hat ein Nutzerprofil für alle diese App-Instanzen.

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
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
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
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
</style>

<table aria-label="Überblick über die einzelnen Ansätze">
  <caption>Überblick über die einzelnen Ansätze</caption>
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
        <td>Der sicherste Weg, um die Kommunikation zu trennen. Campaigns sind garantiert nur auf bestimmte Nutzerprofile ausgerichtet.</td>
        <td>Sie können keine Cross-Promotion-Nachrichten senden, auch wenn Sie wissen, dass eine Nutzerin oder ein Nutzer ein anderes Nutzerprofil in einem anderen Workspace hat.</td>
        <td>Sie können Cross-Promotion-Nachrichten senden, wenn Sie wissen, dass eine Person mehrere Apps in Ihrem Workspace nutzt.<br><br>Sie können Nutzerdaten aus verschiedenen Apps referenzieren. Zum Beispiel hat John ein Attribut X, das für App 1 relevant ist, und ein Attribut Y, das für App 2 relevant ist – beide können in einer Campaign referenziert werden.</td>
        <td>Mehr Raum für menschliche Fehler – Sie könnten versehentlich Nutzer:innen über mehrere App-Instanzen hinweg ansprechen.<br><br>Um In-App-Nachrichten zu senden, benötigen Sie app-spezifische angepasste Events, damit eine Campaign nicht versehentlich in einer anderen App angezeigt wird. Zum Beispiel <code>app_1_action</code> gegenüber <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Angepasste Events und Attribute</th>
        <td>Angepasste Attribute und Events sind garantiert spezifisch für eine App-Instanz.</td>
        <td>Das Nutzerverhalten kann nicht über Workspaces hinweg verfolgt werden.<br><br><b>Tipp:</b> Dazu können Sie mehrere Currents-Konnektoren nutzen.</td>
        <td>Das Nutzerverhalten kann über alle App-Instanzen im Workspace hinweg verfolgt werden.</td>
        <td>Angepasste Attribute und Events würden für alle App-Instanzen gelten, wodurch es schwierig werden könnte, zu erkennen, welche Daten in einem Nutzerprofil für welche App-Instanz relevant sind. Ist zum Beispiel „date_of_parking“ für App 1 oder App 2 relevant? Um dem entgegenzuwirken, sollten Sie gut strukturierte Namenskonventionen verwenden.</td>
    </tr>
    <tr>
        <th scope="row">Frequency-Capping</th>
        <td>Frequency-Capping kann für jede App-Instanz separat definiert werden (basierend auf dem Workspace).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Frequency-Capping gilt für alle Campaigns, nicht pro App, was es schwieriger macht, eine Überflutung der Kund:innen mit Nachrichten zu verhindern.</td>
    </tr>
    <tr>
        <th scope="row">Abo-Status für Nutzerprofile</th>
        <td>Der Abo-Status jedes Nutzerprofils ist für jede App-Instanz eindeutig.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Die Abo-Status eines Nutzerprofils werden über App-Instanzen hinweg kombiniert.<br><br><b>Tipp:</b> Sie könnten stattdessen <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>angepasste Attribute</a> verwenden, um die Abos Ihrer Nutzer:innen zu verwalten.</td>
    </tr>
    <tr>
        <th scope="row">Unternehmensnutzer:innen-Berechtigungen</th>
        <td>N/A</td>
        <td>Das Aktualisieren der <a href='/docs/user_guide/administer/global/user_management/permissions'>Berechtigungen</a> für eine Dashboard-Nutzerin oder einen Dashboard-Nutzer muss für jeden Workspace, auf den die Person Zugriff benötigt, separat durchgeführt werden.</td>
        <td><a href='/docs/user_guide/administer/global/user_management/permissions'>Berechtigungen</a> können einmalig für eine Dashboard-Nutzerin oder einen Dashboard-Nutzer festgelegt werden und gelten dann für alle App-Instanzen im Workspace.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Duplizieren von Inhalten</th>
        <td>N/A</td>
        <td>Einige Inhalte, wie Segmente und Content-Card-Kampagnen, können nicht über Workspaces hinweg kopiert werden.</td>
        <td>Sie können <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces/'>Campaigns, Canvases und Landing-Pages über Workspaces hinweg kopieren</a>. Unterstützte Inhalte umfassen Campaigns und Canvases für berechtigte Kanäle sowie Landing-Pages, E-Mail-Templates, Feature-Flags und Content Blocks.<br><br>Sie können Segmente, Campaigns, Canvases und Landing-Pages duplizieren, um Inhalte von einer App-Instanz zur anderen wiederzuverwenden.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Analytics</th>
        <td>Die globalen Statistiken werden auf der Startseite korrekt angezeigt.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Die globalen Statistiken werden für alle App-Instanzen im Workspace auf der Startseite zusammengefasst.</td>
    </tr>
    </tbody>
</table>

## Best Practices {#best-practices}

### Einen Test-Workspace einrichten {#set-up-a-testing-workspace}

Wenn Sie planen, einen Produktions-Workspace einzurichten (einen Workspace, der Nachrichten an echte Nutzer:innen sendet), sollten Sie auch einen Test-Workspace einrichten. Ein Test-Workspace ist ein Duplikat Ihres Produktions-Workspace ohne echte Nutzerdaten.

Dies gilt aus mehreren Gründen als Best Practice:

- **Isolierung von Änderungen:** Sie können neue Features, Konfigurationen oder Updates in einer isolierten Umgebung testen, ohne Ihre Produktionsumgebung zu beeinträchtigen. Wenn also während der Tests etwas schiefgeht, bleibt Ihre Produktionsumgebung davon unberührt.
- **Genaues Testen:** Die Daten in der Testumgebung können kontrolliert und bearbeitet werden, ohne dass Sie sich Gedanken über reale Daten machen müssen. Das ermöglicht genauere Tests.
- **Fehlerbehebung:** Es ist einfacher, Probleme in einer Testumgebung zu beheben, da Sie die Umgebung frei bearbeiten können, ohne sich Gedanken über die Auswirkungen auf die Produktionsumgebung zu machen.
- **Training:** Neue Teammitglieder können sich in einer sicheren Umgebung mit dem Workspace vertraut machen, in der Fehler keine realen Konsequenzen haben.

{% alert tip %}
Die Reihenfolge, in der Sie einen Test-Workspace und einen Produktions-Workspace einrichten, kann von Ihren spezifischen Bedürfnissen und Umständen abhängen. Es ist jedoch generell eine gute Idee, zunächst einen Test-Workspace einzurichten. So können Sie Features, Konfigurationen und Updates testen, bevor sie im Produktions-Workspace implementiert werden. Wenn Sie mit den Tests und Ergebnissen zufrieden sind, können Sie anschließend Ihren Produktions-Workspace einrichten.
{% endalert %}

### Administrator:innen hinzufügen {#add-administrators}

Sie sollten mehr als eine Braze-Nutzerin oder einen Braze-Nutzer mit Admin-Berechtigungen für einen einzelnen Workspace haben. So stellen Sie sicher, dass es in Ihrem Unternehmen genügend Personen gibt, die die Berechtigungen anderer Nutzer:innen verwalten können.

## Nächste Schritte {#next-steps}

Nachdem Sie Ihren Workspace-Plan festgelegt haben, ist es an der Zeit, Ihren Workspace zu erstellen und App-Instanzen hinzuzufügen. Die entsprechenden Schritte finden Sie unter [Workspaces erstellen und verwalten]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/).