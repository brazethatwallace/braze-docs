{% if include.page == "testing" %}Ao [redigir sua mensagem de Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), selecione{% elsif include.page == "campaigns" %}Selecione{% endif %} **Pré-visualização** para visualizar seu Banner ou enviar uma mensagem de teste.

![Guia de pré-visualização do criador de Banner.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Lembre-se de que a pré-visualização pode não ser idêntica à renderização final no dispositivo do usuário devido a diferenças de hardware.

Para enviar uma mensagem de teste, adicione um grupo de teste de conteúdo ou um ou mais usuários individuais como **Destinatários de Teste** e selecione **Enviar Teste**. Você poderá visualizar sua mensagem de teste no dispositivo por até 5 minutos. Em seguida, selecione **Copiar link de pré-visualização** para gerar e copiar um link compartilhável que mostra como o banner ficará para um usuário aleatório. O link ficará válido por sete dias antes de precisar ser regenerado.

![Guia de pré-visualização do criador de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

Ao revisar seu Banner de teste, verifique o seguinte:

- A sua Campaign de Banner está atribuída a um posicionamento?
- As imagens e mídias aparecem e funcionam como esperado nos tipos de dispositivos e tamanhos de tela segmentados?
- Os links e botões direcionam o usuário para onde deveriam ir?
- O Liquid funciona conforme o esperado? Você definiu um valor de atributo padrão para o caso de o Liquid não retornar nenhuma informação?
- O texto está claro, conciso e correto?

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/).