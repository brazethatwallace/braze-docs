---
nav_title: Sendefehler
article_title: WhatsApp-Sendefehler untersuchen
page_order: 22
page_type: reference
description: "Verwenden Sie Campaign-Analytics, das Nachrichtenaktivitätsprotokoll und Currents, um WhatsApp-Sendefehler und häufige Meta-Fehlercodes zu untersuchen."
tool:
  - Reports
channel:
  - WhatsApp
---

# WhatsApp-Sendefehler untersuchen {#investigate-whatsapp-send-failures}

> Verwenden Sie diese Seite, wenn WhatsApp-Zustellungen oder Lesebestätigungen niedriger als erwartet ausfallen oder wenn die **Failures** in den Campaign-Analytics erhöht erscheinen.

## Untersuchungsablauf {#investigation-workflow}

Arbeiten Sie die folgenden Schritte der Reihe nach durch.

1. **Fehler in den Campaign- oder Canvas-Analytics bestätigen.** Öffnen Sie den Nachrichtenschritt und überprüfen Sie die Anzahl der **Failures** sowie die Fehlerrate. Wenn die Fehleranzahl im Vergleich zu Sends oder Zustellungen erhöht erscheint, fahren Sie mit dem nächsten Schritt fort.
2. **Fehlercode im Nachrichtenaktivitätsprotokoll finden.** Öffnen Sie das [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) für denselben Send, filtern Sie nach fehlgeschlagenen Nachrichten und notieren Sie den Anbieter-Fehlercode (zum Beispiel `131049` für nutzerbezogene Marketing-Limits). Verwenden Sie [Häufige Fehlercodes](#common-failure-codes), um den Code zu interpretieren und die nächsten Schritte festzulegen.
3. **Fehler mit Currents für Analysen oder Retargeting exportieren.** Nachdem Sie den Fehlercode kennen, exportieren Sie WhatsApp-Sendefehler-Events über Currents. Nutzen Sie diese Daten, um Fehlertrends in Ihrem Data Warehouse zu analysieren oder um Segmente zu erstellen und Nutzer:innen über einen anderen Kanal erneut anzusprechen.

## Häufige Fehlercodes {#common-failure-codes}

| Fehlercode | Typische Ursache | Nächster Schritt |
|---|---|---|
| `131049` | Meta-Frequenzlimit für nutzerbezogenes Marketing oder US-Marketing-Pause | Siehe [Meta-Ressourcen]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources) und [Nutzer:innen über andere Braze-Kanäle erneut ansprechen]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels) |
| `130472` | Meta-Marketing-Experiment-Holdout | Siehe [Meta-Ressourcen – FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq) |
| `131026` | Verschiedene Gründe für Nichtzustellung (Meta gibt keine Details bekannt) | Vermeiden Sie sofortige Wiederholungsversuche; lesen Sie die [Meta Cloud API-Fehlerbehebung](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Häufige WhatsApp-Fehlercodes" }