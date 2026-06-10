---
nav_title: Fontes de conhecimento
article_title: Fontes de conhecimento
permalink: "/knowledge_sources/"
description: "Este artigo de referência aborda como criar e gerenciar fontes de conhecimento para seus agentes BrazeAI."
page_type: reference
---

# Fontes de conhecimento {#knowledge-sources}

> As fontes de conhecimento ajudam seus agentes de IA a interpretar dados do catálogo e recuperar as informações certas para atingir seus objetivos.

{% alert important %}
As fontes de conhecimento para o Console do agente estão atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se tiver interesse em participar deste acesso antecipado.
{% endalert %}

## Como funciona {#how-it-works}

As fontes de conhecimento são um tipo de contexto de agente. Um agente de IA pode consultar uma fonte de conhecimento para recuperar dados do catálogo com mais precisão do que se o catálogo fosse referenciado diretamente nas instruções do agente.

Digamos que você esteja criando um agente para recomendar restaurantes em Nova York com base na culinária favorita de um usuário, que é um atributo personalizado. Esse agente faz referência à fonte de conhecimento do catálogo "nyc_restaurants". Ao criar essa fonte de conhecimento, você inclui apenas os campos de que o agente precisa — como nome do restaurante, localização e tipo de culinária — e exclui outras colunas do catálogo que não contribuem para as recomendações.

As instruções do agente descrevem claramente seu papel e suas restrições:

{% raw %}
```
You are a restaurant recommendation agent. Use your knowledge to help find restaurants for the user. Only include filters in your knowledge source query. Don't ask any followup questions. The user's favorite cuisine is {{custom_attribute.${favorite_cuisine}}}
```
{% endraw %}

Se a culinária favorita de um usuário for pizza, o agente pode retornar a seguinte resposta com base na fonte de conhecimento:

```
Here are some pizza recommendations for you:
- Dale's Pizza (Greenwich Village, Manhattan): Dale's Pizza invites you to savor the taste of authentic New York. Nestled in the heart of Manhattan, this iconic pizzeria offers a warm and inviting atmosphere perfect for any occasion.
- Pizza Palace (Carroll Gardens, Brooklyn): Pizza Palace is a highly-rated culinary gem renowned for its exquisite pizza. This inviting spot offers a warm and modern dining experience.
```

## Criar uma fonte de conhecimento {#create-a-knowledge-source}

Para criar uma fonte de conhecimento:

1. Acesse **Console do agente** > **Fontes de conhecimento**.
2. Selecione **Adicionar fonte de conhecimento**. No menu suspenso, selecione **Catálogo**.
3. Selecione o catálogo no menu suspenso.
4. Revise os campos do catálogo e desmarque os que não se aplicam ao caso de uso do seu agente. Recomendamos excluir campos do catálogo que não sejam úteis para recuperação ou geração — limite a fonte de conhecimento apenas aos campos de que o agente precisa.
5. (opcional) Adicione uma descrição para descrever o que a fonte de conhecimento contém.
6. Selecione **Adicionar fonte de conhecimento**.

Incluir todos os campos do catálogo pode adicionar contexto desnecessário e reduzir a qualidade da saída. Desmarcar campos que não são relevantes para o seu caso de uso ajuda o agente a se concentrar nos dados que realmente importam.

![Uma fonte de conhecimento "nyc_restaurants" que faz referência ao catálogo "nyc_restaurants".]({% image_buster /assets/unlisted_docs/img/knowledge_sources/knowledge_source_example.png %}){: style="max-width:80%;"}

Você também pode criar uma fonte de conhecimento enquanto constrói um agente, acessando a seção **Instruções** do seu agente. Em seguida, selecione **Adicionar conhecimento** > **Criar fonte de conhecimento**.

## Usar uma fonte de conhecimento no seu agente de IA {#use-a-knowledge-source-in-your-ai-agent}

Você pode gerenciar fontes de conhecimento na seção **Fontes de conhecimento**. Aqui, é possível ver detalhes como quais fontes de conhecimento estão ativas e quando foram sincronizadas pela última vez. O nome da fonte de conhecimento corresponde ao nome do catálogo usado como origem.

Para usar uma fonte de conhecimento no seu agente de IA:

1. Acesse a seção **Instruções** do seu agente.
2. Em seguida, selecione **+ Contexto do agente** > **Adicionar conhecimento**.
3. No menu suspenso, selecione a fonte de conhecimento.

Agora, seu agente pode consultar a fonte de conhecimento e recuperar os dados relevantes do catálogo.

## Perguntas frequentes {#frequently-asked-questions}

### Como as fontes de conhecimento funcionam? {#how-do-knowledge-sources-work}

Converter um catálogo em uma fonte de conhecimento ajuda os agentes da Braze a entender o verdadeiro significado por trás das palavras e frases no catálogo, para que os agentes possam encontrar dados relevantes de forma mais eficaz e gerar melhores resultados.

### Quando devo criar uma fonte de conhecimento? {#when-should-i-create-a-knowledge-source}

Crie uma fonte de conhecimento quando quiser configurar um agente personalizado (agente de Canvas ou agente de catálogo) que possa usar um catálogo como contexto. Usar fontes de conhecimento é uma forma melhor de vincular um catálogo como contexto em comparação com o método existente.

### Se um agente recebeu uma fonte de conhecimento como contexto, também preciso atribuir o catálogo original como contexto? {#if-an-agent-has-been-given-a-knowledge-source-as-context-do-i-also-need-to-assign-the-original-catalog-as-context}

Não. A fonte de conhecimento substitui o catálogo como contexto do agente — você não precisa vincular ambos. Ao criar a fonte de conhecimento, inclua apenas os campos do catálogo de que o agente precisa.

### Como devo avaliar a eficácia de uma fonte de conhecimento? {#how-should-i-evaluate-the-efficacy-of-knowledge-source}

Duplique qualquer agente existente que faça referência a um catálogo comum e altere-o para referenciar a fonte de conhecimento equivalente. Execute algumas invocações de teste no Console do agente para garantir a precisão e, em seguida, considere substituir o agente existente onde ele está implantado ou fazer testes A/B entre o agente antigo e o novo (usando a etapa de jornada experimental) para entender o impacto no desempenho.