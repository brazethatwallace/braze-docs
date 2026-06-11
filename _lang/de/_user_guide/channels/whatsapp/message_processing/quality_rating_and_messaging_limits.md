---
nav_title: Qualitätsbewertung und Messaging-Limits
article_title: Qualitätsbewertung und Messaging-Limits
description: "Dieser Referenzartikel beschreibt, wie Meta Ihre Qualitätsbewertung und Messaging-Limits für den WhatsApp-Kanal beeinflusst."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
---

# Qualitätsbewertung und Messaging-Limits {#quality-rating-and-messaging-limits}

> Meta beeinflusst Ihre Qualitätsbewertung und [Messaging-Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits) ab dem Moment, in dem Sie den WhatsApp-Kanal nutzen, und wird diese auch weiterhin in Abhängigkeit von Ihrer WhatsApp-Nutzung beeinflussen.

## Definitionen {#definitions}

| Begriff | Definition |
| --- | --- |
| Qualitätsbewertung | Eine Bewertung, die auf den Nachrichten basiert, die Ihre Kund:innen in den letzten sieben Tagen erhalten haben. Diese Bewertung wird durch das Feedback Ihrer Kund:innen bestimmt, z. B. durch den Grund für das Blockieren Ihrer Telefonnummer und andere gemeldete Probleme. Lesen Sie die Dokumentation von Meta, um mehr [über Ihre Qualitätsbewertung](https://www.facebook.com/business/help/896873687365001) zu erfahren. |
| Messaging-Limit | Die maximale Anzahl von geschäftlich initiierten Konversationen, die Sie mit jeder Ihrer Telefonnummern in einem rollierenden 24-Stunden-Zeitraum beginnen können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definitionen" }

## Onboarding {#onboarding}

Wenn ein neues WhatsApp Business-Konto erstellt wird, verwendet Meta verschiedene Faktoren, um das anfängliche Sendelimit zu bestimmen. Sie finden dieses Limit in Ihrem WhatsApp Business Manager sowie weitere Details auf Ihrer Seite „Phone Number Insights“.

Lesen Sie die Dokumentation von Meta, um mehr über das [Überprüfen Ihres Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) und die [Anforderungen an Telefonnummern](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) zu erfahren.

## Durchsatz {#throughput}

Meta startet jede registrierte geschäftliche Telefonnummer mit einem Durchsatz von 80 Messages pro Sekunde. Upgrades auf 1.000 Messages pro Sekunde können automatisch oder auf Anfrage erfolgen.

Lesen Sie die Dokumentation von Meta, um mehr über Ihren [Durchsatz](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput) zu erfahren.

## Template-Pacing {#template-pacing}

Kürzlich erstellte Marketing-Templates und pausierte Marketing-Templates, deren Pausierung aufgehoben wird, unterliegen möglicherweise dem Pacing. Die Pacing-Auswahlkriterien von Meta werden hauptsächlich durch Ihren Template-Qualitätsverlauf bestimmt. Wenn Sie ein kürzlich erstelltes Marketing-Template oder ein kürzlich wieder aktiviertes Marketing-Template verwenden, werden Nachrichten normal gesendet, bis ein nicht näher spezifizierter Schwellenwert erreicht wird. Nachdem dieser Schwellenwert erreicht wurde, werden nachfolgende Nachrichten mit diesem Template zurückgehalten, um genügend Zeit für Kund:innen-Feedback zu ermöglichen.

Lesen Sie die Dokumentation von Meta, um mehr über [Template-Pacing](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing) zu erfahren.