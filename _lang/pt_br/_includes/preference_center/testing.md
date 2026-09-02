## Testando Centrais de Preferências {#testing-preference-centers}

Os links da Central de Preferências são gerados para cada usuário no momento do envio e estão vinculados a um envio ativo de Campaign ou Canvas. Envios de teste e prévias do editor não suportam salvar alterações de inscrição. Esse é o comportamento esperado.

### O que você verá {#what-youll-see}

- **Envios de teste:** As Liquid tags da Central de Preferências podem não resolver para um link válido. Se a página carregar, o botão **Save Preferences** estará desativado e as alterações de inscrição não serão salvas.
- **Guia de prévia do editor de arrastar e soltar:** Você pode visualizar o layout e o estilo, mas não pode testar o salvamento de preferências a partir do editor.

### Como testar de ponta a ponta {#how-to-test-end-to-end}

Para verificar se os links e botões da Central de Preferências funcionam antes de um lançamento completo:

1. Crie uma Campaign de e-mail ou uma etapa de e-mail no Canvas que inclua sua Liquid tag da Central de Preferências.
2. Direcione apenas seus usuários teste ou um pequeno Segment or segmento interno.
3. Lance a mensagem e abra o e-mail a partir de uma caixa de entrada real (não use **Send Test**).
4. Selecione o link da Central de Preferências, atualize os grupos de inscrições e selecione **Save Preferences**.
5. Confirme as alterações no perfil do usuário no dashboard da Braze.

{% if include.section == "API or interface de programação do aplicativo (API)" %}
Como alternativa para Centrais de Preferências criadas via API or interface de programação do aplicativo (API), use o [endpoint Gerar URL da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) para obter uma URL funcional para um usuário específico fora de um envio de teste.
{% endif %}

Para outras limitações de envio de teste, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages#limitations).

### Prévia, envio de teste e envio ativo {#preview-test-send-and-live-send}

| Método | Prévia do layout | Salvar alterações de inscrição |
| --- | --- | --- |
| Guia **prévia** do editor de arrastar e soltar | Sim | Não |
| **Send Test** de Campaign ou Canvas | Parcial (o e-mail é entregue) | Não |
| Envio ativo para um usuário teste ou Segment or segmento | Sim | Sim |
| API or interface de programação do aplicativo (API) [Gerar URL da Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Sim | Sim |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prévia, envio de teste e envio ativo" }