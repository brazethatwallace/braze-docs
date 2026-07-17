---
nav_title: Landing-Pages personalisieren
article_title: Landing-Pages personalisieren
description: "Dieser Artikel beschreibt, wie Sie Braze-Landing-Pages mit dem Drag-and-Drop-Editor personalisieren können."
page_order: 4
---

# Landing-Pages personalisieren {#personalize-landing-pages}

> Verwenden Sie Liquid-Personalisierung in Landing-Pages, um den Inhalt dynamisch mit Nutzerprofildaten anzupassen. So können Sie beispielsweise Überschriften basierend auf verschiedenen Nutzerattributen personalisieren, ohne mehrere statische Landing-Pages verwalten zu müssen.

{% alert important %}
Liquid-Personalisierung für Landing-Pages ist nur im Pro-Tier der Landing-Pages verfügbar. Derzeit werden [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [Mehrsprachigkeit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings) und [Aktionscodes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) nicht mit Liquid-Personalisierung in Landing-Pages unterstützt.
{% endalert %}

## Liquid einfügen {#inserting-liquid}

Im Drag-and-Drop-Editor können Sie Liquid-Personalisierung sowohl im Editor als auch in den Seiten- oder Block-Einstellungen im rechten Panel einfügen. Anleitungen zur Implementierung von Liquid finden Sie in unserer speziellen [Liquid-Dokumentation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).

![Landing-Page-Editor mit hinzugefügter Liquid-Personalisierung.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Vorschau und Testen {#previewing-and-testing}

Wenn Sie eine Landing-Page im Editor in der Vorschau anzeigen, können Sie die Seite als zufällige:r Nutzer:in, als bestehende:r Nutzer:in oder als benutzerdefinierte:r Nutzer:in betrachten.

Wenn Sie die Landing-Page jedoch über die Datentabelle oder die Seite **Landing-Page-Details** in der Vorschau anzeigen, können Sie sie nur als zufällige:r Nutzer:in betrachten.

## Hinweise zur Personalisierung {#personalization-considerations}

Um eine optimale Performance bei personalisierten Landing-Pages zu gewährleisten, beachten Sie die folgenden Größenbeschränkungen:

- **Speichern einer Landing-Page:** Wenn die Größe 500&nbsp;KB überschreitet, erhalten Sie möglicherweise eine Warnmeldung, die darauf hinweist, dass die Seite unsere Größenbeschränkungen überschritten hat, was die Veröffentlichung verhindern kann.
- **Rendering mit Liquid-Personalisierung:** Die Gesamtgröße darf 1&nbsp;MB nicht überschreiten. Andernfalls kann die Seite automatisch von Braze zurückgezogen werden.

### Zurückziehen von Landing-Pages vermeiden {#avoid-unpublishing-landing-pages}

Wenn Ihre Seite diese Größenbeschränkungen überschreitet, erhalten Sie eine E-Mail, dass sie möglicherweise zurückgezogen wird, wenn sie die Grenze weiterhin überschreitet. Wenn der Schwellenwert erreicht ist, wird die Seite automatisch zurückgezogen, und Sie erhalten eine Benachrichtigung.

Um zu verhindern, dass Ihre Seite die Größenbeschränkungen überschreitet oder langsame Ladezeiten auftreten, stellen Sie sicher, dass die Liquid-Personalisierung:

- Nicht kontinuierlich durch große Datensätze iteriert oder diese referenziert.
- Nicht auf umfangreiche mathematische oder bedingte Logik innerhalb des Liquid-Blocks angewiesen ist.

Vermeiden Sie außerdem das direkte Einbetten großer Skripte, Stylesheets und Base64-kodierter Assets in Ihren Landing-Page-Code. Diese Inline-Assets zählen zur Seitengrößenbeschränkung und können das Rendering verlangsamen. Laden Sie stattdessen Schriftarten, Bilder, Stylesheets und Skripte in die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) hoch. Assets, die über die Medienbibliothek bereitgestellt werden, werden auf dem CDN von Braze gehostet, sodass sie nicht für das Liquid-Rendering verarbeitet werden und nicht zur Seitengrößenbeschränkung zählen.

### Liquid für identifizierte und anonyme Nutzer:innen verwenden {#use-liquid-for-identified-and-anonymous-users}

Liquid kann das Landing-Page-Erlebnis sowohl für identifizierte als auch für anonyme Besucher:innen anpassen.

- **Identifizierte Nutzer:innen:** Verlinken Sie die Landing-Page aus einer Braze-Nachricht und fügen Sie den [Landing-Page-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users#using-landing-page-liquid-tags) hinzu. Dadurch wird die Person mit ihrem Braze-Profil verknüpft und das Seitenerlebnis personalisiert.
- **Anonyme Besucher:innen:** Verwenden Sie Liquid für kontextuelle, nicht profilbasierte Inhalte, wie z. B. eine Zufallszahl oder eine tageszeitabhängige Begrüßung.

### Formularfelder vorausfüllen {#pre-fill-form-fields}

Wenn ein Landing-Page-Formularfeld einem Nutzerprofilattribut zugeordnet ist, können Sie dieses Feld für wiederkehrende Nutzer:innen vorausfüllen. Dies reduziert die Hürden beim Ausfüllen von Formularen und verbessert die Abschlussraten für bekannte Besucher:innen.

So verwenden Sie vorausgefüllte Formularfelder:

1. Wählen Sie Ihr Formularfeld im Drag-and-Drop-Editor aus.
2. Ordnen Sie im rechten Einstellungs-Panel das Feld dem entsprechenden Profilattribut zu.
3. Wählen Sie **Pre-fill from user profile** aus.

![Einstellungen für Landing-Page-Formularfelder mit der Option zum Vorausfüllen aus Nutzerprofildaten.]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

Das Vorausfüllen funktioniert nur für [identifizierte Nutzer:innen](#use-liquid-for-identified-and-anonymous-users). Für anonyme Besucher:innen behalten Formularfelder ihren Standardzustand bei:

- **Eingabefelder:** Zeigen ihren Platzhaltertext an.
- **Kontrollkästchen, Optionsfelder und ähnliche Steuerelemente:** Bleiben nicht ausgewählt, bis Nutzer:innen mit ihnen interagieren.

{% alert warning %}
Wenn Nutzer:innen einen Landing-Page-Link (aus einer E-Mail, SMS oder einer anderen Nachricht) an eine andere Person weiterleiten, sieht die empfangende Person die vorausgefüllten Daten, die für die ursprünglichen Nutzer:innen bestimmt waren. Dies ist die gleiche Sicherheitsüberlegung, die auch für Abmeldelinks und Preference-Center-Links gilt. Berücksichtigen Sie die Sensibilität der vorausgefüllten Daten und das Weiterleitungsverhalten Ihrer Zielgruppe, wenn Sie dieses Feature verwenden.
{% endalert %}

## Externe Daten mit benutzerdefiniertem Code abrufen {#fetching-external-data-with-custom-code}

Sie können einen **Custom-Code**-Block verwenden, um Daten von externen Endpunkten abzurufen und auf Ihrer Landing-Page anzuzeigen. Dieser Ansatz führt die Anfrage clientseitig (im Browser der Nutzer:innen) aus, sodass die Seite schnell geladen wird, ohne serverseitige Rendering-Verzögerungen.

{% alert warning %}
Beim Abrufen externer Daten sind Sie für die Sicherheit Ihrer Implementierung verantwortlich. Externe Bezeichner, die in API-Aufrufen verwendet werden, sollten UUIDs sein oder ein gleichwertig sicheres Benennungsschema verwenden – siehe [Best Practices für die Benennung von Nutzer-IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).
{% endalert %}

### Anwendungsfall {#use-case}

Dieses Muster ist nützlich, wenn Sie nutzerspezifische Daten anzeigen müssen, die nicht in Braze gespeichert sind. Beispiele hierfür sind Realtime-Bestandsdaten, personalisierte Empfehlungen oder andere Daten, die Ihre Organisation in separaten Systemen verwaltet.

### Beispielimplementierung {#example-implementation}

Dieses Beispiel zeigt, wie Sie Nutzerdaten von einer externen API abrufen. Ersetzen Sie den API-Endpunkt durch Ihren eigenen sicheren Endpunkt und verwenden Sie einen sicheren Bezeichner.

{% raw %}
```html
<script>
window.onload = () => {
  // Use Liquid to template the user's external ID
  const userId = "{{${user_id}}}";

  const loadUserData = async () => {
    try {
      // Replace with your own secure API endpoint
      const response = await fetch(`https://your-api.example.com/user/${userId}`);

      if (!response.ok) {
        throw new Error('Failed to load data');
      }

      const data = await response.json();

      // Update the page with the fetched data
      document.querySelector("#user-data").textContent = JSON.stringify(data, null, 2);
      document.querySelector("#user-name").textContent = data.name || "User";
    } catch (error) {
      // Handle errors gracefully
      document.querySelector("#user-data").textContent = "Unable to load data at this time.";
    }
  };

  loadUserData();
};
</script>

<!-- Display area for fetched data -->
<p>Welcome, <span id="user-name">Loading...</span></p>
<pre id="user-data">Loading your information...</pre>
```
{% endraw %}

### Hinweise {#considerations}

Beim Abrufen externer Daten in Landing-Pages:

- **Ladezustände:** Nutzer:innen sehen Platzhaltertext, bis der Endpunkt antwortet. Erwägen Sie, einen Ladeindikator oder ein Skeleton-Screen hinzuzufügen.
- **Fehlerbehandlung:** Wenn der Endpunkt fehlschlägt oder langsam antwortet, kann die Seite fehlerhaft erscheinen. Implementieren Sie geeignete Fehlermeldungen und Fallbacks.
- **Performance:** Die Seite wird sofort geladen, aber die Daten erscheinen erst, nachdem die externe Anfrage abgeschlossen ist. Halten Sie Ihre API-Antworten schnell für das beste Nutzererlebnis.
- **Sicherheit:** Stellen Sie sicher, dass Ihr API-Endpunkt den Bezeichner validiert und nur Daten zurückgibt, die die Person sehen darf. Implementieren Sie Rate-Limiting, um Missbrauch zu verhindern. Hinweise zur Wahl sicherer Bezeichner finden Sie unter [Best Practices für die Benennung von Nutzer-IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices).

## Fallback-Seiten {#fallback-pages}

Wenn Ihre Nutzer:innen versuchen, auf eine Seite zuzugreifen, die zurückgezogen wurde, sehen sie eine Meldung, dass die Seite derzeit nicht geladen werden kann. Gründe für das Zurückziehen einer Seite sind unter anderem:

- Komplexes oder fehlerhaftes Liquid, das zu langen Renderzeiten führen kann
- Netzwerkprobleme der Nutzer:innen
- Überschreitung der maximalen Landing-Page-Größenbeschränkungen