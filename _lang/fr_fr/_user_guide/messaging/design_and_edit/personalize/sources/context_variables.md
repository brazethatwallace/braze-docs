---
nav_title: Variables de contexte
article_title: Variables de contexte
page_type: reference
description: "Cet article de référence explique les variables de contexte dans les Canvas Braze, y compris leurs types, leur utilisation et les bonnes pratiques."
---

# Variables de contexte {#context-variables}

> Les variables de contexte sont des données temporaires que vous pouvez créer et utiliser au cours du parcours d'un utilisateur dans un Canvas spécifique. Elles vous permettent de personnaliser les délais, de segmenter les utilisateurs de manière dynamique et d'enrichir les messages sans modifier de façon permanente les informations du profil utilisateur. Les variables de contexte n'existent que dans la session du Canvas et ne persistent pas entre différents Canvas ni en dehors de la session.

## Fonctionnement des variables de contexte {#how-context-variables-work}

Les variables de contexte peuvent être définies de deux manières :

- **À l'entrée du Canvas :** lorsque les utilisateurs entrent dans un Canvas, les données de l'événement ou du déclencheur API peuvent automatiquement renseigner les variables de contexte.
- **Dans une étape de contexte :** vous pouvez définir ou mettre à jour manuellement des variables de contexte à l'intérieur du Canvas en ajoutant une [étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context).

Chaque variable de contexte comprend :

- Un nom (tel que `flight_time` ou `subscription_renewal_date`)
- Un type de données (tel que nombre, chaîne de caractères, heure ou tableau)
- Une valeur que vous attribuez à l'aide de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou via l'outil **Add Personalization**.

Une fois définie, vous pouvez utiliser une variable de contexte dans l'ensemble du Canvas en la référençant dans ce format : {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Par exemple, {% raw %}`{{context.${flight_time}}}`{% endraw %} pourrait renvoyer l'heure de vol prévue de l'utilisateur.

Chaque fois qu'un utilisateur entre dans le Canvas — même s'il y est déjà entré auparavant — les variables de contexte sont redéfinies en fonction des dernières données d'entrée et de la configuration du Canvas. Cette approche avec état permet à chaque entrée dans le Canvas de maintenir son propre contexte indépendant, permettant aux utilisateurs d'avoir plusieurs états actifs au sein du même parcours tout en conservant le contexte spécifique de chaque état.

Par exemple, si un client a deux vols à venir, il aura deux états de parcours distincts s'exécutant simultanément, chacun avec ses propres variables de contexte spécifiques au vol, comme l'heure de départ et la destination. Cela vous permet d'envoyer des rappels personnalisés concernant son vol de 14 h vers New York tout en envoyant des mises à jour différentes concernant son vol de 8 h vers Los Angeles le lendemain, de sorte que chaque message reste pertinent par rapport à la réservation spécifique.

## Considérations {#considerations}

Vous pouvez définir jusqu'à 10 variables de contexte par [étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context). Chaque nom de variable peut contenir jusqu'à 100 caractères et ne doit utiliser que des lettres, des chiffres ou des underscores.

Les définitions de variables de contexte peuvent contenir jusqu'à 10 240 caractères. Si vous transmettez des variables de contexte dans un Canvas déclenché par API, elles partagent le même espace de noms que les variables créées dans une étape de contexte. Par exemple, si vous envoyez une variable `purchased_item` dans l'objet de contexte de l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), vous pouvez la référencer comme {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Si vous redéfinissez cette variable dans une étape de contexte, la nouvelle valeur remplacera la valeur API pour le parcours de cet utilisateur.

Vous pouvez stocker jusqu'à 50 Ko par étape de contexte, répartis sur un maximum de 10 variables. Si la taille totale de toutes les variables d'une étape dépasse 50 Ko, les variables qui dépassent la limite ne seront ni évaluées ni stockées. Par exemple, si vous avez trois variables dans une étape de contexte :

- Variable 1 : 30 Ko
- Variable 2 : 19 Ko
- Variable 3 : 2 Ko

La variable 3 ne sera ni évaluée ni stockée car la somme des variables précédentes dépasse 50 Ko.

## Types de données {#data-types}

Les variables de contexte créées ou mises à jour dans l'étape peuvent se voir attribuer les types de données suivants.

{% alert note %}
Les variables de contexte ont les mêmes formats attendus pour les types de données que les [propriétés d'événement]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#expected-format). <br><br>Lorsque vous utilisez le type tableau, Braze tente d'analyser la valeur en JSON, ce qui permet de créer avec succès des tableaux d'objets. Si les objets au sein de vos tableaux ne sont pas du JSON valide, le résultat sera un simple tableau de chaînes de caractères. <br><br>Pour les objets imbriqués et les tableaux d'objets, utilisez le [filtre Liquid `as_json_string`](#converting-connected-content-strings-to-json). Si vous créez le même objet dans une étape de contexte, vous devrez rendre l'objet en utilisant `as_json_string`, comme {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| Type de données | Exemple de nom de variable | Exemple de valeur |
|---|---|---|
| Valeur booléenne | loyalty_program |{% raw %}<code>true</code>{% endraw %}|
| Nombre | credit_score |{% raw %}<code>740</code>{% endraw %}|
| Chaîne de caractères | product_name |{% raw %}<code>green_tea</code>{% endraw %} |
| Tableau | favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
| Tableau (d'objets) | pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
| Heure (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
| Objet (aplati) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de données" }

Par défaut, le type de données heure est en UTC. Si vous utilisez un type de données chaîne de caractères pour stocker une valeur temporelle, vous pouvez définir l'heure dans un fuseau horaire différent comme PST.

Par exemple, si vous envoyez un message à un utilisateur la veille de son anniversaire, vous enregistreriez la variable de contexte comme type de données heure car il y a une logique Liquid associée à l'envoi la veille. En revanche, si vous envoyez un message de fête le jour de Noël (25 décembre), vous n'auriez pas besoin de référencer l'heure comme variable dynamique, donc utiliser un type de données chaîne de caractères serait préférable.

Pour les types de données objet, vous pouvez utiliser la notation par points pour spécifier un chemin à travers les données. Par exemple, si votre étape de contexte définit une variable de contexte `order_summary` avec cette structure :

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

Dans un filtre [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) ou [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split), saisissez le chemin comme nom de variable de contexte en utilisant la notation par points (par exemple, `order_summary.shipping.carrier`). Lorsque le filtre est évalué, Braze résout ce chemin vers la valeur `overnight`.

En Liquid (comme dans une étape [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)), utilisez plutôt {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}.

## Utilisation des variables de contexte {#using-context-variables}

Vous pouvez utiliser les variables de contexte partout où vous utilisez Liquid dans un Canvas, comme dans les étapes [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) et [Mise à jour utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update), en sélectionnant **Add Personalization**. Pour les messages in-app et les bannières dans les étapes Message, vous pouvez sélectionner des variables de contexte pour déterminer quand le message doit expirer.

Par exemple, imaginons que vous souhaitez informer les passagers de leur accès au salon VIP avant leur prochain vol. Ce message ne doit être envoyé qu'aux passagers ayant acheté un billet en première classe. Une variable de contexte est un moyen flexible de suivre cette information.

Les utilisateurs entreront dans le Canvas lorsqu'ils achèteront un billet d'avion. Pour déterminer l'éligibilité à l'accès au salon, nous allons créer une variable de contexte appelée `lounge_access_granted` dans une étape de contexte, puis référencer cette variable de contexte dans les étapes suivantes du parcours utilisateur.

![Variable de contexte configurée pour suivre si un passager est éligible à l'accès au salon VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

Dans cette étape de contexte, nous utiliserons {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} pour déterminer si le type de vol acheté est `first_class`.

Ensuite, nous créerons une étape Message pour cibler les utilisateurs où {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} est `true`. Ce message sera une notification push incluant des informations personnalisées sur le salon. En fonction de cette variable de contexte, les passagers éligibles recevront les messages pertinents avant leur vol.

- Les passagers en première classe recevront : « Profitez d'un accès exclusif au salon VIP ! »
- Les passagers en classe affaires et économique recevront : « Surclassez votre vol pour un accès exclusif au salon VIP. »

![Une étape Message avec différents messages à envoyer, selon le type de billet d'avion acheté.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Vous pouvez ajouter des [options de délai personnalisé]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) avec les informations de l'étape de contexte, ce qui signifie que vous pouvez sélectionner la variable qui retarde les utilisateurs.
{% endalert %}

### Pour les parcours d'action et les critères de sortie {#for-action-paths-and-exit-criteria}

Vous pouvez tirer parti des filtres de comparaison de propriétés avec des variables de contexte ou des attributs personnalisés dans ces actions de déclenchement : **Perform Custom Event** et **Make Purchase**. Ces déclencheurs d'action prennent également en charge les filtres de propriétés pour les propriétés de base et imbriquées.

- Lors de la comparaison avec des propriétés de base, les comparaisons disponibles correspondront au type de la propriété définie par l'événement personnalisé. Par exemple, les propriétés de type chaîne de caractères auront des comparaisons d'égalité exacte et de correspondance d'expression régulière. Les propriétés booléennes seront vrai ou faux.
- Lors de la comparaison avec des propriétés imbriquées, les types ne sont pas prédéfinis, vous pouvez donc sélectionner des comparaisons sur plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, de manière similaire aux comparaisons pour les attributs personnalisés imbriqués. Si vous sélectionnez un type de données qui ne correspond pas au type de données réel de la propriété imbriquée au moment de la comparaison, l'utilisateur ne correspondra pas au parcours d'action ou aux critères de sortie.

#### Exemples de parcours d'action {#action-path-examples}

{% alert important %}
Pour les comparaisons d'attributs personnalisés, la valeur de l'attribut personnalisé utilisée est celle au moment où l'action est effectuée. Cela signifie qu'un utilisateur ne correspondra pas au groupe du parcours d'action si cet attribut personnalisé n'est pas renseigné au moment de la comparaison, ou si la valeur de l'attribut personnalisé ne correspond pas aux comparaisons de propriétés définies. C'est le cas même si l'utilisateur aurait correspondu au moment de son entrée dans l'étape du parcours d'action.
{% endalert %}

{% tabs %}
{% tab Effectuer un événement personnalisé %}

Le parcours d'action suivant est configuré pour trier les utilisateurs ayant effectué l'événement personnalisé `Account_Created` avec la propriété de base `source` vers la variable de contexte `app_source_variable`.

![Un exemple de parcours d'action qui référence une variable de contexte lors de l'exécution d'un événement personnalisé.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Effectuer un achat %}

Le parcours d'action suivant est configuré pour faire correspondre la propriété de base `brand` pour le nom de produit spécifique `shoes` à une variable de contexte `promoted_shoe_brand`.

![Un exemple de parcours d'action qui référence une variable de contexte lors d'un achat.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exemples de critères de sortie {#exit-criteria-examples}

{% tabs %}
{% tab Effectuer un événement personnalisé %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans le Canvas, il quittera le Canvas si :

- Il effectue l'événement personnalisé **Abandon Cart**, et
- La propriété de base **Item in Cart** correspond à la valeur de chaîne de caractères de la variable de contexte `cart_item_threshold`.

![Critères de sortie configurés pour faire sortir un utilisateur s'il effectue un événement personnalisé basé sur la variable de contexte.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Effectuer un achat %}

Les critères de sortie stipulent qu'à tout moment du parcours d'un utilisateur dans le Canvas, il quittera le Canvas si :

- Il effectue un achat spécifique pour le nom de produit « book », et
- La propriété imbriquée « loyalty_program » de cet achat est égale à l'attribut personnalisé « VIP » de l'utilisateur.

![Critères de sortie configurés pour faire sortir un utilisateur s'il effectue un achat.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Définir une expiration {#set-an-expiration}

Pour les [bannières]({{site.baseurl}}/user_guide/channels/banners) et les [messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages) dans une étape [Message]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) d'un Canvas, sélectionnez **A duration after the step is available** pour l'expiration, puis activez **Personalize duration** pour piloter la fenêtre de disponibilité à partir d'une variable de contexte — par exemple, pour correspondre à la durée d'une promotion ou d'une réservation définie dans une étape de contexte.

**Personalize duration** s'applique à cette option d'expiration basée sur la durée. Si vous choisissez plutôt **On a specific date and time**, définissez l'expiration à l'aide des contrôles de date et d'heure.

### Délais des parcours d'action {#action-path-delays}

Dans une étape [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), sous **Evaluation Window**, activez **Personalize delay** pour définir la durée pendant laquelle les utilisateurs sont retenus dans l'étape à partir d'une variable de contexte. Utilisez cette option lorsque la période d'attente doit varier par utilisateur en fonction de détails tels que le niveau ou la région.

### Filtres de variables de contexte {#context-variable-filters}

Vous pouvez créer des filtres qui utilisent des variables de contexte précédemment déclarées dans les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) et [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split).

{% alert note %}
Les filtres de variables de contexte ne sont disponibles que pour les étapes Parcours d'audience et Arbre décisionnel.
{% endalert %}

Les variables de contexte sont déclarées et accessibles uniquement dans le périmètre d'un Canvas, ce qui signifie qu'elles ne peuvent pas être référencées dans les Segments. Les filtres de variables de contexte fonctionnent de manière similaire dans les étapes Parcours d'audience et Arbre décisionnel — les étapes Parcours d'audience représentent plusieurs groupes, tandis que les étapes Arbre décisionnel représentent des décisions binaires.

![Exemple d'étape Arbre décisionnel avec l'option de créer un filtre avec une variable de contexte.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

De la même manière que les variables de contexte Canvas ont des types prédéfinis, les comparaisons entre variables de contexte et valeurs statiques doivent avoir des [types de données correspondants]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support). Le filtre de variable de contexte permet des comparaisons sur plusieurs types de données pour les booléens, les nombres, les chaînes de caractères, l'heure et le jour de l'année, de manière similaire aux comparaisons pour les [attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% alert note %}
Utilisez le même type de données pour votre variable de contexte et votre comparaison. Par exemple, si votre variable de contexte est de type heure, utilisez des comparaisons temporelles (telles que « avant » ou « après »). L'utilisation de types de données incompatibles (comme des comparaisons de chaînes de caractères avec une variable de contexte de type heure) peut entraîner un comportement inattendu.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Voici un exemple de filtre de variable de contexte comparant la variable de contexte `product_name` à l'expression régulière `/braze/`.

![Configuration d'un filtre pour la variable de contexte « product_name » correspondant à l'expression régulière « /braze/ ».]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparaison avec des variables de contexte ou des attributs personnalisés {#comparing-to-context-variables-or-custom-attributes}

En activant le bouton **Compare to a context variable or custom attribute**, vous pouvez construire des filtres de variables de contexte qui comparent avec des variables de contexte précédemment définies ou des attributs personnalisés utilisateur. Cela peut être utile pour effectuer des comparaisons dynamiques par utilisateur, comme le `context` déclenché par API, ou pour condenser une logique de comparaison complexe définie à travers des variables de contexte.

{% tabs %}
{% tab Exemple 1 %}

Imaginons que vous souhaitez envoyer un rappel personnalisé aux utilisateurs après une période d'inactivité dynamique : toute personne ne s'étant pas connectée à votre application au cours des trois derniers jours doit recevoir un message.

Vous avez une variable de contexte `re_engagement_date` définie comme {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Notez que `3 days` peut être un montant variable également stocké comme attribut personnalisé de l'utilisateur. Ainsi, si la `re_engagement_date` est postérieure à la `last_login_date` (stockée comme attribut personnalisé sur le profil utilisateur), un message leur sera envoyé.

![Configuration d'un filtre avec les attributs personnalisés comme type de personnalisation pour la variable de contexte « re_engagement_date » après l'attribut personnalisé « last_login_date ».]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Exemple 2 %}

Le filtre suivant compare la variable de contexte `reminder_date` pour qu'elle soit antérieure à la variable de contexte `appointment_deadline`. Cela peut aider à regrouper les utilisateurs dans une étape Parcours d'audience pour déterminer s'ils doivent recevoir des rappels supplémentaires avant la date limite de leur rendez-vous.

![Configuration d'un filtre avec les variables de contexte comme type de personnalisation pour la variable de contexte « reminder_date » sur la variable de contexte « appointment_deadline ».]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Standardisation de la cohérence des fuseaux horaires {#time-zone-consistency-standardization}

Bien que la plupart des propriétés d'événement utilisant le type horodatage soient déjà en UTC dans Canvas, il existe quelques exceptions. Avec l'ajout du contexte Canvas, toutes les propriétés d'événement d'horodatage par défaut dans les Canvas basés sur des actions seront systématiquement en UTC. Ce changement s'inscrit dans un effort plus large visant à garantir une expérience plus prévisible et cohérente lors de la modification des étapes et des messages Canvas. Notez que ce changement impactera tous les Canvas basés sur des actions, que le Canvas en question utilise ou non une étape de contexte.

{% alert important %}
Dans tous les cas, nous recommandons fortement d'utiliser les [filtres Liquid time_zone]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) pour que les horodatages soient représentés dans le fuseau horaire souhaité. Vous pouvez consulter cette [question fréquemment posée dans l'article sur l'étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#faq-example) pour un exemple.
{% endalert %}

## Articles connexes {#related-articles}

- [Étape de contexte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Personnalisation et contenu dynamique avec Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)