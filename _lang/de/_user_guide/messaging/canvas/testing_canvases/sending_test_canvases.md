---
nav_title: Test-Canvases senden
article_title: Test-Canvases senden
page_order: 1
description: "Dieser Referenzartikel behandelt, wie Sie ein Canvas vor dem Start testen und welche Best Practices es gibt."
page_type: reference
tool: Canvas
---

# Test-Canvases senden {#send-test-canvases}

> Nach dem [Erstellen Ihres Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) gibt es je nach Details wie Ihrer Zielgruppengröße oder der Anzahl der Segmentierungsfilter mehrere Prüfungen, die Sie vor dem Start durchführen sollten.

Wenn möglich, empfiehlt Braze, ein Canvas vor dem Start zu testen. Dieser Test findet in der Regel in Ihrer Braze-Umgebung statt. Das Testen Ihres Canvas kann beinhalten, es zu duplizieren, Testnutzer:innen durch die User-Journey zu führen und zu überprüfen, ob das Nutzerverhalten mit dem übereinstimmt, was Sie in Ihrem Canvas festgelegt haben.

## Schritt 1: Testplan erstellen {#step-1-create-your-test-plan}

Das Erstellen eines Testplans ist essenziell, bevor Sie mit dem Testen Ihres Canvas beginnen. Ein Testplan kann Ihnen helfen, bestimmte Bereiche Ihrer Canvas-Journey zu identifizieren und nachzuverfolgen.

Berücksichtigen Sie beim Erstellen Ihres Testplans die folgenden Fragen:
- Wurde mindestens ein:e Nutzer:in für jeden Canvas-Branch und -Pfad erstellt?
- Werden in Ihrem Canvas Segmente verwendet?
	- Falls Segmente verwendet werden, kann es Voraussetzungen geben, die ein:e Nutzer:in erfüllen muss, um in das Canvas zu gelangen, bevor er/sie für eine User-Journey berechtigt ist.
- Enthalten die Nachrichten im Test-Canvas Liquid in den Nachrichtentiteln, das die Nutzer-ID oder E-Mail-Adresse einbezieht, um sicherzustellen, dass sowohl die Nachricht als auch der/die Nutzer:in zu Testzwecken leicht identifiziert werden können?

## Schritt 2: Testnutzer:innen identifizieren {#step-2-identify-test-users}

Identifizieren Sie als Nächstes eine Gruppe von Testnutzer:innen, die die Canvas-Schritte durchlaufen, ohne tatsächlich Nachrichten an Ihre vorgesehenen Nutzer:innen zu senden. Testnutzer:innen können entweder bestehende E-Mail-Adressen sein, die nicht für tatsächliche Dienste in Ihrem Braze-Dashboard verwendet werden, oder neue E-Mail-Adressen, die ausschließlich zu Testzwecken genutzt werden.

## Schritt 3: Canvas einrichten {#step-3-set-up-your-canvas}

Als Nächstes ist es an der Zeit, Ihr Canvas zu testen! Um Ihr Original-Canvas und die Test-Canvas-Informationen übersichtlich zu halten, erstellen Sie ein Duplikat Ihres Canvas zu Testzwecken.

Es gibt zwei Möglichkeiten, Ihr Canvas zu testen.

- **Methode 1:** Bearbeiten Sie im duplizierten Canvas den Abschnitt **Entry-Zielgruppe** des Canvas-Builders, sodass nur Testnutzer:innen für das Canvas berechtigt sind. Sie können auch Ihre eigene E-Mail-Adresse als Testnutzer:in hinzufügen, indem Sie den Testfilter **E-Mail-Adresse** verwenden. Im folgenden Beispiel haben wir das Canvas auf zwei Testnutzer:innen beschränkt, die die App vor weniger als drei Tagen zum ersten Mal verwendet haben.

![Ein Canvas mit einer Entry-Zielgruppe „App zum ersten Mal vor weniger als 3 Tagen verwendet“ und den E-Mail-Adressen von zwei Testnutzer:innen.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Methode 2:** [Zeigen Sie eine Vorschau der Nutzerpfade an]({{site.baseurl}}/preview_user_paths), indem Sie den Button **Test Canvas** in der Fußzeile des Canvas-Builders auswählen.

## Schritt 4: Test starten {#step-4-launch-your-test}

Starten Sie Ihr Test-Canvas, damit Nutzer:innen beginnen können, es zu betreten. Führen Sie die Nutzeraktionen in Ihrer Anwendung aus, die Nutzer:innen durch die jeweilige Canvas-Journey senden würden.

Überprüfen Sie, ob Ihre Testnutzer:innen die vorgesehenen Nachrichten aus Ihren Canvas-Schritten erhalten. Beachten Sie, dass Ihre Testnutzer:innen unter anderem aus folgenden Gründen möglicherweise keine Nachricht erhalten:

- Nicht berechtigt für die globale Kontrollgruppe
- Frequency-Capping-Einschränkungen
- Nicht übereinstimmende Segment-Zugehörigkeit
- Abgebrochene Nachrichten
- Push-Token, die anderen Nutzer:innen zugeordnet sind

Fahren Sie mit dem iterativen Testen des Canvas fort, um sicherzustellen, dass Ihr Canvas wie vorgesehen funktioniert.

## Allgemeine Tipps {#general-tips}

### Canvas-Schritte identifizieren {#identify-your-canvas-steps}

In einigen Fällen kann ein:e Nutzer:in beim Durchlaufen eines Canvas potenziell mehrere Nachrichten erhalten. Wenn die Verzögerung zwischen den Schritten zu Testzwecken erheblich reduziert wurde, ist es möglicherweise nicht immer klar, welche Nachricht während des Tests getriggert wird. Wenn Sie sicherstellen, dass die Testnachrichten den Schrittnamen oder die Nutzer-ID (mithilfe von Liquid) enthalten, wird es einfacher, die korrekte Nachricht an die richtigen Nutzer:innen zu identifizieren und zu bestätigen.

### Interne Gruppe erstellen {#create-an-internal-group}

Anstatt einzelne Testnutzer:innen zu erstellen, können Sie eine [Content-Testgruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) erstellen, die eine interne Gruppe ist, deren Zweck es ist, den Inhalt Ihrer Nachricht zu überprüfen. Diese umfasst eine Gruppe von Nutzer:innen, die Testnachrichten von Campaigns und Canvases erhalten. Anschließend können Sie diese Testgruppe im Feld **Content-Testgruppen hinzufügen** unter **Testempfänger:innen** hinzufügen.

### Zeitverzögerungen reduzieren {#reduce-time-delays}

Um Tests effizienter durchzuführen, empfehlen wir, Zeitverzögerungen zu Testzwecken auf Minuten oder Sekunden zu reduzieren, damit Sie Nachrichten zeitnah einsehen können. Lassen Sie beispielsweise mindestens 2–3 Minuten zwischen den Tests, um bestimmte Aktionen bestimmten Canvas-Journeys zuordnen zu können.

### Content Blocks nutzen {#leverage-content-blocks}

Wenn Inhalte in Ihrem Test-Framework wiederholt werden (z. B. komplexes Liquid zum Filtern von Nutzer:innen in verschiedene Canvas-Schritte), versuchen Sie, diese wiederholten Inhalte als [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) zu speichern. So können Sie den Content-Block in den einzelnen Canvas-Schritten einbinden.

### Postman und den Track-User-Endpunkt verwenden {#use-postman-and-the-track-user-endpoint}

Sie können Tests mit Postman und der [Braze Postman Collection]({{site.baseurl}}/api/postman_collection) durchführen. Verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track), um angepasste Events und Käufe für Ihre verschiedenen Testnutzer:innen aufzuzeichnen und nachzuverfolgen.

Beachten Sie, dass das Senden von Daten an die User-Track-API nur mit einer externen ID möglich ist. Daher müssen Testnutzer:innen möglicherweise als Testnutzer:innen innerhalb einer internen Gruppe im Braze-Dashboard hinzugefügt werden, damit bestimmte Fehler weiter untersucht werden können.

#### Testen für mehrere Branches {#testing-for-multiple-branches}

Wenn Sie ein Canvas mit mehreren Branches testen, die Nutzer:innen basierend auf verschiedenen Attributen und Events ansprechen, folgen Sie diesem Testplan:

1. Identifizieren Sie für jeden Branch die Attribute und Events, die ein:e Nutzer:in haben muss, um in die Canvas-Journey aufgenommen zu werden.
2. Bauen Sie diese in ein JSON-Payload ein, das über den `/users/track`-Endpunkt gesendet wird.