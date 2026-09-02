---
nav_title: Oktober
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Oktober 2018."
---
# Oktober 2018 {#october-2018}

{% comment %}
  Fügen Sie diese zu einem späteren Zeitpunkt hinzu...
  Intelligente Auswahl Kontrollgruppe umschalten
  Das Feld Intelligente Auswahl verfügt jetzt über ein Kontrollkästchen, mit dem Sie [die Verwendung einer Kontrollgruppe ein- oder ausschalten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing#including-a-control-group) können. Wenn diese Funktion aktiviert ist, beträgt die Kontrollgruppe 20% der Zielgruppe und ändert sich, wenn das Feature Intelligente Auswahl die Zielgruppengrößen pro Variante optimiert.
  Assistent für Canvas-Eingangseinstellungen (Beta)
  Das Canvas UI wird vereinfacht, um verpasste Aufgaben und daraus resultierende Fehler zu vermeiden. Die Canvas-Konfigurationen werden jetzt in einem Assistenten angezeigt, der dem Design des Assistenten für Kampagnen ähnelt. Dies spiegelt sich derzeit noch nicht in unserer Dokumentation wider, da es schrittweise eingeführt wird. Lesen Sie bald mehr darüber!
  Abo-Gruppe API (ausgeblendet)
  Braze hat einen neuen GET-Aufruf zur Verfügung gestellt, der es Ihnen ermöglicht, eine Anfrage auf der Grundlage einer externen ID oder E-Mail zu stellen. Sie erhalten dann alle Abo-Gruppen, die mit diesem Nutzer:innen verbunden sind.
{% endcomment %}

## Exakte Zielgruppenstatistiken für Campaigns berechnen {#calculate-exact-audience-stats-for-campaigns}

Sie können jetzt zu **Campaign Analytics** navigieren und die exakten Statistiken für Ihre Zielgruppe berechnen. Klicken Sie in der Fußzeile des Abschnitts **Target Audiences** auf **Calculate Exact Stats**, und die exakten Zielgruppenstatistiken werden angezeigt. Sie müssen die Campaign speichern, bevor Sie die Berechnung durchführen (Campaign-Entwürfe werden als Entwürfe gespeichert).

## Einstellung der Windows 8-Unterstützung {#windows-8-deprecation}

Braze unterstützt Windows 8 seit dem 10. Oktober 2018 nicht mehr.

## Partnerschafts-Hub {#partnerships-hub}

Sie finden jetzt eine Liste Ihrer Integrationen auf der Braze-Plattform unter **Integrationen** sowie Integrationsschlüssel und Anleitungen.

## Berechnungen der E-Mail-Analytics {#email-analytics-calculations}

Braze berechnet jetzt alle E-Mail-Analytics anhand der Eventdaten unseres E-Mail-Versandpartners (E-Mail-Anbieter), um die Genauigkeit unserer E-Mail-Analytics erheblich zu verbessern. Diese Lösung nutzt Postgres, eine Open-Source-Datenbanklösung, um die Datenintegrität sicherzustellen.

{% alert important %}
Eindeutige Öffnungen und eindeutige Klicks sind derzeit noch von den aggregierten Daten unserer E-Mail-Versandpartner abhängig. Es wird derzeit daran gearbeitet, diese Eindeutigkeitsstatistiken mithilfe derselben Infrastruktur zu berechnen, die in diesem Release eingeführt wurde.
{% endalert %}

## Steuerelemente des Editor-Panels {#composer-panel-controls}

Die Steuerelemente des Nachrichten-Editors wurden aktualisiert und enthalten jetzt Beschriftungen neben den Symbolen, um die Benutzerfreundlichkeit und Navigation zu verbessern.

## Azure für Currents {#azure-for-currents}

Braze-Kund:innen, die Currents nutzen, können jetzt [Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) als potenzielle Integration sehen.

## Erweiterungen der Eingabefelder {#input-field-expansions}

Sie können jetzt die Eingabefelder für E-Mail-Betreffzeilen und Push-Titel erweitern.