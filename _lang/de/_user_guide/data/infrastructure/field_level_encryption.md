---
nav_title: Verschlüsselung des Bezeichners auf Feldebene
article_title: Verschlüsselung auf Bezeichner-Feldebene
page_order: 2
alias: "/field_level_encryption/"
description: "In diesem Referenzartikel erfahren Sie, wie Sie E-Mail-Adressen verschlüsseln können, um den Austausch von personenbezogenen Daten (PII) in Braze zu minimieren."
page_type: reference
---

# Verschlüsselung des Bezeichners auf Feldebene {#identifier-field-level-encryption}

> Verschlüsseln Sie E-Mail-Adressen, um den Austausch von personenbezogenen Daten (PII) in Braze zu minimieren.

{% multi_lang_include data_activation/field_level_encryption_pii_description.md %}

{% alert important %}
Die Verschlüsselung auf Bezeichner-Feldebene ist als zusätzliches Feature verfügbar. Wenden Sie sich an Ihren Braze Account Manager:in, um mit der Verschlüsselung auf Bezeichner-Feldebene zu beginnen.
{% endalert %}

## So funktioniert es {#how-it-works}

E-Mail-Adressen müssen gehasht und verschlüsselt werden, bevor sie zu Braze hinzugefügt werden. Wenn eine Nachricht gesendet wird, erfolgt ein Aufruf an AWS KMS, um die entschlüsselte E-Mail-Adresse abzurufen. Anschließend wird die gehashte E-Mail-Adresse in die Metadaten eingefügt, damit Zustellungs- und Engagement-Ereignisse mit den ursprünglichen Nutzer:innen verknüpft werden können. Auf diese Weise kann Braze E-Mail-Analytics verfolgen. Braze entfernt alle Klartext-E-Mail-Adressen, die enthalten sind, und speichert die Klartext-E-Mail-Adresse der Nutzer:innen nicht.

## Voraussetzungen {#prerequisites}

Um die Verschlüsselung auf Bezeichner-Feldebene zu verwenden, benötigen Sie Zugriff auf AWS KMS, um E-Mail-Adressen **vor** dem Senden an Braze zu [verschlüsseln](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) und zu [hashen](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html).

Führen Sie die folgenden Schritte aus, um Ihre AWS-Authentifizierungsmethode mit geheimem Schlüssel einzurichten.

1. Um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel abzurufen, [erstellen Sie eine:n IAM-Nutzer:in und eine Administratorgruppe](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) in AWS mit einer Berechtigungsrichtlinie für AWS Key Management Service. Die/der IAM-Nutzer:in muss über die Berechtigungen [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) und [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) verfügen. Weitere Informationen finden Sie unter [AWS KMS-Berechtigungen](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Wählen Sie **Show User Security Credentials** aus, um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel anzuzeigen. Notieren Sie sich diese Zugangsdaten oder wählen Sie den Button **Download Credentials** aus, da Sie diese beim Verbinden Ihrer AWS KMS-Schlüssel eingeben müssen.
3. Sie müssen KMS in den folgenden AWS-Regionen einrichten:
    - **Braze US-Cluster:** `us-east-1`
    - **Braze EU-Cluster:** `eu-central-1`
    - **Braze AU-Cluster:** `ap-southeast-2`
    - **Braze ID-Cluster:** `ap-southeast-3`
    - **Braze JP-Cluster:** `ap-northeast-1`
4. Erstellen Sie in AWS Key Management Service zwei Schlüssel und stellen Sie sicher, dass die/der IAM-Nutzer:in in den Schlüsselverwendungsberechtigungen hinzugefügt ist:
    - **[Verschlüsseln/Entschlüsseln](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Wählen Sie den Schlüsseltyp **Symmetric** und die Schlüsselverwendung **Encrypt and Decrypt** aus.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Wählen Sie den Schlüsseltyp **Symmetric** und die Schlüsselverwendung **Generate and Verify MAC** aus. Die Schlüsselspezifikation sollte **HMAC_256** sein. Notieren Sie sich nach dem Erstellen des Schlüssels die HMAC-Schlüssel-ID, da Sie diese in Braze eingeben müssen.

![Schlüsseleinstellungen konfigurieren mit den ausgewählten Optionen „Symmetric“, „Generate and Verify MAC“ und „HMAC_256“.]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Schritt 1: AWS KMS-Schlüssel verbinden {#step-1-connect-your-aws-kms-keys}

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Verschlüsselung auf Feldebene**. Geben Sie für Ihre AWS KMS-Einstellungen Folgendes ein:

- Zugriffsschlüssel-ID
- Geheimer Zugriffsschlüssel
- HMAC-Schlüsselbezeichner (Schlüssel-ID oder Schlüssel-ARN; kann nach dem Speichern nicht mehr aktualisiert werden)

## Schritt 2: Verschlüsselte Felder auswählen {#step-2-select-your-encrypted-fields}

Wählen Sie als Nächstes **Email address** aus, um das Feld zu verschlüsseln.

Wenn die Verschlüsselung für ein Feld aktiviert ist, kann sie nicht wieder rückgängig gemacht werden. Das bedeutet, dass die Verschlüsselung eine permanente Einstellung ist. Stellen Sie beim Einrichten der Verschlüsselung für E-Mail-Adressen sicher, dass keine Nutzer:innen E-Mail-Adressen im Workspace haben. So wird gewährleistet, dass keine E-Mail-Adressen im Klartext in Braze gespeichert werden, wenn das Feature für den Workspace aktiviert wird.

![Einstellungen für Verschlüsselung auf Feldebene.]({% image_buster /assets/img/field_level_encryption.png %})

## Schritt 3: Nutzer:innen importieren und Update or aktualisieren or aktualisieren {#step-3-import-and-update-users}

Wenn die Verschlüsselung auf Bezeichnerebene aktiviert ist, müssen Sie die E-Mail-Adresse hashen und verschlüsseln, bevor Sie sie zu Braze hinzufügen. Stellen Sie sicher, dass Sie die E-Mail-Adresse vor dem Hashen in Kleinbuchstaben umwandeln. Weitere Details finden Sie unter [Nutzer:innenattribut-Objekt](#user-attributes-object).

Wenn Sie die E-Mail-Adresse in Braze Update or aktualisieren or aktualisieren, sollten Sie den gehashten E-Mail-Wert überall dort verwenden, wo `email` enthalten ist. Dies umfasst:

- Representational State Transfer-Endpunkte:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Hinzufügen oder Update or aktualisieren or aktualisieren von Nutzer:innen per CSV

{% alert note %}
Wenn Sie eine:n neue:n Nutzer:in mit einer E-Mail-Adresse erstellen, müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert hinzufügen. Andernfalls wird die/der Nutzer:in nicht erstellt. Wenn Sie eine E-Mail-Adresse zu einer/einem bestehenden Nutzer:in hinzufügen, die/der noch keine E-Mail hat, müssen Sie ebenfalls `email_encrypted` hinzufügen. Andernfalls wird die/der Nutzer:in nicht aktualisiert.
{% endalert %}

## Überlegungen {#considerations}

Diese Features werden bei der Verschlüsselung auf Bezeichnerebene nicht unterstützt:

- Identifizierung und Erfassung von E-Mail-Adressen über das SDK or Software-Development-Kit
- E-Mail-Erfassungsformulare für In-App-Nachrichten
- Berichte über Empfänger:innen-Domains, einschließlich der E-Mail-Insights-Charts nach E-Mail-Anbieter
- E-Mail-Adressfilter mit regulärem Ausdruck
- Zielgruppensynchronisierung
- Shopify-Integration

### User-Attributes-Objekt {#user-attributes-object}

Wenn Sie die Verschlüsselung auf Bezeichnerebene mit dem Endpunkt `/users/track` verwenden, beachten Sie die folgenden Felddetails für das [User-Attributes-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- Das Feld `email` muss der gehashte Wert der E-Mail-Adresse sein.
- Das Feld `email_encrypted` muss der verschlüsselte Wert der E-Mail-Adresse sein.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was ist der Unterschied zwischen Verschlüsselung und Hashing? {#what-is-the-difference-between-encrypting-and-hashing}

Verschlüsselung ist eine bidirektionale Funktion, bei der es möglich ist, Daten zu verschlüsseln und zu entschlüsseln. Wenn derselbe Klartextwert mehrfach verschlüsselt wird, erzeugt der Verschlüsselungsalgorithmus von AWS (AES-256-GCM) unterschiedliche verschlüsselte Werte. Hashing ist eine Einwegfunktion, bei der der Klartext so umgewandelt wird, dass er nicht entschlüsselt werden kann. Hashing liefert jedes Mal denselben Wert. Dadurch können wir die Verwaltung von Abo-Status für mehrere Nutzer:innen unterstützen, die dieselbe E-Mail-Adresse teilen.

### Welche E-Mail-Adresse sollte ich in meinem Testversand verwenden? {#what-email-address-should-i-use-in-my-test-send}

Klartext-E-Mail-Adressen werden beim Testversand unterstützt. Um zu sehen, wie eine E-Mail für eine:n bestimmte:n Nutzer:in aussieht, gehen Sie wie folgt vor:

1. Wählen Sie **Nachricht als Nutzer:in in Vorschau anzeigen** aus.
2. Wählen Sie unter **Testversand** die Option **Empfängerattribute mit den Attributen der aktuellen Vorschau-Nutzer:in überschreiben** aus.

### Kann ich einen ARN für den HMAC-Schlüssel verwenden? {#can-i-use-an-arn-for-the-hmac-key}

Ja. Unter **Dateneinstellungen** > **Verschlüsselung auf Feldebene** akzeptiert das HMAC-Schlüssel-Bezeichnerfeld sowohl eine Schlüssel-ID als auch einen Schlüssel-ARN.

### Wie entferne oder setze ich einen HMAC-Schlüssel zurück? {#how-do-i-remove-or-reset-an-hmac-key}

Sie können einen HMAC-Schlüssel nach dem Speichern nicht mehr im Dashboard entfernen oder zurücksetzen. Um ein Zurücksetzen des HMAC-Schlüssels oder die Entfernung der Bezeichner-Verschlüsselung auf Feldebene anzufordern, wenden Sie sich an Ihren Braze Account Manager:in oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).

{%raw%}
### Was passiert, wenn ich diese E-Mail-Adressen-Liquid-Variable `{{${email_address}}}` in Braze hinzufüge? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Braze rendert beim Versand der E-Mail die Klartext-E-Mail-Adresse. In Vorschauen wird die verschlüsselte Version der E-Mail angezeigt. Wir empfehlen, die externe ID der Nutzer:innen zu verwenden, wenn Sie eine:n Nutzer:in in einer benutzerdefinierten One-Klick, der or klicken-URL referenzieren.

`{{${email_address}}}` wird derzeit im Preference Center und auf Abmeldeseiten nicht unterstützt.
{%endraw%}

### Welche E-Mail-Adresse sollte ich in Currents erwarten? {#what-email-address-should-i-expect-to-see-in-currents}

Die gehashte E-Mail-Adresse ist in E-Mail-Zustell- und Engagement-Ereignissen enthalten.

### Welche E-Mail-Adresse sollte ich in der Nachrichtenarchivierung erwarten? {#what-email-address-should-i-expect-to-see-in-message-archiving}

Die Klartext-E-Mail-Adresse ist in der Nachrichtenarchivierung enthalten. Diese werden direkt an den Cloud-Storage-Anbieter der Kund:innen gesendet, und es können weitere personenbezogene Daten in den E-Mail-Inhalten enthalten sein.

### Kann ich die Mail-to-List-Unsubscribe-Methode für das Abo-Management mit Bezeichner-Verschlüsselung auf Feldebene verwenden? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

Nein. Die Verwendung der Mail-to-List-Unsubscribe-Methode würde die entschlüsselte Klartext-E-Mail-Adresse an Braze senden. Bei aktivierter Bezeichner-Verschlüsselung auf Feldebene unterstützen wir die URL-basierte HTTP-Methode, einschließlich One-Klick, der or klicken. Wir empfehlen außerdem, einen One-Klick, der or klicken-Abmeldelink in Ihren E-Mail-Text einzufügen.

### Unterstützt die Bezeichner-Verschlüsselung auf Feldebene andere Bezeichner wie Telefonnummern? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

Nein. Derzeit wird die Bezeichner-Verschlüsselung auf Feldebene nur für E-Mail-Adressen unterstützt.