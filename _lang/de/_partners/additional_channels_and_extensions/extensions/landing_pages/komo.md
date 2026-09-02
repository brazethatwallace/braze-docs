---
nav_title: Komo
article_title: Komo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Komo, einer Customer-Engagement-Plattform, die auf Gamification, interaktive Inhalte, Wettbewerbe, Prämien und Loyalität spezialisiert ist. Durch diese Integration können First-Party-Daten und Zero-Party-Daten, die in Komo erfasst wurden, in Braze veröffentlicht werden."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) ist eine Customer-Engagement-Plattform, die sich auf Gamification, interaktive Inhalte, Wettbewerbe, Prämien und Loyalität spezialisiert hat.

_Diese Integration wird von Komo gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Komo ermöglicht es Ihnen, First-Party- und Zero-Party-Daten über Komo Engagement Hubs zu sammeln. Diese Hubs sind dynamische Microsites, die interaktive Inhalte und Gamification-Features bieten. Die über diese Hubs gesammelten Nutzerdaten werden dann an die Braze-API übermittelt.

{% multi_lang_include partners/extensions/landing_pages/komo_integration_bullets.md %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Komo-Konto | Sie benötigen ein aktives Komo-Konto, um diese Partnerschaft nutzen zu können. Besuchen Sie [Komo](https://komo.tech/), um jetzt eine Testversion zu starten. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab.<br><br>Zum Beispiel sollte er in etwa so aussehen: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

{% tabs local %}
{% tab Datenerfassung – Formularübermittlung %}

Wenn Nutzer:innen ein anpassbares Datenerfassungsformular in Komo absenden, werden die in der Braze-Integration zugeordneten Komo-Felder über den `/users/track/`-API-Aufruf an Braze übergeben.

Datenerfassungsformulare befinden sich entweder am Anfang oder am Ende von Cards.

{% endtab %}
{% tab Marktforschung – Demnächst verfügbar %}

Komo ermöglicht es außerdem, Marktforschungsdaten weiterzuleiten, die erfasst werden, wenn Nutzer:innen eine Quizfrage, Umfrage, einen Persönlichkeitstest, Swiper oder Ähnliches beantworten. Diese Daten ermöglichen es Ihnen, das Profil von Nutzer:innen über die in Formularübermittlungen erfassten Daten hinaus zu erweitern.

{% endtab %}
{% endtabs %}

## Integration

### 1. Schritt: Veröffentlichen Sie einen Komo Engagement Hub und eine Karte {#step-1-publish-a-komo-engagement-hub-and-card}

Sie müssen einen Komo Hub mit mindestens einer Karte veröffentlichen, die ein Datenerfassungsformular enthält. Nach der Veröffentlichung können Sie die Nutzererfahrung End-to-End testen und überprüfen, ob die Integration korrekt funktioniert.

![Komo Hub.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### 2. Schritt: Hinzufügen der Braze Connected App {#step-2-add-the-braze-connected-app}

Gehen Sie in Komo auf den Tab **Company Settings** und wählen Sie den Abschnitt **Connected Apps** aus.

Suchen Sie dann die Braze-Integration in der Liste und wählen Sie den Button **Connect**, um die Integration zu aktivieren.

![Braze-Integration verbinden.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Braze-Integration verbinden – Schritt 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Konfigurieren Sie die Integration über einen Workflow {#configure-the-integration-via-a-workflow}

Jetzt müssen Sie einen Workflow innerhalb eines Workspace, einer Site oder einer Karte einrichten, um Daten mit Braze zu synchronisieren.

Ob Sie den Workflow auf den gesamten Workspace, eine Site (die viele Karten enthält) oder eine einzelne Karte anwenden, hängt davon ab, ob Sie den Workflow über viele Karten oder Campaigns hinweg Trigger or triggern or triggern möchten.

Nachdem Sie einen Workflow erstellt haben, definieren Sie Ihren Trigger or triggern, suchen Sie im Schrittmenü nach Braze und fügen Sie den Schritt „Track User“ hinzu.

![Einrichtung „Track User“.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

Von hier aus konfigurieren Sie die Ereignisse, Attribute und Abos, die Sie von Komo mit Braze synchronisieren möchten.

![Content-Block-Liste.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Verwendung der Integration {#using-the-integration}

Ihre Integration ist nun eingerichtet und aktiv, und Sie können jeden Durchlauf im Tab „Workflow Runs“ überwachen.