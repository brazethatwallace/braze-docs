---
nav_title: Criar códigos
article_title: Criar códigos de promoção
page_order: 0.1
description: "Saiba como criar códigos de promoção nas suas campanhas e Canvas."
---

# Criar códigos de promoção {#create-promotion-codes}

> Saiba como criar códigos de promoção nas suas campanhas e Canvas.

## Criando uma lista de códigos de promoção {#create}

### Etapa 1: Criar uma nova lista {#step-1-create-a-new-list}

No dashboard, acesse **Configurações de dados** > **Códigos de promoção** e selecione **Criar lista de códigos de promoção**.

![Botão para criar um código de promoção.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Etapa 2: Inserir as informações {#step-2-enter-the-details}

1. Dê um nome à sua lista de códigos de promoção e adicione uma descrição opcional.
2. Em seguida, crie um snippet de código para o código de promoção.

Veja alguns detalhes a considerar ao criar um snippet de código:

- Não é possível editar um snippet de código depois de salvar.
- Os snippets diferenciam maiúsculas de minúsculas. Por exemplo, o sistema reconhece "Birthday_promo" e "birthday_promo" como dois snippets diferentes.
- Use o nome do snippet em Liquid para referenciar esse conjunto de códigos de promoção.
- Verifique se o snippet de código não está sendo usado em outra lista.

![Uma lista de códigos de promoção chamada "SpringSale2025" com o snippet de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Etapa 3: Escolher as opções do código de promoção {#step-3-choose-promotion-code-options}

Cada lista de códigos de promoção tem uma data e hora de expiração correspondentes, definidas no momento da criação. O prazo máximo de expiração é de seis meses a partir do dia em que você criar ou editar a lista.

Dentro desse período, você pode alterar e atualizar a data de expiração repetidamente. Essa data de expiração se aplica a todos os códigos adicionados a essa lista. Após a expiração, os códigos são excluídos do sistema da Braze, e qualquer mensagem que chame o snippet de código dessa lista não será enviada.

![Configurações de expiração da lista indicando que todos os códigos restantes expirarão em 30 de abril de 2025 às 0h.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Você também tem a opção de configurar alertas de limite opcionais e personalizados. Se configurados, esses alertas enviam um e-mail ao destinatário designado quando a lista estiver com poucos códigos de promoção disponíveis ou quando a lista de códigos de promoção estiver próxima da expiração. O destinatário é notificado uma vez por dia.

![Um exemplo de alerta de limite para notificar "marketing@abc.com" quando a lista de códigos de promoção expirar em 5 dias.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Etapa 4: Fazer upload dos códigos de promoção {#step-4-upload-promotion-codes}

A Braze não gerencia a criação ou o resgate de códigos, o que significa que você deve gerar seus códigos de promoção em um arquivo CSV e fazer upload deles na Braze.

Verifique se o seu arquivo CSV segue estas diretrizes:

- Inclui uma coluna para códigos de promoção.
- Tem um código de promoção por linha.

Você pode usar nossa integração nativa com o [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify) ou o [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone) para criar e exportar códigos de promoção.

{% alert important %}
O tamanho máximo do arquivo é 100&nbsp;MB e o tamanho máximo da lista é de 20 milhões de códigos não utilizados. Se você fez upload do arquivo errado, faça upload de um novo para substituir o anterior.
{% endalert %}

1. Após a conclusão do upload, selecione **Salvar lista** para salvar todas as informações e códigos que você acabou de inserir.

![Arquivo CSV chamado "springsale" que foi enviado com sucesso.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2. Após selecionar salvar, uma nova linha aparece no **Histórico de importação**.
3. Para atualizar a tabela e verificar se a importação foi concluída, selecione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** no topo da tabela.

![Códigos de promoção em processo de upload.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Arquivos maiores levam alguns minutos para importar. Enquanto espera, você pode sair da página e trabalhar em outra coisa enquanto a importação está em andamento. Quando a importação terminar, o status muda para **Concluir** na tabela.
{% endalert %}

## Atualizando uma lista de códigos de promoção {#updating-a-promotion-code-list}

Para atualizar uma lista, selecione uma das suas listas existentes. Você pode alterar o nome, a descrição, a expiração da lista e os alertas de limite. Também é possível adicionar mais códigos à lista fazendo upload de novos arquivos e selecionando **Atualizar lista**. Todos os códigos na lista têm a mesma expiração, independentemente da data de importação.

{% alert important %}
Códigos de promoção não podem ser excluídos.
{% endalert %}

### Corrigindo uma lista de códigos de promoção incorreta {#modifying-an-incorrect-promotion-code-list}

Se você fez upload de um arquivo CSV com os códigos de promoção incorretos e selecionou **Salvar lista**, é possível resolver isso por um dos seguintes métodos:

- Descontinuar a lista inteira: pare de usar a lista de códigos de promoção atual em quaisquer Campaigns, Canvas ou modelos. Em seguida, faça upload do arquivo CSV com os códigos corretos e use-os no seu envio de mensagens.
- Usar os códigos incorretos: crie uma Campaign que envie códigos de promoção da lista incorreta para um placeholder até que todos os códigos incorretos sejam usados. Em seguida, faça upload dos códigos de promoção corretos na mesma lista.