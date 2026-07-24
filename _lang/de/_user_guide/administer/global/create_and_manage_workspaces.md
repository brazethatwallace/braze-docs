---
nav_title: Workspaces erstellen und verwalten
article_title: Workspaces erstellen und verwalten
page_order: 0
layout: dev_guide
guide_top_header: "Workspaces erstellen und verwalten"
guide_top_text: "Dieser Artikel beschreibt, wie Sie Ihre Workspaces erstellen, einrichten und verwalten."
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Ihre Workspaces erstellen, einrichten und verwalten."

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
- name: Daten zwischen Workspaces migrieren
  link: /docs/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data
  image: /assets/img/braze_icons/switch-horizontal-01.svg
---

<br>

# Workspaces erstellen und verwalten {#create-and-manage-workspaces}

> Dieser Artikel beschreibt, wie Sie Ihre Workspaces erstellen, einrichten und verwalten.

## Was ist ein Workspace? {#what-is-a-workspace}

Alles, was Sie in Braze tun, findet innerhalb eines Workspace statt. Workspaces sind eine gemeinsame Umgebung, in der Sie das Engagement für zusammengehörige mobile Apps oder Websites verfolgen und verwalten können. Workspaces fassen gleiche oder sehr ähnliche Apps zusammen: zum Beispiel die Android- und iOS-Versionen Ihrer mobilen App.

## Einen Workspace erstellen {#creating-a-workspace}

### 1. Schritt: Einen Plan erstellen {#step-1-have-a-plan}

Bevor Sie beginnen, stellen Sie sicher, dass Sie mit Ihrem Team und Ihrer/Ihrem Braze-Onboarding-Manager:in die beste Workspace-Konfiguration für Ihren Anwendungsfall erarbeitet haben. Um mehr über die Planung Ihrer Workspaces in Braze zu erfahren, lesen Sie unseren Leitfaden [Erste Schritte: Workspaces]({{site.baseurl}}/user_guide/get_started/workspaces).

{% alert warning %}
**Best Practice: Verwenden Sie dedizierte Firebase-Projekte pro Workspace**<br>
Braze erlaubt zwar das Hochladen derselben Firebase-Service-Account-JSON-Datei in mehrere Workspaces, aber alle Workspaces, die dieselbe Google-Projekt-ID verwenden, teilen sich das Standard-Rate-Limit von Firebase Cloud Messaging von 600.000 Nachrichten pro Minute. Absender mit hohem Volumen können bei gleichzeitigen Campaign-Starts über mehrere Workspaces hinweg auf „Quota Exceeded“-Fehler stoßen.<br><br>Verwenden Sie für eine isolierte Zustellbarkeit und Kontingent-Verwaltung separate, dedizierte Firebase-Projekte für jeden Braze-Workspace.
{% endalert %}

### 2. Schritt: Ihren Workspace hinzufügen {#step-2-add-your-workspace}

Sie können neue Workspaces erstellen oder zwischen bestehenden Workspaces wechseln, indem Sie das Workspace-Dropdown im globalen Header verwenden.

1. Wählen Sie das Workspace-Dropdown aus und klicken Sie dann auf <i class="fa-solid fa-square-plus" style="color: #0b8294;" aria-hidden="true"></i> **Workspace erstellen**.

![Das Workspace-Dropdown mit dem Button „Workspace erstellen“.]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. Geben Sie Ihrem Workspace einen Namen.

{% alert tip %}
Möglicherweise möchten Sie eine Namenskonvention einführen, damit andere in Ihrem Unternehmen Ihren Workspace leicht finden können. Zum Beispiel: „Upon Voyage US – Production“ und „Upon Voyage US – Staging“.
{% endalert %}

{:start="3"}
3. Wählen Sie **Create**. Es kann einige Sekunden dauern, bis Braze Ihren Workspace erstellt hat.

![Das Modal „Workspace erstellen“ mit dem Namen „Upon Voyage US - Staging“.]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Sie werden zur Seite **App Settings** weitergeleitet, um Ihre App-Instanzen hinzuzufügen. Sie können diese Seite jederzeit über **Settings** > **App Settings** aufrufen.

![Die Seite „App Settings“ für den Workspace „Upon Voyage US - Staging“ mit einem Button zum Hinzufügen einer App.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### 3. Schritt: Ihre App-Instanzen hinzufügen {#step-3-add-your-app-instances}

Die verschiedenen Websites und Apps, die in einem Workspace zusammengefasst werden, bezeichnen wir als „App-Instanzen“.

1. Wählen Sie auf der Seite **App Settings** die Option **+ Add app**.
2. Geben Sie Ihrer App-Instanz einen Namen und wählen Sie aus, auf welcher Plattform oder welchen Plattformen sich diese App-Instanz befindet. Wenn Sie mehrere Plattformen auswählen, erstellt Braze für jede Plattform eine eigene App-Instanz.

![Das Modal „Add New App to Upon Voyage US - Staging“ mit Optionen zur Auswahl von App-Details.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. Wählen Sie **Add app**, um zu bestätigen.

#### App-API-Schlüssel {#app-api-keys}

Nach dem Hinzufügen Ihrer App-Instanz haben Sie Zugriff auf deren API-Schlüssel. Der API-Schlüssel wird verwendet, wenn Anfragen zwischen Ihrer App-Instanz und der Braze-API gestellt werden. Der API-Schlüssel ist auch wichtig für die Integration des Braze SDK mit Ihrer App oder Website.

![Die Einstellungsseite für die App „Upon Voyage iOS“ mit Feldern für den API-Schlüssel und den SDK-Endpunkt.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Sie müssen für jede Version Ihrer App auf jeder Plattform separate App-Instanzen erstellen. Wenn Sie beispielsweise eine Free- und eine Pro-Version Ihrer App sowohl für iOS als auch für Android haben, erstellen Sie vier App-Instanzen in Ihrem Workspace (Free iOS-App, Free Android-App, Pro iOS-App und Pro Android-App). So erhalten Sie vier API-Schlüssel, einen für jede App-Instanz.
{% endalert %}

#### Live-SDK-Version {#live-sdk-version}

Die auf der Seite „App Settings“ für eine bestimmte App angezeigte Live-SDK-Version ist die höchste App-Version mit mindestens 5 % Ihrer gesamten täglichen Sitzungen und mindestens 500 Sitzungen am Vortag.

Dieses Feld erscheint, nachdem Sie das Braze SDK mit Ihrer App oder Website integriert haben. Wenn eine neuere Version des Braze SDK für Ihre Plattform verfügbar ist, wird dies hier mit dem Tag „Neuere Version verfügbar“ angezeigt.

![Der Abschnitt „Live-SDK-Version“ mit dem Feldwert „5.4.0“ und einem Symbol, das anzeigt, dass eine neue Version verfügbar ist.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### 4. Schritt: Bei Bedarf wiederholen {#step-4-repeat-as-needed}

Wiederholen Sie die Schritte 2 und 3, um so viele Workspaces einzurichten, wie Ihr Plan erfordert. Als Best Practice empfehlen wir, einen Test-Workspace für Integrations- und Campaign-Tests zu erstellen.

{% alert tip %}
**Einen Test-Workspace hinzufügen**<br>Sie können App-Tests durchführen, indem Sie bestimmte Nutzer:innen vollständig von Ihrer Produktionsinstanz isolieren. Erstellen Sie einen neuen Workspace, und wenn Sie Ihre Anwendung veröffentlichen, stellen Sie sicher, dass Sie den API-Schlüssel, den Braze verwendet, so ändern, dass er mit dem Ihres Produktions-Workspace übereinstimmt und nicht mit dem Ihres Test-Workspace.
{% endalert %}

## Workspaces verwalten {#managing-workspaces}

### Favoriten hinzufügen {#adding-favorites}

Sie können bevorzugte Workspaces hinzufügen, um noch schneller auf die Workspaces zuzugreifen, die Sie am häufigsten verwenden.

![Workspace-Dropdown mit dem Tab „Bevorzugte Workspaces“.]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

So fügen Sie bevorzugte Workspaces hinzu:

1. Wählen Sie Ihr Profil-Dropdown aus und klicken Sie dann auf **Konto verwalten**.
2. Suchen Sie im Abschnitt **Kontoprofil** das Feld **Bevorzugte Workspaces**.
3. Wählen Sie Ihre Workspaces aus der Liste aus.
4. Wählen Sie **Änderungen speichern**.

Es gibt keine Begrenzung für die Anzahl der Workspaces, die Sie als Favoriten markieren können, aber wir empfehlen, diese Liste der Übersichtlichkeit halber kurz zu halten.

### Workspaces umbenennen {#renaming-workspaces}

So benennen Sie Ihren Workspace um:

1. Gehen Sie zu **Settings** > **App Settings**.
2. Fahren Sie mit der Maus über den Namen Ihres Workspace und wählen Sie <i class="fa-solid fa-pencil" style="color: #0b8294;" aria-hidden="true"></i> **Bearbeiten**.
3. Geben Sie Ihrem Workspace einen neuen Namen und wählen Sie dann <i class="fa-solid fa-square-check" style="color: #0b8294;" aria-hidden="true"></i> **Speichern**.

![Das Stiftsymbol, das neben dem Workspace-Namen erscheint.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Workspaces und App-Instanzen löschen {#deleting-workspaces-and-app-instances}

So löschen Sie Ihren Workspace oder Ihre App-Instanz:

1. Gehen Sie zu **Settings** > **App Settings**.
2. Wählen Sie **Delete workspace**, um den jeweiligen Workspace zu löschen, oder wählen Sie das Papierkorbsymbol neben der jeweiligen App-Instanz.

Sie können keine App-Instanzen oder Workspaces löschen, die derzeit für das Targeting von Nutzer:innen verwendet werden oder die über 1.000 Nutzer:innen haben. Wenn Sie dies versuchen, erhalten Sie eine Fehlermeldung. Um fortzufahren und sie zu löschen, [erstellen Sie einen Support-Fall]({{site.baseurl}}/user_guide/administer/personal/braze_support), der einen Dashboard-Link und den Namen der zu löschenden App-Instanz oder des Workspace enthält.

{% alert warning %}
Seien Sie vorsichtig beim Löschen von Workspaces! Nachdem ein Workspace gelöscht wurde, kann er nicht wiederhergestellt werden.
{% endalert %}

![Die Seite „App Settings“ mit einem Button zum Löschen eines Workspace und einem Papierkorbsymbol zum Löschen einer App.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sollte ich einen neuen Workspace erstellen, wenn ich eine aktualisierte App veröffentliche? {#should-i-create-a-new-workspace-when-im-releasing-an-updated-app}

Das hängt davon ab, ob Sie Ihre App aktualisieren oder eine völlig neue App erstellen.

#### Ihre App aktualisieren {#updating-your-app}

Wenn Sie Ihre App aktualisieren, sollten Sie die alte und die neue Version trennen, indem Sie eine neue App-Instanz innerhalb desselben Workspace erstellen. Auf diese Weise können Sie Nutzer:innen der neuen Version effektiv ansprechen, wenn Sie diese App bei der Segmentierung auswählen. Wenn Sie Nutzer:innen der alten Version eine Nachricht senden möchten, können Sie Filter verwenden, um [die vorherige App-Version anzusprechen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

Wenn Sie einen neuen Workspace erstellen, existieren Ihre Nutzer:innen an zwei Stellen: im alten Workspace und im neuen Workspace. Sie könnten auch potenziell dasselbe Push-Token haben. Dies kann dazu führen, dass Nutzer:innen eine Marketing-Nachricht erhalten, die nur für Nutzer:innen des alten Workspace bestimmt war, selbst wenn sie bereits ein Upgrade durchgeführt haben.

#### Eine neue App veröffentlichen {#releasing-a-new-app}

Wenn Sie eine völlig neue App im App Store veröffentlichen, sollten Sie einen neuen Workspace erstellen. Durch das Erstellen eines neuen Workspace sind keine historischen Daten und Nutzerprofile aus der älteren App-Version in diesem neuen Workspace vorhanden. Wenn bestehende Nutzer:innen auf die neue App-Version upgraden, wird ein neues Profil ohne Verhaltensdaten aus der alten App erstellt.

### Ich habe mehrere App-Instanzen in einem Workspace – wie kann ich sicherstellen, dass meine Nachricht nur eine einzelne App anspricht? {#singular-app}

Um sicherzustellen, dass Ihre Nachricht nur eine bestimmte App anspricht, fügen Sie ein Segment hinzu, das nur Nutzer:innen Ihrer ausgewählten App-Instanzen enthält. Dies ist besonders wichtig, wenn Nutzer:innen möglicherweise zwei Push-Token für verschiedene App-Instanzen im selben Workspace haben. In diesem Szenario könnten Nutzer:innen eine Benachrichtigung für eine andere App erhalten als die, die sie gerade verwenden. Keine ideale Erfahrung!

Standardmäßig zielt ein Segment auf alle Apps und Websites im Workspace ab. So richten Sie ein Segment ein, das nur eine App oder Website anspricht:

1. Erstellen Sie ein Segment mit einem aussagekräftigen Namen. Bei Braze verwenden wir das Format „Alle Nutzer:innen ({Name} {Plattform})“. Zum Beispiel: „Alle Nutzer:innen (Upon Voyage iOS)“.
2. Wählen Sie unter **Apps and websites targeted** die Option **Users from specific apps**.
3. Wählen Sie im Dropdown **Specific apps** Ihre App oder Website aus.

![Segment, das Nutzer:innen aus bestimmten Apps anspricht.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Sie können dieses Segment dann zu Ihrer Nachricht hinzufügen und Ihre Zielgruppe bei Bedarf mit zusätzlichen Segmenten und Filtern weiter verfeinern.

#### Campaigns {#campaigns}

Fügen Sie bei Campaigns Ihr Segment im Schritt **Target Audiences** des Composers hinzu.

#### Canvas {#canvas}

Fügen Sie in Canvas Ihr Segment zu Ihren Nachrichtenschritten im Abschnitt **Delivery Validations** hinzu. Zustellungsvalidierungen überprüfen doppelt, ob Ihre Zielgruppe Ihre Zustellungskriterien zum Zeitpunkt des Nachrichtenversands erfüllt. Denken Sie daran, Zustellungsvalidierungen für jeden Nachrichtenschritt festzulegen, um sicherzustellen, dass die Nachricht an die richtige App zugestellt wird. Eine Segmentierung auf Eingangsebene ist nicht erforderlich.

{% details Erweitern für Schritte im ursprünglichen Canvas-Workflow %}

Im ursprünglichen Canvas-Workflow fügen Sie Ihr Segment auf der Canvas-Komponentenebene im Abschnitt **Audience** hinzu. Eine Segmentierung auf Eingangsebene ist nicht erforderlich.

{% enddetails %}

## Nächste Schritte {#next-steps}

Nachdem Sie Ihren Workspace erstellt haben, konfigurieren Sie ihn:

- [Workspace-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings), um API-Schlüssel, E-Mail-Präferenzen, Push-Einstellungen und mehr festzulegen.
- [Unternehmensnutzer:innen verwalten]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users), um Nutzer:innen hinzuzufügen und Berechtigungen für diesen Workspace zuzuweisen.