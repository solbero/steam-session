# Steam Session
> Minimal Xsession for Steam Big Picture

A minimal Xsession for Steam Big Picture. Only Steam in Big Picture mode and a window manager; nothing more, nothing less.

## Getting Started

Clone the repository and run the install script as root.

```shell
git clone https://github.com/solbero/steam-session.git
cd steam-session
chmod +x ./install.sh
sudo ./install.sh --install
```

Then log out of your current session and select the *Steam* session in your display manager.

## Dependencies

You must have these dependencies installed for Steam Session to function:

* **xfwm4**: window manager
* **xset**: disabling the screensaver and screen energy saving mode
* **unclutter**: hiding the mouse cursor
* **steam**: displaying and playing games

## Configuration

#### Autologin

To get a console-like experience, enable autologin in your display manager.

How to enable auto login for:
* [LightDM](https://wiki.archlinux.org/title/LightDM#Enabling_autologin)
* [GDM](https://wiki.archlinux.org/title/GDM#Automatic_login)
* [LXDM](https://wiki.archlinux.org/title/LXDM#Autologin)
* [SSDM](https://wiki.archlinux.org/title/SDDM#Autologin)

#### Installation

```shell
sudo ./install -i | --install
```

#### Removal

```shell
sudo ./install -r | --remove
```

#### Logs

```shell
/tmp/steam-session.log
```

## Contributing

If you'd like to contribute, please fork the repository, use a feature branch and submit a pull request.


## Licensing

The code in this project is licensed under the GNU Lesser General Public License v2.1.
