{% if include.section == "SDK requirements" %}

## Conditions préalables {#prerequisites}

### Versions minimales du SDK {#minimum-sdk-versions}

Les messages créés à l'aide de l'éditeur par glisser-déposer ne peuvent être envoyés qu'aux utilisateurs disposant des versions minimales suivantes du SDK. Pour plus d'informations, consultez [Créer un message in-app par glisser-déposer : Prérequis]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#prerequisites).

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versions du SDK pour les liens texte {#sdk-versions-for-text-links}

Pour inclure des liens texte qui ne ferment pas le message, les versions minimales suivantes du SDK sont requises :

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Si vous incluez dans votre message in-app un lien qui redirige vers une URL et que l'utilisateur ne dispose pas des versions minimales du SDK spécifiées, le fait de cliquer sur le lien fermera le message et l'utilisateur ne pourra pas revenir au message pour soumettre le formulaire.
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

Avant de commencer à personnaliser votre modèle, vous pouvez définir des styles au niveau du message pour l'ensemble du message à l'aide du menu latéral. Par exemple, vous pouvez personnaliser la police de tout le texte ou la couleur de tous les liens inclus dans votre message. Vous pouvez également faire en sorte que le message s'affiche sous forme de fenêtre modale ou en plein écran.

{% endif %}


<!-- Add this after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

Nous vous recommandons d'inclure dans votre message des mentions d'abonnement et des liens vers la politique de confidentialité et les conditions générales de votre marque. Veillez à collaborer avec votre équipe juridique pour élaborer un texte adapté à votre marque.

{% alert note %}
Les bonnes pratiques en matière de livrabilité dépassent souvent les exigences légales, et notre recommandation est de toujours obtenir un consentement explicite pour l'envoi d'e-mails et de permettre aux utilisateurs de se désabonner facilement.
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

Si l'utilisateur saisit une adresse e-mail contenant des caractères spéciaux non acceptés, un indicateur d'erreur générique s'affichera et il ne pourra pas soumettre le formulaire. Ce message d'erreur n'est pas personnalisable. Vous pouvez visualiser le comportement de l'erreur dans l'onglet **Preview & Test** et sur votre appareil de test. Pour en savoir plus sur la manière dont Braze formate les adresses e-mail, consultez [Validation de l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation).

{% endif %}

{% if include.section == "email double opt-in" %}

### Double vérification d'abonnement {#double-opt-in-verification}

Pour vous assurer que toute personne inscrite à votre liste souhaitait réellement s'y inscrire et a fourni la bonne adresse e-mail, nous vous recommandons d'obtenir une seconde confirmation de la part de toute personne inscrite via votre formulaire d'inscription par e-mail en envoyant un flux de [double opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in).

L'un des moyens d'y parvenir est d'utiliser Canvas :

1. Créez un Canvas basé sur l'action et configurez-le pour qu'il se déclenche lorsqu'un utilisateur ajoute une adresse e-mail à Braze. Assurez-vous de permettre le ciblage des utilisateurs qui découvrent la plateforme (par exemple, en utilisant un segment sans filtre dans le Canvas).
2. Créez une étape de message e-mail avec un CTA comportant un lien hypertexte vers l'étiquette Liquid {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. L'état d'abonnement e-mail de l'utilisateur passera ainsi à `opted_in` lorsqu'il cliquera sur le bouton.
3. Ajoutez une [étape de parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. Pour le premier parcours, déclenchez un e-mail lorsqu'un utilisateur modifie son statut d'abonnement e-mail sur `opted_in`. Cet e-mail doit informer les utilisateurs que leur adresse e-mail a été confirmée.
5. Configurez l'autre parcours pour quitter le Canvas après l'expiration de la fenêtre.

{% endif %}

{% if include.section == "reporting" %}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour savoir combien d'utilisateurs ont interagi avec votre campagne. Pour savoir combien d'utilisateurs se sont abonnés au groupe d'abonnement, vous pouvez [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) d'utilisateurs abonnés au groupe d'abonnement en filtrant ceux qui ont reçu le message in-app et soumis le formulaire.

{% endif %}