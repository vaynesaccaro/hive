---
description: >
  Encerra a sessão de forma git-cêntrica: resume o que foi feito, registra um log curto
  da sessão, sincroniza comandos e faz o encerramento git (staging seguro + commit semântico
  + consolidação no main + push), tratando o bug dos hooks de sessão do HIVE.
  Ativar quando o usuário disser: "/encerrarsessão", "encerrar", "vamos encerrar",
  "fechar sessão", "fim de sessão", "finaliza", "para por aqui", "pode encerrar".
---

# /encerrarsessão — fim de sessão (git-cêntrico)

Automatiza o ritual de fim de sessão: em vez de lembrar de commitar, descrever o que fez e
anotar onde parou, uma frase faz tudo. Garante que **nada se perca** — todo o trabalho é
commitado no `main` e enviado (push) para o `origin`.

Trabalho do Vayne é **git-cêntrico**: a fonte da verdade é o `main` no remoto
(`origin` = github.com/vaynesaccaro/hive). Trabalho que não foi pro remoto não existe.

## Regras absolutas

1. **Nunca `git add -A`.** Use `git add -u` (só arquivos já rastreados) + adicione arquivos
   novos explicitamente (`git add caminho/arquivo`), conferindo um a um. `-A` arrasta lixo e segredo.
2. **Nunca commitar segredo.** Antes do commit, conferir que `.env`/chaves/tokens estão no
   `.gitignore` e fora do staged. Se aparecer segredo no diff, **PARAR** e avisar.
3. **Sempre fazer push ao final.** Push é operação de saída: se falhar (auth, rede), reporte
   claramente — não finja sucesso.
4. **Não inventar o que foi feito.** Resumo e log saem do que realmente mudou no diff/na conversa.
5. **Se um merge der conflito, NÃO deixe branch órfã silenciosamente** — pare e reporte.

## Fluxo (execute via Bash, nesta ordem)

### Passo 1 — Identificar estado e resumir
- `git rev-parse --abbrev-ref HEAD` · `git status --porcelain` · `git branch --list "session/*"`
- A partir do diff e da conversa, montar um resumo curto: **o que foi feito** (entregas
  concretas), **o que ficou pela metade**, **próximo passo** pra retomar.

### Passo 2 — Registrar o log da sessão
Criar/atualizar `docs/sessions/AAAA-MM-DD.md` (criar a pasta se não existir):

```markdown
# Sessão AAAA-MM-DD

## Feito
- ...

## Em andamento / pela metade
- ...

## Próximo passo
- ...
```

Se houver `STATE.md` da squad relevante com seção de progresso, atualizar L1/L2 também.

### Passo 3 — Sincronizar comandos
- `python _core/sync-commands.py` — espelha `skills/` e `squads/*/skills/` para
  `.claude/commands/` (mantém o menu `/` atualizado). Idempotente.

### Passo 4 — Conferir o que vai pro commit
- `git status` e, após adicionar, `git diff --staged`.
- Confirmar que `.env`/segredos NÃO estão na lista. Arquivo novo → `git add caminho/arquivo`
  explícito, nunca `-A`.

### Passo 5 — Commit + consolidação no `main` (contorna o bug dos hooks — issue #1)
Mensagem semântica: `feat: ...`, `fix: ...`, `docs: ...`, `chore: ...`.

- Commitar na branch atual: `git add -u` (+ novos explícitos) · `git commit -m "<tipo>: <resumo>"`.
- O comando de merge DEVE começar com `git checkout main &&` para cair no `main` mesmo que o
  pretooluse hook crie uma nova `session/*`.
- Para cada `session/*` à frente do main, mergear:
  `git checkout main && git merge <branch> --no-ff -m "merge: <resumo>"`
- Deletar branches `session/*` já mergeadas e as vazias residuais (`git branch -D ...`).

> Nota: aqui o HIVE é diferente do fluxo solo padrão — por causa do bug dos hooks, branches
> `session/*` PRECISAM ser consolidadas no `main`, senão o trabalho some. Não deixar branch viva.

### Passo 6 — Push para o origin
- `git push origin main`

### Passo 7 — Verificar e reportar
- `git log --oneline -1`, `git status`, `git branch --list "session/*"` (deve ser 0).
- Confirmar `git rev-parse main origin/main` (local == remoto). Nunca declarar sucesso sem isso.

```
✅ Sessão encerrada.
📄 Log: docs/sessions/AAAA-MM-DD.md
🌿 main == origin/main · commit + merge + push OK
➡️ Próximo passo: <o que retomar>
```

## NÃO faz
- Não usa `git add -A`.
- Não commita se houver segredo no diff — para e avisa.
- Não inventa entregas que não aconteceram.
- Não deixa branch `session/*` órfã (diferente do fluxo solo: aqui consolida no main).
