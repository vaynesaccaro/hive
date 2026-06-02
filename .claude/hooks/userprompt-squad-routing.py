#!/usr/bin/env python3
"""UserPromptSubmit — Squad Routing: detects squad keywords and hints context load."""
import json, sys

SQUADS = {
    "commercial": ["commercial","sales","lead","pipeline","proposal","crm","victor","deal","prospect","quota"],
    "cs": ["customer success","onboarding","churn","health score","leah","retention","nps","client health"],
    "marketing": ["marketing","content","brand","campaign","social media","maya","copywriting","audience","seo"],
    "product": ["product","roadmap","story","sprint","feature","owen","backlog","prioriti","user story","acceptance"],
    "finance": ["finance","invoice","cash flow","budget","clara","revenue","expense","p&l","dre","tax","billing"],
    "dev": ["dev","code","bug","pull request","ethan","branch","architecture","refactor","test","typescript","python"],
    "infra": ["infra","server","deploy","dns","ssl","monitoring","dean","vps","ci/cd","docker","kubernetes","nginx"],
    "operations": ["operations","hiring","okr","culture","harper","onboard","offboard","sop","process","team health"],
    "quality": ["quality","audit","standard","nora","stranger test","checklist","sop review"],
    "intelligence": ["intelligence","competitor","competitive","market research","war game","rex","bias audit"],
    "orchestrator": ["stamper","orchestrat","all squads","company status","overview","weekly"],
}

def detect(prompt):
    pl = prompt.lower()
    return [s for s,kws in SQUADS.items() if any(kw in pl for kw in kws)]

def main():
    try: data=json.loads(sys.stdin.read())
    except: sys.exit(0)
    prompt=data.get("prompt","")
    if not prompt: sys.exit(0)
    squads=detect(prompt)
    if not squads: sys.exit(0)
    if len(squads)==1:
        s=squads[0]
        print(f"[hive/routing] Detected squad: {s}")
        print(f"  Context: squads/{s}/CLAUDE.md | State: squads/{s}/memory/STATE.md")
        if s!="orchestrator": print(f"  Run /open-squad {s} for full context")
    else:
        print(f"[hive/routing] Multiple squads detected: {', '.join(squads)}")
        for s in squads: print(f"  squads/{s}/")
    sys.exit(0)

if __name__=="__main__": main()
