<ul>
<li><code>dispatch_id</code> es un ID para un envío de mensaje específico, como el envío de una campaña. Todos los eventos push que se originan en el mismo envío incluyen el mismo <code>dispatch_id</code>. Usa <code>dispatch_id</code> para agrupar eventos que pertenecen al mismo envío, lo que te permite agrupar y correlacionar el ciclo de vida de los mensajes push para ese envío (como envío, rebote y apertura).</li>
<li><code>state_change_source</code> devuelve una cadena con el nombre completo de la fuente. Por ejemplo, la fuente de importación de usuarios en CSV devolverá la cadena <code>CSV import</code>. Las fuentes disponibles se enumeran a continuación:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Fuente</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>Endpoints del SDK</td></tr>
<tr><td>Dashboard</td><td>Cuando el estado de suscripción de un usuario se actualiza desde la página de perfil de usuario en el panel</td></tr>
<tr><td>Página de suscripción</td><td>Cuando un usuario cancela su suscripción a través de un enlace de correo electrónico que no es el centro de preferencias</td></tr>
<tr><td>REST API</td><td>Endpoints de la REST API</td></tr>
<tr><td>Importación CSV</td><td>Importación de usuarios en CSV</td></tr>
<tr><td>Centro de preferencias</td><td>Cuando un usuario se actualiza desde el centro de preferencias</td></tr>
<tr><td>Mensaje entrante</td><td>Cuando un usuario se actualiza mediante mensajes entrantes de usuarios finales a través de canales como SMS</td></tr>
<tr><td>Migración</td><td>Cuando un usuario se actualiza mediante migraciones internas o scripts de mantenimiento</td></tr>
<tr><td>Fusión de usuarios</td><td>Cuando un usuario se actualiza mediante el proceso de fusión de usuarios</td></tr>
<tr><td>Paso de actualización de usuario de Canvas</td><td>Cuando un usuario se actualiza mediante el paso de actualización de usuario de Canvas</td></tr>
</tbody>
</table>