<p align="center">
  <pre align="center">
  __  __   _    _   _ 
 |  \/  | / \  | | | |
 | |\/| |/ _ \ | |_| |
 | |  | / ___ \|  _  |
 |_|  |/_/   \_\_| |_|
  <i>minimal · graphite · matcha · driftwm</i>
  </pre>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OS-CachyOS-00a4dc?style=for-the-badge&logo=arch-linux" alt="CachyOS" />
  <img src="https://img.shields.io/badge/WM-driftwm-e5e2e3?style=for-the-badge" alt="driftwm" />
  <img src="https://img.shields.io/badge/Terminal-Kitty-e0af68?style=for-the-badge&logo=kitty" alt="Kitty" />
  <img src="https://img.shields.io/badge/Shell-Fish_4.7.1-b4f9f8?style=for-the-badge" alt="Fish" />
  <img src="https://img.shields.io/badge/Palette-Mocha_Graphite-7aa2f7?style=for-the-badge" alt="Palette" />
</p>

<p align="center">
  <b>Minimalist dotfiles for CachyOS featuring the <a href="https://github.com/malbiruk/driftwm">driftwm</a> infinite canvas tiling Wayland compositor.</b><br/>
  <i>Deep graphite background, soft pastel accents (matcha green, muted purple, dusty rose), borderless rounded windows, and custom Python desktop widgets.</i>
</p>

---

## 🖼️ Gallery

<p align="center">
  <img src="./preview/Screenshot_20260921_210828.png" alt="Desktop Overview" width="100%" />
</p>

<p align="center">
  <img src="./preview/Screenshot_20260921_210102.png" alt="Terminal & ikifetch" width="49%" />
  <img src="./preview/Screenshot_20260921_210151.png" alt="Workspace & Windows" width="49%" />
</p>

<p align="center">
  <img src="./preview/Screenshot_20260921_205605.png" alt="Custom Widgets" width="32%" />
  <img src="./preview/Screenshot_20260921_205525.png" alt="Widgets & Media" width="32%" />
  <img src="./preview/Screenshot_20260921_203217.png" alt="Active Setup" width="32%" />
</p>

---

## 💻 Software Stack

| Category | Component / Application | Description |
| :--- | :--- | :--- |
| **Operating System** | **CachyOS** | Performance-optimized Arch Linux (Linux kernel with BORE scheduler) |
| **Window Manager** | [driftwm](https://github.com/malbiruk/driftwm) | Infinite canvas tiling Wayland compositor |
| **Status Bar** | [Waybar](https://github.com/Alexays/Waybar) | Floating pill-style dock with media, weather, and tray drawer |
| **Desktop Widgets** | Python GTK Widgets (`widgets/`) | Standalone widgets for clock, calendar, CPU/RAM monitor, and weather |
| **Control Center** | [drift-shell-settings](https://github.com/ikittohk14-beep/drift-shell-settings) | GUI settings panel for Wi-Fi, Bluetooth, PipeWire audio, and window rules |
| **Terminal Emulator** | [Kitty](https://sw.kovidgoyal.net/kitty/) | Fast GPU-accelerated terminal with Kitty Graphics Protocol |
| **Shell** | [Fish shell](https://fishshell.com/) 4.7.1 | Interactive shell with autosuggestions and `ikifetch` integration |
| **System Info Fetch** | [ikifetch](https://github.com/ikittohk14-beep/ikifetch) | Lightweight system fetcher with animated GIF playback support |
| **Notification Center** | [SwayNC](https://github.com/ErikReider/SwayNotificationCenter) | Wayland notification center and widget panel |
| **On-Screen Display** | [SwayOSD](https://github.com/ErikReider/SwayOSD) | Floating indicators for volume, brightness, and CapsLock |
| **Application Launcher** | [Rofi](https://github.com/lbonn/rofi) (Wayland) | Minimalist application launcher styled in graphite palette |
| **File Managers** | [Yazi](https://github.com/sxyazi/yazi) / Nautilus | Terminal and graphical file managers |
| **Typography** | Inter Nerd Font / JetBrainsMono NF | Crisp monospace typography with Nerd Font glyphs |

---

## 📦 Included Components

- **[ikifetch](https://github.com/ikittohk14-beep/ikifetch)** — Fast, lightweight Python system fetcher with animated GIF rendering and disk caching in Kitty.
- **[drift-shell-settings](https://github.com/ikittohk14-beep/drift-shell-settings)** — Modern control center tailored for driftwm with management for Wi-Fi, Bluetooth, PipeWire audio, wallpapers, and window rules.
- **`driftwm/`** — Compositor configuration (`config.toml`), XWayland setup, and startup scripts.
- **`waybar/`** — Floating dock status bar with integrated media player, weather, resource stats, and collapsible tray drawer.
- **`widgets/`** — Collection of custom Python desktop widgets (clock, calendar, system resources, weather, power menu).
- **`kitty/`** — Terminal profile configured with `Inter Nerd Font` and pastel Mocha graphite theme.
- **`fish/`** — Shell configuration, aliases, and `ikifetch` helper functions.
- **`swaync/` & `swayosd/`** — Notification center styling and on-screen volume/brightness popups.
- **`rofi/`** — Application menu styled in graphite tones.

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/ikittohk14-beep/dotfiles.git
cd dotfiles
```

### 2. Install dependencies (CachyOS / Arch Linux)
```bash
# Core packages and tools
sudo pacman -S waybar kitty fish rofi swaync swayosd python python-pillow btop yazi micro git stow

# ikifetch and Drift Shell Settings
git clone https://github.com/ikittohk14-beep/ikifetch.git && cd ikifetch && ./install.sh && cd ..
git clone https://github.com/ikittohk14-beep/drift-shell-settings.git
```

### 3. Deploy with GNU Stow
```bash
stow driftwm
stow waybar
stow widgets
stow kitty
stow fish
stow ikifetch
stow rofi
stow swaync
stow swayosd
```

---

## ⌨️ Keybindings

| Shortcut | Action |
| :--- | :--- |
| `Super + Enter` | Kitty Terminal |
| `Super + D` | Application Launcher (Rofi) |
| `Super + G` | File Manager (Nautilus) |
| `Super + N` | Notification Center (SwayNC) |
| `Super + Shift + D` | Toggle Theme |
| `Super + L` | Lock Screen |
