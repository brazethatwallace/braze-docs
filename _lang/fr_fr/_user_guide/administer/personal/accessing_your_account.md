---
nav_title: Accéder à votre compte
article_title: Accéder à votre compte
page_order: 0
page_type: reference
description: "Cet article explique comment obtenir votre compte Braze, comment vous connecter après avoir reçu l'accès et comment résoudre les problèmes d'accès et de performance du tableau de bord."

---

# Accéder à votre compte {#access-your-account}

> Cet article explique comment obtenir votre compte Braze, comment vous connecter après avoir reçu l'accès et comment résoudre les problèmes d'accès et de performance du tableau de bord.

Si vous êtes le premier utilisateur Braze de votre entreprise et que vous vous connectez pour la première fois, vous recevrez un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre adresse e-mail et de vous connecter le premier jour de votre contrat.

Après avoir confirmé votre compte, vous pouvez ajouter des utilisateurs supplémentaires depuis la page [Utilisateurs de l'entreprise]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) de votre tableau de bord. Tous les utilisateurs reçoivent un e-mail leur demandant de confirmer leur compte après avoir été ajoutés.

Si vous n'êtes pas le premier utilisateur du compte Braze de votre entreprise, contactez l'administrateur du compte Braze de votre entreprise et demandez-lui de créer votre compte. Vous recevrez alors un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre adresse e-mail et de vous connecter.

## Connexion {#logging-in}

Que ce soit votre première connexion ou la centième, voici comment accéder à votre tableau de bord. Si vous êtes le premier utilisateur de votre entreprise, suivez les instructions de la section précédente. Sinon, vous pouvez vous connecter une fois que l'administrateur Braze de votre entreprise a créé votre compte.

Vous pouvez vous connecter depuis le site [Braze.com](https://www.braze.com), ou utiliser l'URL de votre tableau de bord correspondant à votre [instance Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) spécifique. Pour plus de commodité, Braze propose plusieurs options d'authentification unique (SSO), telles que :

* [Authentification unique (SSO) SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [Provisionnement juste-à-temps SAML]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [SSO Microsoft Entra]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

Une fois connecté à Braze via le SSO, vous ne pouvez plus utiliser votre mot de passe pour vous connecter au tableau de bord. Les deux adresses e-mail dirigeront les e-mails vers la même boîte de réception, mais Braze les reconnaîtra comme des comptes distincts lors de la connexion. La suppression des cookies vous déconnectera, et tout travail non enregistré sera perdu.

## Navigateurs pris en charge {#supported-browsers}

Le tableau de bord de Braze prend en charge les navigateurs suivants :
- Chrome (version 87 ou ultérieure)
- Firefox (version 85 ou ultérieure)
- Safari (version 15.4 ou ultérieure)
- Edge (version 87 ou ultérieure)

Si votre tableau de bord de Braze affiche une erreur inattendue et que l'outil de console de votre navigateur indique l'erreur `ReferenceError: structuredClone is not defined`, votre navigateur est obsolète. Si cette erreur persiste, désinstallez puis réinstallez votre navigateur.

## Accéder à plusieurs tableaux de bord Braze {#accessing-multiple-braze-dashboards}

Braze ne vous permet pas d'enregistrer la même adresse e-mail pour plusieurs utilisateurs du tableau de bord dans le même cluster (par exemple, si vous avez deux tableaux de bord sur US-01). Vous pouvez utiliser le même e-mail pour créer des comptes sur différents clusters (par exemple, si vous avez un tableau de bord sur US-01 et un autre sur US-05). Si vous devez accéder à plusieurs tableaux de bord Braze dans le même cluster, vous pouvez procéder comme suit :

### Utiliser des alias d'e-mail {#use-email-aliases}

Si votre fournisseur de messagerie est Gmail, vous pouvez créer des alias en ajoutant un signe `+` suivi de n'importe quel texte à votre adresse e-mail. Par exemple :
- **E-mail d'origine :** `rocky@gmail.com`
- **Alias d'e-mail :** `rocky+1@gmail.com`

Les deux adresses e-mail dirigent les messages vers la même boîte de réception, mais Braze les reconnaît comme des comptes distincts lorsque vous vous connectez.

### Créer des alias distincts avec d'autres fournisseurs {#create-separate-aliases-with-other-providers}

Si votre fournisseur de messagerie ne prend pas en charge l'aliasing avec `+`, vous pouvez tout de même créer des alias distincts, par exemple en configurant `rocky@braze.com` pour qu'il redirige vers `rocky.lotito@braze.com`. Cela permet à plusieurs adresses de converger vers la même boîte de réception tout en étant reconnues comme des e-mails différents par Braze.

### Utiliser les développeurs multi-entreprises {#use-multi-company-developers}

La fonctionnalité de développeurs multi-entreprises permet de partager un seul compte utilisateur entre plusieurs entreprises. Les utilisateurs du tableau de bord peuvent basculer entre les tableaux de bord de différentes entreprises depuis le menu de leur profil utilisateur.

Si vous utilisez l'authentification unique (SSO) et souhaitez configurer les développeurs multi-entreprises, vous devez activer un identifiant d'entité SAML personnalisé en mettant en place une intégration SSO SAML personnalisée. Suivez les étapes décrites dans [Connexion initiée par le fournisseur de services (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), mais appliquez les modifications suivantes :
- Remplacez l'**Entity ID** par `braze_dashboard_<companyID>` pour chaque intégration de tableau de bord.
- Contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer le feature flipper `saml_sso_custom_entity_id` pour chaque tableau de bord.

#### Authentification à deux facteurs (2FA) {#two-factor-authentication-2fa}

Le fonctionnement de la 2FA pour les développeurs multi-entreprises dépend de votre méthode de 2FA :

- **E-mail et SMS :** Vos paramètres de 2FA sont copiés sur tous les comptes développeur liés. Après avoir configuré la 2FA par e-mail ou SMS sur un compte, la même méthode s'applique à l'ensemble de vos tableaux de bord d'entreprise.
- **Mot de passe à usage unique basé sur le temps (TOTP) :** Les paramètres TOTP ne sont pas synchronisés entre les comptes. Si vous utilisez une application d'authentification, vous devez configurer un code distinct pour chaque tableau de bord auquel vous vous connectez directement.

Lorsque vous basculez entre les comptes depuis le tableau de bord, vous n'avez besoin de compléter la 2FA qu'une seule fois — la première fois que vous vous connectez à un compte lié au cours de cette session.

### Considérations relatives à l'authentification unique (SSO) {#considerations-for-single-sign-on-sso}

Si vous utilisez l'authentification unique (SSO), sachez que le fait d'avoir plusieurs adresses e-mail différentes pourrait entraîner des complications. Vérifiez que vos paramètres SSO sont correctement configurés pour éviter les problèmes d'accès.

## Résolution des problèmes {#troubleshooting}

### Réinitialiser votre mot de passe {#resetting-your-password}

Pour réinitialiser votre mot de passe, sélectionnez le lien **Forgot your password?** sur la page de connexion du tableau de bord. Vous serez invité à saisir votre adresse e-mail pour recevoir un lien de réinitialisation de votre mot de passe.

![Page de connexion du tableau de bord avec l'invite « Forgot your password? ».]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Vider le cache et les cookies de votre navigateur {#clearing-your-browser-cache-and-cookies}

Si vous rencontrez des problèmes de performance du tableau de bord, comme le non-chargement de votre tableau de bord ou de la liste de performance des Segments, essayez de vider le cache et les cookies de votre navigateur en suivant les étapes correspondant à votre navigateur.

{% alert important %}
La suppression des cookies vous déconnecte, et tout travail non enregistré sera perdu.
{% endalert %}

- [Vider le cache et les cookies dans Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Supprimer les cookies dans Safari sur Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Supprimer les cookies et les données de site dans Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Supprimer tous les cookies dans Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si vider le cache et les cookies de votre navigateur ne résout pas vos problèmes, contactez le [Support]({{site.baseurl}}/support_contact).

### Erreur « Aw, Snap! » dans Google Chrome {#aw-snap-error-in-google-chrome}

Si Google Chrome affiche une erreur « Aw, Snap! », Chrome a des difficultés à charger la page du tableau de bord de Braze. Pour les étapes de résolution des problèmes, consultez [Obtenir de l'aide pour les messages d'erreur courants dans Chrome](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en).

### « Please Refresh Page » ou « Unexpected Error » lors de la navigation dans le tableau de bord {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

Cette erreur peut apparaître lorsqu'un utilisateur de l'entreprise n'appartient à aucun espace de travail. Pour résoudre le problème :

1. Accédez à la page [Utilisateurs de l'entreprise]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users).
2. Vérifiez si l'utilisateur a été ajouté à un espace de travail.
3. S'il ne fait partie d'aucun espace de travail, ajoutez-le et attribuez-lui les permissions appropriées.
4. Demandez à l'utilisateur d'actualiser son tableau de bord.
5. Si le problème persiste, contactez le [Support]({{site.baseurl}}/support_contact).

### Accéder à l'éditeur par glisser-déposer {#accessing-the-drag-and-drop-editor}

Pour la plupart des utilisateurs de l'entreprise, l'éditeur par glisser-déposer devrait se charger. Cependant, si vous utilisez un VPN ou êtes derrière un pare-feu, vous devrez peut-être ajouter un domaine à la liste d'autorisation. Contactez votre administrateur informatique pour vérifier que `*.bz-rndr.com` est autorisé.

L'éditeur peut rencontrer des problèmes de chargement pour les raisons suivantes :

- **Erreur transitoire :** il s'agit de défaillances temporaires qui peuvent affecter la connectivité, la communication ou le transfert de données. Heureusement, elles se résolvent généralement d'elles-mêmes sans nécessiter d'intervention significative, car elles sont souvent causées par des conditions de courte durée et n'indiquent pas de problèmes systémiques.
- **Erreur majeure :** cela peut impliquer un problème d'infrastructure ou de produit sous-jacent. Vous pouvez consulter notre [page de statut du système Braze](https://braze.statuspage.io/) car nous sommes probablement au courant de la situation et travaillons activement à sa résolution.

{% alert important %}
Si vous rencontrez toujours des problèmes, [ouvrez un ticket de support]({{site.baseurl}}/user_guide/administer/personal/braze_support). Avant de le faire, vérifiez que votre administrateur informatique a confirmé que `*.bz-rndr.com` est autorisé de votre côté.
{% endalert %}

### Accéder à Braze Learning {#accessing-braze-learning}

Si vous rencontrez des problèmes de connexion à Braze Learning et que vous êtes bloqué dans une boucle qui vous redirige vers le tableau de bord, suivez ces étapes :

1. Si vous avez plusieurs comptes Braze, vous connecter avec le mauvais compte deux fois vous renvoie vers le tableau de bord de Braze. Confirmez que vous vous connectez au bon compte.
2. Si vous avez un bloqueur de publicités, confirmez qu'il est désactivé. Il peut bloquer les cookies nécessaires au fonctionnement de l'authentification unique.
3. Accédez à **Paramètres de l'entreprise** > **Paramètres de sécurité** et vérifiez que l'authentification unique (SSO) est activée.
4. Confirmez que votre profil utilisateur du tableau de bord inclut à la fois un prénom et un nom de famille. L'absence de nom de famille peut perturber le processus de connexion.
5. Accédez à Braze Learning depuis votre tableau de bord en allant dans **Support** > **Braze Learning**.
6. Si vous continuez à rencontrer des problèmes, envisagez de recréer votre compte. Les utilisateurs qui ont accédé à Braze Learning pendant la phase d'essai gratuit peuvent avoir des difficultés à y accéder maintenant.

### Problèmes d'authentification à deux facteurs (2FA) {#two-factor-authentication-2fa-issues}

Si un utilisateur rencontre des problèmes avec l'authentification à deux facteurs (2FA) et ne peut pas accéder au tableau de bord de Braze, cela peut être dû à plusieurs raisons. Le plus souvent, il n'a peut-être plus accès au numéro de téléphone enregistré ou à l'appareil sur lequel l'application Authy est installée.

Un administrateur doit réinitialiser la 2FA pour l'utilisateur concerné en procédant comme suit :

1. Accédez à **Gérer les utilisateurs**.
2. Sélectionnez **Modifier l'utilisateur** pour l'utilisateur rencontrant des problèmes de 2FA.
3. Choisissez l'option pour réinitialiser la 2FA.
4. Confirmez la réinitialisation de la 2FA lorsque vous y êtes invité.
5. Si la réinitialisation ne résout pas immédiatement le problème, videz vos cookies et votre cache.

Braze ne peut pas réinitialiser la 2FA au nom des utilisateurs pour des raisons de sécurité. Si l'administrateur n'est pas en mesure de réinitialiser la 2FA, créez un ticket de support.

#### Considérations {#considerations}

- Si la 2FA est imposée au niveau de l'entreprise : après la réinitialisation, Braze invite l'utilisateur à configurer à nouveau sa 2FA lors de sa prochaine connexion.
- Si la 2FA n'est pas imposée au niveau de l'entreprise : l'utilisateur se connecte au tableau de bord sans avoir besoin de reconfigurer la 2FA. S'il souhaite activer la 2FA, il peut le faire dans les paramètres du compte.

{% alert note %}
Ce processus de réinitialisation s'applique également aux utilisateurs qui ont été verrouillés de leur compte pour avoir demandé trop de jetons au cours de la dernière heure.
{% endalert %}

### Compte verrouillé {#locked-out-of-account}

Si vous êtes verrouillé de votre compte Braze, vous pouvez y accéder à nouveau en suivant ces étapes.

Vous pouvez identifier le type de verrouillage que vous rencontrez grâce au message d'erreur que vous recevez :

- [Je vois une erreur concernant mon mot de passe.](#password-error)
- [Je ne vois pas d'erreur, mais Braze ne me laisse toujours pas entrer.](#instance-error)
- [Je vois une erreur concernant la suspension du compte.](#account-suspension)

#### Erreur de mot de passe {#password-error}

La sécurité de votre compte est importante pour nous, c'est pourquoi un mot de passe est requis pour vous connecter à votre compte Braze.
- Vérifiez que vous vous connectez à la bonne [instance du tableau de bord de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Vérifiez auprès de votre administrateur de compte ou de votre gestionnaire de compte Braze pour vous en assurer.
- Votre mot de passe a peut-être expiré, vous devez donc le [réinitialiser](#resetting-your-password).
- Si vous utilisez un service d'[authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup), vérifiez auprès de votre administrateur de compte que la configuration a été effectuée correctement.
- Si votre entreprise utilise plusieurs instances de Braze, vous utilisez peut-être la mauvaise adresse e-mail pour vous connecter.

En cas de doute, vous pouvez toujours [réinitialiser votre mot de passe](#resetting-your-password).

#### Erreur d'instance {#instance-error}

Si vous utilisez la même machine que d'habitude pour vous connecter, Braze devrait automatiquement détecter la bonne instance. Cependant, si ce n'est pas le cas ou si vous vous connectez pour la première fois, tenez compte des éléments suivants :

- Vérifiez que vous vous connectez à la bonne [instance du tableau de bord de Braze]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Vérifiez auprès de votre administrateur de compte ou de votre gestionnaire de compte Braze pour vous en assurer.
- Si votre entreprise utilise plusieurs instances de Braze, vous utilisez peut-être la mauvaise adresse e-mail pour vous connecter.

#### Suspension du compte {#account-suspension}

Cela n'arrive pas très souvent, mais Braze prend la suspension et la suppression de comptes très au sérieux. Si vous rencontrez cette erreur, contactez l'administrateur Braze de votre entreprise, votre gestionnaire de compte Braze ou le [Support][support].

### Le tableau de bord de Braze ne se charge pas ou ne fonctionne pas comme prévu {#braze-dashboard-wont-load-or-work-as-expected}

Tout d'abord, testez si le tableau de bord se charge dans un autre navigateur. Si le problème ne persiste pas dans un autre navigateur, essayez ce qui suit :

- **Relancez le tableau de bord :** déconnectez-vous, quittez votre navigateur, puis essayez de vous reconnecter à votre tableau de bord.
- **Actualisez votre navigateur local :** [videz vos cookies et le cache de votre navigateur](#clearing-your-browser-cache-and-cookies), puis essayez de vous reconnecter à votre tableau de bord.
- **Utilisez des plugins ou outils tiers compatibles :** les bloqueurs de publicités ou les logiciels de sécurité peuvent empêcher le chargement du tableau de bord de Braze. Testez cela en désactivant un bloqueur de publicités, puis en vous connectant à votre tableau de bord de Braze.
        - Vous pouvez également vérifier les journaux de la console de votre navigateur. Les erreurs liées à `ERR_BLOCKED_BY_CLIENT` peuvent indiquer que le contenu est bloqué par un bloqueur de publicités.
- **Vérifiez la qualité de votre connexion :** la qualité de votre connexion peut être mauvaise. Essayez de vous connecter à votre tableau de bord de Braze sur un autre appareil.
- **Confirmez que vous accédez au bon cluster :** assurez-vous que vous vous connectez au cluster attribué à votre entreprise. Par exemple, vous êtes peut-être assigné à US-03, mais vous vous connectez à US-01.
- **Mettez à jour votre navigateur :** mettez à jour votre navigateur vers la dernière version des [navigateurs pris en charge](#supported-browsers), puis essayez de vous reconnecter à votre tableau de bord.

Si le problème se produit sur tous les navigateurs, essayez ce qui suit :

- **Vérifiez votre connexion réseau :** essayez de désactiver votre VPN, si possible, ou désactivez puis réactivez votre connexion réseau.
- **Redémarrez votre appareil :** essayez de vous connecter à votre tableau de bord de Braze après avoir redémarré votre appareil.

Si vous avez résolu les problèmes précédents et que votre tableau de bord ne se charge toujours pas ou ne fonctionne pas comme prévu, contactez le [Support]({{site.baseurl}}/braze_support).

### L'utilisateur n'appartient à aucun espace de travail {#the-user-belongs-to-no-workspace}

Vérifiez cela en accédant à **Paramètres** > **Utilisateurs de l'entreprise** et en vérifiant les permissions au niveau de l'espace de travail de l'utilisateur. Ajoutez les espaces de travail nécessaires dans **Espaces de travail**.

### Résolution des problèmes en tant que nouvel utilisateur {#troubleshooting-as-a-new-user}

Si vous êtes un nouvel utilisateur de Braze et que vous avez des difficultés à vous connecter ou à accéder à votre compte pour la première fois, suivez ces étapes pour résoudre les problèmes courants :

#### Je n'ai jamais reçu l'e-mail de bienvenue {#i-never-received-the-welcome-email}

- Vérifiez votre dossier de spam : confirmez que l'e-mail d'activation du compte n'a pas été filtré dans votre dossier de spam ou de courrier indésirable.
- Vérifiez votre adresse e-mail : demandez à votre administrateur de vérifier l'adresse e-mail associée à votre nouveau compte Braze pour confirmer qu'elle est correcte.
- Politiques informatiques : confirmez auprès de votre équipe informatique qu'il n'y a pas de politiques en place qui pourraient empêcher la réception de l'e-mail d'activation.

#### J'ai reçu l'e-mail, mais je suis bloqué lors de la configuration de l'authentification à deux facteurs (2FA) {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- Réinitialiser la 2FA : si vous avez des difficultés à configurer la 2FA, votre administrateur peut réinitialiser la 2FA pour votre compte utilisateur dans les paramètres.
- Rajouter l'utilisateur : si les problèmes persistent, l'administrateur peut supprimer votre compte utilisateur du tableau de bord et vous rajouter. Cela permet de recréer l'utilisateur avec les mêmes informations.

Si les problèmes persistent après ces étapes, contactez le [Support]({{site.baseurl}}/braze_support) pour obtenir une assistance supplémentaire.

## Étapes suivantes {#next-steps}

Après avoir accédé à votre compte, explorez ces ressources :

- [Le tableau de bord de Braze]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard) pour apprendre à naviguer parmi les fonctionnalités et outils clés.
- [Paramètres de langue]({{site.baseurl}}/user_guide/administer/personal/language_settings) pour définir la langue de votre tableau de bord.