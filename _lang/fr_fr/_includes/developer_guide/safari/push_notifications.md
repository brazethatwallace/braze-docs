{% multi_lang_include developer_guide/prerequisites/web.md %} Il sera également nécessaire de [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) pour le SDK Web. Veuillez noter que vous ne pouvez envoyer des notifications push qu'aux utilisateurs iOS et iPadOS qui utilisent [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) ou une version ultérieure.

## Configuration des notifications push Safari pour mobile {#setting-up-safari-push-for-mobile}

### Étape 1 : Créer un fichier manifeste {#manifest}

Un [manifeste d'application web](https://developer.mozilla.org/en-US/docs/Web/Manifest) est un fichier JSON qui contrôle la façon dont votre site web est présenté lorsqu'il est installé sur l'écran d'accueil d'un utilisateur.

Par exemple, vous pouvez définir la couleur du thème d'arrière-plan et l'icône utilisés par le [sélecteur d'applications](https://support.apple.com/en-us/HT202070), choisir si le site s'affiche en plein écran pour ressembler à une application native, ou si l'application doit s'ouvrir en mode paysage ou portrait.

Créez un nouveau fichier `manifest.json` dans le répertoire racine de votre site web, avec les champs obligatoires suivants.

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

La liste complète des champs pris en charge est disponible dans la [documentation MDN sur les manifestes d'applications web](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Étape 2 : Lier le fichier manifeste {#manifest-link}

Ajoutez la balise `<link>` suivante à l'élément `<head>` de votre site web, en pointant vers l'emplacement où votre fichier manifeste est hébergé.

```html
<link rel="manifest" href="/manifest.json" />
```

### Étape 3 : Ajouter un service de traitement {#service-worker}

Votre site web doit disposer d'un fichier de service de traitement qui importe la bibliothèque de service de traitement de Braze, comme décrit dans notre [guide d'intégration des notifications push web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker).

### Étape 4 : Ajouter à l'écran d'accueil {#add-to-homescreen}

Les navigateurs les plus populaires (tels que Safari, Chrome, FireFox et Edge) prennent tous en charge les notifications push web dans leurs versions récentes. Pour demander l'autorisation de notification push sur iOS ou iPadOS, votre site web doit être ajouté à l'écran d'accueil de l'utilisateur en sélectionnant **Partager** > **Ajouter à l'écran d'accueil**. [Ajouter à l'écran d'accueil](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permet aux utilisateurs de mettre votre site web en favori, en ajoutant votre icône à leur écran d'accueil.

![Un iPhone affichant les options pour mettre un site web en favori et l'enregistrer sur l'écran d'accueil]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Étape 5 : Afficher l'invite de notification push native {#push-prompt}
Une fois l'application ajoutée à votre écran d'accueil, vous pouvez demander l'autorisation de notification push lorsque l'utilisateur effectue une action (comme cliquer sur un bouton). Cela peut être fait à l'aide de la méthode [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission), ou avec un [message in-app d'amorce de notification push sans code]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

{% alert note %}
Après avoir accepté ou refusé l'invite, vous devez supprimer et réinstaller le site web sur votre écran d'accueil pour pouvoir afficher à nouveau l'invite.
{% endalert %}

![Une invite de notification push demandant d'autoriser ou de ne pas autoriser les notifications]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Par exemple :

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## Étapes suivantes {#next-steps}

Ensuite, envoyez-vous un [message de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) pour valider l'intégration. Une fois votre intégration terminée, vous pouvez utiliser nos [messages d'amorce de notification push sans code]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) pour optimiser vos taux d'abonnement aux notifications push.