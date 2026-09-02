#!/usr/bin/env python3
"""Repair known German glossary propagation corruption patterns in _lang/de."""

from __future__ import annotations

import difflib
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LANG_ROOT = REPO_ROOT / "_lang" / "de"

# Targeted phrase fixes (longest first).
PHRASE_REPLACEMENTS = [
    # Bug 1: Taxi product name leaked into rideshare example
    ("Taxi for Email-/Mitfahr-App", "Taxi-/Mitfahr-App"),
    ("Taxi for Email- oder Mitfahr-App", "Taxi- oder Mitfahr-App"),
    ("ein Taxi for Email zu rufen", "ein Taxi zu rufen"),
    ("ein Taxi for Email rufen", "ein Taxi rufen"),
    ("Taxi for Email anzufordern", "ein Taxi anzufordern"),
    ("ein Taxi for Email anzufordern", "ein Taxi anzufordern"),
    ("ein Taxi for Email gerufen", "ein Taxi gerufen"),
    ("Successful Taxi for Email Hails", "Successful Taxi Hails"),
    ("Unsuccessful Taxi for Email Hails", "Unsuccessful Taxi Hails"),
    ("Successful Taxi for Email Hail", "Successful Taxi Hail"),
    ("Unsuccessful Taxi for Email Hail", "Unsuccessful Taxi Hail"),
    ("Taxi for Email for Email", "Taxi for Email"),
    # Bug 2: click glossary corrupted On-Click UI labels
    ("On-Klick, der-Verhalten", "On-Click-Verhalten"),
    ("On-Klick, der-Verhaltens", "On-Click-Verhaltens"),
    ("On-Klick, der-Aktionen", "On-Click-Aktionen"),
    ("On-Klick, der-Aktion", "On-Click-Aktion"),
    ("On-Klick, der Behavior", "On-Click Behavior"),
    ("On-Klick, der behavior", "On-Click behavior"),
    ("On-Klick, der-UI/UX", "On-Click-UI/UX"),
    # Bug 3: sign-up glossary noun replaced imperative/infinitive verb forms
    ("Registrierung Sie", "Registrieren Sie"),
    ("zu Registrierung", "zu registrieren"),
    ("sich zu Registrierung", "sich zu registrieren"),
    ("Für Push-to-Start Registrierung", "Für Push-to-Start registrieren"),
    ("Für Push Registrierung", "Für Push registrieren"),
    ("Für Push-Benachrichtigungen Registrierung", "Für Push-Benachrichtigungen registrieren"),
    ("Geräte Registrierung sich", "Geräte registrieren sich"),
    ("bei APNs Registrierung", "bei APNs registrieren"),
    ("bei FCM Registrierung", "bei FCM registrieren"),
    ("Stammverzeichnis Registrierung", "Stammverzeichnis registrieren"),
    ("Root-Domain Registrierung", "Root-Domain registrieren"),
    ("im Stammverzeichnis Registrierung", "im Stammverzeichnis registrieren"),
    ("und zu Registrierung", "und zu registrieren"),
    ("selbst Registrierung", "selbst registrieren"),
    ("Registrierung, indem", "registrieren, indem"),
    ("Registrierung können", "registrieren können"),
    ("Registrierung erneut", "erneut registrieren"),
    ("Erstellen und Registrierung", "Erstellen und registrieren"),
    ("remote Registrierung", "remote registrieren"),
    ("manuell Registrierung", "manuell registrieren"),
    ("Geofences Registrierung", "Geofences registrieren"),
    ("Schema Registrierung", "Schema registrieren"),
    ("Ein Schema Registrierung", "Ein Schema registrieren"),
    ("Push-Öffnungen Registrierung", "Push-Öffnungen registrieren"),
    ("Messaging Service Registrierung", "Messaging Service registrieren"),
    ("Services Registrierung", "Services registrieren"),
    ("Callbacks Registrierung", "Callbacks registrieren"),
    ("Handler zu Registrierung", "Handler zu registrieren"),
    ("Klassen Registrierung", "Klassen registrieren"),
    ("Aktivität Registrierung möchten", "Aktivität registrieren möchten"),
    ("Ihre Aktivität Registrierung", "Ihre Aktivität registrieren"),
    ("Activity-Lifecycle-Callbacks Registrierung", "Activity-Lifecycle-Callbacks registrieren"),
    ("Lifecycle-Callbacks Registrierung", "Lifecycle-Callbacks registrieren"),
    ("in Braze zu Registrierung", "in Braze zu registrieren"),
    ("in Ihrer App zu Registrierung", "in Ihrer App zu registrieren"),
    ("in dieser Domain zu Registrierung", "in dieser Domain zu registrieren"),
    ("bei Braze Registrierung", "bei Braze registrieren"),
    ("und Registrierung Sie", "und registrieren Sie"),
    ("Registrierung sich", "registrieren sich"),
    ("Registrierung ihn selbst", "registrieren ihn selbst"),
    ("Registrierung ihn", "registrieren ihn"),
    ("Registrierung das", "registrieren das"),
    ("Registrierung die", "registrieren die"),
    ("Registrierung den", "registrieren den"),
    ("Registrierung eine", "registrieren eine"),
    ("Registrierung einen", "registrieren einen"),
    ("Registrierung ein", "registrieren ein"),
    ("Registrierung als", "Registrieren als"),
    ("Registrierung unter", "registrieren unter"),
    ("Registrierung mit navigator", "registrieren mit navigator"),
    ("Registrierung mit", "registrieren mit"),
    ("Registrierung auf beiden", "registrieren auf beiden"),
    ("Registrierung nicht", "registrieren nicht"),
    ("Registrierung Ihren", "registrieren Ihren"),
    ("Registrierung Ihre", "registrieren Ihre"),
    ("Registrierung Ihr", "registrieren Ihr"),
    ("Registrierung anschließend", "registrieren anschließend"),
    ("Registrierung dann", "registrieren dann"),
    ("Registrierung anhand", "registrieren anhand"),
    ("Registrierung intern", "registrieren intern"),
    ("Registrierung möchten", "registrieren möchten"),
    ("Token / Textbaustein Registrierung", "Token manuell registrieren"),
    ("Token-Registrierung Registrierung", "Token-Registrierung registrieren"),
    ("FCM-Token / Textbaustein-Registrierung Registrierung", "FCM-Token manuell registrieren"),
    ("automatische FCM-Token / Textbaustein-Registrierung", "automatische FCM-Token-Registrierung"),
    ("Registrierung Sie sich", "Registrieren Sie sich"),
    ("melden Sie sich an oder Registrierung Sie sich", "melden Sie sich an oder registrieren Sie sich"),
]
PHRASE_REPLACEMENTS.sort(key=lambda pair: len(pair[0]), reverse=True)

NOUN_RESTORATION = [
    ("die registrieren Ihrer", "die Registrierung Ihrer"),
    ("bei der registrieren Ihrer", "bei der Registrierung Ihrer"),
    ("nach der registrieren Ihres", "nach der Registrierung Ihres"),
    ("nach der registrieren Ihrer", "nach der Registrierung Ihrer"),
    ("nach der registrieren einer", "nach der Registrierung einer"),
    ("nach der registrieren", "nach der Registrierung"),
    ("vor der registrieren", "vor der Registrierung"),
    ("bei der registrieren", "bei der Registrierung"),
    ("während der registrieren", "während der Registrierung"),
    ("durch die registrieren", "durch die Registrierung"),
    ("für die registrieren", "für die Registrierung"),
    ("in die registrieren", "in die Registrierung"),
    ("zur registrieren einer", "zur Registrierung einer"),
    ("zur registrieren", "zur Registrierung"),
    ("die registrieren eines", "die Registrierung eines"),
    ("die registrieren einer", "die Registrierung einer"),
    ("die registrieren,", "die Registrierung,"),
    ("die registrieren;", "die Registrierung;"),
    ("die registrieren.", "die Registrierung."),
    ("die registrieren ", "die Registrierung "),
    ("der registrieren", "der Registrierung"),
    ("vereinfacht die registrieren", "vereinfacht die Registrierung"),
    ("bei jeder registrieren", "bei jeder Registrierung"),
    ("sich Registrierung und", "sich registrieren und"),
]
NOUN_RESTORATION.sort(key=lambda pair: len(pair[0]), reverse=True)


def apply_phrase_repairs(text: str) -> tuple[str, int]:
    total = 0
    for old, new in PHRASE_REPLACEMENTS:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            total += count
    for old, new in NOUN_RESTORATION:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            total += count
    return text, total


def restore_registrieren_lines_from_develop(text: str, rel_path: str) -> tuple[str, int]:
    """Restore lines from develop when only registrieren/registrierung verb corruption differs."""
    try:
        develop = subprocess.check_output(
            ["git", "show", f"develop:{rel_path}"],
            cwd=REPO_ROOT,
        ).decode()
    except subprocess.CalledProcessError:
        return text, 0

    dev_lines = develop.splitlines(keepends=True)
    cur_lines = text.splitlines(keepends=True)
    if len(dev_lines) != len(cur_lines):
        return text, 0

    restored = 0
    out: list[str] = []
    for dev_line, cur_line in zip(dev_lines, cur_lines):
        if dev_line == cur_line:
            out.append(cur_line)
            continue
        if (
            "registrieren" in dev_line.lower()
            and "registrieren" not in cur_line.lower()
            and "Registrierung" in cur_line
            and difflib.SequenceMatcher(
                None, dev_line.lower(), cur_line.lower()
            ).ratio()
            >= 0.88
        ):
            out.append(dev_line)
            restored += 1
        else:
            out.append(cur_line)
    return "".join(out), restored


def repair_file(path: Path) -> int:
    rel_path = path.relative_to(REPO_ROOT).as_posix()
    original = path.read_text(encoding="utf-8")
    text, phrase_count = apply_phrase_repairs(original)
    text, line_count = restore_registrieren_lines_from_develop(text, rel_path)
    total = phrase_count + line_count
    if total and text != original:
        path.write_text(text, encoding="utf-8")
    return total


def main() -> None:
    files_changed = 0
    total_replacements = 0
    for path in sorted(LANG_ROOT.rglob("*.md")):
        count = repair_file(path)
        if count:
            files_changed += 1
            total_replacements += count
            print(f"{path.relative_to(REPO_ROOT)}: {count}")
    print(f"Repaired {total_replacements} occurrences in {files_changed} files.")


if __name__ == "__main__":
    main()
