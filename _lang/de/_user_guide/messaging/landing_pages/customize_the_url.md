---
nav_title: URL anpassen
article_title: URL anpassen
description: "Erfahren Sie, wie Sie Ihre Landing-Page-URLs mit der Marke Ihres Unternehmens anpassen, indem Sie Ihre Domain mit Ihrem Braze-Workspace verbinden."
page_order: 1
---

# Landing-Page-URLs anpassen {#customize-landing-page-urls}

> Erfahren Sie, wie Sie Ihre Landing-Page-URLs mit der Marke Ihres Unternehmens anpassen, indem Sie Ihre Domain mit Ihrem Braze-Workspace verbinden.

## So funktioniert es {#how-it-works}

Wenn Sie [Ihre Domain mit Braze verbinden](#connect-your-domain-to-braze), wird sie als Standard-Domain für alle Landing-Pages verwendet. Wenn Sie beispielsweise die Subdomain `forms.example.com` verbinden, lauten Ihre Landing-Page-URLs nun `forms.example.com/holiday-sale`.

Die Anzahl der angepassten Domains, die Sie mit Ihrem Braze-Konto verbinden können, hängt von Ihrer [Planstufe]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers) ab. Um Ihr Limit zu erhöhen, kontaktieren Sie Ihren Braze Account Manager:in.

## Ihre Domain mit Braze verbinden {#connect-your-domain-to-braze}

Um eine Domain mit Ihrem Braze-Konto zu verbinden, lassen Sie eine:n Administrator:in die folgenden Schritte ausführen.

1. Gehen Sie zu **Einstellungen** > **Landing-Page-Einstellungen**.
2. Geben Sie die Domain ein, die Sie verbinden möchten, und wählen Sie **Senden**. Zum Beispiel `forms.example.com`.
3. Kopieren Sie die **TXT**- und **CNAME**-Einträge und fügen Sie sie in die DNS-Einstellungen Ihres Domain-Anbieters ein.
4. Kehren Sie zum Braze-Dashboard zurück, um die Verbindung zu überprüfen.

![Seite „Landing-Page-Einstellungen“ mit einem TXT- und zwei CNAME-Einträgen, die mit ihren jeweiligen Namen und Werten aufgelistet sind.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Je nach Domain-Anbieter kann die Verbindung bis zu 48 Stunden dauern. Wenn der Vorgang abgeschlossen ist, verwenden wir Ihre angepasste Domain für Ihre Landing-Pages im Braze-Dashboard.
{% endalert %}

### SSL-Zertifikat einrichten {#ssl-certificate-setup}

Braze verwendet Cloudflare, um automatisch SSL-Zertifikate für Ihre angepasste Domain über eine [ACME DNS-01-Challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) bereitzustellen. Diese kontinuierliche Validierungsmethode wird durch einen der CNAME-Einträge ermöglicht, die Sie während der Einrichtung angegeben haben, und erlaubt es der Zertifizierungsstelle (LetsEncrypt), den Besitz Ihrer Domain über DNS-Einträge zu überprüfen, ohne dass Braze Ihre Domain besitzen muss.

## Ihre Domain entfernen {#remove-your-domain}

Wenn Sie Braze-Administrator:in sind, können Sie eine zuvor konfigurierte Domain entfernen, indem Sie die folgenden Schritte ausführen:

1. Gehen Sie zu **Einstellungen** > **Landing-Page-Einstellungen**.
2. Wählen Sie **Angepasste Domain entfernen**.
3. Bestätigen Sie das Entfernen der Domain.
4. Entfernen Sie die aufgelisteten DNS-Einträge aus Ihren Domain-Einstellungen.

{% alert important %}
Wenn Sie eine angepasste Domain entfernen, ist diese URL nicht mehr gültig. Alle Landing-Pages, die diese Domain verwendet haben, werden automatisch auf die von Braze festgelegte Standard-Domain zurückgesetzt.
{% endalert %}

## Ihre Domain migrieren {#migrate-your-domain}

So migrieren Sie eine angepasste Domain in einen anderen Workspace:

1. Entfernen Sie die angepasste Domain.
2. Erstellen Sie eine neue angepasste Domain im gewünschten Workspace.
3. Konfigurieren Sie die angepasste Domain mit den neuen DNS-Einträgen neu. Beachten Sie, dass Ihre Subdomain während dieses Vorgangs nicht verfügbar sein wird.

## DNS-Ressourcen {#dns-resources}

{% multi_lang_include channels/email/dns_records.md %}

## Fehlerbehebung {#troubleshooting}

### Meine Domain-Verbindung ist fehlgeschlagen {#my-domain-connection-failed}

Überprüfen Sie, ob Ihre Domain korrekt eingegeben wurde und mit dem übereinstimmt, was Sie von Ihrem Domain-Anbieter-Konto an Braze übermittelt haben. Wenn sie korrekt ist und übereinstimmt, überprüfen Sie die von Braze bereitgestellten TXT- und CNAME-Einträge. Sie sollten mit den Einträgen übereinstimmen, die Sie in Ihrem Domain-Anbieter-Konto eingegeben haben.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich verschachtelte Subdomains für meine angepasste Domain verwenden? {#can-i-use-nested-subdomains-for-my-custom-domain}

Ja, Sie können verschachtelte Subdomains für Ihre Landing-Pages verwenden. Zum Beispiel werden `forms.braze.com`, `pages.forms.braze.com` oder tiefere Ebenen alle unterstützt. Die einzige Voraussetzung ist, dass Sie keine Apex-Domain (wie `braze.com`) verwenden können, da Braze CNAME-Einträge für die Verbindung nutzt.

### Kann ich mehrere Subdomains mit meinem Workspace verbinden oder eine Subdomain mit mehreren Workspaces verbinden? {#can-i-connect-multiple-subdomains-to-my-workspace-or-connect-one-subdomain-to-multiple-workspaces}

Nein, derzeit können Sie nur eine Subdomain mit einem Workspace verbinden.

### Kann ich dieselbe Subdomain verwenden, die ich derzeit für meine Hauptwebsite oder meine Versand-Domain nutze? {#can-i-use-the-same-subdomain-that-i-currently-use-for-my-main-website-or-my-sending-domain}

Nein, Sie können keine Subdomains verwenden, die bereits in Gebrauch sind. Obwohl diese Subdomains gültig sind, können sie nicht für Landing-Pages verwendet werden, wenn sie bereits anderen Zwecken zugewiesen sind oder DNS-Einträge haben, die mit den erforderlichen CNAME-Einträgen in Konflikt stehen.

### Warum bleibt meine angepasste Domain bei „Verbindung wird hergestellt“ hängen, obwohl die DNS-Einträge gültig sind? {#why-is-my-custom-domain-stuck-on-connecting-despite-valid-dns-records}

Wenn Ihre angepasste Domain alle DNS-Einträge als „Verbunden“ anzeigt, der Domain-Status aber länger als vier Stunden auf „Verbindung wird hergestellt“ bleibt, verwendet Ihre Organisation möglicherweise CAA-Einträge (Certificate Authority Authorization) oder Cloudflare-Zone-Holds, die Braze daran hindern, Ihre Seite abzusichern.

#### CAA-Einträge {#caa-records}

CAA-Einträge beschränken, welche Zertifizierungsstellen SSL-Zertifikate für Ihre Domain ausstellen dürfen. Wenn Ihre CAA-Einträge LetsEncrypt nicht enthalten, kann Braze (über Cloudflare) das erforderliche SSL-Zertifikat nicht ausstellen.

Um dies zu beheben, bitten Sie Ihr IT-Team, einen CAA-Eintrag zu Ihrer Subdomain mit den folgenden Werten hinzuzufügen:
- **Eintragstyp:** CAA
- **Wert:** `0 issue "letsencrypt.org"`

Weitere Informationen finden Sie in der [CAA-Dokumentation von LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Cloudflare-Zone-Holds {#cloudflare-zone-holds}

Wenn Ihre Organisation Cloudflare verwendet, verhindert möglicherweise ein Zone-Hold-Sicherheitsfeature, dass Braze Ihre angepasste Domain erstellen kann.

Um dies zu beheben, bitten Sie Ihr IT-Team, den Zone-Hold vorübergehend aufzuheben. Weitere Informationen finden Sie in der [Zone-Hold-Dokumentation von Cloudflare](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Validierungsprozess neu starten {#restarting-the-validation-process}

Nachdem Sie eines der beiden Probleme behoben haben, löschen Sie Ihre angepasste Domain im Braze-Dashboard und erstellen Sie sie neu, um den Validierungsprozess neu zu starten.

### Kann ich einen Reverse-Proxy verwenden, um Landing-Pages unter meiner Hauptdomain oder einem Unterverzeichnis bereitzustellen? {#can-i-use-a-reverse-proxy-to-serve-landing-pages-under-my-main-domain-or-a-subdirectory}

Nein, Landing-Page-URL-Liquid-Tags funktionieren mit Reverse-Proxys nicht korrekt.