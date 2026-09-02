<ul>
<li><code>dispatch_id</code> é um ID para um envio de mensagem específico, como um envio de campanha. Todos os eventos de push que se originam do mesmo envio incluem o mesmo <code>dispatch_id</code>. Use <code>dispatch_id</code> para agrupar eventos que pertencem ao mesmo envio, permitindo que você agrupe e correlacione o ciclo de vida da mensagem push para esse envio (como Envio, Bounce e Abertura).</li>
<li><code>state_change_source</code> retorna uma string com o nome completo da fonte. Por exemplo, a fonte de importação de CSV retornará a string <code>CSV import</code>. As fontes disponíveis estão listadas a seguir:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Fonte</th><th>Descrição</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>Endpoints de SDK</td></tr>
<tr><td>Dashboard</td><td>Quando o estado da inscrição de um usuário é atualizado na página de perfil de usuário no dashboard</td></tr>
<tr><td>Página de inscrição</td><td>Quando um usuário cancela a inscrição por meio de um link de e-mail que não seja a Central de Preferências</td></tr>
<tr><td>REST API</td><td>Endpoints da REST API</td></tr>
<tr><td>Importação de CSV</td><td>Importação de usuários via CSV</td></tr>
<tr><td>Central de Preferências</td><td>Quando um usuário é atualizado a partir da Central de Preferências</td></tr>
<tr><td>Mensagem recebida</td><td>Quando um usuário é atualizado por mensagens recebidas de usuários finais por meio de canais como SMS</td></tr>
<tr><td>Migração</td><td>Quando um usuário é atualizado por migrações internas ou scripts de manutenção</td></tr>
<tr><td>Mesclagem de usuários</td><td>Quando um usuário é atualizado pelo processo de mesclagem de usuários</td></tr>
<tr><td>Etapa de atualização do usuário do Canvas</td><td>Quando um usuário é atualizado pela etapa de atualização do usuário do Canvas</td></tr>
</tbody>
</table>