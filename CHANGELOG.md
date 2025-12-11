# Release notes

<!-- do not remove -->

## 1.0.35

### Bugs Squashed

- `label_kw` not used in `ToggleBtn` ([#149](https://github.com/AnswerDotAI/MonsterUI/issues/149))


## 1.0.34

### New Features

- Add `Textarea` alias for consistency with FastHTML ([#146](https://github.com/AnswerDotAI/MonsterUI/pull/146)), thanks to [@erikgaas](https://github.com/erikgaas)


### Bugs Squashed

- Fix SyntaxWarning: use raw string for spy_js regex ([#147](https://github.com/AnswerDotAI/MonsterUI/pull/147)), thanks to [@erikgaas](https://github.com/erikgaas)


## 1.0.32

### New Features

- Add JS Scrollspy ([#136](https://github.com/AnswerDotAI/MonsterUI/pull/136)), thanks to [@curtis-allan](https://github.com/curtis-allan)
- Add Toggle Button & Loader Button components, thanks to [@curtis-allan](https://github.com/curtis-allan)


## 1.0.29

### Bugs Squashed

- `apply_classes` wraps some elements in html/body/head tags ([#135](https://github.com/AnswerDotAI/MonsterUI/issues/135))


## 1.0.28

### New Features

- allow optional renderer ([#134](https://github.com/AnswerDotAI/MonsterUI/pull/134))

### Bugs Squashed

- `render_md` doesn't render images with data uris when `img_dir` is set ([#132](https://github.com/AnswerDotAI/MonsterUI/issues/132))


## 1.0.26

### Bugs Squashed

- fix `render_md` non http/s urls ([#133](https://github.com/AnswerDotAI/MonsterUI/pull/133)), thanks to [@comhar](https://github.com/comhar)


## 1.0.25

### Bugs Squashed

- remove modal on close ([#130](https://github.com/AnswerDotAI/MonsterUI/pull/130)), thanks to [@comhar](https://github.com/comhar)
- Buttons not working in Modal added to the DOM by HTMX. ([#126](https://github.com/AnswerDotAI/MonsterUI/issues/126))


## 1.0.24

### New Features

- use uikit to initialise and open modals inserted with htmx ([#127](https://github.com/AnswerDotAI/MonsterUI/pull/127)), thanks to [@comhar](https://github.com/comhar)


## 1.0.23

### Bugs Squashed

- fragment md parsing does not work ([#124](https://github.com/AnswerDotAI/MonsterUI/issues/124))
- llms.txt showing "internal server" errors ([#122](https://github.com/AnswerDotAI/MonsterUI/issues/122))


## 1.0.22

- Create custom themes

### Bugs Squashed

- Unicode strings with encoding declaration are not supported ([#123](https://github.com/AnswerDotAI/MonsterUI/issues/123))
- Update DropDownNavContainer class to remove unnecessary width class ([#114](https://github.com/AnswerDotAI/MonsterUI/pull/114)), thanks to [@ndendic](https://github.com/ndendic)
- fix font weight ordering ([#113](https://github.com/AnswerDotAI/MonsterUI/pull/113)), thanks to [@comhar](https://github.com/comhar)
- FieldSet inputs in Form are misaligned when monsterui is active ([#87](https://github.com/AnswerDotAI/MonsterUI/issues/87))


## 1.0.21

### New Features

- The new `ApexChart` component can create line charts, pie charts and [more](https://monsterui.answer.ai/api_ref/docs_charts). ([#110](https://github.com/AnswerDotAI/MonsterUI/pull/110)), thanks to [@ndendic](https://github.com/ndendic)
- Toasts now disappear automatically after 5 seconds. You can adjust the duration by using the `dur` field (e.g. `Toast('My Toast', dur=10.0)`). ([#109](https://github.com/AnswerDotAI/MonsterUI/pull/109)), thanks to [@comhar](https://github.com/comhar)

### Breaking Change

- Katex is no longer included in the default headers. To include it set `katex=True` when calling `.headers`. (i.e. `Theme.slate.headers(katex=True)`). ([#105](https://github.com/AnswerDotAI/MonsterUI/pull/105)), thanks to [@comhar](https://github.com/comhar)


## 1.0.20

### New Features

- Add `icon` header param to optionally not bring in icons js lib ([#99](https://github.com/AnswerDotAI/MonsterUI/issues/99))

### Bugs Squashed

- added fh. to unqid ([#98](https://github.com/AnswerDotAI/MonsterUI/pull/98)), thanks to [@MorsCerta-crypto](https://github.com/MorsCerta-crypto)


## 1.0.19

### New Features

- Add accordion component ([#94](https://github.com/AnswerDotAI/MonsterUI/pull/94)), thanks to [@MichlF](https://github.com/MichlF)
- Fix theme logic ([#93](https://github.com/AnswerDotAI/MonsterUI/pull/93)), thanks to [@curtis-allan](https://github.com/curtis-allan)


## 1.0.18

- Hotfix accidental deletion of label select :(


## 1.0.16

### Bugs Squashed

- Select not properly checking presence of hx-trigger

## 1.0.14

### New Features

- Move CDN's to jsdelivr ([#88](https://github.com/AnswerDotAI/MonsterUI/pull/88)), thanks to [@curtis-allan](https://github.com/curtis-allan)

### Bugs Squashed

- Select htmx compatibility bug
- SVG Path Name Collision Issue in MonsterUI ([#85](https://github.com/AnswerDotAI/MonsterUI/issues/85))


## 1.0.13

### Bugs Squashed

- LabelCheckboxX ignores id set manually ([#80](https://github.com/AnswerDotAI/MonsterUI/issues/80))
- Select sending multiple values to HTMX 


## 1.0.10

### New Features

- Cusom Themes support in ThemePicker ([#71](https://github.com/AnswerDotAI/MonsterUI/pull/71)), thanks to [@ndendic](https://github.com/ndendic)


## 1.0.8

- Add lightbox and Insertable select

## 1.0.7

### New Features

- Add select kwargs to Select and LabelSelect ([#70](https://github.com/AnswerDotAI/MonsterUI/issues/70))

### Bugs Squashed

- Update component classes to align with Franken UI v2.0 ([#67](https://github.com/AnswerDotAI/MonsterUI/pull/67)), thanks to [@Zaseem-BIsquared](https://github.com/Zaseem-BIsquared)
- Updated ContainerT, CardT, and TableT class names to match the documented patterns from Franken UI v2.0 docs

## 1.0.6


### Bugs Squashed

- Update component classes to align with Franken UI v2.0 ([#67](https://github.com/AnswerDotAI/MonsterUI/pull/67)), thanks to [@Zaseem-BIsquared](https://github.com/Zaseem-BIsquared)


## 1.0.5

- Add Center component

## 1.0.4

### New Features

- Bug fix to correct theming conflict in theme initialization


## 1.0.2

- Bug fix to add dark mode theme selector to TW config, thanks to [@curtis-allan](https://github.com/curtis-allan)

## 1.0.1

- Theme bug fix not allowing theme changes to stick, thanks to [@zaseem-bisquared](https://github.com/Zaseem-BIsquared)
- Documentation bug fix on tutorial app, thanks to [@decherd](https://github.com/decherd)


## 1.0.0

### New Features

- Migrated to use FrankenUI version 2.0 version

- Brand new simplified NavBar api, including enhanced sticky and scrollspy options, thanks to [@ohmeow](https://github.com/ohmeow) and [@curtis-allan](https://github.com/curtis-allan)

- Latex rendering enabled via katex ([#58](https://github.com/AnswerDotAI/MonsterUI/pull/58)), thanks to [@algal](https://github.com/algal)

- Add API References and Guides to llms.txt ([#54](https://github.com/AnswerDotAI/MonsterUI/issues/54))

- New Range component, which includes min/max range

- New center component thanks to inspiration from Carson of HTMX ([#52](https://github.com/AnswerDotAI/MonsterUI/issues/52))

- Better Theme Picker ([#51](https://github.com/AnswerDotAI/MonsterUI/issues/51))

- Upload Zone and Upload Button Components added ([#50](https://github.com/AnswerDotAI/MonsterUI/issues/50))

### Bugs Squashed

- fix: correct PaddingT class naming for padding variants ([#55](https://github.com/AnswerDotAI/MonsterUI/pull/55)), thanks to [@Zaseem-BIsquared](https://github.com/Zaseem-BIsquared)


## 0.0.34


### Bugs Squashed

- Table markdown rendering bug fix ([#46](https://github.com/AnswerDotAI/MonsterUI/issues/46))


## 0.0.33

### New Features

- Add subtitle function for common semantic styling option ([#44](https://github.com/AnswerDotAI/MonsterUI/pull/44))

- Add semantic text styling to docs examples ([#42](https://github.com/AnswerDotAI/MonsterUI/pull/42))

- Created higher level Navbars function for auto-responsive collapse to mobile and easier interface ([#33](https://github.com/AnswerDotAI/MonsterUI/issues/33)), thanks to @curtis-allan

- Added Scrollspy to Nav and NavBar and example that demonstrates it ([#31](https://github.com/AnswerDotAI/MonsterUI/issues/31)), thanks to @99ch

- Added Highlight JS integration to headers ([#28](https://github.com/AnswerDotAI/MonsterUI/issues/28)), thanks to @99ch

### Bugs Squashed

- Improve defaults for Navbar when components are passed so it doesn't override styling specified toby user  ([#43](https://github.com/AnswerDotAI/MonsterUI/pull/43))


