Antes de criar modelos de WhatsApp, você deve concluir a [configuração do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) e ter:
- Uma conta ativa do WhatsApp Business (WABA) conectada à Braze
- Grupos de inscrições apropriados configurados na sua WABA
- Ativos de mídia (imagens ou vídeos) prontos para fazer upload
- Permissões da Braze para usuários não administradores
    - Para que os usuários criem novos modelos no Template Builder:
        - "View WhatsApp Message Templates"
        - "Edit WhatsApp Message Templates"
    - Para que os usuários redijam campaigns ou Canvas com modelos de carrossel:
        - "View WhatsApp Message Templates"
- Conhecimento de modelos Liquid (opcional, para conteúdo dinâmico)

{% alert important %}
Todos os números de telefone e grupos de inscrições dentro da mesma conta do WhatsApp Business (WABA) compartilham modelos. Se você tiver múltiplos grupos de inscrições em uma WABA, todos podem acessar os mesmos modelos de carrossel. No entanto, os modelos não são compartilhados entre WABAs diferentes.
{% endalert %}