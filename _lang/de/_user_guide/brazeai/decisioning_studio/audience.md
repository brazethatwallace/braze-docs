---
nav_title: Zielgruppe definieren
article_title: Zielgruppe definieren
page_order: 3
page_type: reference
description: "Erfahren Sie, wie Sie die Zielgruppe für Ihren BrazeAI Decisioning Studio-Agenten definieren und konfigurieren – einschließlich Behandlungsgruppen und plattformspezifischer Einrichtungsschritte."
---

# Zielgruppe definieren {#define-your-audience}

> Zielgruppen für Anwendungsfälle werden in der Regel in einer Customer-Engagement-Plattform (wie Braze oder Salesforce Marketing Cloud) definiert und dann an den Decisioning Studio-Agenten gesendet. Der Agent teilt die Kund:innen anschließend in Behandlungsgruppen ein, um randomisierte kontrollierte Tests durchzuführen.

## Behandlungsgruppen {#treatment-groups}

| Gruppe | Beschreibung |
|--------|--------------|
| **Decisioning Studio** | Kund:innen, die KI-optimierte Empfehlungen erhalten |
| **Random Control** | Kund:innen, die zufällig ausgewählte Optionen erhalten (Baseline-Vergleich) |
| **Business-as-Usual (optional)** | Kund:innen, die die aktuelle Marketing-Journey erhalten (zum Vergleich mit der bestehenden Performance) |
| **Holdout (optional)** | Kund:innen, die keine Kommunikation erhalten (um die Gesamtwirkung der Campaign zu messen) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Behandlungsgruppen" }

## Zielgruppe konfigurieren {#configure-your-audience}

{% tabs %}
{% tab Braze %}

1. Erstellen Sie ein Segment für die Zielgruppe, die Sie ansprechen möchten.
2. Geben Sie die Segment-ID an Ihr AI Decisioning Services-Team weiter.

{% alert note %}
Für Braze können wir mehrere Segmente aufnehmen und kombinieren, um die Zielgruppe zu erstellen. Decisioning Studio kann ein Segment für eine Business-as-Usual-Vergleichs-Campaign aufnehmen. Alle diese Muster sind zulässig.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

1. Konfigurieren Sie eine SFMC Data Extension für Ihre Zielgruppe und geben Sie die Data-Extension-ID an.
2. Richten Sie ein SFMC Installed Package für die API-Integration mit den von Decisioning Studio benötigten Berechtigungen ein.
3. Stellen Sie sicher, dass diese Data Extension täglich aktualisiert wird, da Decisioning Studio die neuesten inkrementellen Daten abruft.

Geben Sie die Extension-ID und den API-Schlüssel an unser AI Decisioning Services-Team weiter, das Sie bei den nächsten Schritten zur Aufnahme von Kundendaten unterstützt.

{% endtab %}
{% tab Weitere Plattformen %}

### Google Cloud Storage

Wenn die Zielgruppe derzeit nicht in Braze oder Salesforce Marketing Cloud gespeichert ist, besteht der nächste Schritt darin, einen automatisierten Export direkt in einen von Braze verwalteten Google Cloud Storage-Bucket (GCS) zu konfigurieren.

Um festzustellen, ob dies möglich ist, lesen Sie die Dokumentation Ihrer Plattform. Beispielsweise bietet mParticle eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/) an. In diesem Fall können wir einen GCS-Bucket bereitstellen, in den Zielgruppendaten exportiert werden können.

### Zusätzliche Ressourcen {#additional-resources}

- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Nächste Schritte {#next-steps}

Nachdem Sie Ihre Zielgruppe definiert haben, fahren Sie mit der Einrichtung der Orchestrierung fort:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/orchestration_setup)