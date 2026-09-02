---
nav_title: Zoom-Registrierung automatisieren
article_title: Zoom-Registrierung automatisieren
page_order: 1
page_type: tutorial
description: "Dieser Artikel beschreibt, wie Sie die Zoom-Teilnehmerregistrierung in Ihren E-Mail-, Push- und In-App-Nachrichten-Campaigns automatisieren können."
channel:
  - email
  - push
  - in-app messages

---

# Zoom-Registrierung automatisieren {#automate-zoom-registration}

> Webinare sind in den letzten Jahren bei Braze-Kund:innen zu einem gängigen Format geworden. Beim Hosten eines Zoom-Webinars müssen Nutzer:innen ihre Daten auf einer Zoom-Landing-Page eingeben, um sich anzumelden.

Ein empfohlener Nutzerfluss ist im Folgenden beschrieben:
1. Planen Sie ein Webinar in Zoom und generieren Sie eine `webinarId`.
2. Nutzen Sie Braze, um Zoom-Webinare über E-Mail-, Push- und In-App-Nachrichten-Kanäle zu bewerben.
3. Fügen Sie in diesen Kommunikationen einen Aktions-Button ein, der Nutzer:innen automatisch zum Webinar hinzufügt.

Dies lässt sich mithilfe der [Zoom-APIs](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) umsetzen, um Nutzer:innen per Button-Klick in einer E-Mail, Push- oder In-App-Nachricht automatisch zu einem Webinar hinzuzufügen. Verwenden Sie den folgenden Endpunkt und ersetzen Sie die Webinar-ID in der API-Anfrage.

POST: `/meetings/{webinarId}/registrants`

Weitere Informationen finden Sie beim Zoom-Endpunkt [Webinar-Registrierung hinzufügen](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate).<br><br>

{% tabs %}
{% tab E-Mail %}

Erstellen Sie eine E-Mail-Campaign mit einem Aktions-Button im Nachrichtentext. Wenn Nutzer:innen auf den Button klicken, leiten Sie sie zur Webinar-Landing-Page weiter (mit entsprechenden Parametern im Redirect-Link).

Verwenden Sie die Parameter in der URL, um Nutzerdaten zu übergeben, und erstellen Sie einen API-Aufruf, der beim Laden der Seite ausgelöst wird, um die Nutzer:innen zum Webinar hinzuzufügen.

![E-Mail-Nachricht mit Liquid-Templating zur Einbindung von Vorname, Nachname, E-Mail-Adresse und Ort.]({% image_buster /assets/img/zoom/zoom1.png %})

Die Nutzer:innen sind nun mit den Daten, die bereits in ihrem Braze-Profil vorhanden sind, für das Webinar registriert.

{% endtab %}
{% tab Push %}

1. Erstellen Sie eine Push-Campaign<br><br>

	Legen Sie das Klickverhalten für den Button so fest, dass er zur Webinar-Landing-Page weiterleitet.<br>

	![Weiterleitung zum Webinar, wenn ein Button angeklickt wird.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Ein einfaches Beispiel einer Landing-Page für Nutzer:innen, die sich per Button-Klick aus einer Push-Nachricht anmelden. Informieren Sie die Nutzer:innen darüber, wofür sie sich angemeldet haben, und bestätigen Sie ihre registrieren:<br>

	![Bestätigungs-Landing-Page für das Webinar, nachdem sich Nutzer:innen über Braze angemeldet haben.]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Erstellen Sie eine Webhook-Campaign, die durch die In-App-Nachricht oder den Button-Klick getriggert wird.<br><br>
 	Melden Sie die Nutzer:innen mithilfe der vorhandenen Nutzerdaten aus ihrem Braze-Profil für das Webinar an.<br>

	![Eine aktionsbasierte Campaign, die an Nutzer:innen gesendet wird, die einen Button in einer bestimmten Campaign angeklickt haben.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Beispiel eines Webhook-Aufrufs an den Zoom-Endpunkt.<br>
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

3. Die Nutzer:innen sind nun mit den Daten, die bereits in ihrem Braze-Profil vorhanden sind, für das Webinar registriert.

{% endtab %}
{% tab In-App-Nachricht %}

1. Erstellen Sie eine In-App-Nachrichten-Campaign<br><br>

	Legen Sie das Klickverhalten für den Button so fest, dass er zur Webinar-Landing-Page weiterleitet.<br>

	![Weiterleitung zum Webinar, wenn ein Button angeklickt wird.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Ein einfaches Beispiel einer Landing-Page für Nutzer:innen, die sich per Button-Klick aus einer In-App-Nachricht anmelden. Informieren Sie die Nutzer:innen darüber, wofür sie sich angemeldet haben, und bestätigen Sie ihre registrieren:<br>

	![Bestätigungs-Landing-Page für das Webinar, nachdem sich Nutzer:innen über Braze angemeldet haben.]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Erstellen Sie eine Webhook-Campaign, die durch die In-App-Nachricht oder den Button-Klick getriggert wird.<br><br>
	Melden Sie die Nutzer:innen mithilfe der vorhandenen Nutzerdaten aus ihrem Braze-Profil für das Webinar an.<br>

	![Eine aktionsbasierte Campaign, die an Nutzer:innen gesendet wird, die einen Button in einer bestimmten Campaign angeklickt haben.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Beispiel eines Webhook-Aufrufs an den Zoom-Endpunkt.<br>
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
3. Die Nutzer:innen sind nun mit den Daten, die bereits in ihrem Braze-Profil vorhanden sind, für das Webinar registriert.

{% endtab %}
{% endtabs %}