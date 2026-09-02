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

Nichts in den folgenden Ausführungen ist als Rechtsberatung durch Braze beabsichtigt oder soll als solche angesehen werden. Es wird empfohlen, sich in Bezug auf Ihre besondere Situation und die Anwendbarkeit der Datenschutzgesetze auf Sie und Ihre Nutzung der Braze-Dienste an Ihren eigenen Rechtsberater zu wenden.

## Terminologie {#terminology}

Im Rahmen dieses Dokuments kann jede Bezugnahme auf personenbezogene Daten auch als Bezugnahme auf persönliche Informationen oder personenbezogene Informationen („personenbezogene Daten“) verstanden werden. Der Einfachheit halber orientieren wir uns im Allgemeinen an der Sprache der DSGVO, wenn es um die Rechte von Endnutzer:innen geht. Die Sprache der DSGVO ist häufig austauschbar oder eng an einen definierten Begriff oder ein Konzept aus anderen Datenschutzgesetzen angelehnt.

## Die Grundlagen {#the-basics}

Die meisten Datenschutzgesetze definieren drei Hauptbeteiligte, die an der Verarbeitung personenbezogener Daten beteiligt sind: betroffene Personen, Verantwortliche und Auftragsverarbeiter. Jede Gruppe hat unterschiedliche Rechte und Pflichten in Bezug auf die Verwendung personenbezogener Daten:

- Eine betroffene Person ist eine natürliche Person, deren personenbezogene Daten vom Auftragsverarbeiter oder Verantwortlichen verarbeitet werden
- Ein Verantwortlicher ist eine Stelle, die die Zwecke und Mittel der Verarbeitung personenbezogener Daten festlegt
- Ein Auftragsverarbeiter ist eine Stelle, die personenbezogene Daten im Auftrag und nach den Weisungen des Verantwortlichen verarbeitet

In Bezug auf die Braze-Dienste:

- Die betroffenen Personen sind beispielsweise die Endnutzer:innen Ihrer Kundenanwendung (z. B. Ihre Kund:innen) oder Ihre Mitarbeiter:innen, die als Unternehmensnutzer:innen in Ihrer Instanz der Braze-Dienste arbeiten.
- Sie, als Braze-Kund:in, sind der Verantwortliche, der entscheidet, wie und warum die personenbezogenen Daten der betroffenen Personen innerhalb der Braze-Dienste erfasst und verarbeitet werden.
- Braze ist ein Auftragsverarbeiter, der personenbezogene Daten in den Braze-Diensten in Ihrem Auftrag und gemäß den Weisungen verarbeitet, die wir von Ihnen erhalten.

Die oben genannten Begriffe stammen aus der DSGVO. Vergleichbare Begriffe im Rahmen des CCPA sind beispielsweise:
- „Verbraucher:innen“ für betroffene Personen.
- „Unternehmen“ für Verantwortliche.
- „Dienstleister“ für Auftragsverarbeiter.

Nachfolgend finden Sie relevante Informationen zu den häufigsten Datenschutzanfragen von betroffenen Personen, einschließlich der Möglichkeiten, wie Sie über die technischen Funktionen der Braze-Dienste darauf reagieren können.

## Das Recht auf Information {#the-right-to-be-informed}

Das Recht auf Information umfasst Ihre Verpflichtung, „faire Verarbeitungsinformationen“ bereitzustellen, in der Regel durch eine Datenschutzerklärung. Es betont die Notwendigkeit von Transparenz darüber, wie Sie personenbezogene Daten verwenden.

### Braze-Empfehlung {#braze-recommendation}

Die meisten Datenschutzgesetze betonen die Notwendigkeit von Transparenz im Zusammenhang mit der Verwendung personenbezogener Daten. Dies liegt in der Verantwortung der Datenverantwortlichen, die in der Regel eine Datenschutzerklärung vorhalten, die für die Nutzer:innen ihrer Produkte und Dienste leicht zugänglich ist und die durch Braze durchgeführte Verarbeitung abdeckt.

## Das Recht auf Auskunft {#the-right-of-access}

Gemäß den Datenschutzgesetzen können betroffene Personen das Recht haben, Folgendes zu erhalten:

- Die Bestätigung, dass ihre personenbezogenen Daten verarbeitet werden,
- Zugang zu ihren personenbezogenen Daten und
- Weitere ergänzende Informationen, wie sie durch das jeweils geltende Datenschutzgesetz bestimmt werden.

### Empfehlung von Braze

Um personenbezogene Daten aus Braze in einem maschinenlesbaren Format als Antwort auf eine Auskunftsanfrage einer betroffenen Person bereitzustellen, können Sie deren Endnutzer:innen-Profil exportieren, indem Sie einen API-Aufruf an die [REST APIs]({{site.baseurl}}/api/endpoints/export) von Braze senden – entweder mit deren Nutzer:innen-Bezeichner (von Ihnen als die an Braze übermittelte `external_id` definiert) und/oder deren Geräte-Bezeichner.

#### BrazeAI Decisioning Studio™

Um eine Auskunftsanfrage in Bezug auf personenbezogene Daten in BrazeAI Decisioning Studio™ zu erfüllen, wenden Sie sich mit den relevanten customer_id(s) und/oder E-Mail(s) an Ihren Account Manager:in.

## Das Recht auf Berichtigung {#the-right-to-rectification}

Einzelpersonen haben das Recht, personenbezogene Daten berichtigen zu lassen, wenn diese unrichtig oder unvollständig sind. Wenn Sie die betreffenden personenbezogenen Daten an Dritte weitergegeben haben, sollten Sie gegebenenfalls erwägen, diese über die Berichtigung zu informieren.

### Braze-Empfehlung

Für den Fall, dass eine betroffene Person Sie auffordert, Ungenauigkeiten in den personenbezogenen Daten zu berichtigen, die von Ihnen oder von Braze in Ihrem Auftrag verarbeitet werden, können Sie die Braze SDKs oder die Braze [REST APIs]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um diese personenbezogenen Daten zu korrigieren.

## Das Recht auf Löschung {#the-right-to-erasure}

Das Recht auf Löschung ist auch als „Recht auf Vergessenwerden“ oder „Recht auf Datenlöschung“ bekannt.

### Braze-Empfehlung

#### Standardmäßige Löschung {#standard-deletion}

Nachdem Sie die Datenerfassung eingestellt haben, können Sie den [REST-API-Endpunkt zur Löschung von Nutzer:innen von Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) verwenden, um eine:n Endnutzer:in zu löschen. Dadurch werden alle Datensätze dieser:dieses Endnutzer:in aus den Braze-Diensten entfernt:

- Für Endnutzer:innen, die eine external_id innerhalb der Braze-Dienste haben, können Sie diese ID verwenden, um die Daten dieser:dieses Endnutzer:in zu löschen.
- Für anonyme Endnutzer:innen, die keine external_id innerhalb der Braze-Dienste haben, können Sie den Gerätebezeichner über das Braze SDK abrufen und mit diesem Gerätebezeichner das Kundenprofil finden, das mit diesem Gerät verknüpft ist. Anschließend können Sie die API zur Löschung von Nutzer:innen verwenden, um das mit dieser:diesem Endnutzer:in verknüpfte Profil zu löschen.

Das Löschen einer:eines Endnutzer:in aus den Braze-Diensten löscht dauerhaft das zentrale Kundenprofil dieser:dieses Endnutzer:in bei Braze, wie durch die bereitgestellte `external_id` definiert. Dies umfasst strukturierte Profilinformationen, die Braze standardmäßig erfasst hat oder die Sie die Braze-Dienste zur Erfassung konfiguriert haben, wie z. B. Geräteinformationen, Land, Sprache und E-Mail-Adresse.

Beachten Sie, dass die E-Mail-Adresse oder Telefonnummer, die mit dem Profil der:des Endnutzer:in verknüpft ist, möglicherweise weiterhin bei Braze gespeichert sein kann, da sie mit dem Profil einer:eines anderen Endnutzer:in verknüpft sein könnte. E-Mail-Adressen und Telefonnummern sind in den Braze-Diensten nicht eindeutig. Das bedeutet, dass Ihr Team Braze so konfiguriert haben könnte, dass dieselbe E-Mail-Adresse oder Telefonnummer in mehreren Nutzerprofilen gespeichert ist. Wenn Ihr Team Braze auf diese Weise konfiguriert hat, beachten Sie, dass Sie möglicherweise alle Nutzerprofile löschen müssen, die eine bestimmte betroffene Person repräsentieren, um einem Löschungsantrag einer betroffenen Person nachzukommen, und Ihr Team müsste mehrere API-Aufrufe durchführen, um alle Nutzerprofile zu löschen, die sich auf eine bestimmte betroffene Person beziehen.

#### BrazeAI Decisioning Studio™

Um einem Recht-auf-Löschung-Antrag in Bezug auf personenbezogene Daten in BrazeAI Decisioning Studio™ nachzukommen, kontaktieren Sie Ihre:n Account Manager:in mit den relevanten customer_id(s) und/oder E-Mail(s). Ihr:e Account Manager:in kann veranlassen, dass alle zugehörigen personenbezogenen Daten im Data Warehouse gelöscht werden.

#### Zusätzliche Hinweise zur Löschung {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Zusätzliche Hinweise zur Löschung</caption>
<tbody>
  <tr>
    <td>
        <p>Kund:innen können angepasste Felder für Event-Eigenschaften und Nachrichten-Extras erstellen. Diese Felder sind nicht für personenbezogene Daten vorgesehen, daher sind sie nicht im oben beschriebenen Standard-Löschprozess enthalten. Wenn Sie jedoch Braze verwenden, um personenbezogene Daten über Event-Eigenschaften und Nachrichten-Extras einzugeben oder zu erfassen, können Sie den Löschprozess, der durch den REST-API-Endpunkt zur Löschung von Nutzer:innen ausgelöst wird, so einrichten, dass auch diese Felder einbezogen werden, sodass die in diesen Feldern enthaltenen Daten ebenfalls gelöscht werden.</p>
        <p>Standardeinstellungen werden auf Unternehmensebene festgelegt, Sie können jedoch wählen, die folgenden Felder beim Ausführen des Löschprozesses auf App-Gruppen-/Workspace-Ebene zu löschen:</p>
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
    <p>Die Einstellungen dafür sind über <b>Unternehmenseinstellungen</b> > <b>Administratoreinstellungen</b> > <b>Sicherheitseinstellungen</b> zugänglich. Datenlösch-Präferenzen werden pro Ereignistyp oder -kategorie festgelegt. Nur Nutzer:innen mit Administratorberechtigungen können Änderungen an diesen Einstellungen vornehmen. Alternativ kann ein:e Administrator:in diese Berechtigungen an eine:n andere:n Nutzer:in delegieren.</p>
    <p>Wenn ein Ereignistyp oder Nachrichten-Extra so eingestellt ist, dass er im Löschprozess einbezogen wird, werden die Daten in diesem Feld künftig für Nutzer:innen gelöscht, für die Sie einen REST-API-Endpunkt zur Löschung von Nutzer:innen ausführen. Darüber hinaus werden beim nächsten geplanten Löschvorgang die Daten aus diesen Feldern aus allen vorhandenen anonymisierten Datensätzen gelöscht, die diese Felder enthalten. Eine Wiederherstellung der gelöschten Datenfelder ist nicht möglich.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analytics

Um die Integrität der Campaign- und Anwendungsnutzungs-Analytics zu wahren, werden anonyme, aggregierte Daten nicht geändert, wenn eine:ein Endnutzer:in gelöscht wird. Braze wird beispielsweise nicht die Gesamtzahl der Sitzungen einer App verringern, wenn eine:ein Endnutzer:in gelöscht wird. Die Sitzung(en), in denen diese:dieser Endnutzer:in die App besucht hat, werden weiterhin in der Gesamtzahl der Besuche dieser App enthalten sein, aber diese Daten werden in keiner Weise mit dem Profil der:des vergessenen Endnutzer:in verbunden sein, sodass sichergestellt ist, dass diese anonymisierten und aggregierten Daten nicht auf eine:n einzelne:n Endnutzer:in zurückgeführt werden können.

Analytics innerhalb der Braze-Dienste sind mit dem Braze-Endnutzer:innen-Bezeichner verknüpft. Nachdem das Profil der:des Endnutzer:in gelöscht wurde, wird der Braze-Nutzer:innen-Bezeichner effektiv zu einem vollständig anonymisierten Bezeichner, da Braze ihn nicht mehr einer:einem einzelnen Endnutzer:in zuordnen kann.

#### Nach erfolgter Löschung {#once-deletion-has-happened}

Es wird allgemein erwartet, dass Sie angemessene Anstrengungen unternehmen, um betroffene Personen zu benachrichtigen, wenn Sie deren Antrag auf Löschung ihrer personenbezogenen Daten nachgekommen sind. Eine:ein gelöschte:r Endnutzer:in kann sich zu einem späteren Zeitpunkt erneut registrieren oder wieder mit Ihrer App oder Ihrem Dienst interagieren, und Braze wird nicht in der Lage sein, sie:ihn als die:den gelöschte:n oder vergessene:n Nutzer:in zu identifizieren. Die Braze-Dienste sind nicht in der Lage, in Ihrem Auftrag Listen gelöschter Nutzer:innen-Bezeichner oder E-Mail-Adressen zu erstellen.

## Das Recht auf Einschränkung der Verarbeitung {#the-right-to-restriction-of-processing}

Betroffene Personen können unter bestimmten Umständen das Recht haben, die Verarbeitung ihrer personenbezogenen Daten zu „blockieren“ oder zu unterbinden. Die Einschränkung der Verarbeitung bedeutet, dass keine Verarbeitung durchgeführt wird, der eine betroffene Person widersprochen hat.

### Braze-Empfehlung

Die Braze-Dienste unterstützen keine Einschränkung der Verarbeitung einzelner Kategorien personenbezogener Daten. Wenn Sie von einer betroffenen Person aufgefordert wurden, die Verarbeitung bestimmter Teilmengen der personenbezogenen Daten dieser betroffenen Person einzuschränken, sollten Sie die [Braze-APIs]({{site.baseurl}}/api/home) verwenden, um das gesamte Profil bzw. die gesamten Profile dieser Endnutzer:in zu exportieren und es bzw. sie anschließend aus Braze zu [löschen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete). Die APIs von Braze können verwendet werden, um diese Daten erneut zu importieren, falls die Endnutzer:in Ihnen anschließend erlaubt, diese bestimmten Teilmengen ihrer personenbezogenen Daten zu verarbeiten. Darüber hinaus sollten Sie Ihrer Endnutzer:in empfehlen, alle Ihre Anwendungen, die das Braze SDK verwenden, zu deinstallieren oder sich von ihnen abzumelden, um die Erfassung weiterer Daten über die betroffene Person zu beenden.

Für Kund:innen, die ausschließlich BrazeAI Decisioning Studio™ nutzen, sollten Sie keine Daten mehr an Decisioning Studio senden.

## Das Recht auf Datenübertragbarkeit {#the-right-to-data-portability}

Das Recht auf Datenübertragbarkeit ermöglicht es betroffenen Personen, ihre personenbezogenen Daten für eigene Zwecke über verschiedene Dienste hinweg zu erhalten und weiterzuverwenden. Die personenbezogenen Daten sollten in einem strukturierten, maschinenlesbaren und gängigen Format bereitgestellt werden.

### Braze-Empfehlung

Ähnlich wie beim Recht auf Auskunft können Sie die Braze [REST API]({{site.baseurl}}/api/endpoints/export) verwenden, um die personenbezogenen Daten einer Endnutzerin oder eines Endnutzers zu exportieren und sie der betroffenen Person auf deren Anfrage hin zur Verfügung zu stellen. Wenden Sie sich darüber hinaus mit den relevanten customer_id(s) und/oder E-Mail(s) an Ihren Account Manager:in, um eine Kopie aller in BrazeAI Decisioning Studio gespeicherten personenbezogenen Daten anzufordern.

## Das Recht auf Widerspruch {#the-right-to-object}

Einzelpersonen können das Recht haben, Widerspruch einzulegen gegen:

- Verarbeitung auf Grundlage berechtigter Interessen oder der Wahrnehmung einer Aufgabe im öffentlichen Interesse/Ausübung öffentlicher Gewalt (einschließlich Profiling);
- Direktmarketing (einschließlich Profiling); und
- Verarbeitung zu Zwecken der wissenschaftlichen/historischen Forschung und Statistik.

### Braze-Empfehlung

Braze bietet die Möglichkeit, ein Kundenprofil über unsere [REST APIs]({{site.baseurl}}/api/home) sowie über die [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift)-, [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android)- und [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web)-SDKs als von SMS, E-Mails oder Push-Benachrichtigungen abgemeldet zu markieren. Wenn Sie von betroffenen Personen Widersprüche gegen den Erhalt solcher Nachrichten erhalten, können Sie die APIs von Braze nutzen, um diese Endnutzer:innen abzumelden.

Falls dies nicht ausreichend ist, sollte das Endnutzer:innenprofil – um die Verarbeitung personenbezogener Daten von Endnutzer:innen durch Braze zu vermeiden – auf die gleiche Weise gelöscht werden, wie im Abschnitt „Recht auf Löschung“ beschrieben.

## Rechte in Bezug auf automatisierte Entscheidungsfindung und Profiling {#rights-related-to-automated-decision-making-and-profiling}

Einige Datenschutzgesetze verbieten oder ermöglichen es betroffenen Personen, der automatisierten Entscheidungsfindung oder dem Profiling unter bestimmten Umständen zu widersprechen, insbesondere bei Entscheidungen, die „rechtliche Wirkung entfalten oder eine ähnlich erhebliche Auswirkung auf die betroffene Person haben“.

### Empfehlung von Braze

Braze führt kein automatisiertes Profiling und keine automatisierte Entscheidungsfindung mit rechtlichen oder gleichwertigen Auswirkungen für betroffene Personen durch. Wenn Sie der Meinung sind, dass Ihre eigene Nutzung der Braze-Dienste rechtliche oder gleichwertige Auswirkungen hat und Sie einen Widerspruch dagegen erhalten haben, können Sie das Kundenprofil auf die gleiche Weise löschen wie unter dem „Recht auf Löschung“ beschrieben.

## Targeting Advertising

Nach einigen US-amerikanischen Datenschutzgesetzen der Bundesstaaten können betroffene Personen der Verwendung ihrer personenbezogenen Daten für Zwecke des Targeted Advertising widersprechen.

### Braze-Empfehlung

Wenn Sie Zielgruppen erstellen, um Ihren betroffenen Personen gezielte Werbung anzuzeigen, sollten Sie sicherstellen, dass Sie alle betroffenen Personen ausgeschlossen haben, die dem Targeted Advertising widersprochen haben – beispielsweise kalifornische Verbraucher:innen, die ihr Recht auf „Do Not Sell or Share“ gemäß dem CCPA ausgeübt haben.

Weitere Informationen zum Erstellen von Zielgruppen für die Synchronisierung mit Drittanbieterplattformen finden Sie unter [Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync).

## Das Recht auf Nichtdiskriminierung {#the-right-to-non-discrimination}

Betroffene Personen haben das Recht, ihre Datenschutzrechte ohne Diskriminierung auszuüben.

### Braze-Empfehlung

Bei der Nutzung der Braze-Dienste müssen Kund:innen sicherstellen, dass sie betroffene Personen, die ihre Datenschutzrechte ausgeübt haben, nicht diskriminieren. Wir empfehlen beispielsweise, dass betroffene Personen, die ihre Datenschutzrechte ausgeübt haben, nicht in Zielgruppen segmentiert oder anderweitig so angesprochen werden, dass dies zu einer Diskriminierung führen könnte.