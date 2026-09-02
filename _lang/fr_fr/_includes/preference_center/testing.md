## Tester les centres de préférences {#testing-preference-centers}

Les liens du centre de préférences sont générés pour chaque utilisateur au moment de l'envoi et sont liés à l'envoi d'une Campaign ou d'un Canvas en direct or en ligne/en production/instantané. Les envois de test et les prévisualisations de l'éditeur ne prennent pas en charge l'enregistrement des modifications d'abonnement. Il s'agit du comportement attendu.

### Ce que vous verrez {#what-youll-see}

- **Envois de test :** Les étiquettes Liquid du centre de préférences peuvent ne pas se résoudre en un lien valide. Si la page se charge, le bouton **Enregistrer les préférences** est désactivé et les modifications d'abonnement ne sont pas enregistrées.
- **Onglet Prévisualisation de l'éditeur par glisser-déposer :** Vous pouvez prévisualiser la mise en page et le style, mais vous ne pouvez pas tester l'enregistrement des préférences depuis l'éditeur.

### Comment tester de bout en bout {#how-to-test-end-to-end}

Pour vérifier que les liens et les boutons du centre de préférences fonctionnent avant un lancement complet :

1. Créez une Campaign ou une étape d'e-mail Canvas qui inclut votre étiquette Liquid du centre de préférences.
2. Ciblez uniquement vos utilisateurs test ou un petit segment interne.
3. Lancez le message et ouvrez l'e-mail depuis une vraie boîte de réception (pas **Envoyer le test**).
4. Sélectionnez le lien du centre de préférences, mettez à jour les groupes d'abonnement et sélectionnez **Enregistrer les préférences**.
5. Confirmez les modifications sur le profil de l'utilisateur dans le tableau de bord de Braze.

{% if include.section == "api" %}
Comme alternative pour les centres de préférences créés via l'API, utilisez l'[endpoint Générer l'URL du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) pour récupérer une URL fonctionnelle pour un utilisateur spécifique en dehors d'un envoi de test.
{% endif %}

Pour les autres limitations des envois de test, consultez la section [Envoyer des messages test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages#limitations).

### Prévisualisation, envoi de test et envoi en direct or en ligne/en production/instantané {#preview-test-send-and-live-send}

| Méthode | Prévisualisation de la mise en page | Enregistrement des modifications d'abonnement |
| --- | --- | --- |
| Onglet **Prévisualisation** de l'éditeur par glisser-déposer | Oui | Non |
| **Envoyer le test** de la Campaign ou du Canvas | Partiel (l'e-mail arrive) | Non |
| Envoi en direct or en ligne/en production/instantané à un utilisateur test ou un segment | Oui | Oui |
| API [Générer l'URL du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Oui | Oui |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prévisualisation, envoi de test et envoi en direct or en ligne/en production/instantané" }