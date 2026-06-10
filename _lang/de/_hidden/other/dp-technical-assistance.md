---
nav_title: Technische Unterstützung beim Datenschutz
article_title: Technische Unterstützung beim Datenschutz in den Braze-Diensten
page_order: 1
description: "Diese Seite enthält technische Anweisungen, die es Ihnen ermöglichen, über die Braze-Dienste Anfragen von Einzelpersonen in Bezug auf ihre Rechte an personenbezogenen Daten zu verwalten."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Technische Unterstützung beim Datenschutz in den Braze-Diensten {#data-protection-technical-assistance-in-the-braze-services}

Es gibt eine Reihe von Datenschutzgesetzen, die regeln, was Unternehmen mit personenbezogenen Daten tun dürfen („Datenschutzgesetze“), darunter die EU- und UK-Datenschutz-Grundverordnung („DSGVO“), der California Consumer Privacy Act („CCPA“) und das US-Gesetz zum Schutz medizinischer Daten (HIPAA). Es gibt weitere nationale, bundesstaatliche und branchenspezifische Datenschutzgesetze und -vorschriften, die für Ihr Unternehmen gelten können.

Diese Datenschutzgesetze gewähren Einzelpersonen „Datenschutzrechte“ in Bezug auf ihre personenbezogenen Daten. Unternehmen sind verpflichtet, Anfragen von Personen, die ihre Datenschutzrechte ausüben, entgegenzunehmen und zu beantworten. Die Braze-Dienste können Sie bei der Einhaltung dieser Datenschutzgesetze unterstützen, indem sie Features bereitstellen, die bestimmte nach diesen Gesetzen vorgeschriebene Maßnahmen erleichtern. Dieses Dokument enthält technische Anweisungen zur Verwendung dieser Features für die Verwaltung von Anfragen zu Datenschutzrechten. Es liegt an Ihnen, zu bestimmen, welche Datenschutzgesetze für Ihr Unternehmen gelten und wie Sie diese einhalten.

## Rechtlicher Hinweis {#legal-disclaimer}

Nichts von dem, was im Folgenden beschrieben wird, ist als Rechtsberatung durch Braze gedacht und darf auch nicht als solche angesehen werden. Wir empfehlen Ihnen, sich in Bezug auf Ihre spezielle Situation und die Anwendung der Datenschutzgesetze auf Sie und Ihre Nutzung der Braze-Dienste von Ihrem eigenen Rechtsbeistand beraten zu lassen.

## Terminologie {#terminology}

Im Sinne dieses Dokuments können Bezugnahmen auf personenbezogene Daten auch als Bezugnahmen auf persönliche Daten oder persönlich identifizierbare Informationen („Personenbezogene Daten“) verstanden werden. Der Einfachheit halber werden im Allgemeinen die Begriffe der DSGVO verwendet, wenn es um die Rechte von Endnutzer:innen geht. Die Begriffe der DSGVO sind häufig austauschbar oder eng an definierte Begriffe oder Konzepte anderer Datenschutzgesetze angelehnt.

## Die Grundlagen {#the-basics}

Die meisten Datenschutzgesetze unterscheiden drei Hauptakteure, die an der Verarbeitung personenbezogener Daten beteiligt sind: betroffene Personen, Verantwortliche und Auftragsverarbeiter. Jede Gruppe hat unterschiedliche Rechte und Pflichten in Bezug auf die Verwendung personenbezogener Daten:

- Eine betroffene Person ist eine Einzelperson, deren personenbezogene Daten vom Auftragsverarbeiter oder Verantwortlichen verarbeitet werden.
- Ein Verantwortlicher ist eine Stelle, die die Zwecke und Mittel der Verarbeitung personenbezogener Daten festlegt.
- Ein Auftragsverarbeiter ist eine Stelle, die personenbezogene Daten im Auftrag und auf Anweisung des Verantwortlichen verarbeitet.

In Bezug auf die Braze-Dienste:

- Bei den betroffenen Personen handelt es sich beispielsweise um die Endnutzer:innen Ihrer Kundenanwendung (z. B. Ihre Kund:innen) oder um Ihre Mitarbeiter:innen, die Unternehmensnutzer:innen in Ihrer Instanz der Braze-Dienste sind.
- Sie, als Braze-Kunde, sind der Verantwortliche, der entscheidet, wie und warum die personenbezogenen Daten der betroffenen Personen innerhalb der Braze-Dienste erhoben und verarbeitet werden.
- Braze ist ein Auftragsverarbeiter, der personenbezogene Daten in den Braze-Diensten in Ihrem Auftrag und gemäß den Anweisungen verarbeitet, die wir von Ihnen erhalten.

Bei den oben genannten Begriffen handelt es sich um DSGVO-Begriffe. Vergleichbare Begriffe unter dem CCPA lauten beispielsweise:

- „Verbraucher:innen“ für betroffene Personen.
- „Unternehmen“ für Verantwortliche.
- „Dienstleister“ für Auftragsverarbeiter.

Im Folgenden finden Sie relevante Informationen zu den häufigsten Anfragen von betroffenen Personen zu ihren Datenschutzrechten, einschließlich Informationen darüber, wie Sie über die technischen Features der Braze-Dienste auf diese Anfragen reagieren können.

## Das Recht auf Information {#the-right-to-be-informed}

Das Recht auf Information umfasst Ihre Verpflichtung, Informationen über die „angemessene Verarbeitung“ bereitzustellen, in der Regel in Form eines Datenschutzhinweises. Es betont die Notwendigkeit von Transparenz darüber, wie Sie personenbezogene Daten verwenden.

### Braze-Empfehlung {#braze-recommendation}

Die meisten Datenschutzgesetze betonen die Notwendigkeit von Transparenz im Zusammenhang mit der Verwendung personenbezogener Daten. Dies liegt in der Verantwortung der Verantwortlichen, die in der Regel einen Datenschutzhinweis bereithalten, der für die Nutzer:innen ihrer Produkte und Dienste leicht zugänglich ist und die von Braze durchgeführte Verarbeitung abdeckt.

## Das Recht auf Auskunft {#the-right-of-access}

Gemäß den Datenschutzgesetzen haben betroffene Personen möglicherweise das Recht auf:

- Bestätigung, dass ihre personenbezogenen Daten verarbeitet werden,
- Zugang zu ihren personenbezogenen Daten und
- weitere ergänzende Informationen, die durch das geltende Datenschutzgesetz festgelegt sind.

### Braze-Empfehlung

Um personenbezogene Daten von Braze in einem maschinenlesbaren Format als Antwort auf die Auskunftsanfrage einer betroffenen Person bereitzustellen, können Sie deren Endnutzerprofil exportieren, indem Sie einen API-Aufruf an die [REST-APIs]({{site.baseurl}}/api/endpoints/export/#user-export) von Braze mit entweder der Nutzerkennung (von Ihnen definiert als die `external_id`, die Braze bereitgestellt wurde) und/oder der Gerätekennung tätigen.

#### BrazeAI Decisioning Studio™

Um einer Auskunftsanfrage in Bezug auf personenbezogene Daten in BrazeAI Decisioning Studio™ nachzukommen, wenden Sie sich mit den relevanten customer_id(s) und/oder E-Mail(s) an Ihre:n Account Manager:in.

## Das Recht auf Berichtigung {#the-right-to-rectification}

Einzelpersonen haben das Recht, personenbezogene Daten berichtigen zu lassen, wenn diese unrichtig oder unvollständig sind. Wenn Sie die betreffenden personenbezogenen Daten an Dritte weitergegeben haben, sollten Sie gegebenenfalls prüfen, ob es notwendig ist, diese über die Berichtigung zu informieren.

### Braze-Empfehlung

Für den Fall, dass eine betroffene Person Sie auffordert, Ungenauigkeiten in den von Ihnen oder von Braze in Ihrem Auftrag verarbeiteten personenbezogenen Daten zu berichtigen, können Sie die Braze SDKs oder die Braze [REST-APIs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) verwenden, um diese personenbezogenen Daten zu korrigieren.

## Das Recht auf Löschung {#the-right-to-erasure}

Das Recht auf Löschung ist auch als „Recht auf Vergessenwerden“ bekannt.

### Braze-Empfehlung

#### Standardlöschung {#standard-deletion}

Sobald Sie die Datenerfassung gestoppt haben, können Sie den [REST-API-Endpunkt User Deletion von Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) verwenden, um eine:n Endnutzer:in zu löschen. Dadurch werden alle Datensätze dieser:dieses Endnutzer:in aus den Braze-Diensten entfernt:

- Für Endnutzer:innen, die eine external_id innerhalb der Braze-Dienste haben, können Sie diese ID verwenden, um die Daten dieser:dieses Endnutzer:in zu löschen.
- Bei anonymen Endnutzer:innen, die keine external_id innerhalb der Braze-Dienste haben, können Sie die Gerätekennung dieser:dieses Endnutzer:in mit dem Braze SDK abrufen und die Gerätekennung verwenden, um das mit diesem Gerät verbundene Endnutzerprofil zu finden. Anschließend können Sie die User Deletion API verwenden, um das mit dieser:diesem Endnutzer:in verknüpfte Profil zu löschen.

Das Löschen einer:eines Endnutzer:in aus den Braze-Diensten entfernt dauerhaft das zentrale Braze-Nutzerprofil für diese:diesen Endnutzer:in, wie es durch die bereitgestellte `external_id` definiert ist. Dies umfasst strukturierte Profildaten, die Braze standardmäßig erfasst hat oder die Sie für die Erfassung durch die Braze-Dienste konfiguriert haben, wie z. B. Geräteinformationen, Land, Sprache und E-Mail-Adresse.

Beachten Sie, dass die E-Mail-Adresse oder Telefonnummer, die mit dem Profil der:des Endnutzer:in verknüpft ist, weiterhin von Braze gespeichert sein könnte, da sie mit dem Profil einer:eines anderen Endnutzer:in verknüpft sein könnte. E-Mail-Adressen und Telefonnummern sind in den Braze-Diensten nicht eindeutig. Das bedeutet, dass Ihr Team Braze so konfiguriert haben könnte, dass dieselbe E-Mail-Adresse oder Telefonnummer in mehreren Nutzerprofilen gespeichert wird. Wenn Ihr Team Braze auf diese Weise konfiguriert hat, beachten Sie, dass Sie möglicherweise alle Nutzerprofile, die eine bestimmte betroffene Person repräsentieren, löschen müssen, um einer Löschanfrage einer betroffenen Person nachzukommen, und dass Ihr Team mehrere API-Aufrufe tätigen muss, um alle Nutzerprofile zu löschen, die sich auf eine bestimmte betroffene Person beziehen.

#### BrazeAI Decisioning Studio™

Um einer Löschanfrage in Bezug auf personenbezogene Daten in BrazeAI Decisioning Studio™ nachzukommen, wenden Sie sich mit den relevanten customer_id(s) und/oder E-Mail(s) an Ihre:n Account Manager:in. Ihre:Ihr Account Manager:in kann veranlassen, dass alle zugehörigen personenbezogenen Daten im Data Warehouse gelöscht werden.

#### Zusätzliche Überlegungen zur Löschung {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Zusätzliche Überlegungen zur Löschung</caption>
<tbody>
  <tr>
    <td>
        <p>Kund:innen können benutzerdefinierte Felder für Event-Eigenschaften und Nachrichtenextras erstellen. Diese Felder sind nicht für personenbezogene Daten vorgesehen, weshalb sie nicht in den oben beschriebenen Standard-Löschvorgang einbezogen werden. Wenn Sie jedoch Braze verwenden, um personenbezogene Daten über Event-Eigenschaften und Nachrichtenextras einzugeben oder zu erfassen, können Sie den durch den REST-API-Endpunkt User Deletion ausgelösten Löschvorgang so einrichten, dass auch diese Felder einbezogen werden, sodass die darin enthaltenen Daten ebenfalls gelöscht werden.</p>
        <p>Die Standardeinstellungen werden auf Unternehmensebene angewendet. Sie können jedoch die folgenden Felder löschen lassen, wenn der Löschvorgang auf der Ebene der App-Gruppe/des Workspace ausgeführt wird:</p>
    <ul>
        <li>PROPERTIES für USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES für USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS für:
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Zukünftige Nachrichtenversand-Ereignisse</li>
            </ul>
        </li>
    </ul>
    <p>Auf diese Einstellungen können Sie über <b>Unternehmenseinstellungen</b> > <b>Admin-Einstellungen</b> > <b>Sicherheitseinstellungen</b> zugreifen. Die Einstellungen zur Datenlöschung werden je Event-Typ oder Kategorie festgelegt. Nur Nutzer:innen mit Administratorberechtigungen können Änderungen an diesen Einstellungen vornehmen. Alternativ kann ein:e Administrator:in diese Berechtigungen an eine:n andere:n Nutzer:in delegieren.</p>
    <p>Wenn ein Event-Typ oder ein Nachrichtenextra so eingestellt ist, dass es in den Löschvorgang einbezogen wird, werden die Daten in diesem Feld künftig für Nutzer:innen gelöscht, für die Sie den REST-API-Endpunkt User Deletion ausführen. Wenn Sie diese Löschpräferenz auswählen, werden darüber hinaus beim nächsten geplanten Löschauftrag die Daten aus diesen Feldern aus allen bestehenden anonymisierten Datensätzen gelöscht, die diese Felder enthalten. Eine Wiederherstellung der gelöschten Datenfelder ist nicht möglich.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analytics

Um die Integrität der Analytics für Campaigns und die Anwendungsnutzung zu wahren, werden anonyme aggregierte Daten nicht verändert, wenn eine:ein Endnutzer:in gelöscht wird. Braze verringert beispielsweise nicht die Gesamtzahl der Sitzungen einer App, wenn eine:ein Endnutzer:in gelöscht wird. Die Sitzung(en), in denen diese:dieser Endnutzer:in die App besucht hat, werden weiterhin in die Gesamtzahl der Besuche dieser App einbezogen, aber diese Daten werden in keiner Weise mit dem Profil der:des vergessenen Endnutzer:in in Verbindung gebracht, sodass sichergestellt ist, dass diese anonymisierten und aggregierten Daten nicht auf eine:n einzelne:n Endnutzer:in zurückgeführt werden können.

Die Analytics innerhalb der Braze-Dienste sind an die Braze-Endnutzerkennung gebunden. Nachdem das Nutzerprofil gelöscht wurde, wird die Braze-Nutzerkennung zu einer vollständig anonymisierten Kennung, da Braze sie keiner:keinem einzelnen Endnutzer:in mehr zuordnen kann.

#### Nach der Löschung {#once-deletion-has-happened}

Im Allgemeinen wird von Ihnen erwartet, dass Sie sich in angemessener Weise bemühen, die betroffenen Personen zu benachrichtigen, wenn Sie ihrer Bitte um Löschung ihrer personenbezogenen Daten nachgekommen sind. Eine:ein gelöschte:r Endnutzer:in kann sich zu einem späteren Zeitpunkt erneut registrieren oder mit Ihrer App oder Ihrem Dienst in Kontakt treten, und Braze wird sie:ihn nicht als die:den gelöschte:n oder vergessene:n Nutzer:in identifizieren können. Die Braze-Dienste sind nicht in der Lage, in Ihrem Auftrag Listen mit gelöschten Nutzerkennungen oder E-Mail-Adressen zu erstellen.

## Das Recht auf Einschränkung der Verarbeitung {#the-right-to-restriction-of-processing}

Betroffene Personen haben unter bestimmten Umständen möglicherweise das Recht, die Verarbeitung ihrer personenbezogenen Daten zu „blockieren“ oder zu unterbinden. Die Einschränkung der Verarbeitung bedeutet, dass keine Verarbeitung durchgeführt wird, gegen die eine betroffene Person Einspruch erhoben hat.

### Braze-Empfehlung

Die Braze-Dienste unterstützen keine Einschränkung der Verarbeitung einzelner Kategorien personenbezogener Daten. Wenn Sie von einer betroffenen Person gebeten wurden, die Verarbeitung bestimmter Teilmengen der personenbezogenen Daten dieser Person einzuschränken, sollten Sie die [Braze-APIs]({{site.baseurl}}/api/home/) verwenden, um das gesamte Profil bzw. die gesamten Profile dieser:dieses Endnutzer:in zu exportieren und es dann aus Braze [zu löschen]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint). Die Braze-APIs können verwendet werden, um diese Daten erneut zu importieren, falls die:der Endnutzer:in Ihnen anschließend erlaubt, diese bestimmten Teilmengen ihrer:seiner personenbezogenen Daten zu verarbeiten. Darüber hinaus sollten Sie Ihren Endnutzer:innen empfehlen, alle Anwendungen, die das Braze SDK verwenden, zu deinstallieren oder sich davon abzumelden, um die Erfassung weiterer Daten über die betroffene Person zu unterbinden.

Für Kund:innen, die ausschließlich BrazeAI Decisioning Studio™ nutzen, sollten Sie keine Daten mehr an Decisioning Studio senden.

## Das Recht auf Datenübertragbarkeit {#the-right-to-data-portability}

Das Recht auf Datenübertragbarkeit ermöglicht es betroffenen Personen, ihre personenbezogenen Daten für eigene Zwecke über verschiedene Dienste hinweg zu erhalten und wiederzuverwenden. Die personenbezogenen Daten sollten in einem strukturierten, maschinenlesbaren und gängigen Format bereitgestellt werden.

### Braze-Empfehlung

Ähnlich wie beim Recht auf Auskunft können Sie die Braze [REST-API]({{site.baseurl}}/api/endpoints/export/#user-export) verwenden, um die personenbezogenen Daten einer:eines Endnutzer:in zu exportieren und sie der betroffenen Person auf deren Anfrage hin zur Verfügung zu stellen. Wenden Sie sich darüber hinaus mit den relevanten customer_id(s) und/oder E-Mail(s) an Ihre:n Account Manager:in, um eine Kopie aller in BrazeAI Decisioning Studio gespeicherten personenbezogenen Daten anzufordern.

## Das Widerspruchsrecht {#the-right-to-object}

Einzelpersonen haben möglicherweise das Recht, Widerspruch einzulegen gegen:

- Verarbeitung auf der Grundlage berechtigter Interessen oder der Wahrnehmung einer Aufgabe im öffentlichen Interesse/Ausübung öffentlicher Gewalt (einschließlich Profiling);
- Direktmarketing (einschließlich Profiling); und
- Verarbeitung zu Zwecken der wissenschaftlichen/historischen Forschung und Statistik.

### Braze-Empfehlung

Braze bietet die Möglichkeit, ein Nutzerprofil als von SMS, E-Mails oder Push-Benachrichtigungen abgemeldet zu markieren, sowohl über unsere [REST-APIs]({{site.baseurl}}/api/home/) als auch über die [iOS-]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) und [Web-SDKs]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Wenn Sie von betroffenen Personen Einwände gegen den Erhalt solcher Nachrichten erhalten, können Sie die Braze-APIs verwenden, um diese Endnutzer:innen abzumelden.

Wenn dies nicht ausreicht, um die Verarbeitung personenbezogener Daten von Endnutzer:innen durch Braze zu verhindern, sollte das Nutzerprofil auf die gleiche Weise wie unter dem „Recht auf Löschung“ beschrieben gelöscht werden.


## Rechte in Bezug auf automatisierte Entscheidungsfindung und Profiling {#rights-related-to-automated-decision-making-and-profiling}

Einige Datenschutzgesetze verhindern automatisierte Entscheidungsfindung oder Profiling unter bestimmten Umständen oder ermöglichen es betroffenen Personen, sich dagegen zu entscheiden, insbesondere bei Entscheidungen, die „eine rechtliche Wirkung oder eine ähnlich erhebliche Auswirkung auf die betroffene Person haben“.

### Braze-Empfehlung

Braze führt keine automatisierte Profilerstellung oder Entscheidungsfindung durch, die rechtliche oder gleichwertige Auswirkungen auf betroffene Personen hat. Wenn Sie der Meinung sind, dass Ihre eigene Nutzung der Braze-Dienste rechtliche oder gleichwertige Auswirkungen hat und Sie einen entsprechenden Widerspruch erhalten haben, können Sie das Nutzerprofil auf die gleiche Weise wie unter dem „Recht auf Löschung“ beschrieben löschen.

## Zielgerichtete Werbung {#targeting-advertising}

Nach den Datenschutzgesetzen einiger US-Bundesstaaten können betroffene Personen der Verwendung ihrer personenbezogenen Daten für gezielte Werbezwecke widersprechen.

### Braze-Empfehlung

Bei der Erstellung von Zielgruppen für die gezielte Werbung an Ihre betroffenen Personen sollten Sie sicherstellen, dass Sie alle betroffenen Personen ausgeschlossen haben, die gezielter Werbung widersprochen haben, beispielsweise kalifornische Verbraucher:innen, die ihr Recht auf „Nicht verkaufen oder weitergeben“ gemäß dem CCPA ausgeübt haben.

Weitere Informationen zur Erstellung von Zielgruppen, die mit Drittanbieter-Plattformen synchronisiert werden können, finden Sie unter [Zielgruppensynchronisierung]({{site.baseurl}}/partners/canvas_steps/).

## Das Recht auf Nichtdiskriminierung {#the-right-to-non-discrimination}

Betroffene Personen haben das Recht, ihre Datenschutzrechte ohne Diskriminierung auszuüben.

### Braze-Empfehlung

Bei der Nutzung der Braze-Dienste müssen Kund:innen sicherstellen, dass betroffene Personen, die ihre Datenschutzrechte ausgeübt haben, nicht diskriminiert werden. So empfehlen wir beispielsweise, dass betroffene Personen, die ihre Datenschutzrechte ausgeübt haben, nicht in Zielgruppen segmentiert oder anderweitig in einer Weise angesprochen werden, die sie diskriminieren könnte.