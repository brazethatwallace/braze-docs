---
nav_title: Transcend
article_title: Transcend
description: "Cet article de référence présente le partenariat entre Braze et Transcend, une plateforme d'infrastructure de confidentialité des données, qui aide les utilisateurs de Braze à automatiser le traitement des requêtes des personnes concernées."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend est une société d'infrastructure de confidentialité des données qui permet aux entreprises de donner à leurs utilisateurs le contrôle de leurs données, en répondant automatiquement aux requêtes des personnes concernées au sein des entreprises à travers tous leurs systèmes de données et leurs fournisseurs.

_Cette intégration est maintenue par Transcend._

## À propos de l'intégration {#about-the-integration}

Le partenariat entre Braze et Transcend aide les utilisateurs à automatiser les requêtes de confidentialité en orchestrant les données à travers des dizaines de systèmes de données, aidant ainsi les équipes à se conformer à des réglementations telles que le RGPD et le CCPA. Transcend met à la disposition des utilisateurs finaux un panneau de contrôle, ou centre de confidentialité, hébergé sur `privacy.\<company\>.com`, où les utilisateurs peuvent gérer leurs préférences en matière de confidentialité, exporter leurs données ou les supprimer.

## Conditions préalables {#prerequisites}

| Exigences | Description |
|---|---|
| Compte Transcend | Un compte [Transcend](https://app.transcend.io/) avec des privilèges d'administrateur est nécessaire pour profiter de ce partenariat. |
| Clé API de Braze | Une clé API REST de Braze avec les autorisations `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` et `email.blacklist`.<br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

Transcend vous permet d'accéder de manière programmatique aux données, de les effacer et d'exclure les utilisateurs des communications dans la plateforme Braze, conformément aux réglementations sur la confidentialité des données.

### Étape 1 : Mettre en place l'intégration de Braze {#step-1-set-up-the-braze-integration}
Pour commencer, connectez-vous à [Transcend](https://app.transcend.io/login).
1. Accédez à **Data Map > Add Data Silo > Braze** et sélectionnez le bouton **Connect**.<br><br>
2. Lorsque votre compte est approvisionné, vous vous connectez à l'une des URL correspondantes : `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Utilisez le [tableau]({{site.baseurl}}/api/basics/#endpoints) suivant pour déterminer quel sous-domaine vous devez inclure en fonction de l'URL de votre tableau de bord.<br><br>
3. Une fois connecté, accédez à l'onglet **Privacy Center** de Transcend. Ici, vous devrez mapper les données de Braze à vos pratiques en matière de données. Pour ce faire, créez une nouvelle catégorie et une nouvelle collecte de données avec la convention de nommage appropriée (par exemple, « Listes de diffusion ou profil utilisateur »). Lorsque vous avez terminé, sélectionnez **Publish**.<br><br>
4. Retournez à votre Data Map et sélectionnez le silo de données Braze. Développez **Manage Datapoints** et sélectionnez dans le menu déroulant l'étiquette de collection (catégorie) que vous avez créée à l'étape précédente. Vous pouvez également choisir quelles actions sur les données (par exemple, l'accès ou l'effacement) sont activées et pour quels points de données.<br><br>
5. Ensuite, toujours dans le silo de données Braze, développez **Manage Identifiers**. Cochez les cases correspondant aux identifiants que vous souhaitez activer. Par exemple, si vous souhaitez que Transcend effectue une recherche d'utilisateurs par adresse e-mail, cochez la case pour activer l'identifiant de l'adresse e-mail.

{% alert note %}
Si les identifiants ne sont pas activés correctement, Transcend peut ne pas traiter les requêtes de certains utilisateurs.
{% endalert %}

### Étape 2 : Tester les requêtes {#step-2-test-requests}
Transcend recommande de tester les requêtes sur l'ensemble de votre Data Map avant de commencer à traiter les requêtes des utilisateurs finaux.
1. Accédez au **Privacy Center** dans Transcend et sélectionnez **View your Privacy Center**.<br><br>
2. Dans votre **Privacy Center**, sélectionnez **Take Control**, puis **Download my data**. Saisissez votre adresse e-mail ou connectez-vous pour vous authentifier avant de soumettre la requête.<br><br>
3. Consultez votre boîte de réception pour voir si vous avez reçu un message de Transcend. Il vous sera demandé de cliquer sur un lien de vérification pour valider la requête.<br><br>
4. Ensuite, de retour dans le tableau de bord **Admin**, accédez à l'onglet **Incoming Requests** et sélectionnez votre requête. Contactez Transcend à l'adresse [support@transcend.io](mailto:support@transcend.io) si la requête n'est pas visible.<br><br>
5. Après avoir cliqué sur votre requête, accédez à l'onglet **Data Silos** et sélectionnez **Braze**. Inspectez et confirmez les données renvoyées.<br><br>
6. Enfin, accédez à l'onglet **Report** et cliquez sur **Approve and Send**. Vous devriez recevoir le rapport à l'adresse e-mail que vous avez indiquée lors de la requête.

## Retirer l'intégration de Braze {#remove-the-braze-integration}
Pour supprimer le silo de données Braze de votre Data Map Transcend :
1. Accédez à votre **Data Map** et cliquez sur **Braze**.<br><br>
2. En bas de l'écran, développez **Remove Braze** et cliquez sur **Remove Silo**. Vous serez invité à confirmer que vous souhaitez supprimer le silo. Cliquez sur **Ok**.<br><br>
3. Confirmez la suppression du silo en retournant à votre Data Map.