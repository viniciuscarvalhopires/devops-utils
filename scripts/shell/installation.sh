sudo apt-get update
dpkg -l iscsi-initiator-utils
sudo apt-get install bash curl findmnt grep awk blkid lsblk open-iscsi iscsi-initiator-utils
sudo systemctl enable iscsid
