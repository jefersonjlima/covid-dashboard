### Montando um Pull Request

**1. _Fork_ este respositório**

Tem um botão para isso na interface do Gitlab

**2. Clone o fork do seu repositório**

```console
$ git clone https://gitlab.com/<YOUR-GITLAB-USERNAME>/covid-dashboard.git
```

**3. Crie uma nova branch**

```console
$ git checkout -b <YOUR-GITLAB-USERNAME>/suas-mudanças
```
Note que o prefixo das branches são os nomes de usuário utilizados no Gitlab, isso nos ajuda a acompanhar quais mudanças estão sendo feitas por quem.

**4. Faça o que você faz de melhor**

Escreva códigos significativos para elevar o nível do projeto!

**5. Commite suas mudanças**

```console
$ git commit -am 'My pretty cool contribution'
```

Note que as mensagens dos commits são em inglês.

**6. Faça o push das suas mudanças para o seu fork**

```consle
$ git push origin <YOUR-GITLAB-USERNAME>/suas-mudanças
```

**7. Crie um novo _Merge Request_**

A partir do seu fork normalmente tem um botão para abrir o merge request.

**8. Adicione uma boa decrição ao seu _Merge Request_**

Conta o que você fez no seu merge request, isso nos ajuda a entender e testar o seu código. Se você está criando um merge request relacionado a uma issue, explicite qual. 