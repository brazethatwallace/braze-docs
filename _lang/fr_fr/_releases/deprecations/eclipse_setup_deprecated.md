---
nav_title: Configuration initiale du SDK avec Eclipse
page_order: 1
page_type: update
noindex: true
description: "Cet article archivé décrit comment effectuer une configuration initiale du SDK avec Eclipse. Braze ne prend plus en charge l'IDE Eclipse."
---

# Configuration initiale du SDK avec Eclipse {#initial-sdk-setup-with-eclipse}

{% alert update %}
Braze a supprimé la prise en charge de l'IDE Eclipse en raison de la [temporisation par Google de la prise en charge du plugin Eclipse Android Developer Tools](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Si vous avez besoin d'aide pour votre intégration Eclipse avant la migration, [envoyez un e-mail au service d'assistance]({{site.baseurl}}/support_contact/) pour obtenir de l'aide.
{% endalert %}

## Étape 1 {#step-1}
Dans votre ligne de commande, clonez le [dépôt GitHub de Braze Android](https://github.com/braze-inc/braze-android-sdk).

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Étape 2 {#step-2}
Importez le projet Braze dans votre espace de travail local.

Dans Eclipse :

  - Accédez à **File** > **Import**.

    ![Importation de fichiers]({{site.baseurl}}/assets/img_archive/file_import.png)
  - Sélectionnez **Android** > **Existing Android Code into Workspace**.

    ![Importation Android]({{site.baseurl}}/assets/img_archive/android_import.png)
  - Cliquez sur **Browse**.

    ![Parcourir]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Cochez le dossier du projet Braze UI ainsi que **copy project into workspace**, puis cliquez sur **Finish**.

    ![Sélection du projet Android UI]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## Étape 3 {#step-3}
Référencez Braze dans votre propre projet.
Dans Eclipse :

  - Cliquez avec le bouton droit de la souris sur votre projet et sélectionnez **Properties**.

    ![Cliquez sur Properties]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - Sous **Android**, cliquez sur **Add...** dans la section Library et ajoutez android-sdk-ui à votre application en tant que bibliothèque.

    ![Ajout de Braze]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## Étape 4 {#step-4}
Résolvez les erreurs de dépendance et corrigez la cible du build.

À ce stade, vous pouvez voir des erreurs apparaître avec le code de Braze, car ses dépendances ne sont pas renseignées et la cible du build est peut-être incorrecte :

   - Cliquez avec le bouton droit de la souris sur le projet Braze UI et sélectionnez **Properties** > **Android** pour vous assurer que la cible de build est définie sur la version actuelle des outils de build de Braze.

      ![Cible de build]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Cliquez avec le bouton droit de la souris sur le projet Braze UI et sélectionnez **Properties** > **Java Build Path** > **Add JARs…**, puis ajoutez `android-support-v4.jar` en tant que bibliothèque à partir de l'application principale.

      ![Assistance]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## Étape 5 {#step-5}

Ajoutez les éléments restants.

  - Pour le SDK version 1.10.0 ou supérieure, vous devrez ajouter
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  à votre AndroidManifest.xml, car Eclipse ne prend pas en charge la fusion des manifestes.

  - Pour le SDK version 1.7.0 ou supérieure, vous devrez copier `assets/fontawesome-webfont.ttf` de notre projet de bibliothèque vers votre application. Eclipse n'inclut pas automatiquement le dossier des ressources à partir des bibliothèques.