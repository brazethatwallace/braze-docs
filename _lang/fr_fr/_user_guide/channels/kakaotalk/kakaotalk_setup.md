---
nav_title: Configurer KakaoTalk
article_title: Configurer KakaoTalk
description: "Cet article de référence explique comment configurer votre canal KakaoTalk, notamment comment configurer les utilisateurs, réconcilier les ID utilisateur et créer des utilisateurs test."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# Configurer KakaoTalk {#set-up-kakaotalk}

> Cet article explique comment configurer le [canal de communication KakaoTalk]({{site.baseurl}}/kakaotalk) dans Braze, notamment comment configurer les utilisateurs, réconcilier les ID utilisateur et créer des utilisateurs test KakaoTalk.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte auprès d'un partenaire KakaoTalk pris en charge | Un compte auprès d'un partenaire KakaoTalk pris en charge, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) ou Infobip, est requis pour utiliser le canal de communication KakaoTalk. |
| Canal Business KakaoTalk | Votre compte KakaoTalk doit être un canal Business KakaoTalk pour envoyer des messages KakaoTalk via Braze. Lorsque vous créez un compte, son statut par défaut est basique. Pour faire de votre compte un canal Business, vous devrez vérifier votre entreprise et fournir la documentation pertinente. |
| Clé d'expéditeur KakaoTalk | Une clé d'expéditeur KakaoTalk valide. |
| Numéro de téléphone de contact | Un numéro de téléphone de contact pour l'administrateur de votre canal KakaoTalk. |
| IP Braze ajoutées à la liste d'autorisation du cluster | L'enregistrement de la liste d'autorisation des IP est requis pour tous les clients. Enregistrez les adresses IP Braze de votre cluster avant d'intégrer KakaoTalk dans Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

### Enregistrer les adresses IP Braze {#register-braze-ip-addresses}

Enregistrez les adresses IP Braze de votre cluster dans votre tableau de bord Comm.One.

1. Dans votre tableau de bord Comm.One, accédez à **Account Management (계정 관리)**, sélectionnez l'icône de menu, puis sélectionnez **View Details (자세히보기)**.
2. Sélectionnez **Center & Upload IP Allowlist (센터&업로드 IP 화이트리스트)**.
3. Ajoutez les adresses IP de votre cluster Braze. Pour la liste complète des IP par cluster, consultez [Liste d'autorisation des IP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).

![Tableau de bord Comm.One montrant où ajouter des adresses IP.]({% image_buster /assets/img/kakaotalk/register_braze_ip.png %})

### Types de comptes KakaoTalk {#types-of-kakaotalk-accounts}

| Type de compte | Description |
| --- | --- |
| Canal basique | Un canal KakaoTalk standard que toute organisation peut configurer. Il permet l'envoi de messages diffusés et le chat 1:1 via KakaoTalk. |
| [Canal Business](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Un canal KakaoTalk amélioré et vérifié pour les entreprises, qui nécessite un processus de candidature et de vérification. Il offre des fonctionnalités avancées, telles que {::nomarkdown}<ul><li>Badge vérifié</li><li>Apparition en tant que canal recommandé</li><li>Prise en charge de la messagerie professionnelle</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de comptes KakaoTalk" }

#### Candidater pour un canal Business {#apply-for-a-business-channel}

Avant de commencer la candidature, rassemblez la documentation professionnelle suivante :
- Korean Business Registration Certificate
- ID of the Business Representative
- Employment Certificate
- Industry-specific Licenses

{% alert important %}
Les informations de votre canal KakaoTalk (telles que le nom du canal, l'image de profil et autres) doivent correspondre exactement aux informations figurant sur vos documents officiels soumis.
{% endalert %}

Après avoir rassemblé votre documentation, suivez ces étapes :

1. Connectez-vous au [Centre d'administration des canaux KakaoTalk](https://center-pf.kakao.com/).
2. Sélectionnez le canal KakaoTalk existant que vous souhaitez mettre à niveau.
3. Dans la section **Management (관리)**, sélectionnez l'option **Business Channel Application (비즈니스 채널 신청)**.
4. Sélectionnez le bouton **Apply** ou **Request (신청)** pour lancer le processus.
5. Fournissez les informations requises.
6. Attendez une notification avec les résultats de l'examen.

## Intégrer KakaoTalk {#integrate-kakaotalk}

### Étape 1 : Connecter le canal KakaoTalk à Braze {#step-1-connect-the-kakaotalk-channel-to-braze}

1. Accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez votre fournisseur KakaoTalk.
2. Rassemblez les identifiants requis pour votre fournisseur (voir la section suivante), puis saisissez-les sur la page **Partenaires technologiques** et enregistrez.
3. Utilisez les identifiants nouvellement enregistrés pour l'envoi.

#### CJ OliveNetworks

Accédez à votre [tableau de bord Comm.One](https://ums.cjmplace.com/) et rassemblez les informations suivantes.

| Champ | Emplacement |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Sélectionnez votre profil. |
| **Sender Key (발신프로필 키)** | Accédez à **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | Dans votre tableau de bord Comm.One, accédez à **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Accédez à <b>Account Management (계정 관리)</b>, sélectionnez l'icône de menu, puis sélectionnez <b>View Details (자세히보기)</b>.</li><li>Accédez à <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ol>{:/} |
| **Credential (ID) et Password (비밀번호)** | Accédez au même emplacement que pour le **Sender number (사업자 등록번호)**, puis accédez à **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CJ OliveNetworks" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Tableau de bord Comm.One affichant un identifiant de connexion masqué.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Tableau de bord Comm.One affichant une clé d'expéditeur masquée.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% alert important %}
Vous ne pouvez intégrer une clé d'expéditeur KakaoTalk que dans un seul espace de travail à la fois. Pour utiliser la même clé d'expéditeur dans un autre espace de travail, vous devez d'abord archiver le groupe d'abonnement KakaoTalk dans l'espace de travail d'origine, puis contacter l'[assistance Braze]({{site.baseurl}}/braze_support) pour supprimer l'intégration. Une fois l'intégration supprimée par Braze, vous pouvez configurer l'intégration dans le nouvel espace de travail.
{% endalert %}

![Identifiants pour un canal KakaoTalk Braze.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Tableau de bord Comm.One affichant un nom de canal masqué.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) et Password (비밀번호) %}

![Tableau de bord Comm.One affichant un identifiant et un mot de passe masqués.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Seuls les canaux associés à un identifiant commun unique peuvent être enregistrés.
{% endalert %}

![Champs sur la page Partenaires technologiques pour CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

#### Infobip

Accédez à votre tableau de bord Infobip et rassemblez les informations suivantes.

| Champ | Emplacement |
| --- | --- |
| **API Base URL** | Sélectionnez **Developer Tools** > **API Keys**. |
| **API Key** | Sélectionnez **Developer Tools** > **API Keys**. |
| **Sender name / Sender key** | Sélectionnez **Channels and Numbers** > **Channels**, puis sélectionnez l'onglet **Senders**. |
| **Sender profile UUID** | Fourni directement par Infobip. Contactez Infobip si vous ne disposez pas de cette information. |
| **Channel name** | Fourni directement par Infobip. Contactez Infobip si vous ne disposez pas de cette information. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Infobip" }

## Configurer les profils utilisateur {#set-user-profiles}

Les profils utilisateur doivent contenir des numéros de téléphone au format E.164 pour pouvoir leur envoyer des messages via KakaoTalk. Les numéros de téléphone sont affichés sur le profil utilisateur. KakaoTalk exige que les numéros de téléphone soient au format E.164 (par exemple, `+821025749774`). Cela diffère de certains autres canaux de communication qui peuvent accepter des numéros de téléphone dans plusieurs formats.

### Importer des numéros de téléphone {#import-phone-numbers}

Importez des numéros de téléphone en [chargeant un fichier CSV ou en utilisant l'API]({{site.baseurl}}/user_guide/data/unification/user_data/import_users) pour créer un utilisateur. Assurez-vous que les numéros de téléphone sont au format E.164 avant l'importation.