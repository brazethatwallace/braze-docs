---
nav_title: Verifizierte Domains
article_title: Verifizierte Domains
page_order: 0
page_type: tutorial
channel: email
description: "Dieser Artikel beschreibt, wie Sie verifizierte Domains einrichten, damit Braze die DNS-Verwaltung für den E-Mail-Versand und das HTTPS-Klick-Tracking übernehmen kann."
toc_headers: h2
---

# Verifizierte Domains {#verified-domains}

> Mit verifizierten Domains können Sie Braze die Kontrolle über eine bestimmte Subdomain übertragen, um die E-Mail-Einrichtung und das HTTPS-Tracking zu automatisieren. Durch DNS-Domain-Delegation verwaltet Braze die DNS-Einträge, die für den E-Mail-Versand und das Klick-Tracking erforderlich sind. Wenn Ihre Subdomain beispielsweise „mail.example.com“ lautet, können Sie sie an Braze delegieren, um Ihre Versand- und Tracking-Domains einzurichten.

{% alert important %}
Verifizierte Domains unterstützen derzeit nur Amazon SES. Wenn Sie SendGrid oder SparkPost verwenden, ist dieses Feature nicht verfügbar.<br><br>Verifizierte Domains werden nur für E-Mail unterstützt. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

## Vorteile {#benefits}

- Schnelleres Onboarding: Die Automatisierung dieser Schritte verkürzt die Onboarding-Zeit für E-Mail.
- Weniger Koordinationsaufwand: Sie müssen nicht mehr mit dem Braze-Support für Domain-Konfigurationsaufgaben zusammenarbeiten, was Sie einer vollständig selbstverwalteten Erfahrung näherbringt.
- Automatisierte SSL-Verwaltung: Braze übernimmt die Erstellung und Erneuerung von SSL-Zertifikaten, wodurch ein häufiger Fehlerpunkt und manueller Aufwand entfallen. Die Absicherung Ihrer Links mit SSL ist eine bewährte Standardpraxis – Empfänger:innen vertrauen gesicherten Links eher, und die zusätzliche Authentifizierungsebene schützt Ihre Daten.
- Weniger Konfigurationsfehler: Geführte Onboarding-Abläufe und automatisierte Validierung ersetzen die fehleranfällige manuelle DNS-Einrichtung, sodass Sie weniger Möglichkeiten haben, Einträge falsch zu konfigurieren und die E-Mail-Einrichtung zu beeinträchtigen.
- Proaktive Überwachung: Braze überwacht Ihre DNS-Einträge und benachrichtigt Sie, wenn Probleme erkannt werden, anstatt auf das Auftreten von Fehlern zu warten.

## Hinweise {#considerations}

Bevor Sie beginnen, beachten Sie die folgenden Details:

- Wählen Sie eine dedizierte Subdomain. Nach Abschluss der Domain-Delegation verwaltet Braze alle DNS-Einträge für diese Subdomain. Braze empfiehlt, eine Subdomain statt der übergeordneten Domain Ihrer Marke zu delegieren, da Sie bei der Delegation einer übergeordneten Domain die Sichtbarkeit und Kontrolle darüber verlieren. Wenn Sie eine übergeordnete Domain verwenden möchten, nutzen Sie eine, die nirgendwo anders verwendet wird.
- NS-Delegation (Nameserver) ist erforderlich, damit Braze die DNS-Einträge Ihrer Subdomain wie SPF, DKIM und HTTPS-Tracking verwalten kann, ohne dass Sie jeden einzelnen manuell konfigurieren müssen.

{% alert note %}
CNAME-Delegation wird nicht unterstützt. {% multi_lang_include product_feedback_cta.md context="gap" feature="CNAME delegation for verified domains" %}
{% endalert %}

- Planen Sie eine Versand-Subdomain mit mindestens drei Ebenen ein. Da Braze eine Subdomain unter Ihrer delegierten Domain erstellt (z. B. „mail.example.com“), muss Ihre Versand-Domain mindestens drei Ebenen tief sein. Ein Beispiel ist „e.mail.example.com“.
- Braze verwaltet Ihre DNS-Einträge. Nach Abschluss der Delegation ist Braze für die DNS-Einträge der delegierten Subdomain verantwortlich. Ändern Sie diese Einträge nicht eigenständig, da dies Probleme mit Ihrem E-Mail-Versand verursachen kann.
- Die Berechtigung „Edit Domain Settings“ ist erforderlich, um verifizierte Domains einzurichten.

## Schritt 1: Verifizierte Domain hinzufügen {#step-1-add-the-verified-domain}

1. Gehen Sie zu **Einstellungen** > **Verifizierte Domains** > **Verifizierte Domain hinzufügen**.
2. Geben Sie die Subdomain und den Stammnamen ein. Wenn Sie beispielsweise die Subdomain „mail.example.com“ an Braze delegieren, ist der Stammname „example.com“ und die Subdomain „mail“.
3. Bestätigen Sie, dass die gewählte Subdomain nicht anderweitig verwendet wird und keine widersprüchlichen DNS-Einträge aufweist.
4. Wählen Sie **Hinzufügen** aus, um die TXT- und NS-Einträge zu erhalten.

## Schritt 2: DNS-Einträge konfigurieren {#step-2-configure-dns-records}

Nach dem Einreichen der verifizierten Domain generiert Braze die erforderlichen DNS-Einträge, die Sie bei Ihrem DNS-Anbieter hinzufügen müssen. Dieser Schritt erfordert möglicherweise eine Abstimmung mit Ihrem IT- oder DNS-Team. Sie haben 30 Tage Zeit, bis die Einträge verifiziert werden müssen, bevor sie ablaufen. Danach müssen Sie die Einrichtung erneut durchführen.

{% alert tip %}
Bestätigen Sie mit dem Befehl `dig`, dass alle vier NS-Einträge explizit vorhanden sind, und stellen Sie sicher, dass die Domain im Dashboard validiert wird, bevor Sie die Einrichtung als abgeschlossen betrachten. Die DNS-Verifizierung läuft nach 30 Tagen ab.
{% endalert %}

## Schritt 3: Domain verifizieren {#step-3-verify-the-domain}

Nachdem die DNS-Einträge propagiert wurden, überprüft Braze innerhalb von 24 Stunden, ob die Einträge vorhanden und korrekt konfiguriert sind. Bei erfolgreicher Verifizierung:

- Der Domain-Status wird auf **Verifiziert** aktualisiert.
- Braze sendet eine E-Mail, die Sie darüber informiert, dass die Domain bereit ist.
- Die Domain wird in der Liste **Verifizierte Domains** als aktiv angezeigt.

Nachdem eine Subdomain erfolgreich delegiert wurde, erstellen Sie E-Mail-Domains wie Ihre Versand- und Tracking-Domains, indem Sie zu **Benutzerdefinierte Domain hinzufügen** gehen. Anschließend werden Sie zur Seite **Absenderverifizierung** weitergeleitet, um Ihre Einrichtung abzuschließen. Detaillierte Schritte finden Sie unter [E-Mail-Self-Service]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve).