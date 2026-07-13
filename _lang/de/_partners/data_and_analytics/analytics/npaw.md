---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und NPAW, einer intelligenten Analytics-Plattform, die umsetzbare Insights für führende Online-Medienschaffende liefert."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), auch bekannt als _Nice People at Work_, ist eine intelligente Analytics-Plattform, die umsetzbare Insights für führende Online-Medienschaffende liefert. Mit der YOUBORA-Tool-Suite von NPAW können Braze-Kund:innen jetzt eine prädiktive und robuste KI nutzen, um das Kundenverhalten besser zu verstehen und das Engagement plattformübergreifend zu fördern.

# Voraussetzungen {#prerequisites}

| Anforderung   | Herkunft | Beschreibung |
| --------------|------|-------------|
| YOUBORA-API-Schlüssel | [YOUBORA-Einstellungen](https://youbora.nicepeopleatwork.com/users/login) | Ein API-Schlüssel, der bei der Registrierung generiert wird und unter **Settings** zu finden ist |
| ID | [Braze-Einstellungen](https://dashboard.braze.com/sign_in) | YOUBORA bietet Ihnen die Möglichkeit, die Software mit Braze über eine ***Braze-ID***, eine ***externe Nutzer-ID*** oder eine ***Nutzer-ID*** zu verknüpfen |
| Endpunkt | [Braze-Einstellungen](https://dashboard.braze.com/sign_in) | Ein vollständig anpassbarer URL-Endpunkt, der über Ihr Braze-Dashboard konfiguriert werden kann. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

# Analytics-Integration

## Zugriff auf die Integrationsseite {#accessing-the-integrations-page}

Nachdem Sie sich bei Ihrem YOUBORA-Tool-Suite-Konto angemeldet haben, navigieren Sie zur Integrationsseite, indem Sie die Option **Integrations** aus dem Dropdown-Kontomenü auswählen.

![NPAW-Dropdown-Menü]({% image_buster /assets/img/npaw_dropdown.png %})

## Konfigurieren Ihrer Integration {#configuring-your-integration}

Sobald Sie die Integrationsseite aufgerufen haben, scrollen Sie nach unten, bis Sie die Integrationsoption **Braze** sehen. Nachdem Sie darauf geklickt haben, wird diese erweitert und bietet Ihnen eine Reihe erforderlicher Parameter zum Ausfüllen an:

![NPAW-Integration]({% image_buster /assets/img/npaw_integration.png %})

Füllen Sie die Details mit den entsprechenden Informationen aus dem Abschnitt „Voraussetzungen“ aus, wobei:
* **Connector Name** ein **alphanumerischer** String ist, der in Zukunft verwendet wird, um auf diese Integration zu verweisen. Dieser Wert kann beliebig gewählt werden, solange er **nur** Buchstaben und Zahlen enthält.
* **User ID** die ID ist, die Sie zuvor gewählt haben, um Ihre YOUBORA-Software mit Ihrem Braze-Konto zu verknüpfen. Wenn Sie beispielsweise die Verknüpfung über Ihre **Braze ID** vornehmen möchten, wählen Sie **Braze ID** aus dem Dropdown-Menü aus, um den Wert dem entsprechenden Feld zuzuweisen.
* **API Key** Ihr YOUBORA-Tool-Suite-API-Schlüssel ist, den Sie zuvor im Bereich **API** unter **Settings** gefunden haben.
* **Endpoint** der anpassbare URL-Endpunkt ist, der zuvor in Ihrem Braze-Dashboard eingerichtet wurde.

Sobald alle Felder ausgefüllt sind, klicken Sie einfach auf den Button **Connect**, um eine Verbindung herzustellen und die Änderungen zu speichern.

## Verwendung Ihrer NPAW-Integration {#using-your-npaw-integration}

Wenn Sie die Integration mit Braze fertig konfiguriert haben, navigieren Sie zum Produkt **Users** und wählen Sie den **Sample Manager** innerhalb des **Sections Manager** aus.

Nachdem Sie ein Sample im **Sample Manager** erstellt haben, können Sie auf das Dreipunkt-Symbol im Zeilenaktionsmenü klicken, um alle Nutzer:innen Ihres Samples an Braze zu senden.

![NPAW Sample Manager]({% image_buster /assets/img/npaw_sample_manager.png %})

Nachdem Sie Ihre Nutzer:innen an Braze gesendet haben, können Sie jetzt aktiv werden und Campaigns auf Nutzersegmente ausrichten, um inaktive Nutzer:innen erneut anzusprechen, Ihre treuesten Nutzer:innen zu kontaktieren oder eine beliebige Aktion für ein beliebiges Nutzersegment durchzuführen!