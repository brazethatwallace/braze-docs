---
nav_title: KakaoTalk einrichten
article_title: KakaoTalk einrichten
description: "Dieser Referenzartikel beschreibt, wie Sie Ihren KakaoTalk-Kanal einrichten, einschließlich der Einrichtung von Nutzer:innen, der Abstimmung von Nutzer-IDs und der Erstellung von Testnutzer:innen."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# KakaoTalk einrichten {#set-up-kakaotalk}

> Dieser Artikel beschreibt, wie Sie den [KakaoTalk-Messaging-Kanal]({{site.baseurl}}/kakaotalk) in Braze einrichten, einschließlich der Einrichtung von Nutzer:innen, der Abstimmung von Nutzer-IDs und der Erstellung von KakaoTalk-Testnutzer:innen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Konto bei einem unterstützten KakaoTalk-Partner | Ein Konto bei einem unterstützten KakaoTalk-Partner, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) oder [Infobip](https://marketplace.braze.com/partners/infobip), ist erforderlich, um den KakaoTalk-Messaging-Kanal zu nutzen. |
| KakaoTalk-Business-Kanal | Ihr KakaoTalk-Konto muss ein KakaoTalk-Business-Kanal sein, um KakaoTalk-Nachrichten über Braze zu senden. Wenn Sie ein Konto erstellen, ist der Standardstatus „Basic“. Um Ihr Konto zu einem Business-Kanal zu machen, müssen Sie Ihr Unternehmen verifizieren und die entsprechenden Unterlagen einreichen. |
| KakaoTalk-Sender-Key | Ein gültiger KakaoTalk-Sender-Key. |
| Kontakt-Telefonnummer | Eine Kontakt-Telefonnummer für die Administration Ihres KakaoTalk-Kanals. |
| Braze-Cluster-IPs auf der Allowlist | Die Registrierung auf der IP-Allowlist ist für alle Kund:innen erforderlich. Registrieren Sie die Braze-IP-Adressen für Ihren Cluster, bevor Sie KakaoTalk in Braze integrieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

### Braze-IP-Adressen registrieren {#register-braze-ip-addresses}

Registrieren Sie die Braze-IP-Adressen für Ihren Cluster in Ihrem Comm.One-Dashboard.

1. Gehen Sie in Ihrem Comm.One-Dashboard zu **Account Management (계정 관리)**, wählen Sie das Menüsymbol und dann **View Details (자세히보기)** aus.
2. Wählen Sie **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)** aus.
3. Fügen Sie die IP-Adressen für Ihren Braze-Cluster hinzu. Die vollständige Liste der IPs nach Cluster finden Sie unter [IP-Allowlisting]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).

![Comm.One-Dashboard, das zeigt, wo Sie IP-Adressen hinzufügen können.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### Arten von KakaoTalk-Konten {#types-of-kakaotalk-accounts}

| Kontotyp | Beschreibung |
| --- | --- |
| Basic-Kanal | Ein Standard-KakaoTalk-Kanal, den jede Organisation einrichten kann. Er ermöglicht Broadcast-Messaging und 1:1-Chat über KakaoTalk. |
| [Business-Kanal](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Ein erweiterter, geschäftlich verifizierter KakaoTalk-Kanal, der einen Antrags- und Verifizierungsprozess erfordert. Er bietet erweiterte Features, wie z. B. {::nomarkdown}<ul><li>Verifiziertes Badge</li><li>Anzeige als empfohlener Kanal</li><li>Unterstützung für Business-Messaging</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Arten von KakaoTalk-Konten" }

#### Antrag auf einen Business-Kanal stellen {#apply-for-a-business-channel}

Bevor Sie den Antrag starten, sammeln Sie die folgenden Geschäftsunterlagen:
- Koreanische Gewerbeanmeldung (Business Registration Certificate)
- Ausweis der Unternehmensvertretung
- Beschäftigungsnachweis
- Branchenspezifische Lizenzen

{% alert important %}
Die Informationen in Ihrem KakaoTalk-Kanal (wie Kanalname, Profilbild und andere) müssen exakt mit den Informationen in Ihren offiziell eingereichten Dokumenten übereinstimmen.
{% endalert %}

Nachdem Sie Ihre Unterlagen zusammengestellt haben, führen Sie die folgenden Schritte aus:

1. Melden Sie sich im [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) an.
2. Wählen Sie den bestehenden KakaoTalk-Kanal aus, den Sie upgraden möchten.
3. Wählen Sie im Bereich **Management (관리)** die Option **Business Channel Application (비즈니스 채널 신청)** aus.
4. Wählen Sie den **Apply**- oder **Request-Button (신청)** aus, um den Prozess zu starten.
5. Geben Sie die erforderlichen Informationen an.
6. Warten Sie auf eine Benachrichtigung mit den Ergebnissen der Überprüfung.

## KakaoTalk integrieren {#integrate-kakaotalk}

### Den KakaoTalk-Kanal mit Braze verbinden {#connect-the-kakaotalk-channel-to-braze}

1. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie Ihren KakaoTalk-Anbieter aus.
2. Sammeln Sie die erforderlichen Zugangsdaten für Ihren Anbieter (siehe folgenden Abschnitt), geben Sie diese auf der **Technologie-Partnerseite** ein und speichern Sie sie.
3. Verwenden Sie die neu gespeicherten Zugangsdaten zum Senden.

#### CJ OliveNetworks

Gehen Sie zu Ihrem [Comm.One-Dashboard](https://ums.cjmplace.com/) und sammeln Sie die folgenden Informationen.

| Feld | Standort |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Wählen Sie Ihr Profil aus. |
| **Sender Key (발신프로필 키)** | Gehen Sie zu **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | Gehen Sie in Ihrem Comm.One-Dashboard zu **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Gehen Sie zu <b>Account Management (계정 관리)</b>, wählen Sie das Menüsymbol und dann <b>View Details (자세히보기)</b>.</li><li>Gehen Sie zu <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Gehen Sie zum selben Ort wie für die **Sender number (사업자 등록번호)** und dann zu **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Comm.One-Dashboard mit einer zensierten Login-ID.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Comm.One-Dashboard mit einem zensierten Sender Key.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
Sie können einen KakaoTalk Sender Key jeweils nur in einen Workspace integrieren. Um denselben Sender Key in einem anderen Workspace zu verwenden, müssen Sie zunächst die KakaoTalk-Abo-Gruppe im ursprünglichen Workspace archivieren und dann den [Braze-Support]({{site.baseurl}}/braze_support) kontaktieren, um die Integration zu entfernen. Nachdem Braze die Integration entfernt hat, können Sie die Integration im neuen Workspace einrichten.
{% endalert %}

![Zugangsdaten für einen Braze-KakaoTalk-Kanal.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Comm.One-Dashboard mit einem zensierten Kanalnamen.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Comm.One-Dashboard mit einer zensierten Credential-ID und einem zensierten Passwort.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Es können nur die Kanäle registriert werden, die einer einzelnen gemeinsamen ID zugeordnet sind.
{% endalert %}

![Felder auf der Technologie-Partnerseite für CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Gehen Sie zu Ihrem Infobip-Dashboard und zum [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/), um die folgenden Informationen zu sammeln.

| Feld | Standort |
| --- | --- |
| **API Base URL** | Gehen Sie im Infobip-Portal zu **Developer Tools** > **API Keys**. |
| **API Key** | Gehen Sie im Infobip-Portal zu **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Gehen Sie im Infobip-Portal zu **Channels and Numbers** > **Channels** und wählen Sie dann den Tab **Senders**. |
| **Sender profile UUID** | Gehen Sie im KakaoTalk Channel Admin Center zu **Channels** und suchen Sie die **Search ID** im Kanalinformationsfenster. |
| **Channel name** | Suchen Sie im KakaoTalk Channel Admin Center den **Kanalnamen** im selben Kanalinformationsfenster. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

##### API-Schlüssel und Base URL {#api-key-and-base-url}

1. Wählen Sie im Infobip-Portal **Developer Tools** > **API Keys**.
2. Kopieren Sie auf der Seite **API keys** die **API base URL**.

![Infobip-Seite „API Keys“ mit der API-Base-URL.]({% image_buster /assets/img/kakaotalk/infobip_api_keys_page.png %})

{: start="3"}
3. Wählen Sie **CREATE API KEY**.
4. Geben Sie den **Name** ein, wählen Sie das **Expiration date** und dann die für KakaoTalk erforderlichen API-Scopes aus. Diese Scopes steuern, welche Infobip-API-Aktionen Ihr Schlüssel ausführen kann.

![Infobip-Seite „Create API Key“ mit den Feldern für Name, Ablaufdatum und API-Scopes.]({% image_buster /assets/img/kakaotalk/infobip_api_key_scopes.png %})

{: start="5"}
5. Wählen Sie **CREATE**, um den Schlüssel zu generieren.
6. Kopieren Sie den generierten Schlüssel. Sie können zu dieser Seite zurückkehren, um den Namen, das Ablaufdatum oder die API-Scopes zu aktualisieren.

##### Sender-Profil-UUID und Kanalname {#sender-profile-uuid-and-channel-name}

1. Wählen Sie im [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) **Channels** aus.
2. Suchen Sie im Fenster **Channel Information** den **Kanalnamen** und die **Search id** (Sender-UUID).
3. Geben Sie die **Customer center contact information** ein. Diese Angabe ist beim Senden von Werbenachrichten erforderlich.

![KakaoTalk-Kanalinformationsfenster mit den Kontaktinformationsfeldern des Kundencenters.]({% image_buster /assets/img/kakaotalk/kakao_customer_center_contact.png %})

{: start="4"}
4. Um einen anderen Kanal anzuzeigen, wählen Sie das Kanalsymbol oben im Menü.
5. Wählen Sie in der Liste **My channel** den gewünschten Kanal aus und wiederholen Sie die vorherigen Schritte.

## Nutzerprofile einrichten {#set-user-profiles}

Nutzerprofile müssen Telefonnummern im E.164-Format enthalten, um Nachrichten über KakaoTalk zu senden. Telefonnummern werden im Nutzerprofil angezeigt. KakaoTalk erfordert Telefonnummern im E.164-Format (zum Beispiel `+821025749774`). Dies unterscheidet sich von einigen anderen Messaging-Kanälen, die Telefonnummern in verschiedenen Formaten akzeptieren können.

### Telefonnummern importieren {#import-phone-numbers}

Importieren Sie Telefonnummern, indem Sie [eine CSV-Datei hochladen oder die API verwenden]({{site.baseurl}}/user_guide/data/unification/user_data/import_users), um Nutzer:innen zu erstellen. Stellen Sie sicher, dass die Telefonnummern vor dem Import im E.164-Format vorliegen.