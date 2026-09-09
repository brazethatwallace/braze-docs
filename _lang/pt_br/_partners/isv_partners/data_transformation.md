---
nav_title: Transformação de dados
hidden: true
---

# Transformação de Dados da Braze {#braze-data-transformation}

> A [Transformação de Dados]({{site.baseurl}}/user_guide/data/unification/data_transformation) da Braze pode receber um webhook de uma plataforma parceira e permitir que um cliente defina um mapeamento para converter a carga útil desse webhook nos dados de usuários desejados, como atributos, eventos ou compras nos perfis de usuário da Braze.

## Como seria uma integração baseada em Transformação de Dados {#what-a-data-transformation-based-integration-would-look-like}

Uma integração com parceiros baseada no recurso de Transformação de Dados pode ser um modelo de código de transformação compartilhado com clientes por meio de documentação pública.

Para clientes em comum, o processo seria mais ou menos assim:

1. Eles acessam sua plataforma e configuram webhooks.
2. Eles trabalham com a equipe da Braze para obter acesso à Transformação de Dados da Braze e criar uma nova transformação no dashboard da Braze.
3. A URL gerada pela transformação é copiada.
4. De volta à Braze, eles enviam um webhook de teste para a URL de transformação copiada.
5. Na Braze, eles copiam e colam o modelo de código de transformação.
6. Eles ativam a transformação.
7. Quando ativada, eles podem verificar por meio da ferramenta de pesquisa de usuário da Braze que o perfil de usuário foi atualizado com base no webhook e editar o código de transformação conforme desejado.

{% alert tip %}
É recomendado criar uma transformação por tipo de webhook enviado à Braze ao desenvolver exemplos de código de transformação.
{% endalert %}