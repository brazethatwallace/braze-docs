---
nav_title: Distribution optimisée
article_title: Messages WhatsApp avec distribution optimisée
page_order: 1
description: "Cet article de référence couvre les étapes nécessaires à la création d'un message WhatsApp avec distribution optimisée."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Messages WhatsApp avec distribution optimisée {#whatsapp-messages-with-optimized-delivery}

> Améliorez la livrabilité et l'engagement en atteignant davantage d'utilisateurs pertinents sur WhatsApp grâce à une distribution dynamique basée sur l'engagement.

Les messages WhatsApp avec distribution optimisée sont envoyés via l'[API Marketing Messages pour WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) de Meta (MM API pour WhatsApp), qui offre une distribution dynamique basée sur l'engagement. Cela signifie que vos messages à fort engagement (par exemple, ceux qui ont le plus de chances d'être lus et cliqués) peuvent atteindre davantage d'utilisateurs susceptibles d'interagir avec eux. WhatsApp considère vos messages comme étant à fort engagement s'ils sont attendus, pertinents et opportuns, et donc plus susceptibles d'être lus et cliqués.

Les marques peuvent s'attendre à une livrabilité égale ou supérieure avec la MM API pour WhatsApp, par rapport à la Cloud API. En Inde, les messages marketing à fort engagement ont enregistré jusqu'à 9 % de messages livrés en plus par rapport à la Cloud API, selon Meta. Notez que la MM API pour WhatsApp ne garantit toujours pas une livrabilité de 100 %.

## Disponibilité régionale {#regional-availability}

La disponibilité et les capacités d'optimisation de la livraison optimisée dépendent de la région du numéro de téléphone professionnel et de l'utilisateur. Pour en savoir plus, consultez [Disponibilité géographique des fonctionnalités](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features).

## Configuration de la distribution optimisée {#setting-up-optimized-delivery}

1. Dans Braze, accédez à **Partner Integrations** > **Technology Partners** > **WhatsApp**.
2. Dans la section **Optimize your sending with optimized delivery**, sélectionnez **Upgrade setting** pour déclencher le [flux d'inscription intégrée]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

![La section d'intégration de messagerie WhatsApp avec une option pour optimiser l'envoi avec la distribution optimisée.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. Une fois la distribution optimisée activée, les détails de votre compte dans **WhatsApp Business Account Management** afficheront le statut de la distribution optimisée.

![La section de gestion du compte WhatsApp Business avec un groupe d'abonnement répertorié ayant un statut de numéro actif.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Vous pouvez également activer la distribution optimisée directement dans votre gestionnaire WhatsApp, puis commencer à envoyer des messages dans Braze.

### Résolution des problèmes de configuration {#troubleshooting-your-setup}

- **Erreur générale :** Si un problème survient lors de la mise à niveau, cette bannière d'erreur s'affichera et vous conseillera de [contacter le support]({{site.baseurl}}/user_guide/administer/personal/braze_support).
- **Erreur d'inéligibilité :** Si vous êtes soumis à une restriction par Meta, cette bannière d'erreur s'affichera : « At least one WhatsApp Business Account is restricted by Meta. Accounts must be in good standing to upgrade. » Ce message ne peut pas être fermé tant que le problème n'est pas résolu.

## Utiliser la distribution optimisée dans les Campaigns et les Canvas {#using-optimized-delivery-in-campaigns-and-canvases}

La distribution optimisée doit être utilisée pour les **messages marketing**. Braze supprimera automatiquement l'option de distribution optimisée pour les **messages utilitaires, d'authentification, de service et de réponse**, qui doivent continuer à être envoyés via l'API Cloud, qui est le paramètre par défaut.

### Sélectionner la méthode de distribution {#selecting-the-delivery-method}

1. Dans le compositeur WhatsApp de Braze pour une Campaign ou une étape de message Canvas, accédez à l'onglet **Paramètres**.
2. Dans la section **Méthode de distribution**, la case **Distribution optimisée (recommandée)** sera cochée par défaut si votre compte WhatsApp Business (WABA) est activé. Si vous ne souhaitez pas utiliser la distribution optimisée pour ce message spécifique, décochez la case.
- Si vous sélectionnez la distribution optimisée mais qu'elle n'est pas disponible, le message basculera automatiquement vers la méthode API Cloud.

![Compositeur de message avec un onglet d'aperçu comportant une case à cocher pour sélectionner la distribution optimisée.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Recibler les utilisateurs sur d'autres canaux Braze {#retargeting-users-on-other-braze-channels}

Étant donné que l'API MM pour WhatsApp n'offre pas une livrabilité à 100 %, il est important de comprendre comment recibler les utilisateurs qui n'ont peut-être pas reçu votre message sur d'autres canaux.

Pour recibler les utilisateurs, nous recommandons de créer un Segment d'utilisateurs qui n'ont pas reçu un message spécifique. Pour ce faire, filtrez par le code d'erreur `131049`, qui indique qu'un message de modèle marketing n'a pas été envoyé en raison de l'application par WhatsApp de la limite de modèles marketing par utilisateur. Vous pouvez le faire en utilisant Braze Currents ou les extensions de segments SQL :

- **Braze Currents :** Exportez les événements d'échec de message à l'aide de Braze Currents. Vous pouvez ensuite utiliser ces données pour mettre à jour un attribut personnalisé sur le profil utilisateur (par exemple `whatsapp_failed_last_msg: true`), que vous pouvez utiliser comme filtre pour votre Campaign de reciblage.
- **Extensions de segments SQL :** Si vous avez accès à cette fonctionnalité, vous pouvez utiliser SQL pour interroger les journaux d'échec de message et créer un Segment de ces utilisateurs, puis cibler ce Segment sur un canal différent.