---
nav_title: eduMe
article_title: eduMe
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und eduMe, einem mobilbasierten Trainingstool, mit dem Sie Connected-Content von Braze nutzen können, um Ihren Nutzer:innen in Ihren Braze-Campaigns Zugang zu eduMe-Kursen und -Lektionen zu geben."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com) ist ein mobilbasiertes Trainingstool, das Ihren Mitarbeitenden das Wissen vermittelt, das sie für den Erfolg benötigen – wann immer sie es brauchen und wo immer sie sind.

_Diese Integration wird von eduMe verwaltet._

## Über die Integration {#about-the-integration}

Die Integration von Braze und eduMe nutzt [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) von Braze, um Ihren Nutzer:innen in Ihren Braze-Campaigns Zugang zu eduMe-Kursen und -Lektionen zu geben. Der Fortschritt von Einzelpersonen und Gruppen kann dann über die eduMe-Berichtsfunktionalität nachverfolgt werden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| eduMe-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein eduMe-Konto. |
| eduMe-API-Schlüssel | Sie müssen einen API-Schlüssel bei Ihrer eduMe-Kontaktperson für Kundenerfolg anfragen. Dieser Schlüssel wird in Ihrem Braze-Connected-Content-Aufruf verwendet. |
| eduMe-Link-Signiergeheimnis | Sie müssen Ihre Kontaktperson für Kundenerfolg bei eduMe bitten, ein Link-Signiergeheimnis für Ihre Organisation einzurichten. Dieses Geheimnis wird verwendet, um nahtlose Links in Connected-Content zu ermöglichen. Sie müssen mit diesem Geheimnis nichts weiter tun. |
| eduMe-Gruppen- und Inhalts-IDs | Diese Bezeichner werden benötigt, um Ihre Connected-Content-Aufrufe einzurichten. Wenden Sie sich an Ihre eduMe-Kontaktperson für Kundenerfolg, wenn Sie Hilfe bei der Beschaffung dieser Bezeichner benötigen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Erstellen Sie Ihren Connected-Content-Aufruf {#create-your-connected-content-call}

Um einer Nutzer:in Zugang zu einem Kurs, einer Lektion oder einer eNPS-Umfrage zu geben und den Fortschritt anhand Ihrer internen Nutzer-ID in eduMe zu verfolgen, folgen Sie dem API-Aufruf in diesem Beispiel:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Ersetzen Sie `YOUR-EDUME-API-KEY` durch Ihren eduMe-API-Schlüssel.<br><br>
2. Ersetzen Sie `EDUME-CONTENT-LINK-AND-CONTENT-ID` durch den entsprechenden String für den Inhaltslink und den Bezeichner für das Modul, die Lektion oder die Umfrage. Diese Bezeichner finden Sie in Ihrem eduMe-Konto.
  - Kurs: `getCourseLink?moduleId=12087`
  - Lektion: `getLessonLink?lessonId=25805`
  - eNPS-Umfrage: `getSurveyLink?surveyId=654`<br><br>
3. Nutzer:innen, die über diesen Link zu eduMe gelangen, werden einem eduMe-Team oder einer Gruppe Ihrer Wahl hinzugefügt. Ersetzen Sie `groupId` durch die entsprechende Team-ID oder eduMe-Gruppen-ID. Normalerweise verwenden Sie die Team-ID, außer bei Kursen, die eine Einschreibung erfordern – in diesem Fall sollten Sie die Gruppen-ID verwenden.<br><br>
4. Fügen Sie ein geeignetes Feld ein, um das Feld `externalUserId` zuzuordnen. Das Beispiel für den Connected-Content-Aufruf verwendet `driver_id`, wobei Ihr Feld wahrscheinlich anders lauten wird. Diese ID ist in eduMe-Berichten verfügbar, sodass Sie sie mit Ihren Systemen korrelieren können.<br><br>
5. Passen Sie abschließend Ihre Nachricht nach Bedarf an und testen Sie sie. Wir empfehlen Ihnen, mindestens eine Testnachricht zu versenden, auf die eduMe-Inhalte zuzugreifen, die Lektion oder den Kurs abzuschließen und zu überprüfen, ob die eduMe-Analytics korrekt aufgezeichnet werden.