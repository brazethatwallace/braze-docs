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

> La fonctionnalité Audience Sync de Braze vous permet d'étendre la portée de vos campagnes à de nombreuses technologies sociales et publicitaires de premier plan. Grâce à [Braze Canvas]({{site.baseurl}}/user_guide/messaging/canvas), les marques peuvent synchroniser de manière dynamique et sécurisée les données first-party des utilisateurs dans l'écosystème publicitaire afin de favoriser l'efficacité marketing et opérationnelle.

## Disponibilité de la fonctionnalité {#feature-availability}

Tous les clients Braze ont immédiatement accès à Audience Sync pour Google et Facebook, mais les clients disposant de crédits d'action peuvent accéder à tous les partenaires Audience Sync. Pour débloquer des destinations Audience Sync supplémentaires pour les clients ne disposant pas de crédits d'action, achetez Audience Sync Pro. Contactez votre gestionnaire de compte Braze pour plus de détails.

## Cas d'usage {#use-cases}

- Cibler les utilisateurs à forte valeur via des canaux propriétaires et payants pour générer des achats ou un engagement incrémentaux.
- Créer des audiences similaires à partir de vos utilisateurs à forte valeur pour optimiser les coûts d'acquisition et les conversions de nouveaux utilisateurs.
- Recibler avec des publicités les utilisateurs moins réceptifs aux autres canaux marketing.
- Créer des audiences de suppression pour éviter que les utilisateurs ne reçoivent des publicités lorsqu'ils sont déjà des consommateurs fidèles de votre marque.

## Aperçu {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Destination | Délai de correspondance des membres de l'audience | Limite de débit | Audiences similaires ou actalike | Conseils |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | Jusqu'à 24 heures | 250 000 requêtes par minute. Regroupées par lots toutes les 5 secondes avec une nouvelle tentative automatique. | Oui | {::nomarkdown}<ul><li>Criteo prend en charge jusqu'à 1 000 audiences publicitaires.</li><li>La taille minimale de l'audience est de 500, et la taille recommandée est supérieure à 20 000.</li></ul>{:/} |
| [Facebook ou Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | Jusqu'à 24 heures | 190 000 comptes publicitaires par heure | Oui | {::nomarkdown}<ul><li>Facebook prend en charge jusqu'à 500 audiences publicitaires.</li><li>Facebook exige que les audiences comptent au moins 1 000 utilisateurs.</li></ul>{:/} |
| [Google Ads ou YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | Entre 6 et 12 heures | Regroupées par lots toutes les 5 secondes avec une nouvelle tentative automatique basée sur le retour de Google | Non | {::nomarkdown}<ul><li><b>Customer match :</b> Utilisez soit l'identifiant publicitaire mobile, soit l'adresse e-mail ou le numéro de téléphone.</li><li>Les audiences Google nécessitent au moins 5 000 utilisateurs pour commencer à diffuser des publicités.</li><li>La taille de l'audience affichera zéro tant qu'il n'y aura pas au moins 1 000 utilisateurs.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48 heures | LinkedIn traite 10 requêtes par seconde et 100 000 utilisateurs par requête. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Audiences prédictives par IA | {::nomarkdown}<ul><li>La taille minimale de l'audience est de 300 membres, en tenant compte du ciblage géographique.</li><li>LinkedIn affiche le taux de correspondance dans le tableau de bord de Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | Entre 24 et 48 heures | Pinterest traite 7 requêtes par seconde et 1 900 utilisateurs par requête. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Oui | Les audiences Pinterest nécessitent au moins 100 utilisateurs. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchat traite 10 requêtes par seconde et 100 000 utilisateurs par requête. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Oui | Snapchat prend en charge jusqu'à 1 000 audiences publicitaires. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | Jusqu'à 24 heures | N/A | Oui | {::nomarkdown}<ul><li>Il n'y a pas de taille minimale d'audience pour les audiences CRM dans The Trade Desk.</li><li>Il n'y a pas de limite au nombre d'audiences prises en charge par The Trade Desk.</li><li>Si vous synchronisez vers une audience dont la région est définie sur l'UE, le numéro de téléphone n'est pas pris en charge.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | Entre 24 et 48 heures | TikTok traite 50 requêtes par seconde et 10 000 utilisateurs par requête. Braze regroupe les utilisateurs par lots toutes les 5 secondes. | Oui | {::nomarkdown}<ul><li>TikTok prend en charge jusqu'à 400 audiences publicitaires.</li><li>Les audiences TikTok nécessitent au moins 1 000 utilisateurs pour commencer à diffuser des publicités.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Aperçu" }
<sup>Lorsque la limite de débit est atteinte, Braze relance les synchronisations pendant 13 heures.</sup>

## Fonctionnement {#how-it-works}

Pour utiliser Audience Sync avec Google ou Facebook, connectez votre compte publicitaire en recherchant le partenaire sur la page **Technology Partners**.

![Partenaire technologique Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Partenaire technologique Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Après avoir connecté votre compte publicitaire, vous pouvez créer un Canvas avec une étape Audience Sync.

![Menu des composants Canvas pour ajouter l'étape Audience Sync au parcours utilisateur.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

Ensuite, sélectionnez le partenaire avec lequel synchroniser les audiences.

![Option de sélection de votre partenaire de synchronisation d'audience dans l'étape Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Pour chaque partenaire, vous devrez configurer les éléments suivants dans le cadre de votre étape Audience Sync :

- Compte publicitaire
- Audience
- Action pour ajouter ou supprimer des utilisateurs
- Champs à faire correspondre

Gardez à l'esprit que Braze synchronise les utilisateurs dès qu'ils entrent dans l'étape Audience Sync de votre Canvas.

Pour chaque destination Audience Sync, le partenaire peut avoir des exigences différentes concernant les champs que Braze peut envoyer. Consultez la documentation spécifique du partenaire pour plus de détails.

### Audience Sync Pro

Pour utiliser un partenaire Audience Sync Pro, notamment TikTok, Pinterest, Snapchat ou Criteo, vous pouvez sélectionner vos partenaires en fonction de vos allocations d'achat Audience Sync Pro dans la section **Audience Sync Pro** de la page **Technology Partners**.

![Audience Sync Pro sans partenaire encore sélectionné.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Commencez par sélectionner les partenaires que vous souhaitez utiliser. Chaque achat d'Audience Sync Pro vous offre 3 destinations Audience Sync Pro allouées, disponibles dans chacun de vos espaces de travail au sein de votre tableau de bord.

![Option de sélection de jusqu'à trois partenaires à connecter à Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Après avoir sélectionné vos destinations Audience Sync Pro, connectez le compte publicitaire du partenaire choisi en cliquant sur la tuile du partenaire.

![Exemple avec Snapchat et TikTok sélectionnés comme partenaires pour Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Paramètres Audience Sync de Snapchat avec le message : « Vous avez connecté 1 compte Snapchat avec succès ».]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Enfin, créez votre étape Audience Sync dans Canvas en utilisant cette destination Audience Sync Pro.

### Mise en lots et latence {#batching-and-latency}

Lorsque les utilisateurs entrent dans une étape Audience Sync dans Canvas, Braze les place dans un système de mise en lots qui agrège les mises à jour des utilisateurs avant de les envoyer à l'API du partenaire. Un lot est envoyé lorsque l'une des conditions suivantes est remplie :

- **Le lot atteint sa limite de taille.** Celle-ci varie selon le partenaire :
  - La valeur par défaut prend en charge jusqu'à 2 000 utilisateurs
  - Google Ads prend en charge jusqu'à 10 000 utilisateurs
  - Facebook et TikTok prennent en charge jusqu'à 2 000 utilisateurs
- **Le délai de latence du lot expire.** La valeur par défaut est d'une heure, mais elle est configurable par partenaire. Par exemple, The Trade Desk utilise 10 minutes.

Les Canvas à fort volume peuvent envoyer des lots plus rapidement car ils se remplissent plus vite. Les Canvas à faible volume attendent l'expiration du délai de latence. Braze ne garantit pas un délai d'envoi fixe ; le timing dépend de la taille du lot et de la fenêtre de latence configurée.

Braze enregistre l'activité d'envoi dans des journaux internes à des fins de surveillance et de résolution des problèmes, mais ces horodatages ne sont pas exposés en tant que champs interrogeables. Après que Braze a envoyé un lot à l'API du partenaire, celui-ci traite la mise à jour de l'audience selon ses propres accords de niveau de service, généralement entre 6 et 48 heures.

Braze ne reçoit pas de confirmation de la part des partenaires indiquant que des utilisateurs individuels ont été mis en correspondance ou synchronisés. Les réponses des partenaires sont des accusés de réception HTTP, et non des confirmations de correspondance. Pour vérifier qu'une audience a été remplie, consultez la plateforme publicitaire du partenaire (comme Google Ads Audience Manager ou Meta Business Manager).

### E-mails d'erreur Audience Sync {#audience-sync-error-emails}

Si l'erreur est liée à l'intégration globale du partenaire (comme un problème d'autorisation), un e-mail est envoyé à l'utilisateur qui a connecté l'intégration. Si cet utilisateur n'existe plus, les administrateurs reçoivent les e-mails.

Si l'erreur est liée à des problèmes avec le composant Audience Sync (comme « L'audience n'existe pas ») dans Canvas, un e-mail est envoyé à l'utilisateur qui a configuré le Canvas. Si cet utilisateur n'existe plus, l'e-mail est transmis à l'administrateur de l'entreprise.

Pour configurer les destinataires de ces e-mails, contactez votre gestionnaire du succès des clients afin d'ajouter des destinataires dans **Notification Preferences**. Cette préférence couvre à la fois les erreurs d'intégration et les erreurs du composant Audience Sync. Les destinataires que vous ajoutez reçoivent ces e-mails en plus de l'utilisateur associé à l'erreur.

## Considérations relatives à la confidentialité des données {#data-privacy-considerations}

{% alert important %}
Cette documentation n'est pas destinée à fournir, et ne peut être considérée comme fournissant, des conseils juridiques. L'utilisation d'Audience Sync est soumise à des exigences juridiques spécifiques. Pour vous assurer que vous l'utilisez en conformité avec toutes les lois applicables, vous devriez consulter votre conseiller juridique.
{% endalert %}

Lors de la création d'audiences pour le suivi publicitaire, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et vous conformer aux lois sur la confidentialité, telles que le droit de « Ne pas vendre ni partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs dans les critères d'entrée de leur Canvas. Les options suivantes peuvent vous aider.

Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), vous pourrez utiliser le filtre « Ads Tracking Enabled ». Sélectionnez la valeur `true` pour n'envoyer que les utilisateurs ayant donné leur consentement vers les destinations Audience Sync.

![Un Canvas avec une audience d'entrée « Ad Tracking Enabled is true ».]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Si vous collectez des `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, ou tout autre attribut personnalisé pertinent, vous devriez les inclure dans vos critères d'entrée Canvas en tant que filtre :

![Un Canvas avec une audience d'entrée « opted_in_marketing equals true ».]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Pour en savoir plus sur la manière de vous conformer à ces lois sur la protection des données au sein de la plateforme Braze, consultez l'[Assistance technique en matière de protection des données]({{site.baseurl}}/dp-technical-assistance).

## Gestion du consentement pour le ciblage publicitaire {#managing-consent-for-ad-targeting}

En tant qu'annonceur, il est de votre responsabilité de gérer le consentement pour le suivi publicitaire ou le ciblage de vos utilisateurs.

Pour diffuser des publicités auprès de vos utilisateurs, vous devez respecter l'ensemble des lois et réglementations applicables, ainsi que les politiques et exigences de la plateforme publicitaire. N'utilisez Braze pour cibler et synchroniser des utilisateurs que lorsque vous avez obtenu leur consentement.

Pour maintenir vos listes d'audience à jour sur ces plateformes publicitaires et supprimer les utilisateurs ayant révoqué leur consentement, configurez un Canvas pour retirer ces utilisateurs des listes d'audience existantes à l'aide d'une étape Audience Sync.