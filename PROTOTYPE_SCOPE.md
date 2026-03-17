# PROTOTYPE_SCOPE.md

## Required prototype states
Generate at least these four states as distinct, testable screens:

### 1. Overview
Contains:
- main dashboard
- 4 KPI cards
- chart
- nav
- filter and export buttons

### 2. Filter Open
Contains:
- same overview context
- open filter panel or dropdown
- fields such as insurer, municipality, contract, date range
- apply/reset actions

### 3. Error Details
Contains:
- same product language
- details for data validation issues
- issue rows or cards
- statuses and correction cues

### 4. Export Modal
Contains:
- modal or panel
- export format options
- concise report configuration
- confirm button

## Optional nice-to-have screens
Only add if quality stays high:
- Contracts overview
- Validation dashboard
- Reports page
- Contract detail page

## Prototype behavior
Interactions should support:
- Filter button opens filter state
- Data Errors card opens error details
- Export button opens export modal
- close/back actions return user to overview

## Screenshot quality
Every required state should be polished enough to be inserted directly into a report as a figure.

## Scope discipline
Do not expand the product into a full enterprise suite.
Prefer 4 strong states over 10 shallow ones.
