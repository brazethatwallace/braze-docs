<ul>
<li><code>dispatch_id</code> est un ID correspondant à un envoi de message spécifique, tel qu'un envoi de Campaign. Tous les événements push provenant du même envoi incluent le même <code>dispatch_id</code>. Utilisez <code>dispatch_id</code> pour regrouper les événements appartenant au même envoi, ce qui vous permet de regrouper et de corréler le cycle de vie du message push pour cet envoi (comme l'envoi, le rebond et l'ouverture).</li>
<li><code>state_change_source</code> renvoie une chaîne de caractères contenant le nom complet de la source. Par exemple, la source d'importation CSV renverra la chaîne de caractères <code>CSV import</code>. Les sources disponibles sont énumérées ci-dessous :</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Source</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>Endpoints SDK</td></tr>
<tr><td>Tableau de bord</td><td>Lorsque l'état d'abonnement d'un utilisateur est mis à jour depuis la page de profil utilisateur dans le tableau de bord</td></tr>
<tr><td>Page d'abonnement</td><td>Lorsqu'un utilisateur se désabonne via un lien d'e-mail qui n'est pas le centre de préférences</td></tr>
<tr><td>REST API</td><td>Endpoints REST API</td></tr>
<tr><td>Importation CSV</td><td>Importation d'utilisateurs par CSV</td></tr>
<tr><td>Centre de préférences</td><td>Lorsqu'un utilisateur est mis à jour depuis le centre de préférences</td></tr>
<tr><td>Message entrant</td><td>Lorsqu'un utilisateur est mis à jour par des messages entrants provenant d'utilisateurs finaux via des canaux tels que les SMS</td></tr>
<tr><td>Migration</td><td>Lorsqu'un utilisateur est mis à jour par des migrations internes ou des scripts de maintenance</td></tr>
<tr><td>Fusion d'utilisateurs</td><td>Lorsqu'un utilisateur est mis à jour par le processus de fusion d'utilisateurs</td></tr>
<tr><td>Étape de mise à jour de l'utilisateur Canvas</td><td>Lorsqu'un utilisateur est mis à jour par l'étape de mise à jour de l'utilisateur Canvas</td></tr>
</tbody>
</table>