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
Die Verschlüsselung auf Bezeichner-Feldebene ist als zusätzliches Feature verfügbar. Wenden Sie sich an Ihren Braze Account Manager, um mit der Verschlüsselung auf Bezeichner-Feldebene zu beginnen.
{% endalert %}

## Funktionsweise {#how-it-works}

E-Mail-Adressen müssen gehasht und verschlüsselt werden, bevor sie zu Braze hinzugefügt werden. Wenn eine Nachricht gesendet wird, erfolgt ein Aufruf an AWS KMS für die entschlüsselte E-Mail-Adresse. Anschließend wird die gehashte E-Mail-Adresse in die Metadaten für Zustellungs- und Engagement-Ereignisse eingefügt, um sie mit der/dem ursprünglichen Nutzer:in zu verknüpfen. So kann Braze E-Mail-Analytics tracken. Braze schwärzt alle E-Mail-Adressen im Klartext und speichert die Klartext-E-Mail-Adresse der Nutzer:innen nicht.

## Voraussetzungen {#prerequisites}

Um die Verschlüsselung auf Bezeichner-Feldebene zu verwenden, müssen Sie Zugriff auf AWS KMS haben, um E-Mail-Adressen [zu verschlüsseln](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) und zu [hashen](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html), **bevor** Sie sie an Braze senden.

Führen Sie diese Schritte aus, um Ihre AWS-Secret-Key-Authentifizierungsmethode einzurichten.

1. Um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugangsschlüssel abzurufen, [erstellen Sie eine:n IAM-Nutzer:in und eine Administratorengruppe](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) in AWS mit einer Berechtigungsrichtlinie für den AWS Key Management Service. Die/der IAM-Nutzer:in muss über die Berechtigungen [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) und [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) verfügen. Weitere Einzelheiten finden Sie unter [AWS-KMS-Berechtigungen](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Wählen Sie **Show User Security Credentials**, um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugangsschlüssel anzuzeigen. Notieren Sie sich diese Zugangsdaten, oder wählen Sie den Button **Download Credentials**, da Sie diese eingeben müssen, wenn Sie Ihre AWS-KMS-Schlüssel verbinden.
3. Sie müssen KMS in den folgenden AWS-Regionen einrichten:
    - **Braze US-Cluster:** `us-east-1`
    - **Braze EU-Cluster:** `eu-central-1`
    - **Braze AU-Cluster:** `ap-southeast-2`
    - **Braze ID-Cluster:** `ap-southeast-3`
    - **Braze JP-Cluster:** `ap-northeast-1`
4. Erstellen Sie im AWS Key Management Service zwei Schlüssel und vergewissern Sie sich, dass die/der IAM-Nutzer:in in den Schlüsselverwendungsberechtigungen hinzugefügt ist:
    - **[Verschlüsseln/Entschlüsseln](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Wählen Sie den Schlüsseltyp **Symmetric** und die Schlüsselverwendung **Encrypt and Decrypt**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Wählen Sie den Schlüsseltyp **Symmetric** und die Schlüsselverwendung **Generate and Verify MAC**. Die Schlüsselspezifikation sollte **HMAC_256** lauten. Notieren Sie sich nach der Erstellung des Schlüssels die HMAC-Schlüssel-ID, da Sie diese in Braze eingeben müssen.

![Schlüsseleinstellungen konfigurieren mit den ausgewählten Optionen „Symmetric“, „Generate and Verify MAC“ und „HMAC_256“.]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## 1. Schritt: Verbinden Sie Ihre AWS-KMS-Schlüssel {#step-1-connect-your-aws-kms-keys}

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Verschlüsselung auf Feldebene**. Geben Sie für Ihre AWS-KMS-Einstellungen Folgendes ein:

- Zugriffsschlüssel-ID
- Geheimer Zugangsschlüssel
- HMAC-Schlüssel-ID (kann nach dem Speichern nicht mehr aktualisiert werden)

## 2. Schritt: Wählen Sie Ihre verschlüsselten Felder aus {#step-2-select-your-encrypted-fields}

Wählen Sie anschließend **Email address**, um das Feld zu verschlüsseln.

Wenn die Verschlüsselung für ein Feld aktiviert ist, kann es nicht wieder in ein entschlüsseltes Feld umgewandelt werden. Das bedeutet, dass die Verschlüsselung eine dauerhafte Einstellung ist. Vergewissern Sie sich beim Einrichten der Verschlüsselung für E-Mail-Adressen, dass keine Nutzer:innen über E-Mail-Adressen im Workspace verfügen. Dadurch wird sichergestellt, dass keine E-Mail-Adressen im Klartext in Braze gespeichert werden, wenn Sie das Feature für den Workspace aktivieren.

![Einstellungen für die Verschlüsselung auf Feldebene.]({% image_buster /assets/img/field_level_encryption.png %})

## 3. Schritt: Nutzer:innen importieren und aktualisieren {#step-3-import-and-update-users}

Wenn die Verschlüsselung auf Bezeichner-Feldebene aktiviert ist, müssen Sie die E-Mail-Adresse vor dem Hinzufügen zu Braze hashen und verschlüsseln. Vergewissern Sie sich, dass Sie die E-Mail-Adresse vor dem Hashing in Kleinbuchstaben umwandeln. Weitere Einzelheiten finden Sie unter [Nutzer:innen-Attribute-Objekt](#user-attributes-object).

Wenn Sie die E-Mail-Adresse in Braze aktualisieren, sollten Sie den gehashten E-Mail-Wert verwenden, wo immer `email` enthalten ist. Dies beinhaltet:

- REST-Endpunkte:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Hinzufügen oder Aktualisieren von Nutzer:innen über CSV

{% alert note %}
Wenn Sie eine:n neue:n Nutzer:in mit einer E-Mail-Adresse anlegen, müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail-Wert der/des Nutzers:in hinzufügen. Andernfalls wird die/der Nutzer:in nicht erstellt. Ebenso müssen Sie, wenn Sie einer/einem bestehenden Nutzer:in ohne E-Mail eine E-Mail-Adresse hinzufügen, `email_encrypted` hinzufügen. Andernfalls wird die/der Nutzer:in nicht aktualisiert.
{% endalert %}

## Überlegungen {#considerations}

Diese Features werden bei der Verschlüsselung auf Bezeichner-Feldebene nicht unterstützt:

- Identifizieren und Erfassen von E-Mail-Adressen über SDK
- In-App-Nachricht-E-Mail-Erfassungsformulare
- Berichte über Empfänger:innen-Domains, einschließlich Charts der Email-Insights-Mailbox-Anbieter
- Filter für E-Mail-Adressen mit regulärem Ausdruck
- Zielgruppen-Synchronisation
- Shopify-Integration

### Nutzer:innen-Attribute-Objekt {#user-attributes-object}

Wenn Sie die Verschlüsselung auf Bezeichner-Feldebene mit dem Endpunkt `/users/track` verwenden, beachten Sie diese Felddetails für das [Nutzer:innen-Attribute-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens):

- Das Feld `email` muss der Hash-Wert der E-Mail sein.
- Das Feld `email_encrypted` muss der verschlüsselte Wert für die E-Mail sein.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was ist der Unterschied zwischen Verschlüsseln und Hashing? {#what-is-the-difference-between-encrypting-and-hashing}

Bei der Verschlüsselung handelt es sich um eine bidirektionale Funktion, bei der Daten ver- und entschlüsselt werden können. Wenn derselbe Klartextwert mehrmals verschlüsselt wird, ergibt der Verschlüsselungsalgorithmus von AWS (AES-256-GCM) unterschiedliche verschlüsselte Werte. Hashing ist eine Einwegfunktion, bei der der Klartext so verschlüsselt wird, dass er nicht entschlüsselt werden kann. Hashing ergibt jedes Mal den gleichen Wert. Dies ermöglicht es uns, Abo-Status für mehrere Nutzer:innen zu verwalten, die dieselbe E-Mail-Adresse verwenden.

### Welche E-Mail-Adresse sollte ich für meinen Testversand verwenden? {#what-email-address-should-i-use-in-my-test-send}

E-Mail-Adressen im Klartext werden beim Testversand unterstützt. Um zu sehen, wie eine E-Mail für eine:n bestimmte:n Nutzer:in aussieht, gehen Sie wie folgt vor:

1. Wählen Sie **Preview message as a user**.
2. Wählen Sie in **Test Send** die Option **Override recipients attributes with current preview user's attributes**.

{%raw%}
### Was passiert, wenn ich diesen E-Mail-Adressen-Liquid `{{${email_address}}}` in Braze hinzufüge? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Braze rendert die Klartext-E-Mail-Adresse beim Senden der E-Mail. In der Vorschau wird die verschlüsselte Version der E-Mail angezeigt. Wir empfehlen die Verwendung der externen ID der/des Nutzers:in, wenn Sie in einer angepassten One-Click-URL auf eine:n Nutzer:in verweisen.

`{{${email_address}}}` wird derzeit im Präferenzzentrum und auf den Abmeldeseiten nicht unterstützt.
{%endraw%}

### Welche E-Mail-Adresse sollte ich in Currents sehen? {#what-email-address-should-i-expect-to-see-in-currents}

Die gehashte E-Mail-Adresse ist in E-Mail-Zustellungs- und Engagement-Ereignissen enthalten.

### Welche E-Mail-Adresse sollte ich bei der Nachrichtenarchivierung erwarten? {#what-email-address-should-i-expect-to-see-in-message-archiving}

Die Klartext-E-Mail-Adresse ist in der Nachrichtenarchivierung enthalten. Diese werden direkt an den Cloud-Speicher-Anbieter der Kund:innen gesendet, und die E-Mails können weitere personenbezogene Daten enthalten.

### Kann ich Mail-to-List-Unsubscribe für das Abo-Management mit Verschlüsselung auf Bezeichner-Feldebene verwenden? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

Nein. Die Verwendung von Mail-to-List-Unsubscribe würde die im Klartext entschlüsselte E-Mail-Adresse an Braze senden. Wenn die Verschlüsselung auf Bezeichner-Feldebene aktiviert ist, unterstützen wir die URL-basierte HTTP-Methode, einschließlich One-Click. Wir empfehlen außerdem, einen One-Click-Abmeldelink in Ihre E-Mail aufzunehmen.

### Unterstützt die Verschlüsselung auf Bezeichner-Feldebene auch andere Bezeichner wie Telefonnummern? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

Nein. Derzeit wird die Verschlüsselung auf Bezeichner-Feldebene nur für E-Mail-Adressen unterstützt.