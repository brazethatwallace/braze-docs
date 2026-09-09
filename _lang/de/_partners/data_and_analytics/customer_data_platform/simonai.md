---
nav_title: Simon KI
article_title: Simon KI
description: "Nutzen Sie die Integration von Braze und Simon KI, um anspruchsvolle Zielgruppen zu erstellen und in Echtzeit und ohne Code zur Orchestrierung mit Braze zu synchronisieren."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon KI

> Die [Simon KI][1] Agentic Marketing Platform hilft Marketing-Teams, echte 1:1-Personalisierung zu erreichen. Sie kombiniert eine modulare Customer Data Platform (CDP) mit KI-Agenten, die direkt in der Snowflake KI Data Cloud arbeiten und als Daten- und Ausführungsteam für Marketer fungieren.

Nutzen Sie die Integration von Braze und Simon KI, um fortschrittliche Zielgruppen zu erstellen und für Realtime-Orchestrierung ohne Code mit Braze zu synchronisieren. Mit dieser Integration können Sie die Identitätsauflösung, die Vereinheitlichung von Kundendaten und die KI-gestützte Segmentierung von Simon KI nutzen, um personalisiertere und wirkungsvollere Braze-Campaigns nachgelagert zu unterstützen.

## Voraussetzungen {#prerequisites}

Um loszulegen, müssen Sie Ihr Braze-Konto in Ihrem Simon KI-Konto authentifizieren.

| Anforderung | Beschreibung |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon KI | Sie benötigen ein bestehendes Simon KI-Konto, um die Braze-Integration innerhalb von Simon KI nutzen zu können. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `users.track`, `campaigns.trigger.schedule.create` und `campaigns.trigger.send`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Dashboard-URL | [Ihre REST-Endpunkt-URL][3]. Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

- Einen Braze-Canvas oder eine E-Mail triggern
- Segment-Eigenschaften übergeben und pflegen
- Traits und Kontakteigenschaften synchronisieren

{% alert note %}
Bei der Nutzung der Simon- und Braze-Integration sendet Simon bei jeder Synchronisierung nur Deltas an Braze, um Kosten für irrelevante Daten zu vermeiden. Weitere Informationen finden Sie unter [Traits und Kontakteigenschaften synchronisieren](#sync-traits-and-contact-properties).
{% endalert %}

## Integration

### Ihr Braze-Konto in Simon KI authentifizieren {#authenticate-your-braze-account-in-simon-ai}

Um die Braze-Integration zu nutzen, authentifizieren Sie zunächst Ihr Braze-Konto in Simon:

1. Klicken Sie in der linken Navigation auf **Integrations** und scrollen Sie zu Braze.
2. Geben Sie Ihren Braze-[REST-API-Schlüssel][2] und Ihre [Dashboard-URL][3] ein.
3. Klicken Sie auf **Save Changes**.

Bei einer erfolgreichen Verbindung wird **Connected** im Fenster angezeigt.

![Integrationsbildschirm in Simon KI][8]{: style="max-width:70%"}

### Braze-Aktionen zu Flows oder Journeys in Simon KI hinzufügen {#add-braze-actions-to-flows-or-journeys-in-simon-ai}

Nachdem Sie Ihr Braze-Konto in Simon KI authentifiziert haben, können Sie Braze-Aktionen zu [Flows][4] und [Journeys][5] hinzufügen.

Drei Aktionen stehen zur Verfügung:

- **Simon-Segment-Attribut synchronisieren**: Synchronisieren Sie Ihre Segment-Details mit einem neuen oder bestehenden angepassten Attribut in Braze.
- **Einen Braze-Canvas triggern**: Triggern Sie einen Braze-Canvas, der Ihre Simon-Segment-Daten nutzt.
- **Eine Braze-Campaign senden**: Starten Sie eine vollständige Braze-Campaign aus Simon heraus.

![Dropdown mit einer Liste der verfügbaren Braze-Aktionen in Simon KI.][9]{: style="max-width:60%"}

Einige Aktionen sind nur für bestimmte Flow-Typen oder ausschließlich für Journeys verfügbar. Mehr erfahren Sie unter [docs.simondata.com][6].

### Traits und Kontakteigenschaften synchronisieren {#sync-traits-and-contact-properties}

Um den Datenverbrauch zu minimieren, können Sie bestimmte Traits auswählen, die standardmäßig synchronisiert werden, anstatt jedes Feld für alle Kund:innen in einem Segment zu aktualisieren.

{% alert note %}
Um mit der Trait-Synchronisierung zu beginnen, senden Sie eine Anfrage im [Simon Support Center](https://docs.simondata.com/docs/support-center). Ihr Account Manager:in wird Ihnen mitteilen, wann Sie mit den folgenden Schritten fortfahren können.
{% endalert %}

Nachdem Contact Traits von Ihrem Account Manager:in aktiviert wurde:

1. Erweitern Sie in Simon **Admin Center** in der linken Navigation und wählen Sie **Sync Contact Traits** aus.
2. Wählen Sie **Braze**. Kontakteigenschaften werden hier angezeigt, nach Dataset verschachtelt.
3. Wählen Sie alle Felder aus, die bei der Nutzung der Simon- und Braze-Integration synchronisiert werden sollen:
   1. **Number of traits** gibt an, wie viele Traits in diesem Dataset zur Auswahl stehen. Sie können alle auswählen oder die Zeile erweitern, um einzelne Felder auszuwählen.
   2. Bearbeiten Sie den **Downstream name**, wenn die Feldnamen bei der Ankunft in Braze anders erscheinen sollen.
   3. Wenn Sie die Integration mit Braze aus Simon heraus zum ersten Mal einrichten, klicken Sie auf **Backfill all contacts**. Das Backfilling sendet alle Datenpunkte an Braze, wenn Sie zum ersten Mal eine Aktion in einem Flow oder einer Journey verwenden, um sicherzustellen, dass alle Ihre Daten vollständig synchron sind. Bei nachfolgenden Synchronisierungen werden dann nur die Traits, die Sie in diesem Bildschirm auswählen, an Braze gesendet. So wird sichergestellt, dass Ihnen nur die Daten berechnet werden, die Sie benötigen.

![Auswahl der Sync-Traits in Simon KI.][10]

[1]: https://www.simon.ai/
[2]: {{site.baseurl}}/api/basics#creating-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administer/personal/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}