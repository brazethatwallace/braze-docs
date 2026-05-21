---
nav_title: Suivi des clics
article_title: Suivi des clics
page_order: 2
description: "Cet article de référence explique comment activer le suivi des clics dans vos messages WhatsApp, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Suivi des clics {#click-tracking}

> Cette page explique comment activer le suivi des clics dans vos messages WhatsApp, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore.

Le suivi des clics vous permet de mesurer quand quelqu'un appuie sur un lien dans votre message WhatsApp, ce qui vous donne une vision claire du contenu qui génère de l'engagement. Braze raccourcit vos URL, ajoute le suivi en arrière-plan et enregistre les événements de clic au fur et à mesure.

Vous pouvez activer le suivi des clics dans les messages de réponse et les messages de modèle. Il fonctionne avec les liens dans les boutons et le corps du texte, et prend en charge les URL personnalisées et les domaines personnalisés. Une fois activé, vous verrez les données de clics dans vos rapports de performance WhatsApp et pourrez segmenter les utilisateurs en fonction de qui a cliqué sur quoi.

{% alert note %}
Le suivi des clics ne fonctionne pas avec les liens profonds. Vous pouvez raccourcir les liens universels de fournisseurs tels que Branch ou Appsflyer, mais Braze n'est pas en mesure de résoudre les problèmes qui pourraient survenir (comme la rupture de l'attribution ou la création d'une redirection).
{% endalert %}

## Fonctionnement {#how-it-works}

### Messages de réponse {#response-messages}

Pour configurer le suivi des clics pour les messages de réponse :
1. Créez un message de réponse qui inclut un bouton d'appel à l'action (CTA) avec une URL de site web.
2. Activez le suivi des clics en cliquant sur le bouton désigné dans l'interface.

Le lien sera raccourci vers le domaine Braze, ou le domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisé pour l'utilisateur.

Toutes les URL statiques commençant par `http://` ou `https://` seront raccourcies. Les URL raccourcies contenant une personnalisation Liquid (comme le ciblage au niveau de l'utilisateur) seront valides pendant deux mois.

![Compositeur de messages WhatsApp avec un corps de contenu et un bouton.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Messages de modèle {#template-messages}

Nous recommandons d'activer le suivi des clics pour les messages de modèle via le **générateur de modèles WhatsApp** dans Braze. Cette méthode d'activation gère automatiquement les exigences de formatage des URL, vous n'avez donc rien à configurer manuellement dans WhatsApp Business Manager.

Si vous créez des modèles directement dans WhatsApp Business Manager, consultez [Configurer le suivi des clics depuis WhatsApp Business Manager](#configuring-click-tracking-from-whatsapp-business-manager).

#### Utiliser le générateur de modèles {#use-the-template-builder}

Lors de la création d'un modèle dans le générateur de modèles, le suivi des clics est configuré dans l'onglet **Paramètres**.

##### Étape 1 : Activer le suivi des clics {#step-1-enable-click-tracking}

Dans le générateur de modèles, accédez à l'onglet **Paramètres**. Dans **Link options**, cochez la case **Click tracking**. Lorsque cette option est activée, tous les liens de votre modèle (dans le corps du message et les boutons CTA de site web) sont raccourcis et suivis.

![Onglet Paramètres du générateur de modèles montrant la section Link options avec la case Click tracking cochée et un menu déroulant Custom domain.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_settings.png %})

##### Étape 2 : Sélectionner un domaine personnalisé (facultatif) {#step-2-select-a-custom-domain-optional}

Sous **Custom domain**, sélectionnez le domaine que vous souhaitez utiliser pour les liens raccourcis. Le menu déroulant affiche tous les domaines de suivi personnalisés configurés pour votre espace de travail. Si vous n'en sélectionnez pas, Braze utilise le domaine par défaut `brz.ai`.

Pour ajouter ou modifier des domaines, sélectionnez **Subscription Group Management**.

{% alert important %}
Une fois qu'un modèle est soumis à Meta pour approbation, le domaine de suivi ne peut plus être modifié. Confirmez que vous avez sélectionné le bon domaine avant de soumettre.
{% endalert %}

##### Étape 3 : Ajouter vos URL de destination {#step-3-add-your-destination-urls}

Revenez à l'onglet **Compose** et ajoutez le contenu de votre message.

- **Pour les boutons CTA de site web :** saisissez l'URL de destination dans le champ **Click tracking URL**. Braze stocke votre URL de destination et formate automatiquement l'URL du site web du bouton avec le domaine de suivi et une marque substitutive de variable {% raw %}(par exemple, `https://brz.ai/{{1}}`){% endraw %}. Cette marque substitutive est ce qui est soumis à Meta. Au moment de l'envoi, Braze génère l'URL de suivi complète pour chaque utilisateur et renseigne la variable.
- **Pour les liens dans le corps du texte :** saisissez les URL directement dans le corps.

Vous pouvez prévisualiser le format de l'URL suivie pour chaque bouton directement sous le champ **Website URL** (par exemple, `https://brz.ai/XXXXXXXX`).

![Section des boutons d'appel à l'action montrant un bouton Visit website avec l'URL du site web pré-remplie au format de suivi et un champ Click tracking URL pour la destination.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_compose.png %}){: style="max-width:70%;"}

##### Mettre à jour les URL de destination après la soumission {#update-destination-urls-after-submission}

Une fois qu'un modèle est soumis à Meta, le domaine de suivi est verrouillé, mais l'URL de destination reste modifiable à tout moment. Pour mettre à jour la destination d'un lien, modifiez le champ **Click tracking URL** pour ce bouton. Le format de l'URL suivie reste le même ; Braze redirige les utilisateurs vers la nouvelle destination au moment de l'envoi.

#### Configurer le suivi des clics depuis WhatsApp Business Manager {#configuring-click-tracking-from-whatsapp-business-manager}

Si vous créez des modèles dans WhatsApp Business Manager plutôt que dans le générateur de modèles, suivez ces étapes pour que le suivi des clics fonctionne correctement lorsque le modèle est utilisé dans Braze.

##### Étape 1 : Créer un modèle compatible avec le suivi des clics dans WhatsApp Business Manager {#step-1-build-a-click-tracking-supported-template-in-whatsapp-business-manager}

1. Dans votre WhatsApp Business Manager, créez une URL de base qui est soit votre domaine personnalisé, soit `brz.ai`.
2. Assurez-vous que les liens inclus dans le modèle sont compatibles avec le suivi des clics.
3. Ne modifiez pas les variables du modèle après sa configuration en tant que campagne dans Braze ; les modifications en aval ne peuvent pas être intégrées.
4. Pour les liens de bouton CTA, sélectionnez **Dynamic**, puis fournissez l'URL de base (`brz.ai` ou votre domaine personnalisé).

![Section pour créer un appel à l'action.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %}){: style="max-width:70%;"}

{: start="5"}
5. Pour les liens dans le corps du texte, lors de la rédaction du modèle dans votre WhatsApp Business Manager, supprimez les espaces insérés pour les liens contenus dans le corps que vous souhaitez suivre.

![Zone de texte pour saisir le corps du contenu de l'appel à l'action.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %}){: style="max-width:70%;"}

##### Étape 2 : Compléter votre modèle dans Braze {#step-2-complete-your-template-in-braze}

Lors de la composition, Braze détecte automatiquement quels modèles ont des domaines d'URL compatibles, à la fois dans le corps du texte et pour les boutons CTA. L'état est affiché en bas du modèle.

![Section État du lien montrant un état actif pour le suivi des clics.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Liens compatibles :** les liens soumis avec l'URL de base correspondante ont le suivi des clics activé.
- **Liens partiellement compatibles :** si certains liens d'un modèle sont soumis en tant qu'URL complètes, le suivi des clics **ne sera pas** appliqué à ces liens.
- **Liens non compatibles :** les liens sans URL de base approuvée **n'auront pas** de fonctionnalités de suivi des clics.

L'URL de destination doit être fournie pour tout lien dont l'URL de base correspond à `brz.ai` ou à votre domaine personnalisé.

![Section Boutons avec des champs pour un nom de bouton, une URL de site web et une URL de suivi des clics.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Envoi de messages de modèle via l'API** : le suivi des clics WhatsApp (utilisant `brz.ai` ou un domaine de suivi personnalisé et le champ **Click tracking URL** dans le compositeur de messages) n'est pas pris en charge lors de l'envoi de messages de modèle WhatsApp via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

Si vous envoyez un message de modèle via l'API, vous pouvez renseigner les variables d'URL CTA (en utilisant `button_variables`), mais Braze ne génère pas d'URL de suivi des clics ni de lien de redirection dans le flux de requête API. Pour utiliser le suivi des clics, envoyez le modèle depuis le tableau de bord de Braze ou via un déclencheur de campagne Braze.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Personnalisation Liquid dans les URL {#liquid-personalization-in-urls}

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).
Les URL peuvent être générées dynamiquement grâce à l'utilisation de toutes les balises de personnalisation Liquid prises en charge.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Nous prenons également en charge le raccourcissement des variables Liquid personnalisées, comme dans ces exemples :

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Raccourcir les URL rendues par des variables Liquid {#shorten-urls-rendered-by-liquid-variables}

Braze raccourcit les URL rendues par Liquid, y compris celles incluses dans les propriétés de déclenchement API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcirons et suivrons cette URL avant d'envoyer le message WhatsApp.

## Tests {#testing}

Avant de lancer votre campagne ou Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un WhatsApp à des groupes de test de contenu ou à un utilisateur individuel.

Cette prévisualisation sera mise à jour avec la personnalisation pertinente et l'URL raccourcie.

{% alert important %}
Si un brouillon est créé au sein d'un Canvas actif, une URL raccourcie ne sera pas générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est rendu actif.
{% endalert %}

## Rapports {#reporting}

Lorsque le suivi des clics est activé ou utilisé avec des modèles compatibles, le tableau de performance WhatsApp inclut la colonne **Total Clicks** qui affiche un décompte des événements de clic par variante et un taux de clics associé. Pour plus de détails sur les indicateurs WhatsApp, consultez [Performance des messages WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting/).

![Étape Canvas de message WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Les données de clics seront automatiquement reportées dans le tableau de bord d'analyse.

![Tableau de performance des messages WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Reciblage des utilisateurs {#retargeting-users}

Vous pouvez utiliser le filtre `Clicked/Opened Step` et l'interaction `clicked tracked WhatsApp link` pour segmenter les utilisateurs en fonction de leurs interactions avec les liens.

![Groupe de filtres avec un filtre pour « clicked tracked WhatsApp link ».]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Oui. Lorsque le suivi des clics est activé (ou activé en fonction de la configuration du modèle), vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en exploitant les filtres de reciblage WhatsApp ou les événements de clic WhatsApp (`users.messages.whatsapp.Click`) envoyés par Currents.

### Les prévisualisations sur l'appareil WhatsApp comptent-elles comme des clics ? {#do-previews-on-the-whatsapp-device-count-as-clicks}

Non, elles ne contribuent pas au taux de clics des messages WhatsApp.