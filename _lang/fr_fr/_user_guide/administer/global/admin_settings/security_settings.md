---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
toc_headers: h2
page_type: reference
description: "Cet article de référence traite des paramètres génériques de sécurité interentreprises, y compris des règles d'authentification, de la liste d'adresses IP autorisées, des données d'identification personnelle et de l'authentification à deux facteurs (2FA)."

---

# Paramètres de sécurité {#security-settings}

> En tant qu'administrateur, la sécurité est une priorité absolue. La page **Paramètres de sécurité** vous permet de gérer les paramètres de sécurité génériques et interentreprises, notamment les règles d'authentification, la liste d'adresses IP autorisées et l'authentification à deux facteurs.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité**.

## Règles d'authentification {#authentication-rules}

### Longueur du mot de passe {#password-length}

Utilisez ce champ pour modifier la longueur minimale requise pour le mot de passe. Le nombre minimum par défaut est de huit caractères.

### Complexité du mot de passe {#password-complexity}

Sélectionnez **Appliquer des mots de passe complexes** pour exiger que les mots de passe comprennent au moins un élément de chacune des catégories suivantes :
- Lettre majuscule
- Lettre minuscule
- Nombre
- Caractère spécial

### Réutilisation des mots de passe {#password-re-usability}

Détermine le nombre minimum de nouveaux mots de passe devant être définis avant qu'un utilisateur puisse réutiliser un mot de passe. La valeur par défaut est trois.

### Règles d'expiration du mot de passe {#password-expiration-rules}

Utilisez ce champ pour définir quand vous souhaitez que les utilisateurs de votre compte Braze réinitialisent leur mot de passe.

### Règles de durée de session {#session-duration-rules}

Utilisez ce champ pour définir la durée pendant laquelle Braze maintient votre session active. Lorsque Braze considère votre session comme inactive (aucune activité pendant le nombre de minutes défini), Braze déconnecte l'utilisateur. Le nombre maximum de minutes que vous pouvez saisir est de 10 080 (soit une semaine) si l'authentification à deux facteurs est appliquée pour votre entreprise ; sinon, la durée maximale de session est de 1 440 minutes (soit 24 heures).

### Authentification unique (SSO) {#single-sign-on-sso-authentication}

Vous pouvez restreindre la connexion de vos utilisateurs à un mot de passe ou à l'authentification unique (SSO).

Pour l'[authentification unique (SSO) SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on), les clients doivent configurer leurs paramètres SAML avant d'appliquer cette restriction. Si les clients utilisent Google SSO, ils n'ont qu'à appliquer les paramètres de la page de sécurité sans configuration supplémentaire.

## Liste d'adresses IP autorisées du tableau de bord {#dashboard-ip-allowlisting}

Utilisez le champ affiché pour autoriser des adresses IP et des sous-réseaux spécifiques à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, depuis un réseau d'entreprise ou un VPN). Spécifiez les adresses IP et les sous-réseaux sous forme de plages CIDR dans une liste séparée par des virgules. Si aucune adresse n'est spécifiée, les utilisateurs peuvent se connecter depuis n'importe quelle adresse IP.

## Authentification à deux facteurs (2FA) {#two-factor-authentication-2fa}

L'authentification à deux facteurs est requise pour tous les utilisateurs de l'entreprise. Elle ajoute un second niveau de vérification d'identité lors de la connexion à un compte, le rendant plus sécurisé qu'un simple nom d'utilisateur et mot de passe. Si votre tableau de bord ne prend pas en charge l'authentification à deux facteurs, contactez votre gestionnaire de la satisfaction client.

Lorsque l'authentification à deux facteurs est activée :

- En plus de saisir un mot de passe, les utilisateurs doivent entrer un code de vérification lors de la connexion à leur compte Braze. Le code peut être envoyé via une application d'authentification, par e-mail ou par SMS.
- La case à cocher **Se souvenir de ce compte pendant 30 jours** devient disponible pour les utilisateurs.

Braze verrouille les utilisateurs qui n'ont pas configuré leur authentification à deux facteurs sur leur compte Braze. Les utilisateurs de comptes Braze peuvent également configurer l'authentification à deux facteurs par eux-mêmes dans les **Paramètres du compte**, même si elle n'est pas exigée par l'administrateur.

N'oubliez pas d'enregistrer vos modifications avant de quitter la page !

### Se souvenir de ce compte pendant 30 jours {#remember-me}

Cette fonctionnalité est disponible lorsque l'authentification à deux facteurs est activée.

Lorsque vous sélectionnez **Se souvenir de ce compte pendant 30 jours**, un cookie est stocké sur votre appareil, ce qui vous permet de ne vous connecter avec l'authentification à deux facteurs qu'une seule fois sur une période de 30 jours.

![Case à cocher « Se souvenir de ce compte pendant 30 jours »]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Les clients disposant de plusieurs comptes au sein d'une même entreprise sur le tableau de bord peuvent rencontrer des problèmes avec cette fonctionnalité, car le cookie est lié à un appareil spécifique. Si les utilisateurs utilisent le même appareil pour se connecter à plusieurs comptes, le cookie sera remplacé pour les comptes précédemment autorisés sur cet appareil. Braze s'attend à ce qu'un seul appareil soit associé à un compte, et non un appareil pour plusieurs comptes.

### Réinitialisation de l'authentification utilisateur {#resetting-user-authentication}

Si vous rencontrez des difficultés pour vous connecter avec l'authentification à deux facteurs, contactez les administrateurs de votre entreprise pour réinitialiser votre authentification à deux facteurs. Les administrateurs peuvent effectuer les étapes suivantes :

1. Allez dans **Paramètres** > **Utilisateurs de l'entreprise**.
2. Sélectionnez l'utilisateur dans la liste fournie.
3. Sélectionnez **Réinitialiser** sous **Authentification à deux facteurs**.

Une réinitialisation peut résoudre des problèmes d'authentification courants tels que des difficultés avec les applications d'authentification, la non-réception de la vérification par e-mail, un échec de connexion dû à des pannes SMS ou à une erreur utilisateur, et bien plus encore.

### Exigences de la 2FA au niveau de l'entreprise {#requirements-for-2fa-at-the-company-level}

Tout d'abord, vérifiez si la 2FA est activée pour votre tableau de bord en allant dans **Paramètres de l'entreprise** > **Paramètres de sécurité** > **Authentification à deux facteurs**. Si le bouton est grisé, la 2FA n'a pas été activée pour votre entreprise et n'est pas obligatoire pour tous les utilisateurs de l'entreprise.

#### Options utilisateur lorsque la 2FA n'est pas obligatoire {#user-options-when-2fa-isnt-mandatory}

Si la 2FA n'est pas appliquée au niveau de l'entreprise, les utilisateurs individuels peuvent configurer la 2FA par eux-mêmes sur leur page Paramètres du compte. Dans ce cas, les utilisateurs ne seront pas verrouillés hors de leur compte s'ils ne la configurent pas. Vous pouvez identifier les utilisateurs qui ont choisi d'activer la 2FA en consultant la page Gérer les utilisateurs.

#### Exigences lorsque la 2FA est obligatoire {#requirements-when-2fa-is-mandatory}

Si la 2FA est appliquée au niveau de l'entreprise, les utilisateurs qui ne la configurent pas sur leur propre compte lors de la connexion seront verrouillés hors du tableau de bord. Les utilisateurs doivent compléter la configuration de la 2FA pour maintenir leur accès.

{% alert important %}
La 2FA est requise pour tous les utilisateurs de l'entreprise uniquement si l'authentification unique (SSO) n'est pas activée. Si le SSO est utilisé, la 2FA n'a pas besoin d'être appliquée au niveau de l'entreprise.
{% endalert %}

## Configurer manuellement la 2FA {#manually-set-up-2fa}

Pour activer manuellement l'authentification à deux facteurs (2FA) sur votre compte Braze, suivez ces étapes :

1. Dans Braze, sélectionnez votre icône de profil dans l'en-tête global, puis sélectionnez **Gérer votre compte**. Faites défiler jusqu'à la section **Authentification à deux facteurs**, puis sélectionnez **Démarrer la configuration**.
2. Saisissez votre mot de passe dans la fenêtre modale de connexion, puis sélectionnez **Vérifier le mot de passe**.
3. Dans la fenêtre modale **Configuration de l'authentification à deux facteurs**, saisissez votre numéro de téléphone, puis sélectionnez **Activer**.
4. Copiez le code à sept chiffres généré depuis votre e-mail ou votre SMS, puis retournez dans Braze et collez-le dans la fenêtre modale **Configuration de l'authentification à deux facteurs**. Sélectionnez **Vérifier**.
5. (Facultatif) Pour éviter de saisir la 2FA pendant les 30 prochains jours, activez l'option **Se souvenir de ce compte pendant 30 jours**.

## Accès élevé {#elevated-access}

L'accès élevé ajoute une couche de sécurité supplémentaire pour les actions sensibles dans votre tableau de bord Braze. Lorsqu'il est actif, les utilisateurs doivent re-vérifier leur compte avant d'exporter un segment ou de consulter une clé API. Pour utiliser l'accès élevé, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et activez-le.

Si un utilisateur ne peut pas re-vérifier son identité, il sera redirigé vers l'endroit où il se trouvait et ne pourra pas poursuivre l'action sensible. Après une re-vérification réussie, il n'aura pas besoin de le refaire pendant l'heure suivante, sauf s'il se déconnecte entre-temps.

## Téléchargement d'un rapport d'événements de sécurité {#security-event-report}

Le rapport d'événements de sécurité est un rapport CSV des événements de sécurité tels que les invitations de compte, les suppressions de compte, les tentatives de connexion réussies et échouées, et d'autres activités. Vous pouvez l'utiliser pour effectuer des audits internes.

Pour télécharger ce rapport, procédez comme suit :

1. Allez dans **Paramètres** > **Paramètres d'administration**.
2. Sélectionnez l'onglet **Paramètres de sécurité** et accédez à la section **Téléchargement des événements de sécurité**.
3. Sélectionnez **Télécharger le rapport**.

Ce téléchargement manuel de rapport contient uniquement les 10 000 événements de sécurité les plus récents pour votre compte. Si votre fichier CSV exporté contient exactement 10 001 lignes (y compris la ligne d'en-tête), vous avez atteint la limite de 10 000 événements du rapport et les événements plus anciens peuvent ne pas être inclus.

Pour exporter les événements de sécurité vers Amazon S3 sans cette limite de lignes, consultez [Exportation des événements de sécurité avec Amazon S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3).

### Définitions des colonnes CSV {#csv-column-definitions}

Le rapport CSV des événements de sécurité contient les colonnes suivantes :

| Colonne | Description |
|---------|-------------|
| CreatedAt | Horodatage de l'enregistrement de l'événement, en UTC. |
| EmailAtTimeOfEvent | Adresse e-mail de l'utilisateur du tableau de bord qui a déclenché l'événement, telle qu'enregistrée au moment de l'événement. |
| CurrentEmail | Adresse e-mail actuelle de l'utilisateur du tableau de bord qui a déclenché l'événement. Si l'utilisateur n'existe plus, son identifiant développeur est utilisé à la place. |
| EventName | Type d'événement de sécurité. Consultez la liste déroulante **Événements de sécurité signalés** après ce tableau. |
| OtherAccount | Adresse e-mail d'un autre utilisateur du tableau de bord affecté par l'événement, le cas échéant (par exemple, lorsqu'un compte est ajouté ou supprimé). |
| JsonProperties | Propriétés spécifiques à l'événement au format JSON. Les champs inclus varient selon le type d'événement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Définitions des colonnes CSV" }

Les [exportations S3]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3) incluent ces colonnes ainsi que `Version`, la version du schéma pour le format d'exportation (actuellement `1`).

{% details Événements de sécurité signalés %}
### Connexion et compte {#login-and-account}
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- Added Account
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- Removed Account
- User Subscription Status Updated
- User Updated
- Developer Account Updated

### Accès élevé
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- Enabled Elevated Access Enforcement
- Disabled Elevated Access Enforcement

Campaign
- Added Campaign
- Edited Campaign

Canvas
- Added Canvas
- Edited Canvas

### Segment
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API
- Segment Users Deleted
- Cleared Cohort

### Clé REST API {#rest-api-key}
- Added REST API key
- Removed REST API key

### Identifiant d'authentification basique {#basic-authentication-credential}
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### Autorisation {#permission}
- Cleared Developer 2FA
- Updated Account Permission
- Added Team
- Edited Team
- Archived Team
- Unarchived Team
- Created App Group Permission Set
- Edited App Group Permission Set
- Removed App Group Permission Set
- Created Custom Role
- Updated Custom Role
- Deleted Custom Role

### Paramètres de l'entreprise {#company-settings}
- Added App Group
- Added App
- Company Settings Changed
- Updated Company Security Settings
- Updated Security Event Cloud Export
- Added Landing Pages Custom Domain
- Removed Landing Pages Custom Domain
- Custom Domain Created
- Custom Domain Deleted
- Enabled Global Control Group
- Disabled Global Control Group
- Updated Global Control Exclusions
- Updated Subscription Group SMS Allow List

### Modèle d'e-mail {#email-template}
- Added Email Template
- Updated Email Template

### Identifiant push {#push-credential}
- Updated Push Credential
- Removed Push Credential

### Outil de débogage du SDK {#sdk-debugger}
- Started SDK Debugger Session
- Exported SDK Debugger Log

### Utilisateurs {#users}
- Users Deleted
- Users Viewed
- User Import Started
- User Subscription Group Status Updated
- User Deleted
- Single User Deletion Cancelled
- Bulk User Deletion Cancelled

### Catalogues {#catalogs}
- Catalog Created
- Catalog Deleted

### Braze Agents
- Created Agent
- Edited Agent

### BrazeAI Operator
- Requested BrazeAI Operator Response
- BrazeAI Operator Responded
{% enddetails %}

## Consultation des informations personnelles identifiables (PII) {#view-pii}

L'autorisation **Voir les PII** n'est accessible qu'à quelques utilisateurs sélectionnés de l'entreprise. Par défaut, tous les administrateurs ont leur autorisation **Voir les PII** activée dans les autorisations utilisateur. Cela signifie qu'ils peuvent voir tous les attributs standard et personnalisés que votre entreprise a définis comme PII dans l'ensemble du tableau de bord. Lorsque cette autorisation est désactivée pour des utilisateurs, ces derniers ne peuvent voir aucun de ces attributs.

{% alert note %}
Vous avez besoin de l'autorisation **Voir les PII** pour utiliser le [Générateur de requêtes]({{site.baseurl}}/user_guide/analytics/reports/query_builder/building_queries), car il permet un accès direct à certaines données client.
{% endalert %}

Pour les capacités existantes d'autorisations d'équipe, consultez [Définir les autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

### Définition des PII {#defining-pii}

{% alert important %}
La sélection et la définition de certains champs comme champs PII n'affectent que ce que les utilisateurs peuvent voir sur le tableau de bord de Braze et n'ont aucun impact sur la manière dont les données des utilisateurs finaux dans ces champs PII sont traitées.<br><br>Consultez votre équipe juridique pour aligner les paramètres de votre tableau de bord avec les réglementations et politiques de confidentialité applicables à votre entreprise, y compris celles relatives à la [conservation des données]({{site.baseurl}}/data_retention).
{% endalert %}

Vous pouvez sélectionner les champs que votre entreprise désigne comme PII dans le tableau de bord. Pour ce faire, allez dans **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité**.

Les attributs suivants peuvent être désignés comme PII et masqués aux utilisateurs de l'entreprise qui ne disposent pas de l'autorisation **Voir les PII**.

#### Attributs PII potentiels {#potential-pii-attributes}

| Attributs standard | Attributs personnalisés |
| ------------------- | ----------------- |
| {::nomarkdown}<ul> <li>Adresse e-mail </li> <li> Numéro de téléphone </li> <li> Prénom </li> <li> Nom </li> <li> Genre </li> <li> Date de naissance </li> <li> ID d'appareil </li> <li> LINE ID </li> <li> Emplacement le plus récent </li> </ul> {:/} | {::nomarkdown} <ul> <li> Tous les attributs personnalisés<ul><li>Les attributs personnalisés individuels peuvent être marqués comme PII si vous n'avez pas besoin de masquer tous les attributs.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attributs PII potentiels" }

### Zones restreintes {#limited-areas}

Ce qui suit suppose que tous les champs sont définis comme PII et que les utilisateurs mentionnés sont des utilisateurs de l'entreprise qui utilisent la plateforme Braze. De plus, les attributs « précédents » font référence à ceux du tableau [Attributs PII potentiels](#potential-pii-attributes). La suppression des autorisations PII d'un utilisateur peut avoir un impact sur la convivialité au-delà de ces zones répertoriées.

| Navigation dans le tableau de bord | Résultat | Notes |
| -------------------- | ------ | ----- |
| Recherche d'utilisateurs | L'utilisateur connecté ne peut pas effectuer de recherche par adresse e-mail, numéro de téléphone, prénom ou nom : {::nomarkdown} <ul> <li> Les attributs standard et personnalisés précédents ne seront pas affichés lors de la consultation d'un profil utilisateur. </li> <li> Il ne peut pas modifier les attributs standard précédents d'un profil utilisateur depuis le tableau de bord de Braze. </li> <li> Il ne peut pas mettre à jour le statut d'abonnement d'un profil utilisateur. </li></ul> {:/} | L'accès à cette section nécessite toujours l'accès à la consultation d'un profil utilisateur. |
| Importation d'utilisateurs | L'utilisateur ne peut pas télécharger de fichiers depuis la page **Importation d'utilisateurs**. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | Dans le menu déroulant **Données utilisateur** : {::nomarkdown} <ul> <li> L'utilisateur n'aura pas l'option <b>Exporter les adresses e-mail en CSV</b>. </li> <li> L'utilisateur ne recevra pas les attributs standard et personnalisés précédents dans le fichier CSV lors de la sélection de <b>Exporter les données utilisateur en CSV</b>. </li> </ul> {:/} | |
| Groupe de test interne | L'utilisateur n'aura pas accès aux attributs standard précédents de tout utilisateur ajouté au groupe de test interne. | |
| Journal d'activité des messages | L'utilisateur n'aura pas accès aux attributs standard précédents pour tout utilisateur identifié dans le journal d'activité des messages. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zones restreintes" }

{% alert note %}
Lors de la prévisualisation d'un message, l'autorisation **Voir les PII** n'est pas appliquée, de sorte que les utilisateurs peuvent voir les [attributs standard précédents](#potential-pii-attributes) s'ils ont été référencés dans le message via Liquid.
{% endalert %}

## Préférences de suppression des données {#data-deletion-preferences}

Vous pouvez utiliser ce paramètre pour définir des préférences indiquant si Braze doit supprimer certains champs lors du processus de suppression d'utilisateur pour les événements. Ces préférences ne s'appliquent qu'aux données des utilisateurs que Braze a supprimés.

Lorsqu'un utilisateur est supprimé, Braze supprime toutes les PII des données d'événements mais conserve les données anonymisées à des fins d'analyse. Certains champs définis par l'utilisateur peuvent contenir des PII si vous envoyez des informations d'utilisateur final à Braze. Si ces champs contiennent des PII, vous pouvez choisir de supprimer les données lorsque Braze anonymise les données d'événements pour les utilisateurs supprimés ; si les champs ne contiennent pas de PII, vous pouvez les conserver pour l'analyse.

Vous êtes responsable de la détermination des préférences correctes pour votre espace de travail. La meilleure façon de déterminer les paramètres appropriés est de consulter les équipes internes qui envoient des données d'événements à Braze et les équipes qui utilisent les extras de message dans Braze pour confirmer si les champs peuvent contenir des PII.

### Champs concernés {#relevant-fields}

| Nom ou type d'événement | Champ | Notes |
| -------------------- | ------ | ----- |
| Événement personnalisé | properties |  |
| Événement d'achat | properties |  |
| Envoi de message | message_extras | Plusieurs types d'événements contiennent un champ `message_extras`. La préférence s'applique à tous les types d'événements d'envoi de message qui prennent en charge `message_extras`, y compris les types d'événements ajoutés à l'avenir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Champs concernés" }

{% alert warning %}
**La suppression est permanente !** Si vous choisissez de supprimer des champs de Snowflake pour les utilisateurs supprimés, le paramètre s'applique à toutes les données historiques de vos espaces de travail et à tous les événements pour les utilisateurs supprimés à l'avenir. Une fois que Braze a exécuté le processus pour appliquer les paramètres aux données d'événements historiques des utilisateurs supprimés, vous **ne pouvez pas restaurer** les données.
{% endalert %}

### Configurer les préférences {#configure-preferences}

Définissez les préférences par défaut en cochant les cases pour tous les champs que Braze doit supprimer si un utilisateur est supprimé. Sélectionnez tous les champs qui contiennent des PII. Cette préférence s'applique à tous les espaces de travail actuels et futurs, sauf si des espaces de travail sont explicitement ajoutés à un groupe de préférences.

Pour personnaliser les préférences par espace de travail, vous pouvez ajouter des groupes de préférences avec des paramètres différents de ceux par défaut. Les paramètres par défaut sont appliqués à tous les espaces de travail non ajoutés à un groupe de préférences supplémentaire, y compris les espaces de travail créés à l'avenir.

![Section Préférences de suppression des données avec le bouton activé pour personnaliser les préférences de suppression des données par espace de travail.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Résolution des problèmes {#troubleshooting}

### Problèmes de boucle lors de la configuration de l'authentification à deux facteurs (2FA) {#two-factor-authentication-2fa-setup-loop-issues}

Si vous vous retrouvez dans une boucle après avoir saisi avec succès votre numéro de téléphone pour la 2FA et êtes redirigé vers la page de connexion, cela est probablement dû à un échec de vérification lors de la première tentative. Pour résoudre ce problème, suivez ces étapes :

1. Désactivez tous les bloqueurs de publicités.
2. Activez les cookies dans les paramètres de votre navigateur.
3. Redémarrez votre PC ou ordinateur portable.
4. Tentez à nouveau de configurer la 2FA.

Si le problème persiste après ces étapes, contactez l'[Assistance]({{site.baseurl}}/braze_support) pour obtenir de l'aide.

### Impossible d'activer l'authentification à deux facteurs (2FA) {#cant-enable-two-factor-authentication-2fa}

Si la 2FA est activée mais que rien ne se passe lorsque vous sélectionnez le bouton **Activer**, cela peut être dû au fait que votre navigateur bloque la redirection nécessaire pour envoyer le code de vérification par SMS. Voici les étapes pour résoudre ce problème :

1. Suspendez temporairement tous les bloqueurs de publicités activés dans votre navigateur.
2. Confirmez que vous avez activé les cookies tiers dans les paramètres de votre navigateur.
3. Essayez de configurer la 2FA.

### Le code de vérification n'est pas envoyé {#verification-code-doesnt-send}

Si vous rencontrez des problèmes lors de la saisie de votre numéro de téléphone sur la page Authy et ne recevez pas de SMS, suivez ces étapes :

1. Installez l'application Authy sur votre téléphone et connectez-vous à l'authentificateur Authy.
2. Saisissez votre numéro de téléphone et vérifiez l'application Authy pour tout changement ou notification SMS.
3. Si vous ne recevez toujours pas le SMS, essayez d'utiliser une connexion réseau différente, comme votre réseau domestique ou un Wi-Fi non professionnel. Les réseaux d'entreprise peuvent avoir des politiques de sécurité qui interfèrent avec la réception des SMS.

Si les problèmes persistent, supprimez l'ancien profil dans l'application Authy et scannez à nouveau le code QR pour configurer la 2FA. Assurez-vous d'avoir désactivé tous les bloqueurs de publicités, activé les cookies tiers ou utilisé un autre navigateur avant de tenter à nouveau la configuration.

## Étapes suivantes {#next-steps}

Pour plus d'informations sur l'authentification et l'accès, consultez :

- [SAML et authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) pour configurer le SSO avec votre fournisseur d'identité.
- [Autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour contrôler les actions que les utilisateurs peuvent effectuer dans le tableau de bord.