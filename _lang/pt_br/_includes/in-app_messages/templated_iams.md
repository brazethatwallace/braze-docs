As mensagens no app são entregues como mensagens no app modeladas quando a opção **Reavaliar a elegibilidade da campanha antes de exibir** está selecionada ou se alguma das seguintes Liquid tags existir na mensagem:

- `canvas_entry_properties`
- `connected_content`
- Variáveis de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Isso significa que, no início da sessão, o dispositivo receberá o gatilho dessa mensagem no app em vez da mensagem completa. Quando o usuário acionar a mensagem no app, o dispositivo fará uma solicitação de rede para buscar a mensagem real.

{% alert note %}
A mensagem não será entregue se o dispositivo não tiver acesso à internet. A mensagem também pode não ser entregue se a lógica do Liquid demorar muito para ser resolvida.
{% endalert %}