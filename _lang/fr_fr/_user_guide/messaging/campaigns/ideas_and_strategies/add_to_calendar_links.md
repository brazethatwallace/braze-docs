---
nav_title: Liens d'ajout au calendrier
article_title: Liens d'ajout au calendrier
page_order: 1
page_type: tutorial
description: "Cet article explique comment inclure un lien d'ajout au calendrier dans vos campagnes d'e-mail."
channel: email

---

# Liens d'ajout au calendrier {#add-to-calendar-links}

> Lorsque vous faites la promotion d'un événement, d'une vente ou d'un rendez-vous, vous pouvez aider vos utilisateurs à enregistrer facilement l'événement dans leur calendrier en ajoutant un lien « ajouter au calendrier » dans vos e-mails.

Rédigez votre e-mail et choisissez l'emplacement des deux options de calendrier : un lien pour Google Calendar et un pour les autres calendriers (comme iCal ou Outlook). Utilisez un texte de lien tel que « Ajouter à Google Calendar » et « Ajouter à iCal ou Outlook ».

La manière d'associer les URL dépend de l'éditeur d'e-mail que vous utilisez :

- **Éditeur par glisser-déposer :** Dans un bloc **Paragraph**, sélectionnez les mots à lier, ouvrez le contrôle **Link** dans la barre d'outils et collez l'URL depuis le [format d'URL](#url-format). Vous pouvez également utiliser un bloc **Button**, définir le **Link type** sur **Open web page** et coller l'URL dans **URL**.
- **Éditeur HTML :** Utilisez les contrôles de lien en texte enrichi pour le texte lié, ou ajoutez des balises `<a href="...">` dans votre HTML pour chaque URL de calendrier.

## Format d'URL {#url-format}

Ajoutez l'URL suivante à vos liens, en remplaçant les marques substitutives. La seule différence entre ces deux URL est que Google Calendar nécessite un paramètre supplémentaire : `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal ou Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Remplacez les éléments suivants :

- `EVENT_SUBJECT` : Titre de l'événement
- `EVENT_LOCATION` : Emplacement de l'événement
- `START_TIME` : Heure de début de l'événement au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC
- `END_TIME` : Heure de fin de l'événement au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC
- `EVENT_DESCRIPTION` : Description de l'événement

Remplacez les espaces par le code d'échappement HTML `%20`. Par exemple, un sujet « Meet Braze » deviendrait « Meet%20Braze ».

Voici un exemple d'URL « Ajouter à Google Calendar » :

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Paramètres supplémentaires {#additional-parameters}

Les paramètres suivants sont facultatifs et peuvent être utilisés pour définir des aspects supplémentaires d'un événement.

- **Nom de l'organisateur :** `&organizer=name`
- **Joindre une URL liée à l'événement :** `&attach=http://www.example.com/`
- **Durée :** `duration=30M`, comme alternative à l'heure de fin de l'événement (dtend), spécifiez une durée comme 1H ou 30M
- **Rappel d'alarme, en minutes :** `&reminder=15`
- **Événement sur toute la journée :** `&allday=1`
- **UID :** paramètre facultatif permettant de coder en dur l'identifiant unique de l'événement, offrant à certaines applications de calendrier la possibilité de mettre à jour l'événement au fil du temps. La chaîne de caractères @ics.agical.io est automatiquement ajoutée à la valeur.

Vous pouvez également ajouter des paramètres supplémentaires pour les événements récurrents :
- **Événements hebdomadaires :** `&recur=weekly`
- **Événements mensuels :** `&recur=monthly`
- **Fin de la récurrence :** `&recuruntil=END_DATE`, où `END_DATE` est la date et l'heure de fin de la récurrence au format ISO 8601 (YYYY-MM-DDTHH:MM:SSZ) en UTC

## Comportement des liens {#link-behavior}

Lorsqu'un utilisateur clique sur le lien, les calendriers transforment automatiquement les horodatages UTC dans les URL pour refléter le fuseau horaire défini dans son calendrier.

Par exemple, si vous ouvrez l'exemple de lien « Ajouter à Google Calendar » et que votre calendrier est réglé sur CST, l'heure de l'événement sera pré-remplie en fonction de l'équivalent de 15 h UTC en CST (10 h).

### Google Calendar {#google-calendar}

Lorsqu'on clique dessus, Google Calendar s'ouvre dans un nouvel onglet ou une nouvelle fenêtre avec les détails de l'événement pré-remplis dans l'invitation, prêts à être enregistrés par l'utilisateur. Cela fonctionne aussi bien sur mobile que sur ordinateur.

![Boîte de dialogue Google Calendar pour ajouter un événement avec les détails de l'événement renseignés et prêts à être enregistrés.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal ou Outlook {#ical-or-outlook}

Lorsqu'on clique dessus sur ordinateur, un fichier ICS est téléchargé. L'utilisateur doit ensuite ouvrir le fichier ICS, ce qui lance iCal ou Outlook et l'invite à ajouter l'événement à son calendrier.

![Calendrier iCal avec une boîte de dialogue pour ajouter un nouvel événement, qui invite l'utilisateur à sélectionner un calendrier et à confirmer.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![Calendrier iCal avec l'événement ajouté.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Sur mobile, le comportement dépend de l'appareil et de l'application d'e-mail.

{% alert note %}
Sur iPhone, l'application Mail et Microsoft Outlook téléchargent le fichier ICS lorsque les utilisateurs appuient sur le lien iCal, mais ces applications n'ouvrent pas Calendrier à partir du lien. Pour ajouter l'événement, ouvrez le fichier téléchargé depuis **Fichiers**, **Téléchargements** ou la vue des pièces jointes (selon l'application), puis suivez les étapes dans Calendrier.
{% endalert %}

Dans certaines autres applications d'e-mail ou navigateurs mobiles, un appui long sur le lien peut afficher une option pour ajouter l'événement à un calendrier.

![Pop-up iOS qui s'affiche lors d'un appui long sur un lien de calendrier, avec un bouton « Ajouter au calendrier ».]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Pour en savoir plus, consultez :
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)