## Präferenzcenter testen {#testing-preference-centers}

Links zum Präferenzcenter werden für jede Nutzer:in zum Sendezeitpunkt generiert und sind an einen Live-Versand einer Campaign oder eines Canvas gebunden. Testversand und Editor-Vorschauen unterstützen das Speichern von Abo-Änderungen nicht. Dies ist das erwartete Verhalten.

### Was Sie sehen werden {#what-youll-see}

- **Testversand:** Liquid-Tags des Präferenzcenters werden möglicherweise nicht zu einem gültigen Link aufgelöst. Wenn die Seite geladen wird, ist der Button **Einstellungen speichern** deaktiviert, und Abo-Änderungen werden nicht gespeichert.
- **Tab „Vorschau“ im Drag-and-Drop-Editor:** Sie können Layout und Styling in der Vorschau anzeigen, aber Sie können das Speichern von Präferenzen nicht aus dem Editor heraus testen.

### End-to-End testen {#how-to-test-end-to-end}

Um zu überprüfen, ob Links und Buttons des Präferenzcenters vor einem vollständigen Launch funktionieren:

1. Erstellen Sie eine Campaign oder einen Canvas-E-Mail-Schritt, der Ihren Liquid-Tag für das Präferenzcenter enthält.
2. Richten Sie die Nachricht nur an Ihre Testnutzer:innen oder ein kleines internes Segment.
3. Starten Sie die Nachricht und öffnen Sie die E-Mail aus einem echten Posteingang (nicht über **Test senden**).
4. Wählen Sie den Link zum Präferenzcenter aus, aktualisieren Sie die Abo-Gruppen und wählen Sie **Einstellungen speichern**.
5. Bestätigen Sie die Änderungen im Profil der Nutzer:in im Braze-Dashboard.

{% if include.section == "api" %}
Als Alternative für API-basierte Präferenzcenter können Sie den [Endpunkt „Präferenzcenter-URL generieren“]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) verwenden, um eine funktionierende URL für eine bestimmte Nutzer:in außerhalb eines Testversands abzurufen.
{% endif %}

Weitere Einschränkungen beim Testversand finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages#limitations).

### Vorschau, Testversand und Live-Versand {#preview-test-send-and-live-send}

| Methode | Layout-Vorschau | Abo-Änderungen speichern |
| --- | --- | --- |
| Tab **Vorschau** im Drag-and-Drop-Editor | Ja | Nein |
| **Test senden** in Campaign oder Canvas | Teilweise (E-Mail wird zugestellt) | Nein |
| Live-Versand an Testnutzer:innen oder ein Segment | Ja | Ja |
| API [Präferenzcenter-URL generieren]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Ja | Ja |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vorschau, Testversand und Live-Versand" }