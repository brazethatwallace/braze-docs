---
nav_title: À propos d'Audience Sync
article_title: À propos d'Audience Sync
alias: /partners/about_audience_sync/
description: "Cet article de référence vous explique comment utiliser la fonctionnalité Audience Sync de Braze vers Facebook, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 0
tool:
  - Canvas

---

# À propos d'Audience Sync {#about-audience-sync}

> La fonctionnalité Audience Sync de Braze vous permet d'étendre la portée de vos campagnes à de nombreuses technologies sociales et publicitaires de premier plan. Grâce à [Braze Canvas]({{site.baseurl}}/user_guide/messaging/canvas/), les marques peuvent synchroniser de manière dynamique et sécurisée les données first-party des utilisateurs dans l'écosystème publicitaire afin de favoriser l'efficacité marketing et opérationnelle.

## Disponibilité de la fonctionnalité {#feature-availability}

Tous les clients de Braze ont immédiatement accès à Audience Sync vers Google et Facebook, mais les clients qui utilisent des crédits d'action peuvent accéder à l'ensemble des partenaires Audience Sync. Pour débloquer des destinations Audience Sync supplémentaires pour les clients qui n'utilisent pas de crédits d'action, achetez Audience Sync Pro. Contactez votre gestionnaire de compte Braze pour plus de détails.

## Cas d'utilisation {#use-cases}

- Cibler les utilisateurs à forte valeur ajoutée via des canaux propriétaires et payants pour générer des achats ou un engagement incrémentaux.
- Créer des audiences lookalike de vos utilisateurs à forte valeur ajoutée pour optimiser les coûts par acquisition de nouveaux utilisateurs et les conversions.
- Recibler avec des publicités les utilisateurs moins réactifs aux autres canaux marketing.
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités alors qu'ils sont déjà des consommateurs fidèles de votre marque.

## Aperçu {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Destination | Délai de correspondance des membres de l'audience | Limite de débit | Lookalike ou actalike | Conseils |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | Jusqu'à 24 heures | 250 000 demandes par minute. Les données sont regroupées toutes les 5 secondes, avec une relance automatique basée sur les retours de Google. | Oui | {::nomarkdown}<ul><li>Criteo prend en charge jusqu'à 1 000 audiences publicitaires.</li><li>La taille minimale de l'audience est de 500 personnes, et la taille recommandée est de plus de 20 000 personnes.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | Jusqu'à 24 heures | 190 000 comptes publicitaires par heure | Oui | {::nomarkdown}<ul><li>Facebook prend en charge jusqu'à 500 audiences publicitaires.</li><li>Facebook exige que les audiences soient composées d'au moins 1 000 utilisateurs.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | Entre 6 et 12 heures | Les données sont regroupées toutes les 5 secondes, avec une relance automatique basée sur les retours de Google. | Non | {::nomarkdown}<ul><li><b>Customer match :</b> Utilisez soit l'identifiant publicitaire mobile, soit l'adresse e-mail ou le numéro de téléphone.</li><li>Google Audiences nécessite au moins 5 000 utilisateurs pour commencer à diffuser des annonces.</li><li>La taille de l'audience affichera zéro tant qu'il n'y aura pas au moins 1 000 utilisateurs.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 heures | LinkedIn traite 10 requêtes par seconde et 100 000 utilisateurs par demande. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Audiences prédictives par intelligence artificielle | {::nomarkdown}<ul><li>La taille minimale de l'audience est de 300 membres, le ciblage par localisation étant pris en considération.</li><li>LinkedIn affiche le taux de correspondance dans le tableau de bord de Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | Entre 24 et 48 heures | Pinterest traite 7 requêtes par seconde et 1 900 utilisateurs par demande. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Oui | Les audiences Pinterest nécessitent au moins 100 utilisateurs. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | S.O. | Snapchat traite 10 requêtes par seconde et 100 000 utilisateurs par requête. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Oui | Snapchat prend en charge jusqu'à 1 000 audiences publicitaires. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/) | Jusqu'à 24 heures | S.O. | Oui | {::nomarkdown}<ul><li>Il n'y a pas de taille minimale d'audience pour les audiences CRM dans The Trade Desk.</li><li>Il n'y a pas de limite au nombre d'audiences prises en charge par The Trade Desk.</li><li>Si vous synchronisez vers une audience dont la région est définie sur l'UE, le numéro de téléphone n'est pas pris en charge.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | Entre 24 et 48 heures | TikTok traite 50 requêtes par seconde et 10 000 utilisateurs par demande. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Oui | {::nomarkdown}<ul><li>TikTok prend en charge jusqu'à 400 audiences publicitaires.</li><li>Les audiences TikTok nécessitent au moins 1 000 utilisateurs pour commencer à diffuser des publicités.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Aperçu" }
<sup>Lorsque la limite de débit est atteinte, Braze effectue une nouvelle tentative de synchronisation pendant 13 heures.</sup>

## Fonctionnement {#how-it-works}

Pour utiliser Audience Sync vers Google ou Facebook, connectez votre compte publicitaire en recherchant le partenaire sur la page **Partenaires technologiques**.

![Partenaire technologique Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Partenaire technologique Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Après avoir connecté votre compte publicitaire, vous pouvez créer un Canvas avec une étape Audience Sync.

![Menu des composants Canvas pour ajouter l'étape Audience Sync au parcours utilisateur.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Sélectionnez ensuite le partenaire avec lequel synchroniser les audiences.

![Option permettant de sélectionner votre partenaire de synchronisation d'audience dans l'étape Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Pour chaque partenaire, vous devez configurer les éléments suivants dans le cadre de votre étape Audience Sync :

- Compte publicitaire
- Audience
- Action d'ajout ou de suppression d'utilisateurs
- Champs à faire correspondre

Gardez à l'esprit que Braze synchronisera les utilisateurs dès qu'ils entreront dans l'étape Audience Sync de votre Canvas.

Pour chaque destination Audience Sync, le partenaire peut avoir des exigences différentes quant aux champs pouvant être envoyés. Reportez-vous à la documentation spécifique du partenaire pour plus de détails.

### Audience Sync Pro

Pour utiliser un partenaire Audience Sync Pro, notamment TikTok, Pinterest, Snapchat ou Criteo, vous pourrez sélectionner vos partenaires en fonction de vos attributions d'achat Audience Sync Pro dans la section **Audience Sync Pro** de la page **Partenaires technologiques**.

![Audience Sync Pro sans partenaire sélectionné pour l'instant.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Commencez par sélectionner les partenaires que vous souhaitez utiliser en cliquant sur **Select Partners**. Chaque achat d'Audience Sync Pro vous donne droit à 3 destinations Audience Sync Pro, disponibles dans chacun de vos espaces de travail au sein de votre tableau de bord.

![Possibilité de sélectionner jusqu'à trois partenaires à connecter à Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Après avoir sélectionné vos destinations Audience Sync Pro, connectez le compte publicitaire du partenaire choisi en cliquant sur la vignette du partenaire.

![Exemple avec Snapchat et TikTok sélectionnés comme partenaires pour Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Paramètres Audience Sync de Snapchat avec le message : « You successfully connected 1 Snapchat account ».]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Enfin, créez votre étape Audience Sync dans Canvas en utilisant cette destination Audience Sync Pro.

### Regroupement par lots et latence {#batching-and-latency}

Lorsque les utilisateurs entrent dans une étape Audience Sync dans Canvas, Braze les place dans une file d'attente au sein d'un système de regroupement par lots qui agrège les mises à jour utilisateur avant de les envoyer à l'API du partenaire. Un lot est envoyé lorsque l'une des conditions suivantes est remplie :

- **Le lot atteint sa limite de taille.** Celle-ci varie selon le partenaire :
  - Par défaut, jusqu'à 2 000 utilisateurs
  - Google Ads prend en charge jusqu'à 10 000 utilisateurs
  - Facebook et TikTok prennent en charge jusqu'à 2 000 utilisateurs
- **Le délai de latence du lot expire.** La valeur par défaut est d'une heure, mais elle est configurable par partenaire. Par exemple, The Trade Desk utilise 10 minutes.

Les Canvas à fort volume peuvent envoyer des lots plus rapidement, car ceux-ci se remplissent plus vite. Les Canvas à faible volume attendent l'expiration du délai de latence. Braze ne garantit pas un délai d'envoi fixe ; le timing dépend de la taille du lot et de la fenêtre de latence configurée.

Braze enregistre l'activité d'envoi dans des journaux internes à des fins de surveillance et de résolution des problèmes, mais ces horodatages ne sont pas exposés en tant que champs interrogeables. Après l'envoi d'un lot par Braze à l'API du partenaire, celui-ci traite la mise à jour de l'audience conformément à ses propres accords de niveau de service, généralement entre 6 et 48 heures.

Braze ne reçoit pas de confirmation de la part des partenaires indiquant que des utilisateurs individuels ont été mis en correspondance ou synchronisés. Les réponses des partenaires sont des accusés de réception HTTP, et non des confirmations de correspondance. Pour vérifier qu'une audience a été alimentée, consultez la plateforme publicitaire du partenaire (comme Google Ads Audience Manager ou Meta Business Manager).

### E-mails d'erreur d'Audience Sync {#audience-sync-error-emails}

Si l'erreur est liée à l'intégration globale du partenaire (comme un problème d'autorisation), un e-mail est envoyé à l'utilisateur qui a connecté l'intégration. Si cet utilisateur n'existe plus, les administrateurs recevront les e-mails.

Si l'erreur est liée à des problèmes avec le composant Audience Sync (tel que « Audience Does Not Exist ») dans Canvas, un e-mail est envoyé à l'utilisateur qui a configuré le Canvas. Si cet utilisateur n'existe plus, l'e-mail est transmis à l'administrateur de la société.

Pour configurer les destinataires de ces e-mails, contactez votre gestionnaire de la satisfaction client afin d'ajouter des destinataires sous **Préférences de notification**. Cette fonctionnalité modifiant le comportement actuel, vous devrez immédiatement ajouter des destinataires à cette nouvelle préférence de notification, car Braze n'inscrit personne par défaut. Veillez à ce qu'aucun e-mail d'erreur ne soit manqué.

## Considérations relatives à la confidentialité des données {#data-privacy-considerations}

{% alert important %}
Cette documentation n'a pas pour but de fournir des conseils juridiques et ne peut être considérée comme telle. L'utilisation d'Audience Sync est soumise à des exigences légales spécifiques. Pour vous assurer que vous l'utilisez en conformité avec toutes les lois applicables, vous devez demander l'avis de votre conseiller juridique.
{% endalert %}

Lorsque vous créez des audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et vous conformer aux lois sur la protection de la vie privée, telles que le droit « Ne pas vendre ou partager » en vertu de la [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs devraient implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée de Canvas. Voici quelques options.

Si vous avez collecté l'[IDFA iOS via le SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pourrez utiliser le filtre « Ads Tracking Enabled ». Sélectionnez la valeur `true` afin d'envoyer uniquement les utilisateurs vers les destinations Audience Sync où ils ont donné leur consentement.

![Un Canvas dont l'audience d'entrée est « Ad Tracking Enabled is true ».]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Si vous collectez `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devez les inclure dans les critères d'entrée de votre Canvas en tant que filtre :

![Un Canvas dont l'audience d'entrée est « opted_in_marketing equals true ».]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Pour en savoir plus sur la manière de vous conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez [Assistance technique à la protection des données]({{site.baseurl}}/dp-technical-assistance/).

## Gérer le consentement pour le ciblage publicitaire {#managing-consent-for-ad-targeting}

En tant qu'annonceur, il vous incombe de gérer le consentement au suivi publicitaire ou au ciblage de vos utilisateurs.

Pour envoyer des publicités à vos utilisateurs, vous devez vous conformer à toutes les lois et réglementations applicables, ainsi qu'aux politiques et exigences de la plateforme publicitaire. N'utilisez Braze pour cibler et synchroniser les utilisateurs que lorsque vous avez obtenu leur consentement.

Pour maintenir à jour vos listes d'audience sur ces plateformes publicitaires et supprimer les utilisateurs qui ont révoqué leur consentement, configurez un Canvas pour retirer les utilisateurs de ces listes d'audience existantes à l'aide d'une étape Audience Sync.