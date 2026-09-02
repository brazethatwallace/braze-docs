---
nav_title: Facebook
article_title: Exportation de l'audience Facebook
alias: /partners/facebook/
description: "Cet article de référence décrit le partenariat entre Braze et Facebook, une plateforme de réseau social de premier plan permettant aux marques d'atteindre et d'engager leurs clients."
page_type: partner
search_tag: Partner
---

# Exportation de l'audience Facebook {#facebook-audience-export}

> L'intégration de Braze et Facebook vous permet d'exporter manuellement vos Segments Braze vers Facebook pour créer des audiences personnalisées Facebook. Il s'agit d'un export d'audience statique et ponctuel qui ne crée que de nouvelles audiences personnalisées Facebook.

Les cas d'usage courants pour l'exportation des audiences personnalisées Facebook incluent :
- Recibler des utilisateurs à des points spécifiques de leur cycle de vie
- Créer des listes de ciblage d'exclusion
- Créer des [audiences similaires](https://www.facebook.com/business/help/164749007013531?id=401668390442328) pour acquérir de nouveaux utilisateurs plus efficacement
<br><br>

{% alert note %}
L'exportation de l'audience Facebook utilise le **jeton d'accès utilisateur** pour autoriser les requêtes.<br><br>
Si vous utilisez cette fonctionnalité avec la fonctionnalité [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook), Braze utilisera par défaut le **jeton d'utilisateur système** plus fiable que vous avez déjà généré pour autoriser les requêtes.
{% endalert %}

{% alert note %}
Si vous participez au test des comptes Meta Work en version bêta, assurez-vous de déconnecter et reconnecter votre compte à la [page partenaire Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Prérequis {#prerequisites}

| Condition requise | Description |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages, les applications). |
| [Compte publicitaire Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Un compte publicitaire Facebook actif lié au gestionnaire commercial de votre marque que vous souhaitez utiliser avec les audiences personnalisées de Braze.<br><br>Assurez-vous que l'administrateur de votre Facebook Business Manager vous a accordé les permissions d'administrateur pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze, et que vous avez accepté les conditions générales de votre compte publicitaire. Dans le cas contraire, vous ne pourrez accéder à aucun compte publicitaire Facebook dans Braze. |
| [Conditions d'utilisation des audiences personnalisées Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Vous devez accepter les conditions d'utilisation des audiences personnalisées de Facebook pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Se connecter à Facebook {#step-1-connect-to-facebook}

1. Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**.

{: start="2"}
2. Dans le module d'exportation d'audience Facebook, sélectionnez **Connect Facebook**. <br><br>![Page des partenaires technologiques Facebook dans la plateforme Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Dans la fenêtre de dialogue oAuth de Facebook, autorisez Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook. <br><br>![La première boîte de dialogue Facebook invitant à « Se connecter en tant que X », où X est votre nom d'utilisateur Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![La seconde boîte de dialogue Facebook demandant l'autorisation de gérer les publicités pour vos comptes publicitaires.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Une fois Braze lié à votre compte Facebook, sélectionnez les comptes publicitaires que vous souhaitez synchroniser au sein de votre espace de travail Braze. <br><br>![Liste des comptes publicitaires disponibles que vous pouvez connecter à Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Une fois la connexion établie, vous êtes redirigé vers la page partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter des comptes existants. <br><br> ![Version mise à jour de la page des partenaires technologiques Facebook montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Votre connexion Facebook s'applique au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous retire de votre Facebook Business Manager ou de l'accès aux comptes Facebook connectés, Braze détecte un jeton invalide. Par conséquent, vos Canvas actifs utilisant les étapes d'audience Facebook affichent des erreurs, et Braze ne peut pas synchroniser les utilisateurs.

{% alert important %}
Pour les clients ayant déjà effectué le processus de révision de l'application Facebook pour [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton utilisateur système reste valide pour l'étape d'audience Facebook. Vous ne pouvez pas modifier ni révoquer le jeton utilisateur système Facebook via la page partenaire Facebook. Vous pouvez toutefois connecter votre compte Facebook pour remplacer votre jeton utilisateur système Facebook au sein de votre espace de travail Braze.

<br><br>La nouvelle configuration oAuth de Facebook s'applique également aux [exportations Facebook via les Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Étape 2 : Exporter vos utilisateurs vers Facebook {#step-2-export-your-users-into-facebook}

Dans Braze, l'exportation d'audience Facebook est accessible depuis la page **Segments**.

1. Sur la page **Segments**, sélectionnez le segment que vous souhaitez exporter.
2. Sélectionnez **User Data**, puis sélectionnez **Export as Facebook Audience**. <br><br>![La section « Segment Details » d'un segment avec « User Data » sélectionné pour afficher un menu déroulant d'options incluant « Export as Facebook Audience ».]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Si vous n'avez pas encore activé Facebook dans Braze, vous êtes invité à accéder à la page des partenaires technologiques Facebook dans le tableau de bord. Si vous avez déjà activé Facebook via **Partenaires technologiques** > **Facebook**, vous pouvez sélectionner votre compte publicitaire Facebook et les champs utilisateur à exporter. <br><br> Vous pouvez exporter les champs suivants :
- IDFA de l'appareil
- Numéro de téléphone
- E-mail

{% alert note %}
Vous ne pouvez sélectionner qu'un seul champ utilisateur par exportation. Si vous choisissez plus d'un type de données, Braze crée une audience personnalisée distincte pour chacun.
{% endalert %}

{: start="4"}
4. Après avoir sélectionné le champ utilisateur, sélectionnez **Export Segment**. Comme pour les exportations CSV, vous recevez un e-mail lorsque le segment a fini d'être exporté vers Facebook.
5. Consultez l'audience personnalisée dans le [Facebook Ads Manager](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Pour des raisons de confidentialité des utilisateurs, Facebook ne vous permet pas de voir :

- Les utilisateurs exacts qui ont été ajoutés avec succès à une audience personnalisée. [Consultez les détails de Facebook sur les raisons pour lesquelles les membres individuels de l'audience sont masqués](https://www.facebook.com/business/help/112061095610075).
- La taille de l'audience personnalisée. [Consultez les détails sur les modifications d'estimation de taille d'audience de Facebook](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% endalert %}

#### Configurer votre exportation d'audience {#configuring-your-audience-export}

Lors de la création d'audiences Facebook, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit « Do Not Sell or Share » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée Canvas. Les options suivantes peuvent vous aider.

- Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), vous pouvez utiliser le filtre **Ads Tracking Enabled**. Sélectionnez la valeur `true` pour envoyer les utilisateurs vers les destinations Audience Sync uniquement lorsqu'ils ont donné leur consentement.

![Filtre d'entrée Canvas montrant Ads Tracking Enabled défini sur true.]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Si vous collectez les consentements, les refus, `Do Not Sell Or Share`, ou d'autres attributs personnalisés pertinents, vous devez les inclure dans vos critères d'entrée Canvas en tant que filtre :

![Un Canvas avec une audience d'entrée où « opted_in_marketing » est égal à « true ».]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Audiences similaires {#lookalike-audiences}

Une fois que vous avez exporté avec succès un segment en tant qu'audience Facebook, vous pouvez créer des groupes supplémentaires à l'aide des [audiences similaires](https://www.facebook.com/business/help/164749007013531?id=401668390442328) de Facebook. Cette fonctionnalité analyse les données démographiques, les centres d'intérêt et les autres attributs de votre audience choisie, puis crée une nouvelle audience de personnes présentant des attributs similaires.

## Résolution des problèmes {#troubleshooting}

### Erreur de validation du jeton d'accès {#error-validating-access-token}

Lors de l'utilisation de l'export Facebook, l'erreur `Error Validating Access Token` apparaît si :
- Vous avez changé votre mot de passe, ce qui invalide votre session en cours
- Facebook vous a déconnecté par mesure de sécurité

Pour résoudre cette erreur, suivez ces étapes :
1. Déconnectez-vous de Facebook, puis reconnectez-vous.
2. Dans Braze, supprimez vos identifiants Facebook et enregistrez. Confirmez que les identifiants ont été supprimés en essayant d'exporter un Segment (l'icône d'export devrait être désactivée).
3. Ajoutez à nouveau vos identifiants Facebook et enregistrez.
4. Essayez d'exporter à nouveau.

Si l'export ne fonctionne pas, procédez comme suit :
1. Supprimez à nouveau vos identifiants et enregistrez.
2. Ajoutez à nouveau vos identifiants et enregistrez.
3. Déconnectez puis reconnectez l'intégration Facebook sur la page **Partenaires technologiques**.

### Erreur lors de l'export d'une audience Facebook {#error-when-exporting-a-facebook-audience}

Si vous recevez une erreur lors de l'export d'un Segment en tant qu'audience Facebook, la documentation développeur de Facebook indique les causes courantes suivantes :

1. **Le jeton d'accès provient d'un utilisateur qui n'est pas administrateur de l'application et du compte publicitaire :** l'utilisateur Facebook dont les identifiants sont connectés à Braze doit disposer des permissions appropriées.
2. **Le compte publicitaire vers lequel vous exportez n'est pas associé à votre application :** le compte publicitaire Facebook doit être lié à votre application dans les paramètres Facebook.

Utilisez les vérifications suivantes pour valider votre configuration :

- **Vérifiez que vous êtes administrateur de l'application :** rendez-vous sur [developers.facebook.com](https://developers.facebook.com/), ouvrez **My Apps** et sélectionnez l'application de votre entreprise. Si vous ne voyez pas l'application, votre équipe de développement devra peut-être vous ajouter. Dans le tableau de bord de l'application, accédez à **Roles** pour confirmer votre rôle (Admin, Developer, Tester ou Analytics User).
- **Vérifiez que votre compte publicitaire est associé à votre application :** dans le tableau de bord de l'application Facebook, accédez à **Settings** > **Advanced**, faites défiler jusqu'à **Advertising Accounts** et ajoutez l'ID du compte publicitaire Facebook que vous souhaitez utiliser pour les exports d'audience Braze s'il n'est pas déjà répertorié.
- **Vérifiez que vous êtes administrateur du compte publicitaire :** rendez-vous sur [business.facebook.com](https://business.facebook.com/), ouvrez **Business Settings** depuis le menu principal, puis accédez à **Accounts** > **Ad accounts** et sélectionnez le compte publicitaire. Confirmez votre accès et que vous disposez des permissions nécessaires pour créer des audiences personnalisées.

Pour plus de détails, consultez la [documentation de l'API Custom Audience de Facebook](https://developers.facebook.com/docs/) et le [guide du Centre d'aide pour les entreprises de Facebook sur les audiences personnalisées](https://www.facebook.com/business/help).