---
nav_title: Messages de droite à gauche
article_title: Créer des messages de droite à gauche
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "Cette page présente les bonnes pratiques pour rédiger des messages dans Braze qui se lisent de droite à gauche."
---

# Créer des messages de droite à gauche {#create-right-to-left-messages}

> L'apparence finale des messages de droite à gauche dépend en grande partie de la façon dont les fournisseurs de services (tels qu'Apple, Android et Google) les affichent. Cette page présente les bonnes pratiques pour rédiger des messages de droite à gauche afin que vos messages s'affichent aussi fidèlement que possible.

## Apparence des messages {#message-appearance}

Lorsque vous créez un message de droite à gauche, gardez les points suivants à l'esprit :

- **Apparence dans le tableau de bord de Braze :** Lorsqu'un message s'affiche sur l'appareil d'un utilisateur, son apparence est largement déterminée par le système d'exploitation et les paramètres de langue de l'appareil&#8212;ce qui signifie que ce que vous voyez dans le tableau de bord n'est pas toujours fidèle à 100 %.
- **Apparence sur l'appareil :** Apple et Android exercent un contrôle important sur le rendu des messages, tandis que les fournisseurs de services d'e-mail marketing or e-mailing (fournisseur de services d'e-mailing) disposent d'un certain contrôle. La personnalisation des e-mails HTML dans Braze peut être plus flexible ; cependant, un même message peut s'afficher différemment selon les appareils en fonction des paramètres de l'utilisateur.

De plus, vérifiez la ponctuation et les emojis pour déterminer si votre message s'affiche en mode standard ou de droite à gauche.

| Rendu occidental standard | Rendu de droite à gauche |
|------------------|------------------------|
| Affiche le point d'exclamation et l'emoji à la **fin** des phrases. | Affiche le point d'exclamation et l'emoji au **début** de la phrase. |
| ![Exemple de message avec rendu standard de droite à gauche.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![Exemple de message avec rendu de gauche à droite.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Apparence des messages" }

## Créer un message de droite à gauche {#creating-a-right-to-left-message}

Pour créer votre message de droite à gauche dans Braze :

1. Rédigez votre message standard dans l'éditeur Braze.
2. Copiez le texte du message depuis Braze, puis utilisez un outil de localisation pour le convertir en message de droite à gauche.
3. Collez votre message converti dans Braze.
4. Vérifiez le formatage et l'alignement du texte. Si vous créez un e-mail en glisser-déposer ou en HTML, vous pouvez le faire directement dans le compositeur. Sinon, vous devrez utiliser un traitement de texte séparé.<br><br>![Menu de l'éditeur d'e-mail en glisser-déposer avec un bouton pour basculer l'alignement du texte entre droite à gauche et gauche à droite.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Points à prendre en compte {#considerations}

### Notifications push longues {#long-push-notifications}

La méthode de copier-coller pour les messages push peut être difficile à utiliser avec les notifications push plus longues, car un contenu plus long peut s'afficher sur plusieurs lignes sur un appareil mobile. Si vous copiez le texte de votre message depuis l'extérieur de Braze (par exemple un document Word) et le collez directement dans Braze, l'alignement des phrases et le placement des mots peuvent changer. Pour éviter ce scénario, copiez et collez par segments et ajoutez un saut de ligne. Par exemple, copiez et collez les cinq premiers mots, ajoutez un saut de ligne, copiez les cinq mots suivants, ajoutez un saut de ligne, et ainsi de suite.

Les fonctions de prévisualisation et de test sont conçues pour les messages de gauche à droite, donc les messages de droite à gauche ne s'afficheront pas correctement dans la section **Preview & Test**, mais s'afficheront correctement sur les appareils des utilisateurs si leurs paramètres sont configurés en conséquence. Nous vous suggérons de vous envoyer des messages dans un environnement en production pour confirmer qu'ils s'affichent correctement en fonction des paramètres de l'appareil.

### Alignement du titre et du corps {#title-and-body-alignment}

Pour les notifications push, l'alignement du titre suit généralement les paramètres de langue de l'appareil, tandis que l'alignement du corps peut suivre le premier caractère directionnel fort de chaque ligne (traitez chaque ligne après un saut de ligne séparément). Cela signifie qu'une seule notification push peut mélanger les alignements d'une ligne à l'autre — par exemple, une ligne de corps de droite à gauche suivie d'une ligne de gauche à droite. Lorsque vous avez besoin d'une mise en page prévisible, maintenez une cohérence directionnelle et utilisez des sauts de ligne entre les segments multilingues.

{% alert note %}
Le rendu dépend toujours du système d'exploitation de l'appareil et du client push. Envoyez des [messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) à vos propres appareils pour confirmer l'alignement avant de passer en production.
{% endalert %}

### Texte bidirectionnel {#bi-directional-text}

De nombreux utilisateurs qui écrivent dans des langues de droite à gauche utilisent en réalité du texte bidirectionnel : une combinaison de langues de gauche à droite et de droite à gauche. Par exemple, un marketeur peut envoyer un message en hébreu contenant un nom d'entreprise en anglais. Braze ne peut pas gérer le formatage du texte bidirectionnel. Deux façons d'éviter les problèmes de formatage sont soit d'éviter complètement le texte bidirectionnel, soit de séparer le texte de gauche à droite du texte de droite à gauche à l'aide de sauts de ligne.

{% alert tip %}
Un formatage correct du texte bidirectionnel est particulièrement important lors de la rédaction de messages contenant des codes promotionnels ; les codes promotionnels sont souvent dans un format de gauche à droite car les mêmes codes peuvent être utilisés sur différents marchés. Deux façons d'intégrer les codes promotionnels sont soit d'utiliser une image pour le code promotionnel, soit d'ajouter le code promotionnel à la fin du message après un saut de ligne.
{% endalert %}

### Caractères spéciaux, nombres et emojis {#special-characters-numbers-and-emojis}

Les caractères spéciaux (tels que la ponctuation, les symboles mathématiques et les devises), les nombres, les puces et les emojis peuvent « se déplacer » lors de la rédaction de messages de droite à gauche dans Braze. Pour contourner ce problème, rédigez votre texte avec un formatage correct dans un traitement de texte externe, puis collez le texte dans Braze. Il peut également être utile d'éviter de placer des emojis au début de votre texte et de les séparer (ainsi que les caractères spéciaux et les nombres) du texte à l'aide de sauts de ligne pour éviter les problèmes d'alignement.

### Messages en arabe {#arabic-messages}

Lors de la rédaction de messages en arabe, utilisez des tailles de police nettement plus grandes pour obtenir la même lisibilité qu'avec d'autres langues. Nous vous suggérons d'utiliser une taille de police environ 20 % plus grande que votre taille habituelle pour les langues utilisant l'alphabet latin ou romain. Cela s'explique par le fait que les polices arabes sont conçues en petite taille pour s'adapter à l'espace vertical occupé par les signes diacritiques (accents).