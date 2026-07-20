---
nav_title: septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2019."
---

# Septembre 2019 {#september-2019}

## Application Braze dans OneLogin {#braze-app-within-onelogin}

Les clients pourront simplement rechercher et sélectionner Braze dans [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin) pour la connexion initiée par le SP ou l'IdP. Cela signifie que les clients n'auront pas à ajouter une application personnalisée dans OneLogin. Par conséquent, certains paramètres devraient être préremplis, notamment les attributs que nous avons vu apparaître depuis le lancement de l'authentification unique (SSO) SAML.

## Partenariat Rokt Calendar {#rokt-calendar-partnership}

[Rokt Calendar]({{site.baseurl}}/partners/home) offre aux clients de Braze la possibilité d'aligner leurs initiatives marketing personnalisées et d'étendre le contenu personnalisé au calendrier de l'utilisateur final. L'expérience est ainsi encore plus harmonieuse pour l'utilisateur final et renforce l'adhérence aux services de nos clients. Les clients pourront…

- Envoyer une invitation de calendrier via la plateforme Braze pour « noter cette date » et étendre la communication
- Mettre à jour une invitation existante si le contenu de l'événement change.

## Partenariat Passkit {#passkit-partnership}

Avec [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit), les clients de Braze pourront étendre leur engagement client au portefeuille mobile. Ils pourront personnaliser les campagnes de portefeuille en utilisant la segmentation puissante de Braze et en orchestrant les divers canaux, comme les notifications push, les messages in-app, et bien plus encore.

## Retour de la valeur du dispatch ID via les endpoints d'envoi de messages {#dispatch-id-value-return-via-messaging-endpoints}

Le `dispatch_id` du message sera inclus dans les réponses suivantes des endpoints d'envoi de messages :
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging)

Ainsi, les clients qui utilisent des messages transactionnels peuvent retracer l'appel via Currents.

## Journal des modifications Canvas {#canvas-changelogs}

Vous vous êtes déjà demandé qui travaillait sur un Canvas dans votre compte ? Ne vous posez plus la question ! Vous pouvez maintenant accéder au journal des modifications Canvas.

![Journal des modifications Canvas]({% image_buster /assets/img/canvas-changelog1.png %})
![Journal des modifications Canvas]({% image_buster /assets/img/canvas-changelog2.png %})