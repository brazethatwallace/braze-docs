---
nav_title: SAML Just-in-Time-Bereitstellung
article_title: SAML Just-in-Time-Bereitstellung
page_order: 1
page_type: tutorial
description: "Dieser Artikel erklärt, wie Sie die SAML Just-in-Time-Bereitstellung konfigurieren, damit neue Unternehmensnutzer:innen bei ihrer ersten Anmeldung automatisch ein Braze-Konto erstellen können."

---

# SAML Just-in-Time-Bereitstellung

> Die Just-in-Time-Bereitstellung funktioniert mit [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/) und ermöglicht es neuen Unternehmensnutzer:innen, bei ihrer ersten Anmeldung automatisch ein Braze-Konto zu erstellen. Dadurch entfällt für Administrator:innen die Notwendigkeit, manuell ein Konto für neue Unternehmensnutzer:innen anzulegen, Berechtigungen auszuwählen, sie einem Workspace zuzuweisen und auf die Aktivierung des Kontos zu warten.

Als Sicherheitsmaßnahme funktioniert die SAML Just-in-Time-Bereitstellung (JITP) nur für Nutzer:innen mit E-Mail-Domains, die bereits in Ihrem Unternehmen vorhanden sind. JITP ist nur für Domains möglich, in denen es bereits mindestens eine:n bestätigte:n Entwickler:in ohne Identitätswechsel im Unternehmen gibt.

Nehmen wir zum Beispiel an, das Konto `jon.smith@decorumsoft.com` kann JITP verwenden, um sich bei Decorumsoft anzumelden. Das Konto `jane.smith@decorumsoft.com` hat dieselbe Domain und kann ebenfalls für die Bereitstellung zugelassen werden. Wenn Sie jedoch versuchen, JITP mit `jon.smith@decorumsoft.eu` zu verwenden, wird die Bereitstellung nicht zugelassen, da es kein `decorumsoft.eu`-Konto im Braze-Dashboard von Decorumsoft gibt.

Um eine Ausnahme für ein Unternehmen zu beantragen, kontaktieren Sie den [Support]({{site.baseurl}}/braze_support/).

## Voraussetzungen

SAML JITP erfordert, dass SAML SSO eingerichtet und integriert ist. Es ist nicht mit Google SSO kompatibel und wird nur für Identity-Provider-initiierte (IdP-initiierte) Anmelde-Workflows unterstützt.

## SAML Just-in-Time-Bereitstellung (JITP) einrichten

Lassen Sie eine:n Braze-Administrator:in die folgenden Schritte ausführen:

1. Navigieren Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen**.
2. Schalten Sie im Abschnitt **SAML SSO** die Option **Automatic user provisioning** ein.
3. Wählen Sie einen Standard-Workspace aus, dem neue Unternehmensnutzer:innen hinzugefügt werden sollen.
4. Wählen Sie das Standard-Berechtigungsset aus, das neuen Unternehmensnutzer:innen zugewiesen werden soll. Informationen zum Erstellen eines Berechtigungssets finden Sie unter [Nutzerberechtigungen festlegen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/).
6. Wählen Sie **Änderungen speichern** am unteren Rand der Seite.
7. Fügen Sie in den Einstellungen Ihres SSO-Anbieters alle Nutzer:innen, die Zugriff auf Braze benötigen, zum Verzeichnis Ihres SSO-Anbieters hinzu.
8. Weisen Sie die Nutzer:innen an, für ihre erste Anmeldung über Ihr IdP-Portal auf Braze zuzugreifen. Danach wird der SAML-Single-Sign-on-Button für zukünftige Anmeldungen angezeigt.

## Häufig gestellte Fragen

### Wie deaktiviere ich SAML JITP?

Nachdem Sie JITP eingerichtet haben, müssen Sie den [Support kontaktieren]({{site.baseurl}}/braze_support/), um es deaktivieren zu lassen.

## Fehlerbehebung

### Single-Sign-on-Button wird bei Microsoft Entra ID nicht angezeigt

Das Feld **Sign-On URL** im Formular **Basic SAML Configuration** von Microsoft Entra für Braze kann dazu führen, dass Nutzer:innen bei der IdP-initiierten Anmeldung nur eine Passwort-Option sehen und keinen SSO-Button. Um dieses Problem zu vermeiden, lassen Sie das Feld **Sign-On URL** leer, wenn Sie Braze in Ihrem Microsoft Entra Admin Center konfigurieren.