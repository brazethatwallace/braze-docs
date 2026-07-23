- **Gravação de tela:** Uma gravação das etapas que você seguiu antes de ver o erro, incluindo quaisquer transições de página.
- **Carimbo de data/hora e fuso horário:** O horário exato em que o erro ocorreu e seu fuso horário.
- **Navegador e versão:** O navegador que você está usando (por exemplo, Chrome 120, Safari 17) e se você tentou reproduzir o erro em um navegador diferente.
{% if include.context == 'canvas' -%}
- **Etapas para reproduzir:** Uma descrição clara das ações que disparam o erro, incluindo quaisquer etapas do Canvas ou configurações específicas envolvidas.
{% elsif include.context == 'campaign' -%}
- **Etapas para reproduzir:** Uma descrição clara das ações que disparam o erro, incluindo quaisquer configurações específicas de Campaign ou Canvas envolvidas.
{% endif -%}
- **Logs de rede (opcional):** Abra as ferramentas de desenvolvedor do seu navegador (guia **Network**), reproduza o erro e exporte o log de rede como um arquivo de log HTTP Archive (HAR). Isso ajuda a equipe de suporte a identificar qual chamada de API está expirando.