---
nav_title: Teams
article_title: Teams
page_order: 2
page_type: reference
alias: /teams/
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Teams im Dashboard verwenden können. Hier erfahren Sie, wie Sie Teams erstellen, Rollen zuweisen und Tags und Filter zuordnen können."

---

# Teams {#teams}

> Als Braze-Administrator:in können Sie die Nutzer:innen Ihres Unternehmens in Teams mit unterschiedlichen Rollen und Berechtigungen gruppieren. Dies ermöglicht es Ihnen, mehrere, voneinander unabhängige Gruppen von Unternehmensnutzer:innen in einem Workspace zusammenarbeiten zu lassen, indem die Arten von Inhalten, die bearbeitet werden können, voneinander getrennt werden.

Teams können nach Standort der Kundenbasis, Sprache und angepassten Attributen eingerichtet werden, sodass Teammitglieder und Nicht-Teammitglieder unterschiedlichen Zugriff auf Messaging-Features und Kundendaten haben. Team-Filter und Tags können über verschiedene Engagement-Tools zugewiesen werden. Es gibt keine Begrenzung hinsichtlich der Anzahl der Teams, die Sie in Ihrem Workspace erstellen können.

Teams sind nicht in allen Braze-Verträgen enthalten. Um auf dieses Feature zuzugreifen, wenden Sie sich bitte an Ihren Braze Account Manager oder [kontaktieren Sie uns](mailto:success@braze.com) für eine Beratung.

## Wie unterscheiden sich Teams von Berechtigungssets und Rollen? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Teams erstellen {#creating-teams}

Gehen Sie zu **Einstellungen** > **Interne Teams** und wählen Sie <i class="fas fa-plus"></i> **Team hinzufügen**.

![Fenster zum Hinzufügen eines neuen Teams.]({% image_buster /assets/img_archive/adding_a_team.png %})

Geben Sie den **Teamnamen** ein. Verwenden Sie bei Bedarf das Feld **Team definieren (Optional)**, um ein angepasstes Attribut, einen Standort oder eine Sprache auszuwählen und so genauer festzulegen, auf welche Nutzerdaten das Team Zugriff hat. Ein möglicher Anwendungsfall ist beispielsweise das [Testen mit Teams](#test-with-teams), indem Sie ein Entwicklungsteam erstellen, das nur Zugriff auf Testnutzer:innen hat, die durch ein angepasstes Attribut identifiziert werden. Ein weiterer Anwendungsfall ist die Einschränkung der Kommunikation mit Nutzer:innen basierend auf dem Produkt.

Wenn ein Team durch ein angepasstes Attribut, eine Sprache oder ein Land definiert ist, können Sie das Team verwenden, um Endnutzer:innen für Features wie Campaigns, Canvases, Content Cards, Segmente und mehr zu filtern. Weitere Informationen finden Sie unter [Team-Tags zuweisen](#tags-and-filters).

## Nutzer:innen Teams zuweisen {#assign-users-to-teams}

Braze-Administrator:innen und eingeschränkte Nutzer:innen mit der unternehmensweiten Berechtigung „Unternehmenseinstellungen verwalten“ können einem/einer Unternehmensnutzer:in mit eingeschränktem Zugriff Berechtigungen auf Team-Ebene zuweisen. Wenn Unternehmensnutzer:innen einem Team zugewiesen werden, sind sie darauf beschränkt, nur Daten zu lesen oder zu schreiben, die ihren jeweiligen Teams zur Verfügung stehen – beispielsweise Nutzersprache, Standort oder angepasste Attribute, wie bei der Erstellung des Teams festgelegt.

### Berechtigungen von Unternehmensnutzer:innen einschränken, ohne sie zu löschen {#limit-company-user-permissions-without-deleting-a-user}

Um zu verhindern, dass sich ein:e Unternehmensnutzer:in anmeldet, ohne das Konto zu löschen, [sperren Sie die/den Nutzer:in]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users). Durch die Sperrung wird das Konto in einen inaktiven Zustand versetzt, in dem sich die/der Nutzer:in nicht anmelden kann.

Wenn die/der Nutzer:in sich weiterhin mit eingeschränkten Möglichkeiten anmelden können soll, gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen**, wählen Sie die/den Nutzer:in aus und bearbeiten Sie die Berechtigungen. Entfernen Sie Berechtigungen auf Workspace-Ebene für Campaigns, Canvases, Segments und Nutzerdaten und belassen Sie nur minimalen Zugriff – zum Beispiel „Medienbibliothek-Assets anzeigen“. Weitere Informationen finden Sie unter [Berechtigungen einer/eines Nutzer:in bearbeiten]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).

Team-Berechtigungen wirken zusätzlich zu Workspace-Berechtigungen. Wenn Sie die/den Nutzer:in einem Team zuweisen, gewähren Sie nur die minimal erforderlichen Berechtigungen auf Team-Ebene und vergeben Sie keine Berechtigungen für Campaigns, Canvases, Segments oder Nutzerprofile. Die/der Nutzer:in bleibt im Workspace und kann sich anmelden, kann aber die meisten Messaging- oder Zielgruppenaktionen nicht ausführen.

Um eine:n Nutzer:in einem Team zuzuweisen, navigieren Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie eine:n Nutzer:in aus, die/den Sie Ihrem Team hinzufügen möchten.

Führen Sie dann die folgenden Schritte aus:

1. Fügen Sie im Abschnitt **Berechtigungen auf Workspace-Ebene** die/den Nutzer:in dem entsprechenden Workspace hinzu, falls sie/er noch nicht enthalten ist.

![Berechtigungen auf Workspace-Ebene mit der festgelegten Banner-Template-Berechtigung.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Wählen Sie **+ Berechtigungen auf Team-Ebene hinzufügen** und dann das **Team** aus, dem Sie diese:n Nutzer:in hinzufügen möchten.
3. Weisen Sie spezifische Berechtigungen im Abschnitt **Team**-Berechtigungen zu.

![Berechtigungen für Landing-Page-Templates auf Team-Ebene.]({% image_buster /assets/img/teams.png %})

### Verfügbare Berechtigungen auf Team-Ebene {#available-team-level-permissions}

Im Folgenden finden Sie alle verfügbaren Berechtigungen, die Sie auf Team-Ebene zuweisen können. Berechtigungen, die hier nicht aufgeführt sind, werden nur auf Workspace-Ebene gewährt und erscheinen in der Spalte **Teams**-Berechtigungen als „--“.

- Campaigns anzeigen
- Campaigns bearbeiten
- Campaigns archivieren
- Campaigns starten
- Campaigns genehmigen
- Canvases anzeigen
- Canvases bearbeiten
- Canvases archivieren
- Canvases starten
- Canvases genehmigen
- Content Blocks anzeigen
- Content Blocks bearbeiten
- Content Blocks archivieren
- Content Blocks starten
- Segmente anzeigen
- Segmente bearbeiten
- Segmente archivieren
- IAM-Templates anzeigen
- IAM-Templates bearbeiten
- IAM-Templates archivieren
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail-Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- E-Mail-Link-Templates anzeigen
- E-Mail-Link-Templates bearbeiten
- Medienbibliothek-Assets anzeigen
- Medienbibliothek-Assets bearbeiten
- Medienbibliothek-Assets löschen
- Nutzerdaten exportieren
- Nutzerprofile anzeigen (PII geschwärzt)
- PII anzeigen
- Dashboard-Nutzer:innen bearbeiten
- Canvas-Templates bearbeiten
- Canvas-Templates anzeigen
- Canvas-Templates archivieren
- Dashboard-Berichte anzeigen
- Dashboard-Berichte bearbeiten
- Dashboard-Berichte löschen

Beschreibungen der einzelnen Nutzerberechtigungen und ihrer Verwendung finden Sie in unserem Abschnitt [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Team-Tags zuweisen {#tags-and-filters}

Sie können ein Team Canvases, Campaigns, Content Cards, Segmenten, E-Mail-Templates, Webhook-Templates, Content Blocks und Medienbibliothek-Assets mit dem Filter **Team hinzufügen** zuweisen.

Bei Canvases prüft Braze nur beim Eintritt in das Canvas, ob Nutzer:innen die Kriterien des Team-Filters erfüllen. Nachdem ein:e Nutzer:in ein Canvas betreten hat, erhält er/sie weiterhin Nachrichten aus allen Canvas-Schritten, auch wenn sich die Attribute ändern und er/sie die Kriterien des Team-Filters nicht mehr erfüllt. Team-Filter verhalten sich nicht wie [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations), die Nutzer:innen bei jedem Nachrichtenschritt-Versand erneut auswerten.

![Hinzufügen eines Team-Tags zu einer Campaign.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Basierend auf den Definitionen, die bei der Erstellung des Teams festgelegt wurden, wird die Zielgruppe des Engagement-Tools bei Zuweisung eines Team-Filters auf Nutzerprofile beschränkt, die der Definition entsprechen.
- Basierend auf den zugewiesenen Berechtigungen können Teammitglieder nur auf Dashboard-Engagement-Tools zugreifen, für die ihr Team-Filter gesetzt ist. Wenn sie eingeschränkte oder keine Berechtigungen auf Workspace-Ebene haben, müssen sie bestimmten Objekten einen Team-Filter hinzufügen, bevor sie diese speichern oder starten können. Teammitglieder können außerdem Canvases, Campaigns, Content Cards und Segmente nach Team filtern, um für sie relevante Inhalte zu identifizieren.
- Nutzer:innen mit ausschließlich Berechtigungen auf Team-Ebene sehen die Filter **Erstellt von** oder **Zuletzt bearbeitet von** auf den Seiten für Segmente, Campaigns oder Canvases nicht. Braze blendet diese Filter aus, damit Nutzer:innen mit reinen Team-Berechtigungen nicht alle Braze-Nutzer:innen über diese Dropdowns durchsuchen können.

### Anwendungsfälle {#use-cases}

Betrachten Sie die folgenden zwei Szenarien für eine Marketerin bei Braze namens Michelle. Michelle ist Mitglied eines Teams namens „Development“. Sie hat Zugriff auf alle Berechtigungen auf Team-Ebene für das Development-Team.

{% tabs %}
{% tab Szenario 1 – Nur Team-Berechtigungen %}

In diesem Szenario ist Michelle eine eingeschränkte Nutzerin ohne Berechtigungen auf Workspace-Ebene. Ihre Berechtigungen sehen in etwa so aus:

![Angepasste Berechtigungen ohne Berechtigungen auf Workspace-Ebene und 16 teambasierte Berechtigungen.]({% image_buster /assets/img_archive/scenario1.png %})

Basierend auf Michelles zugewiesenen Berechtigungen kann sie beim Erstellen einer Campaign nur das Team „Development“ dieser Campaign zuweisen. Sie kann die Campaign nicht starten, solange das Team nicht zugewiesen ist, und sie kann keine anderen Team-Tags anzeigen oder darauf zugreifen.

![Dropdown für Campaign-Team-Tags, das nur den Team-Tag „Development“ anzeigt.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Szenario 2 – Team-Berechtigungen und Workspace-Berechtigungen %}

In diesem Szenario ist Michelle weiterhin Mitglied des Development-Teams, hat aber zusätzlich eine Berechtigung auf Workspace-Ebene.

![Angepasste Berechtigungen mit einer Berechtigung auf Workspace-Ebene und 15 teambasierten Berechtigungen.]({% image_buster /assets/img_archive/scenario2.png %})

Da Michelle die Berechtigung auf Workspace-Ebene „Zugriff auf Campaigns, Canvases, Cards, Content Blocks, Feature-Flags, Segmente, Medienbibliothek und Präferenzzentren“ hat, kann sie andere Team-Filter anzeigen und der von ihr erstellten Campaign zuweisen.

![Dropdown für Campaign-Team-Tags mit mehreren Team-Tags.]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Ähnlich wie im ersten Szenario muss Michelle den Development-Team-Tag zur Campaign hinzufügen, bevor sie diese starten kann.

{% endtab %}
{% endtabs %}

## Testen mit Teams {#test-with-teams}

Ein möglicher Anwendungsfall für Teams ist die Einrichtung eines teambasierten Genehmigungssystems zum Testen und Veröffentlichen von Inhalten in einer Produktionsumgebung.

Erstellen Sie dazu ein „Development“-Team, das nur Zugriff auf Testnutzer:innen hat. Sie können den Zugriff eines Teams auf Testnutzer:innen beschränken, wenn Ihre Testnutzer:innen anhand eines angepassten Attributs identifizierbar sind. Fügen Sie dann das angepasste Attribut als Definition hinzu, wenn Sie das Team erstellen oder bearbeiten (siehe den vorherigen Abschnitt [Teams erstellen](#creating-Teams)). Ihre Genehmigenden sollten Zugriff auf alle Nutzer:innen haben.

Der allgemeine Ablauf wäre wie folgt:

1. Das Development-Team erstellt eine Campaign und fügt den Team-Tag „Development“ hinzu.
2. Das Development-Team startet die Campaign für Testnutzer:innen.
3. Das Genehmigungsteam überprüft das lokale Campaign-Design, gibt es frei und startet es. Zum Starten ändert das Genehmigungsteam den Team-Tag von „Development“ zu „[All Teams]“ und startet die Campaign erneut.

Für Änderungen an aktiven Campaigns:

1. Das Development-Team klont die laufende Campaign, fügt den Team-Tag „Development“ hinzu und speichert.
2. Das Development-Team nimmt Änderungen vor und teilt sie mit dem Genehmigungsteam.
3. Das Genehmigungsteam entfernt den Team-Tag „Development“, pausiert die vorherige Campaign und startet die neue Campaign.

## Ein bestehendes Team archivieren {#archive-an-existing-team}

Sie können Teams auf der Seite **Interne Teams** archivieren.

Wählen Sie ein oder mehrere Teams zum Archivieren aus. Wenn das Team mit keinem Objekt in Braze verknüpft ist, wird es sofort archiviert. Wenn das Team mit einem Objekt verknüpft ist, wird Ihnen die Option angeboten, das Team nach dem Archivierungsprozess zu entfernen oder zu ersetzen.

![Archivierung eines Teams, das mit einem Objekt in Braze verknüpft ist]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze-Admins können ein Team dearchivieren, indem sie das archivierte Team auswählen und **Dearchivieren** wählen.