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

Nichts in den folgenden Ausführungen ist als Rechtsberatung durch Braze gedacht und soll auch nicht als solche angesehen werden. Wir empfehlen Ihnen, sich in Bezug auf Ihre individuelle Situation und die Anwendung der Datenschutzgesetze auf Sie und Ihre Nutzung der Braze-Dienste an Ihren eigenen Rechtsberater zu wenden.

## Terminologie {#terminology}

Im Rahmen dieses Dokuments kann jeder Verweis auf personenbezogene Daten auch als Verweis auf persönliche Informationen oder personenidentifizierbare Informationen verstanden werden („personenbezogene Daten“). Der Einfachheit halber stützen wir uns generell auf die Terminologie der DSGVO, wenn es um die Rechte von Endnutzer:innen geht. Die Terminologie der DSGVO ist häufig austauschbar oder eng an definierte Begriffe oder Konzepte aus anderen Datenschutzgesetzen angelehnt.

## Die Grundlagen {#the-basics}

Die meisten Datenschutzgesetze definieren drei primäre Beteiligte, die an der Verarbeitung personenbezogener Daten mitwirken: betroffene Personen, Verantwortliche und Auftragsverarbeiter. Jede Gruppe hat unterschiedliche Rechte und Pflichten in Bezug auf die Verwendung personenbezogener Daten:

- Eine betroffene Person ist eine natürliche Person, deren personenbezogene Daten vom Auftragsverarbeiter oder Verantwortlichen verarbeitet werden
- Ein Verantwortlicher ist eine Stelle, die die Zwecke und Mittel der Verarbeitung personenbezogener Daten festlegt
- Ein Auftragsverarbeiter ist eine Stelle, die personenbezogene Daten im Auftrag und nach Weisung des Verantwortlichen verarbeitet

In Bezug auf die Braze-Dienste:

- Die betroffenen Personen sind beispielsweise die Endnutzer:innen Ihrer Kundenanwendung (z. B. Ihre Kund:innen) oder Ihre Mitarbeitenden, die Unternehmensnutzer:innen in Ihrer Instanz der Braze-Dienste sind.
- Sie, als Braze-Kund:in, sind der Verantwortliche, der entscheidet, wie und warum die personenbezogenen Daten der betroffenen Personen innerhalb der Braze-Dienste erfasst und verarbeitet werden.
- Braze ist ein Auftragsverarbeiter, der personenbezogene Daten in den Braze-Diensten in Ihrem Auftrag und gemäß den Weisungen verarbeitet, die wir von Ihnen erhalten.

Die oben genannten Begriffe stammen aus der DSGVO, aber vergleichbare Begriffe gibt es beispielsweise auch im CCPA:
- „Verbraucher:innen“ für betroffene Personen.
- „Unternehmen“ für Verantwortliche.
- „Dienstleister“ für Auftragsverarbeiter.

Im Folgenden finden Sie relevante Informationen zu den häufigsten Datenschutzanfragen von betroffenen Personen, einschließlich der Möglichkeiten, wie Sie über die technischen Features der Braze-Dienste darauf reagieren können.

## Das Recht auf Information {#the-right-to-be-informed}

Das Recht auf Information umfasst Ihre Verpflichtung, „faire Verarbeitungsinformationen“ bereitzustellen, in der Regel durch eine Datenschutzerklärung. Es betont die Notwendigkeit der Transparenz hinsichtlich der Verwendung personenbezogener Daten.

### Braze-Empfehlung {#braze-recommendation}

Die meisten Datenschutzgesetze betonen die Notwendigkeit der Transparenz im Zusammenhang mit der Verwendung personenbezogener Daten. Dies liegt in der Verantwortung der Datenverantwortlichen, die in der Regel eine Datenschutzerklärung pflegen, die für Nutzer:innen ihrer Produkte und Dienste leicht zugänglich ist und die durch Braze durchgeführte Verarbeitung abdeckt.

## Das Auskunftsrecht {#the-right-of-access}

Gemäß den Datenschutzgesetzen haben betroffene Personen möglicherweise das Recht, Folgendes zu erhalten:

- Bestätigung, dass ihre personenbezogenen Daten verarbeitet werden,
- Zugang zu ihren personenbezogenen Daten und
- weitere ergänzende Informationen, wie sie durch das jeweils anwendbare Datenschutzgesetz bestimmt werden.

### Braze-Empfehlung

Um personenbezogene Daten aus Braze in einem maschinenlesbaren Format als Antwort auf eine Auskunftsanfrage einer betroffenen Person bereitzustellen, können Sie deren Endnutzer:innen-Profil exportieren, indem Sie einen API-Aufruf an die [REST APIs]({{site.baseurl}}/api/endpoints/export) von Braze senden – entweder mit der Nutzerkennung (von Ihnen als die an Braze übergebene `external_id` definiert) und/oder der Gerätekennung.

#### BrazeAI Decisioning Studio™

Um eine Auskunftsanfrage in Bezug auf personenbezogene Daten in BrazeAI Decisioning Studio™ zu erfüllen, wenden Sie sich mit den entsprechenden customer_id(s) und/oder E-Mail(s) an Ihren Account Manager.

## Das Recht auf Berichtigung {#the-right-to-rectification}

Einzelpersonen haben das Recht, personenbezogene Daten berichtigen zu lassen, wenn diese unrichtig oder unvollständig sind. Wenn Sie die betreffenden personenbezogenen Daten an Dritte weitergegeben haben, sollten Sie erwägen, diese nach Möglichkeit über die Berichtigung zu informieren.

### Braze-Empfehlung

Falls eine betroffene Person Sie auffordert, Unrichtigkeiten in den personenbezogenen Daten zu berichtigen, die von Ihnen oder von Braze in Ihrem Auftrag verarbeitet werden, können Sie die Braze SDKs oder die Braze [REST APIs]({{site.baseurl}}/api/endpoints/user_data/post_user_track) verwenden, um diese personenbezogenen Daten zu korrigieren.

## Das Recht auf Löschung {#the-right-to-erasure}

Das Recht auf Löschung ist auch als „Recht auf Vergessenwerden“ oder „Recht auf Datenlöschung“ bekannt.

### Braze-Empfehlung

#### Standard-Löschung {#standard-deletion}

Sobald Sie die Datenerfassung eingestellt haben, können Sie den [REST-API-Endpunkt zur Nutzerlöschung von Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) verwenden, um eine Endnutzer:in zu löschen. Dadurch werden alle Datensätze dieser Endnutzer:in aus den Braze-Diensten entfernt:

- Für Endnutzer:innen, die eine external_id innerhalb der Braze-Dienste haben, können Sie diese ID verwenden, um die Daten dieser Endnutzer:in zu löschen.
- Für anonyme Endnutzer:innen, die keine external_id innerhalb der Braze-Dienste haben, können Sie die Gerätekennung der Endnutzer:in über das Braze SDK abrufen und damit das mit diesem Gerät verknüpfte Endnutzerprofil finden. Anschließend können Sie die API zur Nutzerlöschung verwenden, um das mit dieser Endnutzer:in verknüpfte Profil zu löschen.

Das Löschen einer Endnutzer:in aus den Braze-Diensten entfernt dauerhaft das zentrale Nutzerprofil dieser Endnutzer:in bei Braze, wie durch die bereitgestellte `external_id` definiert. Dazu gehören strukturierte Profilinformationen, die Braze standardmäßig erfasst hat oder die Sie in den Braze-Diensten zur Erfassung konfiguriert haben, wie z. B. Geräteinformationen, Land, Sprache und E-Mail-Adresse.

Beachten Sie, dass die E-Mail-Adresse oder Telefonnummer, die mit dem Profil der Endnutzer:in verknüpft ist, weiterhin bei Braze gespeichert sein kann, da sie mit dem Profil einer anderen Endnutzer:in verknüpft sein könnte. E-Mail-Adressen und Telefonnummern sind in den Braze-Diensten nicht eindeutig. Das bedeutet, dass Ihr Team Braze so konfiguriert haben könnte, dass dieselbe E-Mail-Adresse oder Telefonnummer in mehreren Nutzerprofilen gespeichert wird. Wenn Ihr Team Braze auf diese Weise konfiguriert hat, beachten Sie, dass Sie möglicherweise alle Nutzerprofile löschen müssen, die eine bestimmte betroffene Person repräsentieren, um einem Löschantrag einer betroffenen Person nachzukommen, und Ihr Team müsste mehrere API-Aufrufe durchführen, um alle Nutzerprofile zu löschen, die sich auf eine bestimmte betroffene Person beziehen.

#### BrazeAI Decisioning Studio™

Um einem Recht-auf-Löschung-Antrag in Bezug auf personenbezogene Daten in BrazeAI Decisioning Studio™ nachzukommen, kontaktieren Sie Ihren Account Manager mit den relevanten customer_id(s) und/oder E-Mail(s). Ihr Account Manager kann veranlassen, dass alle zugehörigen personenbezogenen Daten im Data Warehouse gelöscht werden.

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
        <p>Kund:innen können angepasste Felder für Event-Eigenschaften und Nachrichtenzusätze (Message Extras) erstellen. Diese Felder sind nicht für personenbezogene Daten vorgesehen, weshalb sie nicht im oben beschriebenen Standard-Löschprozess enthalten sind. Wenn Sie jedoch Braze verwenden, um personenbezogene Daten über Event-Eigenschaften und Nachrichtenzusätze einzugeben oder zu erfassen, können Sie den Löschprozess, der durch den REST-API-Endpunkt zur Nutzerlöschung ausgelöst wird, so konfigurieren, dass auch diese Felder eingeschlossen werden, sodass die in diesen Feldern enthaltenen Daten ebenfalls gelöscht werden.</p>
        <p>Standardeinstellungen werden auf Unternehmensebene angewendet, Sie können jedoch auf App-Gruppen-/Workspace-Ebene festlegen, dass die folgenden Felder bei Ausführung des Löschprozesses gelöscht werden:</p>
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
    <p>Die Einstellungen hierfür finden Sie unter <b>Unternehmenseinstellungen</b> > <b>Administratoreinstellungen</b> > <b>Sicherheitseinstellungen</b>. Die Einstellungen zur Datenlöschung werden pro Ereignistyp oder -kategorie festgelegt. Nur Nutzer:innen mit Administratorrechten können Änderungen an diesen Einstellungen vornehmen. Alternativ kann eine Administrator:in diese Berechtigungen an andere Nutzer:innen delegieren.</p>
    <p>Wenn ein Ereignistyp oder Nachrichtenzusatz so konfiguriert ist, dass er in den Löschprozess einbezogen wird, werden die Daten in diesem Feld ab sofort für Nutzer:innen gelöscht, für die Sie den REST-API-Endpunkt zur Nutzerlöschung ausführen. Darüber hinaus werden beim nächsten geplanten Löschjob die Daten aus diesen Feldern aus allen vorhandenen anonymisierten Datensätzen gelöscht, die diese Felder enthalten. Eine Wiederherstellung der gelöschten Datenfelder ist nicht möglich.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analytics

Um die Integrität der Analytics für Campaigns und App-Nutzung zu wahren, werden anonymisierte aggregierte Daten nicht verändert, wenn eine Endnutzer:in gelöscht wird. Braze verringert beispielsweise nicht die Gesamtzahl der Sitzungen einer App, wenn eine Endnutzer:in gelöscht wird. Die Sitzung(en), in denen diese Endnutzer:in die App besucht hat, werden weiterhin in der Gesamtzahl der Besuche dieser App enthalten sein, aber diese Daten werden in keiner Weise mit dem Profil der vergessenen Endnutzer:in verknüpft sein, wodurch sichergestellt wird, dass diese anonymisierten und aggregierten Daten nicht auf eine einzelne Endnutzer:in zurückgeführt werden können.

Analytics innerhalb der Braze-Dienste sind an die Braze-Endnutzerkennung gebunden. Nachdem das Profil der Endnutzer:in gelöscht wurde, wird die Braze-Nutzerkennung praktisch zu einer vollständig anonymisierten Kennung, da Braze sie nicht mehr einer einzelnen Endnutzer:in zuordnen kann.

#### Nach erfolgter Löschung {#once-deletion-has-happened}

Von Ihnen wird im Allgemeinen erwartet, dass Sie angemessene Anstrengungen unternehmen, um betroffene Personen zu benachrichtigen, wenn Sie deren Antrag auf Löschung ihrer personenbezogenen Daten nachgekommen sind. Eine gelöschte Endnutzer:in kann sich zu einem späteren Zeitpunkt erneut registrieren oder wieder mit Ihrer App oder Ihrem Dienst interagieren, und Braze wird nicht in der Lage sein, sie als die gelöschte oder vergessene Nutzer:in zu identifizieren. Die Braze-Dienste sind nicht in der Lage, in Ihrem Auftrag Listen gelöschter Nutzerkennungen oder E-Mail-Adressen zu erstellen.

## Das Recht auf Einschränkung der Verarbeitung {#the-right-to-restriction-of-processing}

Betroffene Personen können unter bestimmten Umständen das Recht haben, die Verarbeitung ihrer personenbezogenen Daten zu „blockieren“ oder zu unterdrücken. Die Einschränkung der Verarbeitung bedeutet, dass keine Verarbeitung durchgeführt wird, gegen die eine betroffene Person Widerspruch eingelegt hat.

### Braze-Empfehlung

Die Braze-Serviceleistungen unterstützen die Einschränkung der Verarbeitung einzelner Kategorien personenbezogener Daten nicht. Wenn Sie von einer betroffenen Person aufgefordert wurden, die Verarbeitung bestimmter Teilmengen der personenbezogenen Daten dieser betroffenen Person einzuschränken, sollten Sie die [Braze-APIs]({{site.baseurl}}/api/home) verwenden, um das/die gesamte(n) Profil(e) dieser/dieses Endnutzer:in zu exportieren und es/sie dann aus Braze zu [löschen]({{site.baseurl}}/api/endpoints/user_data/post_user_delete). Die APIs von Braze können verwendet werden, um diese Daten erneut zu importieren, falls die/der Endnutzer:in Ihnen anschließend die Verarbeitung dieser bestimmten Teilmengen ihrer/seiner personenbezogenen Daten gestattet. Darüber hinaus sollten Sie Ihren Endnutzer:innen empfehlen, alle Ihre Anwendungen, die das Braze SDK verwenden, zu deinstallieren oder sich davon abzumelden, um die Erfassung weiterer Daten über die betroffene Person zu beenden.

Für Kund:innen, die ausschließlich BrazeAI Decisioning Studio™ nutzen, sollten Sie keine Daten mehr an Decisioning Studio senden.

## Das Recht auf Datenübertragbarkeit {#the-right-to-data-portability}

Das Recht auf Datenübertragbarkeit ermöglicht es betroffenen Personen, ihre personenbezogenen Daten für eigene Zwecke über verschiedene Dienste hinweg zu erhalten und weiterzuverwenden. Die personenbezogenen Daten sollten in einem strukturierten, maschinenlesbaren und gängigen Format bereitgestellt werden.

### Braze-Empfehlung

Ähnlich wie beim Auskunftsrecht können Sie die Braze [REST API]({{site.baseurl}}/api/endpoints/export) verwenden, um die personenbezogenen Daten von Endnutzer:innen zu exportieren und sie der betroffenen Person auf deren Anfrage hin zur Verfügung zu stellen. Wenden Sie sich darüber hinaus mit den relevanten `customer_id`(s) und/oder E-Mail(s) an Ihre:n Account Manager, um eine Kopie aller in BrazeAI Decisioning Studio gespeicherten personenbezogenen Daten anzufordern.

## Das Recht auf Widerspruch {#the-right-to-object}

Betroffene Personen können das Recht haben, Widerspruch einzulegen gegen:

- Verarbeitung auf Grundlage berechtigter Interessen oder der Wahrnehmung einer Aufgabe im öffentlichen Interesse/Ausübung öffentlicher Gewalt (einschließlich Profiling);
- Direktmarketing (einschließlich Profiling); und
- Verarbeitung zu Zwecken der wissenschaftlichen/historischen Forschung und Statistik.

### Braze-Empfehlung

Braze bietet die Möglichkeit, ein Nutzerprofil über unsere [REST APIs]({{site.baseurl}}/api/home) sowie über die [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes)-, [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes)- und [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes)-SDKs als von SMS, E-Mails oder Push-Benachrichtigungen abgemeldet zu markieren. Wenn Sie Widersprüche von betroffenen Personen gegen den Empfang solcher Nachrichten erhalten, können Sie die APIs von Braze verwenden, um diese Endnutzer:innen abzumelden.

Falls dies nicht ausreichend ist, sollte das Endnutzer:innen-Profil auf die gleiche Weise gelöscht werden, wie unter dem „Recht auf Löschung“ beschrieben, um die Verarbeitung personenbezogener Daten von Endnutzer:innen durch Braze zu vermeiden.

## Rechte im Zusammenhang mit automatisierter Entscheidungsfindung und Profiling {#rights-related-to-automated-decision-making-and-profiling}

Einige Datenschutzgesetze verhindern automatisierte Entscheidungsfindung oder Profiling unter bestimmten Umständen oder erlauben es betroffenen Personen, dem zu widersprechen, insbesondere bei Entscheidungen, die „rechtliche Wirkung entfalten oder eine ähnlich erhebliche Auswirkung auf die betroffene Person haben“.

### Braze-Empfehlung

Braze führt keine automatisierten Profiling- oder Entscheidungsprozesse durch, die rechtliche oder vergleichbare Auswirkungen auf betroffene Personen haben. Wenn Sie der Ansicht sind, dass Ihre eigene Nutzung der Braze-Dienste rechtliche oder vergleichbare Auswirkungen hat und Sie einen Widerspruch dagegen erhalten haben, können Sie das Nutzerprofil auf die gleiche Weise löschen wie unter „Recht auf Löschung“ beschrieben.

## Targeting Advertising

Nach einigen US-amerikanischen Datenschutzgesetzen der Bundesstaaten können betroffene Personen der Verwendung ihrer personenbezogenen Daten für Zwecke des Targeted Advertising widersprechen.

### Braze-Empfehlung

Wenn Sie Zielgruppen erstellen, um Ihren betroffenen Personen gezielte Werbung anzuzeigen, sollten Sie sicherstellen, dass Sie alle betroffenen Personen ausgeschlossen haben, die dem Targeted Advertising widersprochen haben – beispielsweise kalifornische Verbraucher:innen, die ihr Recht auf „Do Not Sell or Share“ gemäß dem CCPA ausgeübt haben.

Weitere Informationen zum Erstellen von Zielgruppen für die Synchronisierung mit Drittanbieterplattformen finden Sie unter [Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync).

## Das Recht auf Nichtdiskriminierung {#the-right-to-non-discrimination}

Betroffene Personen haben das Recht, ihre Datenschutzrechte auszuüben, ohne dabei diskriminiert zu werden.

### Braze-Empfehlung

Bei der Nutzung der Braze-Dienste müssen Kund:innen sicherstellen, dass sie betroffene Personen, die ihre Datenschutzrechte ausgeübt haben, nicht diskriminieren. Wir empfehlen beispielsweise, dass betroffene Personen, die ihre Datenschutzrechte ausgeübt haben, nicht in Zielgruppen segmentiert oder anderweitig so angesprochen werden, dass dies zu einer Diskriminierung führen könnte.