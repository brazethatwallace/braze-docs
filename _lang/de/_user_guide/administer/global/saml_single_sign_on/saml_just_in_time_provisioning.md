---
nav_title: SAML Just-in-Time-Bereitstellung
article_title: SAML Just-in-Time-Bereitstellung
page_order: 1
page_type: tutorial
description: "Dieser Artikel erklärt, wie Sie die SAML Just-in-Time-Bereitstellung konfigurieren, damit neue Unternehmensnutzer:innen bei ihrer ersten Anmeldung automatisch ein Braze-Konto erstellen können."
---

# SAML Just-in-Time-Bereitstellung {#saml-just-in-time-provisioning}

> Die Just-in-Time-Bereitstellung funktioniert mit [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) und ermöglicht es neuen Unternehmensnutzer:innen, bei ihrer ersten Anmeldung automatisch ein Braze-Konto zu erstellen. Dadurch entfällt für Administrator:innen die Notwendigkeit, manuell ein Konto für neue Unternehmensnutzer:innen anzulegen, Berechtigungen auszuwählen, sie einem Workspace zuzuweisen und auf die Aktivierung des Kontos zu warten.

Als Sicherheitsmaßnahme funktioniert die SAML Just-in-Time-Bereitstellung (JITP) nur für Nutzer:innen mit E-Mail-Domains, die bereits in Ihrem Unternehmen vorhanden sind. JITP ist nur für Domains möglich, in denen es bereits mindestens eine:n bestätigte:n Entwickler:in ohne Identitätswechsel im Unternehmen gibt.

Nehmen wir zum Beispiel an, das Konto `jon.smith@decorumsoft.com` kann JITP verwenden, um sich bei Decorumsoft anzumelden. Das Konto `jane.smith@decorumsoft.com` hat dieselbe Domain und kann ebenfalls für die Bereitstellung zugelassen werden. Wenn Sie jedoch versuchen, JITP mit `jon.smith@decorumsoft.eu` zu verwenden, wird die Bereitstellung nicht zugelassen, da es kein `decorumsoft.eu`-Konto im Braze-Dashboard von Decorumsoft gibt.

Um eine Ausnahme für ein Unternehmen zu beantragen, kontaktieren Sie den [Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Voraussetzungen {#prerequisites}

SAML JITP erfordert, dass SAML SSO eingerichtet und integriert ist. Es ist nicht mit Google SSO kompatibel und wird nur für Identity-Provider-initiierte (IdP-initiierte) Anmeldeworkflows unterstützt.

| Anforderung | Details |
|---|---|
| SAML SSO | Konfiguriert und getestet, bevor JITP aktiviert wird. Siehe [SAML SSO einrichten]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
| IdP-initiierte Anmeldung | Nutzer:innen müssen sich bei der ersten Anmeldung über Ihr IdP-Portal anmelden. Eine ausschließlich SP-initiierte Anmeldung erstellt keine neuen Nutzer:innen. |
| E-Mail-Domain | Die E-Mail-Domain der Nutzer:innen muss bereits in Ihrem Unternehmen vorhanden sein (mindestens eine bestätigte Entwickler:in ohne Identitätswechsel mit dieser Domain). |
| Unternehmensfreischaltung | Braze muss das Feature `saml_jit_provisioning` für Ihr Unternehmen aktivieren, bevor der Umschalter **Automatic user provisioning** angezeigt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JITP-Voraussetzungen" }

{% alert important %}
SAML Just-in-Time-Provisioning muss von Braze für Ihr Unternehmen aktiviert werden. Wenden Sie sich an Ihren Account Manager oder den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support), wenn der Umschalter **Automatic user provisioning** nicht verfügbar ist.
{% endalert %}

## Funktionsweise von JITP {#how-jitp-works}

Wenn JITP aktiviert ist und sich eine neue Nutzer:in zum ersten Mal über Ihren IdP anmeldet:

1. Braze validiert die SAML-Assertion und prüft, ob die E-Mail-Domain der Nutzer:in für JITP zulässig ist.
2. Braze erstellt ein Dashboard-Nutzerkonto mit der E-Mail aus der SAML-Assertion.
3. Braze weist den Standard-Workspace und die in den **Sicherheitseinstellungen** konfigurierten Standardberechtigungen zu.
4. Die Nutzer:in kann sofort auf Braze zugreifen, ohne dass eine separate Einladung oder ein Aktivierungsschritt erforderlich ist.

JITP aktualisiert keine Berechtigungen für bestehende Nutzer:innen. Es erstellt nur Konten für Nutzer:innen, die in Ihrem Unternehmen noch nicht vorhanden sind.

## Einrichtung der SAML-Just-in-Time-Bereitstellung (JITP) {#setting-up-saml-just-in-time-provisioning-jitp}

Lassen Sie eine:n Braze-Administrator:in die folgenden Schritte ausführen:

1. Navigieren Sie zu **Einstellungen** > **Unternehmenseinstellungen** > **Administratoreinstellungen** > **Sicherheitseinstellungen**.
2. Schalten Sie im Abschnitt **SAML SSO** die Option **Automatische Nutzer:innenbereitstellung** ein.
3. Wählen Sie einen Standard-Workspace aus, dem neue Unternehmensnutzer:innen hinzugefügt werden sollen.
4. Wählen Sie das Standard-Berechtigungsset aus, das diesen neuen Unternehmensnutzer:innen zugewiesen werden soll. Informationen zum Erstellen eines Berechtigungssets finden Sie unter [Nutzer:innenberechtigungen festlegen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

{% alert note %}
Wenn Ihr Unternehmen granulare Berechtigungen verwendet, überprüfen Sie das Standard-Berechtigungsset nach der Migration, um sicherzustellen, dass neue JITP-Nutzer:innen den beabsichtigten Zugriff erhalten.
{% endalert %}

{: start="5"}
5. Wählen Sie **Änderungen speichern**.
6. Fügen Sie in den Einstellungen Ihres SSO-Anbieters alle Nutzer:innen, die Braze-Zugriff benötigen, zum Verzeichnis Ihres SSO-Anbieters hinzu.
7. Weisen Sie die Nutzer:innen an, für ihre erste Anmeldung über Ihr IdP-Portal auf Braze zuzugreifen. Danach wird der SAML-Single-Sign-on-Button für zukünftige Anmeldungen angezeigt.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie deaktiviere ich SAML JITP? {#how-do-i-disable-saml-jitp}

Nachdem Sie JITP eingerichtet haben, müssen Sie [den Support kontaktieren]({{site.baseurl}}/user_guide/administer/personal/braze_support), um es deaktivieren zu lassen.

### Kann JITP verschiedenen Nutzer:innen unterschiedliche Berechtigungen zuweisen? {#can-jitp-assign-different-permissions-per-user}

Nein. Alle über JITP erstellten Nutzer:innen erhalten den Standard-Workspace und die Berechtigungen, die in den **Sicherheitseinstellungen** konfiguriert sind. Um unterschiedliche Zugriffsrechte zuzuweisen, erstellen Sie Nutzer:innen manuell oder verwenden Sie die [automatisierte Nutzerbereitstellung über SCIM]({{site.baseurl}}/scim/automated_user_provisioning).

### Funktioniert JITP mit SP-initiierter Anmeldung? {#does-jitp-work-with-sp-initiated-login}

Nein. JITP wird nur bei IdP-initiierter Anmeldung ausgeführt, wenn Nutzer:innen sich über Ihr Identity-Provider-Portal anmelden.

## Fehlerbehebung {#troubleshooting}

### Nutzer:in wurde bei der ersten SSO-Anmeldung nicht bereitgestellt {#user-was-not-provisioned-on-first-sso-sign-in}

Überprüfen Sie Folgendes:

- JITP ist aktiviert und in den **Sicherheitseinstellungen** gespeichert.
- Die/der Nutzer:in hat sich über das IdP-Portal angemeldet (IdP-initiiert), nicht nur über die Braze-Anmeldeseite.
- Die E-Mail-Domain der/des Nutzer:in existiert bereits in Ihrem Unternehmen.
- Die SAML-Assertion enthält ein gültiges `email`-Attribut, das mit der Adresse übereinstimmt, mit der sich die/der Nutzer:in anmeldet.

### Single-Sign-on-Button wird bei Microsoft Entra ID nicht angezeigt {#single-sign-on-button-doesnt-appear-with-microsoft-entra-id}

Das Feld **Sign-On URL** im Formular **Basic SAML Configuration** von Microsoft Entra für Braze kann dazu führen, dass Nutzer:innen bei einer IdP-initiierten Anmeldung nur eine Passwort-Option sehen und keinen SSO-Button. Um dieses Problem zu vermeiden, lassen Sie das Feld **Sign-On URL** leer, wenn Sie Braze in Ihrem Microsoft Entra Admin Center konfigurieren.