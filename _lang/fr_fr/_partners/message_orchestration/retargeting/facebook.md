---
nav_title: Facebook
article_title: Exportation de l'audience Facebook
alias: /partners/facebook/
description: "Cet article de référence décrit le partenariat entre Braze et Facebook, une plateforme de réseau social de premier plan permettant aux marques d'atteindre et d'engager leurs clients."
page_type: partner
search_tag: Partner

---

# Exportation de l'audience Facebook {#facebook-audience-export}

> L'intégration de Braze et Facebook vous permet d'exporter manuellement vos segments Braze vers Facebook pour créer des audiences personnalisées Facebook. Il s'agit d'un export d'audience statique et ponctuel qui ne crée que de nouvelles audiences personnalisées Facebook.

Les cas d'utilisation courants pour l'exportation des audiences personnalisées Facebook incluent :
- Recibler des utilisateurs à des points spécifiques de leur cycle de vie
- Créer des listes de ciblage d'exclusion
- Créer des [audiences similaires](https://www.facebook.com/business/help/164749007013531?id=401668390442328) pour acquérir de nouveaux utilisateurs plus efficacement
<br><br>

{% alert note %}
L'exportation de l'audience Facebook utilise le **jeton d'accès utilisateur** pour autoriser les requêtes.<br><br>
Si vous utilisez cette fonctionnalité avec la fonctionnalité [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/), Braze utilisera par défaut le **jeton d'utilisateur système** plus fiable que vous avez déjà généré pour autoriser les requêtes.
{% endalert %}

{% alert note %}
Si vous participez au test des comptes Meta Work en version bêta, assurez-vous de déconnecter et reconnecter votre compte à la [page partenaire Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#step-1-connect-to-facebook).
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| [Gestionnaire d'entreprise Facebook](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages, les applications). |
| [Compte publicitaire Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Un compte publicitaire Facebook actif lié au gestionnaire d'entreprise de votre marque que vous souhaitez utiliser avec les audiences personnalisées de Braze.<br><br>Assurez-vous que l'administrateur de votre gestionnaire d'entreprise Facebook vous a accordé les autorisations d'administrateur sur les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze, et que vous avez accepté les conditions générales de votre compte publicitaire. Sinon, vous ne pourrez accéder à aucun compte publicitaire Facebook dans Braze. |
| [Conditions des audiences personnalisées Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Vous devez accepter les conditions des audiences personnalisées Facebook pour les comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

### Étape 1 : Se connecter à Facebook {#step-1-connect-to-facebook}

1. Dans le tableau de bord de Braze, allez dans **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**.

{: start="2"}
2. Dans le module d'exportation de l'audience Facebook, sélectionnez **Connect Facebook**. <br><br>![Page des partenaires technologiques Facebook dans la plateforme Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Dans la fenêtre de dialogue oAuth de Facebook, autorisez Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook. <br><br>![La première boîte de dialogue Facebook demandant de « Se connecter en tant que X », où X est votre nom d'utilisateur Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![La deuxième boîte de dialogue Facebook demandant l'autorisation de gérer les publicités pour vos comptes publicitaires.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Après avoir lié Braze à votre compte Facebook, sélectionnez les comptes publicitaires que vous souhaitez synchroniser dans votre espace de travail Braze. <br><br>![Une liste de comptes publicitaires disponibles que vous pouvez connecter à Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Une fois connecté, vous êtes redirigé vers la page partenaire, où vous pouvez voir quels comptes sont connectés et déconnecter les comptes existants. <br><br> ![Version mise à jour de la page des partenaires technologiques Facebook montrant les comptes publicitaires connectés avec succès.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Votre connexion Facebook est appliquée au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous retire de votre gestionnaire d'entreprise Facebook ou de l'accès aux comptes Facebook connectés, Braze détecte un jeton invalide. En conséquence, vos Canvas actifs utilisant des étapes d'audience Facebook affichent des erreurs, et Braze ne peut pas synchroniser les utilisateurs.

{% alert important %}
Pour les clients qui ont déjà suivi le processus de révision de l'application Facebook pour la [gestion des publicités](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et l'[accès standard à la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système reste valide pour l'étape de l'audience Facebook. Vous ne pouvez pas modifier ou révoquer le jeton d'utilisateur système Facebook via la page partenaire Facebook. Vous pouvez en revanche connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre espace de travail Braze.

<br><br>La nouvelle configuration oAuth de Facebook s'applique également aux [exportations Facebook via des segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Étape 2 : Exporter vos utilisateurs vers Facebook {#step-2-export-your-users-into-facebook}

Dans Braze, l'exportation de l'audience Facebook est accessible via la page **Segments**.

1. Sur la page **Segments**, sélectionnez le segment que vous souhaitez exporter.
2. Sélectionnez **User Data**, puis sélectionnez **Export as Facebook Audience**. <br><br>![La section « Détails du segment » d'un segment dont « User Data » est sélectionné pour afficher une liste déroulante d'options comprenant « Export as Facebook Audience ».]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Si vous n'avez pas encore activé Facebook dans Braze, vous êtes invité à accéder à la page des partenaires technologiques Facebook dans le tableau de bord. Si vous avez déjà activé Facebook via **Partenaires technologiques** > **Facebook**, vous pouvez sélectionner votre compte publicitaire Facebook et les champs utilisateur à exporter. <br><br> Vous pouvez exporter les champs suivants :
- IDFA de l'appareil
- Numéro de téléphone
- E-mail

{% alert note %}
Vous ne pouvez sélectionner qu'un seul champ utilisateur par exportation. Si vous choisissez plusieurs types de données, Braze crée une audience personnalisée distincte pour chacun.
{% endalert %}

{: start="4"}
4. Après avoir sélectionné le champ utilisateur, sélectionnez **Export Segment**. Comme pour les exportations CSV, vous recevez un e-mail lorsque le segment a terminé l'exportation vers Facebook.
5. Consultez l'audience personnalisée dans le [gestionnaire des publicités Facebook](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Pour des raisons de confidentialité des utilisateurs, Facebook ne vous permet pas de voir :

- Les utilisateurs exacts qui ont été ajoutés avec succès à une audience personnalisée. [En savoir plus.](https://www.facebook.com/business/help/112061095610075)
- La taille de l'audience personnalisée. [En savoir plus.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configurer votre exportation d'audience {#configuring-your-audience-export}

Lors de la création d'audiences Facebook, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du [CCPA](https://oag.ca.gov/privacy/ccpa). Les marketeurs doivent implémenter les filtres pertinents pour l'éligibilité des utilisateurs dans leurs critères d'entrée Canvas. Voici quelques options.

- Si vous avez collecté l'[IDFA iOS via le SDK Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), vous pouvez utiliser le filtre **Ads Tracking Enabled**. Sélectionnez la valeur `true` pour envoyer uniquement les utilisateurs vers les destinations de synchronisation d'audience où ils ont donné leur consentement.

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Si vous collectez des opt-ins, des opt-outs, `Do Not Sell Or Share`, ou d'autres attributs personnalisés pertinents, vous devez les inclure dans vos critères d'entrée Canvas en tant que filtre :

![Un Canvas dont l'audience d'entrée est « opted_in_marketing » égal à « true ».]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Audiences similaires {#lookalike-audiences}

Une fois que vous avez exporté avec succès un segment en tant qu'audience Facebook, vous pouvez créer des groupes supplémentaires en utilisant les [audiences similaires](https://www.facebook.com/business/help/164749007013531?id=401668390442328) de Facebook. Cette fonctionnalité examine les données démographiques, les intérêts et d'autres attributs de votre audience choisie et crée une nouvelle audience de personnes ayant des attributs similaires.

## Résolution des problèmes {#troubleshooting}

### Erreur de validation du jeton d'accès {#error-validating-access-token}

Lors de l'utilisation de l'exportation Facebook, l'erreur `Error Validating Access Token` apparaît si :
- Vous avez changé votre mot de passe, ce qui invalide votre session en cours
- Facebook vous a déconnecté par mesure de sécurité

Pour résoudre cette erreur, suivez ces étapes :
1. Déconnectez-vous de Facebook, puis reconnectez-vous.
2. Dans Braze, supprimez vos identifiants Facebook et enregistrez. Confirmez que les identifiants ont été supprimés en essayant d'exporter un segment (l'icône d'exportation doit être désactivée).
3. Ajoutez à nouveau vos identifiants Facebook et enregistrez.
4. Essayez d'exporter à nouveau.

Si l'exportation ne fonctionne pas, procédez comme suit :
1. Supprimez à nouveau vos identifiants et enregistrez.
2. Ajoutez à nouveau vos identifiants et enregistrez.
3. Déconnectez et reconnectez l'intégration Facebook sur la page **Partenaires technologiques**.

### Erreur lors de l'exportation d'une audience Facebook {#error-when-exporting-a-facebook-audience}

Si vous recevez une erreur lors de l'exportation d'un segment en tant qu'audience Facebook, la documentation développeur de Facebook indique les causes courantes suivantes :

1. **Le jeton d'accès provient d'un utilisateur qui n'est pas administrateur de l'application et du compte publicitaire :** l'utilisateur Facebook dont les identifiants sont connectés à Braze doit disposer des autorisations appropriées.
2. **Le compte publicitaire vers lequel vous exportez n'est pas associé à votre application :** le compte publicitaire Facebook doit être lié à votre application dans les paramètres Facebook.

Utilisez les vérifications suivantes pour valider votre configuration :

- **Vérifiez que vous êtes administrateur de l'application :** accédez à [developers.facebook.com](https://developers.facebook.com/), ouvrez **My Apps** et sélectionnez l'application de votre entreprise. Si vous ne voyez pas l'application, votre équipe de développement devra peut-être vous ajouter. Dans le tableau de bord de l'application, accédez à **Roles** dans le menu de gauche pour confirmer votre rôle (Admin, Developer, Tester ou Analytics User).
- **Vérifiez que votre compte publicitaire est associé à votre application :** dans le tableau de bord de l'application Facebook, accédez à **Settings** > **Advanced**, faites défiler jusqu'à **Advertising Accounts** et ajoutez l'ID du compte publicitaire Facebook que vous souhaitez utiliser pour les exportations d'audience Braze s'il n'est pas déjà répertorié.
- **Vérifiez que vous êtes administrateur du compte publicitaire :** accédez à [business.facebook.com](https://business.facebook.com/), puis sélectionnez **Business Settings** dans le menu déroulant en haut à gauche. Ensuite, accédez à **Accounts** > **Ad accounts** et sélectionnez le compte publicitaire. Confirmez votre accès et que vous disposez des autorisations nécessaires pour créer des audiences personnalisées.

Pour plus de détails, consultez la [documentation de l'API des audiences personnalisées Facebook](https://developers.facebook.com/docs/) et le [guide du centre d'aide Facebook Business sur les audiences personnalisées](https://www.facebook.com/business/help).