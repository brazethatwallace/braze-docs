---
nav_title: Reciblage des utilisateurs
article_title: Reciblage des utilisateurs
page_order: 5
description: "Cet article de référence explique comment les utilisateurs peuvent recibler leurs messages en fonction des interactions WhatsApp."
page_type: reference
channel:
  - WhatsApp
---

# Reciblage des utilisateurs {#user-retargeting}

> En plus de modifier l'état d'abonnement de l'utilisateur, Braze enregistre également les interactions avec le profil utilisateur à des fins de filtrage et de déclenchement de messages.<br><br>Ces filtres et déclencheurs vous permettent de filtrer les utilisateurs qui ont reçu des messages WhatsApp ou qui ont reçu des messages WhatsApp provenant d'une Campaign WhatsApp ou d'une étape du Canvas spécifique.

## Options de reciblage {#retargeting-options}

{% alert note %}
Lors de la création d'audiences avec le reciblage des utilisateurs, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la confidentialité, telles que le droit « Ne pas vendre ou partager » en vertu du CCPA. Les marketeurs doivent mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs dans les critères d'entrée de leur Canvas et/ou Campaign.
{% endalert %}

### Filtrer les utilisateurs par WhatsApp {#filter-users-by-whatsapp}

Les utilisateurs peuvent être filtrés en fonction de la date de leur dernière réception d'un message WhatsApp ou s'ils ont reçu un message WhatsApp provenant d'une Campaign WhatsApp spécifique. Les filtres peuvent être définis à l'étape Cibler les utilisateurs du générateur de Campaign.

#### Filtrer par dernier message WhatsApp reçu {#filter-by-last-received-whatsapp}

![Filtre pour la dernière réception d'un message WhatsApp le 22 avril 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

#### Filtrer par messages reçus d'une Campaign WhatsApp {#filter-by-received-messages-from-whatsapp-campaign}

Filtre les utilisateurs qui ont reçu un message d'une Campaign WhatsApp spécifique. Avec ce filtre, vous avez également la possibilité de filtrer ceux qui n'ont pas reçu de messages d'une Campaign WhatsApp.

{% alert note %}
Lorsqu'un message WhatsApp est livré, ouvert ou cliqué, Braze met à jour les données de tous les profils partageant le même numéro de téléphone que le profil ayant enregistré l'interaction. Ainsi, les utilisateurs qui partagent ce numéro avec quelqu'un qui a reçu, ouvert ou cliqué le message peuvent correspondre aux filtres « reçu » même s'ils n'en étaient pas directement destinataires.
{% endalert %}

![Filtre pour la réception d'une Campaign WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrer par engagement {#filter-by-engagement}

Reciblez les utilisateurs qui ont, ou n'ont pas, lu une Campaign ou une étape du Canvas WhatsApp.

#### Recibler les utilisateurs qui ont ouvert/lu une Campaign WhatsApp spécifique {#retarget-users-who-have-openedread-a-specific-whatsapp-campaign}

1. Créez un segment en utilisant le filtre **Clicked/Opened Campaign**.
2. Sélectionnez **read WhatsApp message**.
3. Choisissez la Campaign souhaitée.

![Filtre pour avoir lu un message WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

#### Recibler les utilisateurs qui ont ouvert/lu une étape du Canvas spécifique {#retarget-users-who-have-openedread-a-specific-canvas-step}

1. Créez un segment en utilisant le filtre **Clicked/Opened Step**.
2. Sélectionnez **read WhatsApp message**.
3. Choisissez le Canvas et les étapes du Canvas souhaités.

![Filtre pour la lecture d'une étape WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

#### Filtrer par attribution de Campaign ou de Canvas {#filter-by-campaign-or-canvas-attribution}

Filtrez les utilisateurs qui ont ouvert/lu une Campaign ou un composant Canvas WhatsApp spécifique, ou une étiquette.

![Filtre pour l'ouverture d'un message WhatsApp spécifique.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}