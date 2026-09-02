---
nav_title: Datenschutz und Sicherheit
article_title: Datenschutz und Sicherheit für BrazeAI Operator
page_order: 5
page_type: reference
description: "Dieser Referenzartikel behandelt den Umgang von BrazeAI Operator mit Daten, einschließlich HIPAA-Konformität, Datenaufbewahrung, PII-Minimierung und Governance."
---

# Datenschutz und Sicherheit für BrazeAI Operator {#data-privacy-and-security-for-brazeai-operator}

> BrazeAI Operator<sup>TM</sup> ist mit OpenAI integriert, um KI or künstliche Intelligenz-gestützte Unterstützung bereitzustellen. Dieser Artikel behandelt den Umgang von Operator mit Daten, welche Informationen mit OpenAI geteilt werden und wie Sie die PII-Exposition minimieren und den Zugriff kontrollieren können.

## Wie Operator auf Daten zugreift {#how-operator-accesses-data}

Der Zugriff von Operator auf Kundendaten ist strikt ereignisgesteuert und auf den jeweiligen Aufruf beschränkt, nicht persistent. Jede Nutzernachricht oder jedes Navigationsereignis bei geöffnetem Operator löst eine einzelne HTTP-Anfrage an OpenAI aus. Es gibt keine dauerhafte Verbindung oder einen persistenten Datenfeed.

OpenAI hat keinen direkten Zugriff auf Braze-Datenspeicher oder die vollständige Nutzertabelle. Das LLM erhält nur die spezifische Nutzlast, die mit der aktiven Anfrage verknüpft ist.

### Welche Daten in jeder Anfrage enthalten sind {#what-data-is-included-in-each-request}

Jede an OpenAI gesendete Anfragenutzlast kann Folgendes enthalten:

- **Systemmetadaten:** Von Braze erstellte Systemprompts und Tool-Schemata (Definitionen der Tools, die das LLM aufrufen kann).
- **Dashboard-Nutzernachricht:** Die getippte Eingabe der Dashboard-Nutzer:in.
- **Tool-Ausgaben:** Suchergebnisse mit Namen, IDs und zugehörigen Daten.
- **Gescrapte Seiteninhalte:** Inhalte der aktiven Dashboard-Seite, auf etwa 4.000 Zeichen gekürzt.
- **Seitenkontext-Strings:** Kontextuelle Strings der aktiven Dashboard-Seite.

## Daten-Unterauftragsverarbeiter {#data-sub-processors}

### Modellanbieter als Unterauftragsverarbeiter oder Drittanbieter {#model-providers-as-sub-processors-or-third-party-providers}

Wenn Sie eine Integration mit einem LLM-Anbieter nutzen, der von Braze über die Braze-Dienste bereitgestellt wird („von Braze bereitgestelltes LLM“), agieren die Anbieter eines solchen von Braze bereitgestellten LLM als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (Datenschutzbeauftragte:r) zwischen Ihnen und Braze. BrazeAI Operator<sup>TM</sup> ist mit OpenAI integriert.

### Wie Daten mit OpenAI verwendet werden {#how-data-is-used-with-openai}

Um KI or künstliche Intelligenz-Ausgaben über BrazeAI-Features zu generieren, die OpenAI nutzen („Ausgabe“), sendet Braze bestimmte Informationen („Eingabe“) an OpenAI. Die Eingabe besteht aus Ihren Prompts, den im Dashboard angezeigten Inhalten und Workspace-Daten, die für Ihre Abfragen relevant sind. Gemäß den [API-Plattform-Verpflichtungen von OpenAI](https://openai.com/enterprise-privacy/) werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Zwischen Ihnen und Braze ist die Ausgabe Ihr geistiges Eigentum. Braze wird keine Urheberrechtsansprüche auf solche Ausgaben geltend machen. Braze gibt keinerlei Garantie in Bezug auf KI or künstliche Intelligenz-generierte Inhalte, einschließlich der Ausgabe.

## HIPAA-Konformität und Datenaufbewahrung {#hipaa-compliance-and-data-retention}

### HIPAA-Konformität {#hipaa-compliance}

Wenn Sie den US-02-Cluster von Braze verwenden, ist Operator durch die Business Associate Agreement (BAA) von Braze abgedeckt, und persönliche Gesundheitsinformationen (PHI) können gemäß den HIPAA-Anforderungen an das Feature übermittelt werden. Übermitteln Sie keine PHI, die dem HIPAA unterliegen, wenn Sie Operator in anderen Braze-Clustern verwenden.

### PII-Schwärzung {#pii-redaction}

Es gibt keine automatisierte PII-Schwärzungsschicht in der Operator-Anfragepipeline. Daten werden vollständig unverarbeitet gesendet und vor der Übertragung an OpenAI nicht anonymisiert. Der Zugriff ist auf die aktive Dashboard-Seite oder die Eingabe der Dashboard-Nutzer:in beschränkt, aber es wird keine Inhaltsfilterung vor der Übertragung angewendet.

### Datenaufbewahrung bei OpenAI {#openai-data-retention}

Wie lange OpenAI die über Operator gesendeten Daten aufbewahrt, hängt von Ihrem Cluster ab:

| Cluster | Aufbewahrung |
| --- | --- |
| US-02 (HIPAA-Kund:innen) | Zero Data Retention (ZDR). Daten werden nach der Verarbeitung nicht von OpenAI gespeichert. |
| Alle anderen Cluster | 30 Tage zur Missbrauchsüberwachung. Dies ist eine branchenübliche Aufbewahrungsfrist, die von OpenAI vorgegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="OpenAI-Datenaufbewahrung nach Cluster" }

### Modelltraining {#model-training}

Daten, die über Braze an die API von OpenAI gesendet werden, werden nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Dies wird durch vertragliche Vereinbarungen zwischen Braze und OpenAI sowie die API-Plattform-Verpflichtungen von OpenAI geregelt. OpenAI agiert als Braze-Unterauftragsverarbeiter, und alle personenbezogenen Daten unterliegen dem Datenschutzbeauftragte:r zwischen Braze und seinen Kund:innen.

### EU-Datenrouting {#eu-data-routing}

EU-Datenrouting ist derzeit für Operator nicht implementiert, und es gibt aktuell keine Pläne, dies umzusetzen.

## PII-Exposition minimieren {#minimize-pii-exposure}

Es gibt mehrere Schritte, die Sie unternehmen können, um die PII-Exposition bei der Nutzung von Operator zu begrenzen:

- **Deaktivieren Sie die Einstellung „PII anzeigen“** für alle Nutzer:innen, die Operator verwenden. Wenn Nutzer:innen PII nicht einsehen können, kann Operator ebenfalls nicht darauf zugreifen.
- **Öffnen Sie Operator nicht auf einer Nutzerprofilseite.** Seiteninhalte werden gescrapt und in jede an OpenAI gesendete Anfrage einbezogen.
- **Verwenden Sie beim Testen ein angepasstes Kundenprofil or Nutzerprofil**, anstatt ein bestehendes auszuwählen. Dies ist das Standardverhalten von Operator.
- **Geben Sie keine PII direkt in den Operator-Prompt ein** und fügen Sie dort auch keine PII ein. Operator blockiert keine PII, die in Nutzer-Prompts enthalten sind. Wenn Nutzer:innen PII manuell in eine Anfrage eingeben, werden diese Inhalte an das zugrunde liegende Sprachmodell gesendet.
- **Deaktivieren Sie die automatische Genehmigung für Aktionen**, um die Kontrolle darüber zu behalten, worauf Operator zugreifen und was Operator ausführen kann.
- **Bitten Sie Operator nicht, Vorschauwerte für Attribute anzuzeigen**, wenn Sie ein Segment erstellen oder Liquid schreiben.

## Governance und Zugriffskontrolle {#governance-and-access-control}

### Zugriff auf Operator einschränken {#restrict-access-to-operator}

Der Zugriff auf Operator wird auf Workspace-Ebene über [granulare Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) verwaltet. Administrator:innen können die Berechtigung „BrazeAI Operator verwenden“ für einzelne Nutzer:innen gewähren oder entziehen, um sicherzustellen, dass nur autorisiertes Personal mit dem Tool interagieren kann. Ohne diese spezifischen Berechtigungen wird die Operator-Oberfläche vollständig unterdrückt und die Backend-Endpunkte bleiben gesichert.

### Human-in-the-Loop-Modell {#human-in-the-loop-model}

Standardmäßig erfordert Operator eine explizite Genehmigung, bevor eine Änderung übernommen wird. Vorgeschlagene Änderungen werden als [Aktionskarten]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) zur Überprüfung präsentiert. Wenn Nutzer:innen einen Vorschlag ablehnen, werden keine Änderungen vorgenommen. Wenn Nutzer:innen einen Vorschlag annehmen, wird das Dashboard aktualisiert, aber die Änderungen bleiben ausstehend und müssen manuell gespeichert oder gestartet werden, um persistent zu werden.

Nutzer:innen können **Aktionen automatisch genehmigen** im Operator-Chat-Panel aktivieren, wodurch vorgeschlagene Aktionen sofort ohne manuelle Überprüfung ausgeführt werden. Auch bei aktivierter automatischer Genehmigung erfordern einige Aktionen aus Sicherheitsgründen immer eine explizite Genehmigung, darunter das Generieren von Bildern und das Ändern von Workspace-Einstellungen.

### Vererbung von Nutzerberechtigungen {#user-permission-inheritance}

Operator übernimmt vollständig das Berechtigungsprofil der angemeldeten Nutzer:in. Es ist ihm untersagt, Daten einzusehen oder Aktionen auszuführen, wie z. B. Campaign-Änderungen, zu denen die Nutzer:in nicht bereits eigenständig berechtigt ist.

### Berechtigung „PII anzeigen“ {#view-pii-permission}

Operator benötigt die Berechtigung „PII anzeigen“ nicht, um zu funktionieren, und das ist beabsichtigt. Operator hat keinen direkten Zugriff auf Ihren Datenspeicher und führt keine eigenständigen Datenbankabfragen durch. Stattdessen sendet Operator Anfragen an dieselben Backend-Endpunkte wie der Representational State Transfer des Dashboards und verwendet dabei die Sitzungszugangsdaten der authentifizierten Nutzer:in. Das bedeutet, dass Operator vollständig durch die bestehenden [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) der Nutzer:in begrenzt ist und auf nichts zugreifen kann, was die Nutzer:in nicht bereits sehen kann.

PII kann Operator nur auf zwei Wegen erreichen:

- Die Nutzer:in gibt PII direkt in einen Prompt ein.
- Die Nutzer:in sieht bereits PII im Dashboard, wenn sie Operator verwendet.

Wenn Nutzer:innen die Berechtigung „PII anzeigen“ nicht haben, kann Operator ihnen keine PII anzeigen. Beachten Sie, dass Operator keine Inhalte filtert, die direkt in Prompts eingegeben werden – manuell eingegebene PII werden an das zugrunde liegende Sprachmodell gesendet. Um dieses Risiko zu reduzieren, lesen Sie [PII-Exposition minimieren](#minimize-pii-exposure).

### Team-Nutzung überprüfen {#audit-team-usage}

Laden Sie den [Sicherheitsereignisbericht]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report) von Braze herunter, um die Team-Nutzung zu überwachen. Das Ereignis „Requested BrazeAI Operator Response“ bietet einen umfassenden Audit-Trail, mit dem Sie die genauen Eingaben überprüfen können, die an Operator übermittelt wurden.