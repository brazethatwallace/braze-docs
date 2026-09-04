Se você encontrar duas entradas de dados personalizados com o mesmo nome visível, uma delas pode conter um espaço invisível no início ou no final.

Para solucionar e corrigir isso:

1. Acesse **Data Settings** > **Custom Attributes** ou **Custom Events** e localize as duas entradas que parecem ter o mesmo nome.
2. Confirme se um dos nomes contém espaços ocultos:
    1. Clique com o botão direito em cada nome e selecione **Inspecionar**.
    2. Verifique o valor do texto HTML nas ferramentas de desenvolvedor do navegador.
    3. Compare os valores (por exemplo, `email` versus ` email`).
    4. Se necessário, consulte [Inspecionar e editar páginas e estilos com o Chrome DevTools](https://developer.chrome.com/docs/devtools/inspect-mode).
3. Decida qual nome deve permanecer como sua chave canônica e padronize a grafia e o uso de maiúsculas/minúsculas exatos.
4. Se uma entrada incluir espaços no início ou no final e tiver sido criada diretamente no dashboard, pare de usar essa entrada e migre para a chave canônica:
    - Atualize quaisquer fluxos de trabalho do dashboard, importações de CSV e runbooks internos para usar a chave canônica.
    - [Bloqueie dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data) da entrada incorreta quando estiver pronto para descontinuá-la.
5. Verifique seus caminhos de ingestão:
    - As cargas úteis de API e SDK removem automaticamente espaços no início e no final.
    - Nomes criados pelo dashboard não são ajustados automaticamente, então a entrada manual e a governança são necessárias.