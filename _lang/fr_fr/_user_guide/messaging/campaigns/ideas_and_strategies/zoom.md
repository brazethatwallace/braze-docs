---
nav_title: Automatiser l'inscription Zoom
article_title: Automatiser l'inscription Zoom
page_order: 1
page_type: tutorial
description: "Cet article explique comment automatiser l'inscription des participants Zoom dans vos campagnes par e-mail, notification push et message in-app."
channel:
  - email
  - push
  - in-app messages

---

# Automatiser l'inscription Zoom {#automate-zoom-registration}

> Les webinaires sont devenus courants chez les clients de Braze au cours des dernières années. Lors de l'organisation d'un webinaire Zoom, les utilisateurs doivent saisir leurs informations sur une page d'inscription Zoom pour s'inscrire.

Voici le parcours utilisateur recommandé :
1. Planifiez un webinaire dans Zoom et générez un `webinarId`.
2. Utilisez Braze pour promouvoir les webinaires Zoom via les canaux e-mail, notification push et message in-app.
3. Incluez un bouton d'appel à l'action dans ces communications pour inscrire automatiquement les utilisateurs au webinaire.

Pour ce faire, utilisez les [API Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) afin d'ajouter automatiquement un utilisateur à un webinaire via un clic sur un bouton dans un e-mail, une notification push ou un message in-app. Utilisez l'endpoint suivant en remplaçant l'ID du webinaire dans la requête API.

POST : `/meetings/{webinarId}/registrants`

Pour en savoir plus, consultez l'[endpoint d'ajout d'un inscrit au webinaire](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) de Zoom.<br><br>

{% tabs %}
{% tab E-mail %}

Créez une campagne par e-mail avec un bouton d'appel à l'action dans le corps du message. Lorsqu'un utilisateur clique sur le bouton, redirigez-le vers la page d'inscription du webinaire (avec les paramètres appropriés inclus dans le lien de redirection).

En utilisant les paramètres de l'URL pour transmettre les données utilisateur, créez un appel API qui se déclenche au chargement de la page pour inscrire l'utilisateur au webinaire.

![Message e-mail utilisant le templating Liquid pour inclure le prénom, le nom, l'adresse e-mail et la ville.]({% image_buster /assets/img/zoom/zoom1.png %})

Les utilisateurs sont désormais inscrits au webinaire avec les informations déjà présentes sur leur profil Braze.

{% endtab %}
{% tab Notification push %}

1. Créez une campagne de notification push<br><br>

	Définissez le comportement au clic du bouton pour rediriger vers la page d'inscription du webinaire.<br>

	![Redirection vers le webinaire lorsqu'un bouton est cliqué.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Voici un exemple simple de page d'inscription pour les utilisateurs qui s'inscrivent via un clic sur le bouton d'une notification push. Informez l'utilisateur de son inscription et confirmez-la :<br>

	![Page de confirmation d'inscription au webinaire affichée après l'inscription d'un utilisateur depuis Braze.]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Créez une campagne webhook déclenchée par le message in-app ou le clic sur le bouton.<br><br>
 	En utilisant les données utilisateur existantes sur leur profil Braze, inscrivez l'utilisateur au webinaire.<br>

	![Une campagne basée sur une action qui sera envoyée aux utilisateurs ayant cliqué sur un bouton pour une campagne spécifique.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Exemple d'appel webhook vers l'endpoint Zoom.<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Les utilisateurs sont désormais inscrits au webinaire avec les informations déjà présentes sur leur profil Braze.

{% endtab %}
{% tab Message in-app %}

1. Créez une campagne de message in-app<br><br>

	Définissez le comportement au clic du bouton pour rediriger vers la page d'inscription du webinaire.<br>

	![Redirection vers le webinaire lorsqu'un bouton est cliqué.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Voici un exemple simple de page d'inscription pour les utilisateurs qui s'inscrivent via un clic sur le bouton d'un message in-app. Informez l'utilisateur de son inscription et confirmez-la :<br>

	![Page de confirmation d'inscription au webinaire affichée après l'inscription d'un utilisateur depuis Braze.]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Créez une campagne webhook déclenchée par le message in-app ou le clic sur le bouton.<br><br>
	En utilisant les données utilisateur existantes sur leur profil Braze, inscrivez l'utilisateur au webinaire.<br>

	![Une campagne basée sur une action qui sera envoyée aux utilisateurs ayant cliqué sur un bouton pour une campagne spécifique.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Exemple d'appel webhook vers l'endpoint Zoom.<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Les utilisateurs sont désormais inscrits au webinaire avec les informations déjà présentes sur leur profil Braze.

{% endtab %}
{% endtabs %}