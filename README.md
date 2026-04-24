# Kanban Board CLI

Prosta aplikacja konsolowa do zarzadzania zadaniami w stylu Kanban.
Projekt wykorzystywany jako przyklad do laboratorium z Agile / Gitflow.

## Artefakty projektu

- **Product Backlog** - lista user stories w pliku `BACKLOG.md`
- **Sprint Backlog** - zadania wybrane do biezacego sprintu (`SPRINT.md`)
- **Kanban Board** - wizualizacja stanu prac (kolumny: `Todo`, `InProgress`, `Done`)
- **Definition of Done** - sekcja w `BACKLOG.md`
- **Repozytorium Git** - Gitflow:
  - `main` - wersja produkcyjna
  - `develop` - integracja pracy
  - `feature/*` - nowe funkcjonalnosci
  - `hotfix/*` - pilne poprawki z `main`
  - `release/*` - przygotowanie wydania

## Funkcje

- Dodawanie zadan (`add`)
- Przenoszenie miedzy kolumnami (`move`)
- Wyswietlanie tablicy (`show`)
- Usuwanie zadan (`rm`)
- Trwaly zapis w pliku JSON

## Uruchomienie

```bash
python kanban.py add "Zaprojektowac API"
python kanban.py move 1 InProgress
python kanban.py show
```

## Scenariusz Gitflow + Hotfix

1. Na `main` znajduje sie wersja stabilna `v1.0`.
2. Na galezi `feature/priority-tasks` trwa praca nad priorytetami zadan (status `InProgress` na tablicy Kanban).
3. Zgloszono blad produkcyjny: komenda `show` wyrzuca wyjatek przy pustej tablicy.
4. Tworzymy `hotfix/empty-board-crash` z `main`, naprawiamy, mergujemy do `main` i `develop`.
5. Praca na `feature/priority-tasks` jest kontynuowana niezaleznie.

### Komendy Gitflow do wykonania hotfixa

```bash
git checkout main
git checkout -b hotfix/empty-board-crash
# poprawka w board.py (render() - obsluga pustej listy)
git commit -am "hotfix: obsluga pustej tablicy w render()"
git checkout main && git merge --no-ff hotfix/empty-board-crash
git tag -a v1.0.1 -m "Hotfix v1.0.1"
git checkout develop && git merge --no-ff hotfix/empty-board-crash
git branch -d hotfix/empty-board-crash
```
