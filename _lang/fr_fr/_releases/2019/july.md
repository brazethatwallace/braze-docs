---
nav_title: juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2019."
---

# Juillet 2019 {#july-2019}

{% alert update %}
Braze a eu deux (vous avez bien lu — **deux**) cycles de lancement de produits ce mois-ci ! La dernière version est indiquée en haut de page, la version précédente est couverte dans la section [Plus tôt ce mois-ci](#earlier-this-month) !
{% endalert %}

## SAML/authentification unique

L'[authentification unique]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) (authentification unique) offre aux entreprises un moyen sécurisé et centralisé de contrôler l'accès au tableau de bord de Braze. En résumé, un seul jeu d'identifiants peut être utilisé pour accéder à différentes applications, y compris Braze.

En plus de [Google Sign-In avec la prise en charge d'OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), les entreprises souhaitent un authentification unique avec la prise en charge de SAML (Security Assertion Markup Language). Cela leur permet de s'intégrer de façon fluide aux grands fournisseurs d'identité (IdP), notamment [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) et [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta), qui prennent en charge les dernières normes du secteur (SAML 2.0).

Braze prend en charge :
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)

## Affichage de la clé API d'événement d'Adjust {#adjust-event-api-key-shows}

Nous avons mis à jour la page partenaire d'Adjust pour rendre cette clé API accessible aux clients.

## Nouveaux partenaires {#new-partners}

De nouveaux partenaires ont rejoint notre programme Alloys et ont été ajoutés à notre documentation ! Dites bonjour à :
- [Fivetran]({{site.baseurl}}/partners/fivetran)
- [Talon.One]({{site.baseurl}}/partners/talonone)
- [Voucherify]({{site.baseurl}}/partners/voucherify)

## Amélioration des détails de campagne {#campaign-details-improvement}

Les détails étendus de campagne sont désormais affichés dans la section… attendez… **Campaign Details** de la page **Campaign** !

## Afficher uniquement les miennes dans Segments et Canvas {#show-only-mine-in-segments-canvas}

Le filtre « Afficher uniquement les miennes » sur la page **Campaigns** s'est avéré extrêmement populaire. Par conséquent, nous ajoutons également cette option aux listes Canvas et Segments !

### Comportement d'avancement {#advancement-behavior}

Vous pouvez désormais choisir le [moment où un utilisateur passe]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) d'une étape du Canvas à la suivante. Ces options comprennent « Message Sent » (Message envoyé) et « Entire Audience After Delay » (Toute l'audience après un délai).

### Messages in-app dans Canvas {#in-app-messages-in-canvas}

Les [messages in-app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) sont désormais disponibles dans Canvas ! Ajoutez une étape de Canvas et parcourez les canaux disponibles pour ajouter un message in-app.

# Plus tôt ce mois-ci {#earlier-this-month}

## Suppression de l'image du profil utilisateur {#user-profile-image-removal}

Nous supprimons les images de profil utilisateur affichées dans les profils utilisateur de Braze et les recherches d'utilisateurs.

## Contenu connecté dans les Content Cards {#connected-content-in-content-cards}

Vous pouvez désormais utiliser les chaînes de caractères et les fonctionnalités du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content#about-connected-content) dans les [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards).

Les appels de contenu connecté vers des serveurs externes se produisent lorsqu'une carte est réellement envoyée, et non lorsque la carte est vue par l'utilisateur. Comme pour l'e-mail, le contenu dynamique sera calculé et déterminé au moment de l'envoi, et non pas au moment où la carte est visualisée.

## Adresse « reply-to » nulle {#null-reply-to-address}

Les clients peuvent désormais définir une valeur `null` pour l'adresse « reply-to » d'un message e-mail à partir de la page **Paramètres des e-mails** dans Braze ou en utilisant l'[API]({{site.baseurl}}/api/objects_filters/messaging/email_object). Quand cette option est utilisée, les réponses seront envoyées à l'adresse « From » indiquée. Vous pouvez maintenant personnaliser le champ d'adresse « From » en tant que `dan@emailaddress.com`, et vos clients auront la possibilité de répondre directement à Dan.

Pour définir une valeur `null` pour l'adresse « reply-to » d'un message e-mail depuis Braze, allez dans **Gérer les paramètres** dans la navigation, puis dans l'onglet **Paramètres des e-mails**. Faites défiler jusqu'à la section **Paramètres des e-mails sortants** et sélectionnez **Exclure « Reply-To » et envoyer les réponses à « From »** comme adresse par défaut.

## Comparaisons de campagnes {#campaign-comparisons}

Examinez [plusieurs campagnes en même temps pour comparer leurs performances relatives]({{site.baseurl}}/report_builder), côte à côte dans Braze — dans une seule fenêtre !

## Intégrer le dispatch ID dans les messages avec Liquid {#template-dispatch-id-into-messages-with-liquid}

{% alert note %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les étapes de Canvas (à l'exception des étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont « planifiées ». En savoir plus sur le [comportement de `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) dans les Canvas et les campagnes.
{% endalert %}

Si vous souhaitez suivre l'envoi d'un message à partir du message lui-même (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id`. Vous trouverez le formatage correspondant dans notre liste des balises de personnalisation prises en charge, sous [Attributs Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Le comportement est exactement identique à celui de `api_id` : comme `api_id` n'est pas disponible lors de la création de la campagne, il est intégré en tant que marque substitutive et sera prévisualisé comme `dispatch_id_for_unsent_campaign`. L'ID est généré avant l'envoi du message et sera inclus au moment de l'envoi.

{% alert warning %}
Le templating Liquid de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les messages in-app, car les messages in-app n'ont pas de `dispatch_id`.
{% endalert %}

## Le paramètre « Afficher uniquement les miennes » est persistant {#show-only-mine-setting-persists}

Le filtre « Afficher uniquement les miennes » de la grille de campagnes restera activé chaque fois que vous visiterez la page **Campaigns**.

## Mises à jour des tests A/B {#ab-testing-updates}

Vous pouvez envoyer un [test A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) unique comprenant jusqu'à huit variantes (et un contrôle facultatif) à un pourcentage spécifié par l'utilisateur de l'audience d'une campagne, puis envoyer la meilleure variante à l'audience restante à une date planifiée à l'avance.