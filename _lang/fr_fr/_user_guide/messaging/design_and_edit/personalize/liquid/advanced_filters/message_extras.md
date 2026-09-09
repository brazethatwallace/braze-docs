---
nav_title: Étiquette message extras
article_title: Étiquette message extras
page_order: 1
description: "Cet article explique comment utiliser l'étiquette Liquid message extras et comment vérifier la syntaxe."
alias: "/message_extras_tag/"
---

# Étiquette Liquid message extras {#message-extras-liquid-tag}

> Utilisez l'étiquette Liquid `message_extras` pour annoter vos événements d'envoi avec des données dynamiques provenant du contenu connecté, des catalogues, des attributs personnalisés (tels que la langue, le pays), des propriétés d'entrée Canvas ou d'autres sources de données.

L'étiquette Liquid `message_extras` ajoute des paires clé-valeur à l'événement d'envoi correspondant dans Currents et le partage de données Snowflake.

Pour renvoyer des données dynamiques ou supplémentaires à votre événement d'envoi Currents ou partage de données Snowflake, insérez l'étiquette Liquid appropriée dans le corps de votre message.

Voici un exemple du format standard de l'étiquette Liquid pour `message_extras` :

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Vous pouvez ajouter ces étiquettes selon vos besoins pour vos paires clé-valeur dans le corps du message. Cependant, la longueur totale de toutes les clés et valeurs ne doit pas dépasser 1 000 octets (1&nbsp;Ko). Dans Currents et le partage de données Snowflake, vous verrez un nouveau champ d'événement appelé `message_extras` pour vos événements d'envoi. Celui-ci génère une chaîne de caractères sérialisée en JSON dans un seul champ.

{% alert note %}
Les extras d'e-mail envoient des métadonnées aux fournisseurs de services d'e-mail marketing et ne sont pas publiés dans Currents ni dans Snowflake. Pour ajouter des métadonnées ou des valeurs dynamiques aux événements d'envoi Currents ou Snowflake, utilisez l'étiquette Liquid `message_extras`.
{% endalert %}

## Comment les données des extras de message sont envoyées via Currents {#how-message-extras-data-is-sent-using-currents}

Les **extras de message** sont des paires clé-valeur associées au moment de l'envoi. La configuration dépend du canal. Pour l'e-mail, ils sont ajoutés via des en-têtes. Pour les notifications push iOS, ils sont inclus dans le payload push. Tous les événements d'envoi pris en charge exposent le même champ `message_extras` dans Currents (et Snowflake) une fois le message envoyé.

## Canaux pris en charge {#supported-channels}

La balise `message_extras` est prise en charge pour tous les types de messages avec un événement d'envoi, ainsi que pour les événements d'impression de messages in-app. L'utilisation de `message_extras` avec les messages in-app nécessite certaines [versions minimales du SDK](#iam-sdk).

## Comment utiliser la balise `message_extras` {#how-to-use-the-message_extras-tag}

1. Dans le corps du message pour le canal, saisissez la balise Liquid `message_extras`. Vous pouvez également utiliser la fenêtre modale **Add Personalization** et sélectionner **Message Extras** comme type de personnalisation.

![La fenêtre modale Add Personalization avec Message Extras sélectionné comme type de personnalisation.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Saisissez la [paire clé-valeur]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) pour chaque balise `message_extras`.

![Un exemple de paires clé-valeur pour la balise message extras. Le champ de titre indique « Your New Favorites ». Le message affiche des paires clé-valeur pour la balise message extras et la phrase suivante : « We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites »]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Une fois votre Campaign ou Canvas envoyé, Braze attache les données dynamiques au moment de l'envoi au champ `message_extras` dans les événements d'envoi Currents ou Snowflake Data Sharing.

## Vérification de la syntaxe {#checking-syntax}

Toute autre entrée qui ne correspond pas au standard de tag décrit précédemment dans cette section peut ne pas être transmise à Currents ou Snowflake. Vérifiez que votre syntaxe ou votre formatage ne contient aucun des éléments suivants :

- Délimiteurs inexistants, vides ou mal saisis
- Clés en double (Braze envoie par défaut la paire clé-valeur rencontrée en premier)
- Texte supplémentaire avant la définition des clés ou des valeurs
- Clés et valeurs dans le mauvais ordre
  - {% raw %}Par exemple, `{% message_extras :value 123 :key test %}`{% endraw %}

## Envoi des informations de codes de promotion à Currents {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Considérations {#considerations}

- Les paires clé-valeur dépassant 1 000 octets (1&nbsp;Ko) sont tronquées.
- Les espaces comptent dans le nombre de caractères. Notez que Braze omet les espaces en début et en fin de chaîne.
- Les sorties JSON résultantes ne produisent que des valeurs de type chaîne de caractères.
- Vous pouvez inclure des variables Liquid en tant que clé ou valeur, mais vous ne pouvez pas imbriquer d'autres balises Liquid à l'intérieur de `message_extras`.
  - Par exemple, vous pouvez utiliser le Liquid suivant : {% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## Questions fréquemment posées {#frequently-asked-questions}

### Comment puis-je associer le champ message_extras dans les événements d'envoi à mes événements d'engagement comme les ouvertures et les clics ? {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

Un `dispatch_id` est généré et fourni dans vos événements d'envoi. Vous pouvez l'utiliser comme identifiant unique pour le relier à des événements spécifiques de clic, d'ouverture ou de livraison. Interrogez ce champ dans Currents ou Snowflake. Pour plus d'informations, consultez [Comportement du dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

#### Puis-je utiliser message_extras avec les messages in-app ? {#iam-sdk}

Oui, vous pouvez utiliser `message_extras` dans vos messages in-app à condition que les appareils de vos utilisateurs disposent des versions minimales du SDK suivantes :

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}