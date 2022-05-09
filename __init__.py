"""
Fedora : 
LIST GPG KEYS
ALL IMPORTED SIGNING KEYS : rpm -q gpg-pubkey --qf '%{NAME}-%{VERSION}-%{RELEASE}\t%{SUMMARY}\n'
OFFICIAL ARCHIVE SIGNING KEYS : ls /etc/pki/rpm-gpg/
rpm -e gpg-pubkey-b6792c39-53c4fbdd#keyname
REPO LIST
sudo dnf repo list
ENABLING
dnf config-manager --set-enabled repository_url
set the above disabled
sudo dnf config-manager --set-disabled <reponame>
delete repo rm -f /etc/yum.repos.d/<name-of-repository-file>

now for ubuntu, arch, gentoo PaIn
"""
#reload




import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):

        grid = Gtk.Grid()
        self.add(grid)

        quitBtn = Gtk.Button(label="Quit")
        quitBtn.set_size_request(80, 30)
        quitBtn.connect("clicked", self.on_button_clicked)

        grid.attach(quitBtn, 0, 0, 1, 1)

        self.set_border_width(10)
        self.set_title("Quit button")
        self.set_default_size(280, 180)
        self.connect("destroy", Gtk.main_quit)

    def on_button_clicked(self, widget):
        Gtk.main_quit()

win = MyWindow()
win.show_all()
Gtk.main()




#if rpm can be replaced with deb and stuff
#CHECK THE DISTRO