Na Braze, geofences e monitoramento de localização servem a propósitos diferentes:

| | Monitoramento de localização | Geofences |
|---|---|---|
| Propósito | Segmentar usuários com base em onde estiveram | Disparar envio de mensagens quando usuários entram ou saem de uma área |
| Uso típico | `Most Recent Location` e filtros relacionados | Campaigns em tempo real ao entrar ou sair de geofences |
| Quando o local é avaliado | Atualizado quando o app está aberto (início da sessão); reflete o último local conhecido do usuário | Monitorado pelo sistema operacional quando as permissões de localização permitem, inclusive quando o app está em segundo plano ou fechado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Location tracking compared to geofences" }

- **Monitoramento de localização:** Coleta e armazena o local mais recente de cada usuário no perfil. Você usa esses dados para segmentação retroativa — por exemplo, o filtro `Most Recent Location` segmenta usuários com base em onde eles abriram o app pela última vez, não necessariamente onde estão em tempo real.
- **Geofences:** Define limites virtuais em torno de uma latitude, longitude e raio. Quando um usuário entra ou sai de um limite, a Braze pode disparar ações como o envio de uma Campaign. Geofences exigem configuração adicional do SDK além do monitoramento básico de localização.

Ambos os recursos exigem que os usuários concedam permissões de localização. Se um usuário desativar o monitoramento de localização, os dados de localização armazenados anteriormente não são removidos automaticamente do perfil, mas novos dados de localização não são coletados.