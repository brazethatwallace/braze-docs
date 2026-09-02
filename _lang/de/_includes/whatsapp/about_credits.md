Ab dem 1. Juli 2025 rechnet WhatsApp pro Nachricht ab. Die Nachrichtenpreise basieren sowohl auf der Landesvorwahl der Telefonnummer der Empfänger:innen als auch auf dem Typ der Nachricht, die Sie senden. Der Nachrichtentyp wird anhand des [Nachrichten-Templates](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) bestimmt, das Sie im WhatsApp Manager:in zur Genehmigung einreichen.

{% alert note %}
Alle vom Unternehmen initiierten Konversationen auf der Plattform müssen mit einer genehmigten Template-Nachricht beginnen.
{% endalert %}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Definitionen der Nachrichten-Templates

Dies sind die Nachrichten-Templates, die Sie im WhatsApp Manager:in zur Genehmigung einreichen können:

| Template | Definition |
|----------|------------|
| **Marketing-Template** | Mit diesem Template können Sie eine Vielzahl von Zielen erreichen – von der Steigerung der Bekanntheit über die Umsatzförderung bis hin zum Retargeting von Kund:innen. Beispiele sind Ankündigungen neuer Produkte, Dienste oder Features, gezielte Aktionen oder Angebote sowie Erinnerungen bei abgebrochenem Einkauf. |
| **Utility-Template** | Mit diesem Template können Sie auf Nutzer:innen-Aktionen oder -Anfragen reagieren, da diese Nachrichten in der Regel durch Nutzer:innen-Aktionen getriggert werden. Beispiele sind Opt-in-Bestätigungen, Bestell- oder Zustellungsverwaltung (z. B. Zustellungs-Updates), Konto-Updates oder -Benachrichtigungen (z. B. Zahlungserinnerungen) oder Feedback-Umfragen.<br><br>Ab dem 1. Juli 2025:<br>• Utility-Templates dürfen nicht werblich sein und keine überzeugende Absicht verfolgen.<br>• Utility-Templates müssen entweder (1) spezifisch für die Nutzer:innen sein oder von ihnen angefordert worden sein oder (2) für die Nutzer:innen wesentlich oder kritisch sein. |
| **Authentifizierungs-Template** | Mit diesem Template können Sie die Identität von Nutzer:innen überprüfen, potenziell in verschiedenen Schritten der Customer Journey (z. B. Kontoverifizierung, Kontowiederherstellung und Integritätsprüfungen).<br><br>Authentifizierungs-Konversationen werden nur im Einzelfall unterstützt, und Braze kann keine spezifischen SLAs garantieren. Darüber hinaus unterstützt Braze keine PIN-Generierung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Arten kostenloser Nachrichten

Hier sind einige Szenarien, in denen Ihre WhatsApp-Nachricht kostenlos ist:

| Nachricht | Details |
|-----------|---------|
| Alle Service-Konversationen | _Ab dem 1. November 2024_<br><br>Wenn Nutzer:innen Ihre Marke kontaktieren (und damit das 24-Stunden-Kundenservice-Fenster starten), werden nicht-templatebasierte Antwortnachrichten nicht berechnet. Hinweis: Wenn Ihre Marke den Nutzer:innen jedoch mit einem Template antwortet, werden Ihnen weiterhin Kosten basierend auf dem Template-Typ berechnet. |
| Utility-Templates, die innerhalb eines 24-Stunden-Kundenservice-Fensters gesendet werden | _Ab dem 1. Juli 2025_<br><br>Ein 24-Stunden-Kundenservice-Fenster wird erstellt, wenn Endnutzer:innen Ihre Marke kontaktieren. Wenn Ihre Marke mit einem Utility-Template antwortet, ist dies kostenlos. Utility-Templates, die außerhalb eines 24-Stunden-Kundenservice-Fensters gesendet werden (z. B. Utility-Templates, die Ihre Marke proaktiv für Kontoerinnerungen und Auftragsstatus-Updates sendet), werden weiterhin berechnet. |
| Kostenlose Einstiegspunkt-Konversationen | Eine kostenlose Einstiegspunkt-Konversation wird eröffnet, wenn 1) Nutzer:innen Ihre Marke über eine Klick, der-to-WhatsApp-Anzeige oder einen Facebook-Seiten-Call-to-Action-Button kontaktieren und 2) Ihre Marke innerhalb von 24 Stunden antwortet. Die kostenlose Einstiegspunkt-Konversation wird eröffnet, sobald Ihre Marke antwortet, und dauert 72 Stunden. Innerhalb des 72-Stunden-Fensters kann Ihre Marke Nachrichten-Templates kostenlos an Nutzer:innen senden. Ihre Marke kann jedoch nur nicht-templatebasierte Nachrichten senden, wenn ein offenes 24-Stunden-Kundenservice-Fenster besteht. |
| Antwortnachrichten | Antwortnachrichten ermöglichen es Ihrer Marke, nicht-templatebasierte Nachrichten als Antwort auf Nutzer:innen-Nachrichten zu senden. Antwortnachrichten können gesendet werden, wenn ein offenes 24-Stunden-Kundenservice-Fenster besteht, z. B. wenn Nutzer:innen Ihre Marke auf WhatsApp kontaktieren.<br><br>Beachten Sie, dass die Template-Nachricht, die die Konversation startet, weiterhin berechnet wird, nachfolgende Antwortnachrichten jedoch kostenlos sind. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}