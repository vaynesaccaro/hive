---
description: Encerra a sessão de forma git-cêntrica — consolida tudo no main local e dá push no origin
---

# /encerrarsessão

Encerra a sessão de trabalho garantindo que **nada se perca**: todo o trabalho é
commitado localmente no `main` e enviado (push) para o `origin` do usuário.

Trabalho do Vayne é **git-cêntrico**: a fonte da verdade é o `main` no remoto.

## Procedimento (execute via Bash, nesta ordem)

1. **Identificar estado**
   - `git rev-parse --abbrev-ref HEAD` (branch atual)
   - `git status --porcelain` (mudanças pendentes)
   - `git branch --list "session/*"` (branches de sessão órfãs)

2. **Commitar trabalho pendente**
   - Se houver mudanças não commitadas na branch atual, commitá-las com mensagem
     descritiva do que foi feito na sessão (NUNCA `git add` de arquivos com segredos
     — `.env`, chaves, tokens; pule-os e avise).

3. **Consolidar no `main` (contornando o bug dos hooks de sessão — issue #1)**
   - O comando DEVE começar com `git checkout main &&` para garantir que o merge
     caia no `main` mesmo que o pretooluse hook crie uma nova `session/*`.
   - Para cada branch `session/*` com commits à frente do main, mergear no main:
     `git checkout main && git merge <branch> --no-ff -m "merge: <resumo da sessão>"`
   - Deletar as branches `session/*` já mergeadas: `git branch -D <branch> ...`
   - Deletar branches `session/*` vazias residuais (iguais ao main).

4. **Push para o origin**
   - `git push origin main`
   - Confirmar que o remoto é o do usuário: `origin` = github.com/vaynesaccaro/hive.

5. **Verificar e reportar**
   - `git log --oneline -1` no main, `git status`, `git branch --list "session/*"` (deve ser 0).
   - Confirmar com `git rev-parse main origin/main` que local e remoto estão iguais.
   - Reportar ✅ / ⚠️ / ❌ por etapa (commit, merge, push). Nunca declarar sucesso
     sem confirmar que o push subiu e local == remoto.

## Regras
- Segredos nunca vão pro git. Pule arquivos sensíveis e avise.
- Se um merge der conflito, NÃO deixe branch órfã silenciosamente — pare e reporte.
- Push é operação de saída: se falhar (auth, rede), reporte claramente, não finja sucesso.
